#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/8/26 14:48
# @Author : way
# @Site : 
# @Describe:

from random import randint

class SourceDataDemo:

    @property
    def wordcloud(self):
        data = [
            {"name": "图瓦卢", "value": 47},
            {"name": "罗马尼亚", "value": 52},
            {"name": "朝鲜", "value": 90},
            {"name": "古巴", "value": 84},
            {"name": "科威特", "value": 99},
            {"name": "卡塔尔", "value": 37},
            {"name": "美国", "value": 2},
            {"name": "伊拉克", "value": 32},
            {"name": "多米尼克国", "value": 3},
            {"name": "塞舌尔", "value": 20},
        ]
        return data

    @property
    def line(self):
        data = {
            '指数1': [randint(1, 10) for i in range(7)],
            '指数2': [randint(1, 10) for i in range(7)],
            'legend': ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
        }
        return data

    @property
    def bar(self):
        data = {
            '股票A': [randint(15, 30) for i in range(6)],
            '股票B': [randint(15, 30) for i in range(6)],
            '股票C': [randint(15, 30) for i in range(6)],
            'legend': ['一月', '二月', '三月', '四月', '五月', '六月']
        }
        return data

    @property
    def pie(self):
        data = [
            {'value': 335, 'name': '直接访问'},
            {'value': 310, 'name': '邮件营销'},
            {'value': 234, 'name': '联盟广告'},
            {'value': 130, 'name': '视频广告'},
            {'value': 1548, 'name': '搜索引擎'}
        ]
        return data

    @property
    def china(self):
        data = [
            {'name': '四川', 'value': 239},
            {'name': '浙江', 'value': 231},
            {'name': '福建', 'value': 203},
            {'name': '江苏', 'value': 185},
            {'name': '湖南', 'value': 152},
            {'name': '山东', 'value': 131},
            {'name': '安徽', 'value': 100},
            {'name': '广东', 'value': 89},
            {'name': '河北', 'value': 87},
            {'name': '湖北', 'value': 84},
            {'name': '吉林', 'value': 75},
            {'name': '上海', 'value': 70},
            {'name': '江西', 'value': 64},
            {'name': '广西', 'value': 64},
            {'name': '贵州', 'value': 64},
            {'name': '北京', 'value': 63},
            {'name': '云南', 'value': 53},
            {'name': '重庆', 'value': 49},
            {'name': '河南', 'value': 48},
            {'name': '陕西', 'value': 38},
            {'name': '山西', 'value': 37},
            {'name': '辽宁', 'value': 33},
            {'name': '新疆', 'value': 25},
            {'name': '内蒙古', 'value': 23},
            {'name': '黑龙江', 'value': 20},
            {'name': '天津', 'value': 19},
            {'name': '甘肃', 'value': 13},
            {'name': '海南', 'value': 9},
            {'name': '青海', 'value': 7},
            {'name': '宁夏', 'value': 4},
            {'name': '西藏', 'value': 0},
        ]
        return data


class SourceData(SourceDataDemo):
    ...