

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

二级分类设计：
https://blog.csdn.net/weixin_47971206/article/details/124199978

### 常见问题

多对多的查询可通过related_name别名查询
join查询
ForeignKey的时候字段会自动加_id后缀
学习SerializerMethodField
跨域配置 django-cors-headers
数据库备份命令:
mysqldump -u root -p --databases 数据库名称 > xxx.sql
创建管理员命令：
insert into b_user(username,password,role,status) values('admin111',md5('admin111'),1,'0');

### 登录接口

调login -> 生成token

### 字典设计

```
角色字典role
管理员: 1
普通用户: 2
演示帐号: 3

认证
后台认证失败: AUTH_FAIL_END
前台认证失败: AUTH_FAIL_FRONT

```

### 认证

接口添加 @authentication_classes注解



