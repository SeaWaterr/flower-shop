# encoding:utf8
from django.db import models


# Create your models here.

class UserInfo(models.Model):
    uname = models.CharField(max_length=20)  # 用户名
    upwd = models.CharField(max_length=40)  # 密码
    uemail = models.CharField(max_length=30)  # 邮箱
    ushou = models.CharField(max_length=20, default='')  # 收件人    #default给属性一个默认值
    uaddress = models.CharField(max_length=100, default='')  # 地址
    uyoubian = models.CharField(max_length=6, default='')  # 邮编
    uphone = models.CharField(max_length=11, default='')  # 电话

    def __str__(self):
        return self.uname

    # default,blank是python层面的约束，不影响数据库表结构
    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = '用户信息'


class OrderInfo(models.Model):
    oid = models.CharField(max_length=20, primary_key=True)#id
    user =models.CharField(max_length=20)#人
    odate = models.DateTimeField(auto_now_add=True)#时间
    oIsPay = models.BooleanField(default=False)
    ototal = models.DecimalField(max_digits=6, decimal_places=2)#default='带盆载好'
    oaddress = models.CharField(max_length=150)
