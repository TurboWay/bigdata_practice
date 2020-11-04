#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/8/27 14:06
# @Author : way
# @Site : 
# @Describe: 分析 ua ; 安装 pip install pyyaml ua-parser user-agents

import sys
from user_agents import parse
from datetime import datetime


def ua_parse(ua):
    user_agent = parse(ua)
    return str(user_agent).split(' / ')


def format(dt):
    dt =  datetime.strptime(dt, '%d/%b/%Y:%H:%M:%S +0800')
    return str(dt)


if __name__ == '__main__':
    for line in sys.stdin:
        cols = line.replace('\n', '').split('\t')
        cols = cols[:-1] + ua_parse(cols[-1])
        cols[1] = format(cols[1])
        sys.stdout.write('\t'.join(cols) + '\n')
