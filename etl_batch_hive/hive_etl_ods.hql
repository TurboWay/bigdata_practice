-- 建表 原始记录
-- 根据日志格式，使用正则序列化解析，一个（）是一个字段，注意转义
drop table if exists spider.nginx_log;
create table spider.nginx_log(
remote_addr STRING,
remote_user STRING,
time_local STRING,
request STRING,
status STRING,
body_bytes_sent STRING,
http_referer STRING,
http_user_agent STRING
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.RegexSerDe'
WITH SERDEPROPERTIES (
"input.regex" = '(.*?) - (.*?) \\[(.*?)\\] "(.*?)" (\\d+) (\\d+) "(.*?)" "(.*?)" .*',
"output.format.string" = "%1$s %2$s %3$s %4$s %5$s %6$s %7$s %8$s"
);


-- 加载数据
load data local inpath '/home/getway/nginx.log' into table spider.nginx_log;


