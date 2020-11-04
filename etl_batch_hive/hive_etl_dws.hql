-- 建表 清洗后的结果表
-- [纬度表] ip 与 省份的映射表
CREATE TABLE `spider.dim_ip`(
  `remote_addr` string,
  `province` string);

-- [事实表] nginx 日志清洗后的结果表
CREATE TABLE `spider.fact_nginx_log`(
  `remote_addr` string,
  `time_local` string,
  `province` string,
  `request` string,
  `device` string,
  `os` string,
  `browser` string);

-- 通过 udf 获取 ip 所在省份，创建IP和省份的映射表
set hive.exec.mode.local.auto=true;
set hive.exec.mode.local.auto.inputbytes.max=52428800;
set hive.exec.mode.local.auto.input.files.max=10;

add file /home/getway/udf_baidu_api.py;

insert into spider.dim_ip
select transform(remote_addr)
  USING 'python3 udf_baidu_api.py' AS (remote_addr, province)
from (
select remote_addr
from spider.nginx_log
group by remote_addr
) as cte;


add file /home/getway/udf_log_clean.py;

insert into spider.fact_nginx_log
select transform(a.remote_addr,
                 a.time_local,
                 b.province,
                 a.request,
                 a.http_user_agent
                 )
       USING 'python3 udf_log_clean.py' AS (remote_addr,
                                       time_local,
                                       province,
                                       request,
                                       device,
                                       os,
                                       browser)
from spider.nginx_log a
left join spider.dim_ip b on a.remote_addr = b.remote_addr
where a.request not rlike '\\.[css|js|woff|TTF|png|jpg|ico]';