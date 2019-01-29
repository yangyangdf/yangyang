from django.db import models


#买家建模
class Buyer(models.Model):
    username = models.CharField(max_length = 32)    #用户名
    password = models.CharField(max_length = 32)    #密码
    email = models.EmailField(blank = True,null = True)     #邮件
    phone = models.CharField(max_length = 32,blank = True,null = True)  #电话
    photo = models.ImageField(upload_to = "buyer/images",blank = True,null = True)  #图片
    vip = models.CharField(max_length = 32,blank = True,null = True)    #vip



#邮箱验证
class EmailValid(models.Model):
    value = models.CharField(max_length=32)
    email_address = models.EmailField()
    times = models.DateTimeField()


#购物车
class BuyCar(models.Model):
    goods_id = models.CharField(max_length=32)
    goods_name = models.CharField(max_length=32)
    goods_price = models.FloatField()
    goods_picture = models.ImageField(upload_to="image")
    goods_num = models.IntegerField()
    user = models.ForeignKey(Buyer,on_delete=True)

#地址建模
class Address(models.Model):
    address = models.TextField()
    phone = models.CharField(max_length = 32)
    recver = models.CharField(max_length = 32)
    buyer = models.ForeignKey(Buyer,on_delete = True)


#订单
class Order(models.Model):
    order_num = models.CharField(max_length=32) #唯一 日期+随机+订单+id
    order_time = models.DateTimeField() #订单发起时间
    total = models.FloatField() #订单总价
    order_statue = models.CharField(max_length=32) #状态 未支付 支付成功  配送中  完成交易 取消订单

    user = models.ForeignKey(Buyer,on_delete = True) #用户
    order_address = models.ForeignKey(Address, on_delete=True)  # 订单地址

#订单和商品的关系
class OrderGoods(models.Model):
    goods_id = models.IntegerField()
    goods_name = models.CharField(max_length=32)
    goods_price = models.FloatField()
    goods_num = models.IntegerField()
    goods_picture = models.ImageField(upload_to="images")
    order = models.ForeignKey(Order,on_delete=True)

# Create your models here.

