#### 项目名称
    鲜花商城
#### 运行环境
    python 3.6.6
#### 数据库配置
    1、安装Mysql 8.0.12 
    2、创建数据库账户密码（Mysql）
#### 安装依赖
    pip install -r requirements.txt
#### 运行步骤
    1、python manage.py makemigrations
    2、python manage.py migrate
    3、python manage.py runserver

#### 注意
    当执行运行步骤时如果出现报错：
    django.core.exceptions.ImproperlyConfigured: mysqlclient 1.3.13 or newer is required; you have 0.9.3.
    解决办法：
    1、C:\Python37\Lib\site-packages\django\db\backends\mysql（python安装目录）打开base.py，注释掉以下内容： 　　　　　　　
        if version < (1, 3, 13): 　　　　　　　　　　
            raise ImproperlyConfigured('mysqlclient 1.3.13 or newer is required; you have %s.' % Database.__version__) 　　 
    2、File "C:\Python37\lib\site-packages\django\db\backends\mysql\operations.py", line 146, in last_executed_query 
    query = query.decode(errors='replace') AttributeError: 'str' object has no attribute 'decode' 　　
    解决办法：打开此文件把146行的decode修改为encode