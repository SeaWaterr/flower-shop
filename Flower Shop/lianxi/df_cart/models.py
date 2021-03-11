from django.db import models


# Create your models here.
class CartInfo(models.Model):
    user = models.ForeignKey('df_user.UserInfo', on_delete=models.CASCADE)
    goods = models.ForeignKey('df_goods.GoodsInfo', on_delete=models.CASCADE)
    count = models.IntegerField(default=0)  # 买的数量

    class Meta:
        verbose_name = '购物车商品信息'
        verbose_name_plural = '购物车商品信息'


class OrderGoods(models.Model):
    '''订单商品模型类'''
    o_user = models.ForeignKey('df_user.UserInfo', on_delete=models.CASCADE)
    o_goods = models.ForeignKey('df_goods.GoodsInfo', on_delete=models.CASCADE)
    o_count = models.IntegerField(default=0)  # 买的数量

    class Meta:
        verbose_name = '订单信息'
        verbose_name_plural = '订单商品信息'
