#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/8/27 14:06
# @Author : way
# @Site : 
# @Describe: 通过 ip 获取所在省份

import sys
import json
import requests

ak = "your baidu ak" # 百度 ak 自行申请 http://lbsyun.baidu.com/index.php?title=webapi/ip-api

def ip2province(ip):
    url = f"https://api.map.baidu.com/location/ip?ak={ak}&ip={ip}&coor=bd09ll"
    try:
        province = json.loads(requests.get(url).text)['address'].split('|')[1]
        return province
    except:
        return 'ERROR'


if __name__ == '__main__':
    for line in sys.stdin:
        cols = line.replace('\n', '').split('\t')
        cols = [ip2province(cols[0]), cols[1]]
        sys.stdout.write('\t'.join(cols) + '\n')
