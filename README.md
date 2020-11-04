# bigdata_practice
![](https://img.shields.io/badge/hive-1.1-green)
![](https://img.shields.io/badge/python-3.6%2B-brightgreen)
![](https://img.shields.io/badge/flask-1.1%2B-orange)
![](https://img.shields.io/badge/echarts-4.7-yellowgreen)

大数据实践项目 - nginx 日志分析可视化

## 功能说明

通过流、批两种方式，分析 nginx 日志，将分析结果通过 flask + echarts 进行可视化展示

## 数据收集分析过程

![image-20201104093541868](https://gitee.com/TurboWay/blogimg/raw/master/img/image-20201104093541868.png)

[方式一：离线批处理 hive + datax + mysql](http://blog.turboway.top/article/bigdata_practice_batch/)

[方式二：实时流处理 flume + kafka + python + mysql](http://blog.turboway.top/article/bigdata_practice_stream/)

## 配置

* 安装依赖 
```
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
```
* 修改 ironman/data_db.py 的数据库配置
```python
ENGINE_CONFIG = 'mysql+pymysql://root:root@127.0.0.1:3306/test?charset=utf8'
```
* mysql 建表
```
-- nginx_log 日志表
create table fact_nginx_log(
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `remote_addr` VARCHAR(20),
  `time_local` TIMESTAMP(0),
  `province` VARCHAR(20),
  `request` varchar(300),
  `device` varchar(50),
  `os` varchar(50),
  `browser` varchar(100),
  PRIMARY KEY (`id`)
) DEFAULT CHARSET=utf8 ;

-- ip 地区映射表
create table dim_ip(
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ip` VARCHAR(20),
  `province` VARCHAR(20),
  `addtime` TIMESTAMP(0) default now(),
  PRIMARY KEY (`id`)
) DEFAULT CHARSET=utf8  ;
```

## 运行

运行 cd ironman; python app.py

打开 http://127.0.0.1:5000/

## 效果图

### 24 小时访问趋势
![image](https://gitee.com/TurboWay/blogimg/raw/master/img/image-20201104095828851.png)

### 每日访问情况
![image](https://gitee.com/TurboWay/blogimg/raw/master/img/image-20201104095850250.png)

### 客户端设备占比
![image](https://gitee.com/TurboWay/blogimg/raw/master/img/image-20201104095903233.png)

### 用户分布
![image](https://gitee.com/TurboWay/blogimg/raw/master/img/image-20201104095914602.png)

### 爬虫词云
![image](https://gitee.com/TurboWay/blogimg/raw/master/img/image-20201104095933091.png)
