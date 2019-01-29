

from django.db import models

class Types(models.Model):  #商品类型
    label =  models.CharField(max_length = 32)  #商品标签
    parent_id = models.IntegerField()   #商品id
    description = models.TextField()    #商品描述


class Seller(models.Model):                         #卖家
    username = models.CharField(max_length = 32)    #卖家账户
    password = models.CharField(max_length = 32)    #卖家密码
    nickname = models.CharField(max_length = 32)    #卖家昵称
    photo = models.ImageField(upload_to = "image")  #卖家照片
    phone = models.CharField(max_length = 32)       #卖家电话
    address = models.CharField(max_length = 32)     #卖家地址
    email = models.EmailField()                     #卖家邮箱
    id_number = models.CharField(max_length = 32)   #卖家身份证


class Goods(models.Model):                          #商品
    goods_id = models.CharField(max_length = 32)    #商品id
    goods_name = models.CharField(max_length = 32)  #商品名字
    goods_price = models.FloatField()               #商品原价
    goods_now_price = models.FloatField()           #商品当前价格
    goods_num = models.IntegerField()               #商品库存
    goods_description = models.TextField()          #商品描述
    goods_content = models.TextField()              #商品详情
    goods_show_time = models.DateField()            #商品发布时间
    types = models.ForeignKey(Types,on_delete = True) #一个分类会有多个商品
    seller = models.ForeignKey(Seller, on_delete=True) #一家店铺会有多个商品
    def __str__(self):
        return self.goods_name

class Image(models.Model):                          #图片
    img_adress = models.ImageField(upload_to = "image") #图片地址
    img_label = models.CharField(max_length = 32)       #图片标签
    img_description= models.TextField()             #图片详情
    goods = models.ForeignKey(Goods, on_delete=True)  # 一个商品多张图片


class BankCard(models.Model):                       #银行卡
    number = models.CharField(max_length=32)        #银行卡号
    bankAddress = models.CharField(max_length=32)   #银行公司
    username = models.CharField(max_length=32)      # 持卡人姓名
    idCard = models.CharField(max_length=32)        #持卡人身份证
    phone = models.CharField(max_length=32)         #持卡人电话

    seller = models.ForeignKey(Seller, on_delete=True) #一个人可有多张银行卡


# Create your models here.
