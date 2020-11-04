#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/8/27 19:32
# @Author : way
# @Site : 
# @Describe:

import pandas as pd
from sqlalchemy import create_engine
from ironman.data import SourceDataDemo

ENGINE_CONFIG = 'mysql+pymysql://root:root@127.0.0.1:3306/test?charset=utf8'


class SourceData(SourceDataDemo):

    def __init__(self):
        self.ENGINE = create_engine(ENGINE_CONFIG)

    @property
    def china(self):
        sql = "select province, count(distinct remote_addr) from fact_nginx_log where device <> 'Spider' group by province;"
        df = pd.read_sql(sql, self.ENGINE)
        data = [{"name": row[0], "value": row[1]} for row in df.values]
        return data

    @property
    def line(self):
        sql = """
        select case when device='Spider' then 'Spider' else 'Normal' end, hour(time_local), count(1) 
        from fact_nginx_log 
        group by case when device='Spider' then 'Spider' else 'Normal' end, hour(time_local);
        """
        df = pd.read_sql(sql, self.ENGINE)
        data = {
            '正常访问量': [row[2] for row in df.values if row[0] == 'Normal'],
            '爬虫访问量': [row[2] for row in df.values if row[0] == 'Spider'],
            'legend': [row[1] for row in df.values if row[0] == 'Normal']
        }
        return data

    @property
    def bar(self):
        sql = """
        select case when device='Spider' then 'Spider' else 'Normal' end, DATE_FORMAT(time_local, '%Y%m%d'), count(1) 
        from fact_nginx_log 
        where time_local > date_add(CURRENT_DATE, interval - 7 day)
        group by case when device='Spider' then 'Spider' else 'Normal' end, DATE_FORMAT(time_local, '%Y%m%d');
        """
        df = pd.read_sql(sql, self.ENGINE)
        data = {
            '正常访问量': [row[2] for row in df.values if row[0] == 'Normal'],
            '爬虫访问量': [row[2] for row in df.values if row[0] == 'Spider'],
            'legend': [row[1] for row in df.values if row[0] == 'Normal']
        }
        return data

    @property
    def pie(self):
        sql = """
        select device, count(1)
        from fact_nginx_log
        where device not in ('Other', 'Spider') -- 过滤掉干扰数据
        group by device
        order by 2 desc
        limit 10
        """
        df = pd.read_sql(sql, self.ENGINE)
        client_data = [{'name': row[0].strip(), 'value': row[1]} for row in df.values]
        return client_data

    @property
    def wordcloud(self):
        sql = "select browser, count(1) from fact_nginx_log where device = 'Spider' group by browser;"
        df = pd.read_sql(sql, self.ENGINE)
        spider_data = [{'name': row[0].strip(), 'value': row[1]} for row in df.values]
        return spider_data
