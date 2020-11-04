#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/11/2 16:10
# @Author : way
# @Site : 
# @Describe:

import re
import requests
import pandas as pd
from datetime import datetime
from user_agents import parse
from kafka import KafkaConsumer
from sqlalchemy import create_engine

AK = "" # 百度 ak 自行申请 http://lbsyun.baidu.com/index.php?title=webapi/ip-api
ENGINE_CONFIG = 'mysql+pymysql://root:root@127.0.0.1:3306/spider?charset=utf8'
ENGINE = create_engine(ENGINE_CONFIG)


class NginxLog:

    def __init__(self, *args):
        self.remote_addr = args[0]
        # self.remote_user = args[1]
        self.time_local = datetime.strptime(args[2], '%d/%b/%Y:%H:%M:%S +0800')
        self.request = args[3]
        # self.status = args[4]
        # self.body_bytes_sent = args[5]
        # self.http_referer = args[6]
        http_user_agent = args[7]
        self.device, self.os, self.browser = str(parse(http_user_agent)).split(' / ')

    def get_province_baidu(self):
        url = f"https://api.map.baidu.com/location/ip?ak={AK}&ip={self.remote_addr}&coor=bd09ll"
        try:
            province = requests.get(url).json()['address'].split('|')[1]
            return province
        except:
            return 'ERROR'

    def get_province(self):
        sql = f"select province from dim_ip where ip = '{self.remote_addr}' limit 1;"
        data = pd.read_sql(sql, ENGINE)
        if data.values:
            return data.values[0][0]
        else:
            province = self.get_province_baidu()
            value = {'ip': self.remote_addr, 'province': province}
            df = pd.DataFrame([value])
            df.to_sql('dim_ip', con=ENGINE, index=False, if_exists='append')
            return province

    def save(self):
        if not re.findall('\.[css|js|woff|TTF|png|jpg|ico]', log.request):
            province = self.get_province()
            value = {
                'remote_addr': self.remote_addr,
                'time_local': self.time_local,
                'province': province,
                'request': self.request,
                'device': self.device,
                'os': self.os,
                'browser': self.browser
            }
            df = pd.DataFrame([value])
            print(value)
            df.to_sql('fact_nginx_log', con=ENGINE, index=False, if_exists='append')


servers = ['172.16.122.23:9092', ]
consumer = KafkaConsumer(
    bootstrap_servers=servers,
    auto_offset_reset='latest',  # 重置偏移量 earliest移到最早的可用消息，latest最新的消息，默认为latest
)
consumer.subscribe(topics=['nginxlog'])
for msg in consumer:
    info = re.findall('(.*?) - (.*?) \[(.*?)\] "(.*?)" (\\d+) (\\d+) "(.*?)" "(.*?)" .*', msg.value.decode())
    log = NginxLog(*info[0])
    log.save()
