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