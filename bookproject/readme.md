

### 删除数据库

drop database if exists book;

### 创建数据库

CREATE DATABASE IF NOT EXISTS book DEFAULT CHARSET utf8 COLLATE utf8_general_ci;


### 迁移数据库表

```
python manage.py makemigrations;

python manage.py migrate;

python manage.py makemigrations myapp;

python manage.py migrate myapp;
```

### 跨域配置

django-cors-headers


### 多对多

https://www.cnblogs.com/SunshineKimi/p/14140900.html

### 常见问题

多对多的查询可通过related_name别名查询
join查询


