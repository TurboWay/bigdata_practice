#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/8/27 14:06
# @Author : way
# @Site : 
# @Describe: 通过 ip 获取所在省份

import sys
import requests

AK = "" # 百度 ak 自行申请 http://lbsyun.baidu.com/index.php?title=webapi/ip-api

def ip2province(ip):
    url = f"https://api.map.baidu.com/location/ip?ak={AK}&ip={ip}&coor=bd09ll"
    try:
        province = requests.get(url).json()['address'].split('|')[1]
        return province
    except:
        return 'ERROR'


if __name__ == '__main__':
    for line in sys.stdin:
        cols = line.replace('\n', '').split('\t')
        cols = [cols[0], ip2province(cols[0])]
        sys.stdout.write('\t'.join(cols) + '\n')
