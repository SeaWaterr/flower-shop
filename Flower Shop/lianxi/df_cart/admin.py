from django.contrib import admin
from .models import CartInfo
# Register your models here.

class CartInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'goods','count']
admin.site.register(CartInfo,CartInfoAdmin)

admin.site.site_header = '花花后台管理系统'
admin.site.site_title = '花花'