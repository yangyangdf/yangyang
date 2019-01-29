from django.shortcuts import render
from Qshop.settings import *


#Cookie校验
def cookieValid(fun):
    def inner(request,*args,**kwargs):
        cookie = request.COOKIES
        session = request.session.get("nickname")
        user = Seller.objects.filter(username= cookie.get("username")).first()

        if user and user.nickname == session:
            return fun(request,*args,**kwargs)
        else:
            return HttpResponseRedirect("/seller/login/")
    return inner

# 主页面视图
@cookieValid
def index(request):
    return render(request,"seller/index.html")

from Seller.models import Seller
from django.http import HttpResponseRedirect
# hashlib加密
import hashlib
def getPassword(password):
    md5 = hashlib.md5()
    #实例化md5加密方法
    md5.update(password.encode())
    #进行加密，python2可以给字符串加密，python3只能给字节加密
    result = md5.hexdigest()
    return result

#登录页面
def login(request):
    # 定义错误返回字符串
    result = {"error":""}
    #请求的方法是“POST”and 能获到数据，判断
    if request.method== "POST" and request.POST:
        login_valid = request.POST.get("login_valid")
        froms = request.COOKIES.get("from")
        if login_valid == "login_valid" and froms =="http://127.0.0.1:8000/seller/login/":
            #username是获取到用户的usernam
            username = request.POST.get("username")
            #user是获取数据库中的用户usermane
            user = Seller.objects.filter(username=username).first()
            #如果数据库的user不为空，判断
            if user:
                #db_password数据库的密码等于用户密码
                db_password = user.password
                #password的密码等于获取到的用户密码
                password = getPassword(request.POST.get("password"))
                #如果数据库密码等于用户输入密码
                if db_password == password:
                    #相应返回seller界面
                    response = HttpResponseRedirect("/seller/")
                    #为密码加cookie
                    response.set_cookie("username",user.username)
                    response.set_cookie("id",user.id)
                    # 设置session
                    request.session["nickname"] = user.nickname
                    return response
                else:
                    result["error"] = "密码错误"
            else:
                result["error"] = "用户不存在"
        else:
            result["error"] = "请查询正确的接口进行登录"
    response = render(request, "seller/login.html", {"result": result})
    response.set_cookie("from", "http://127.0.0.1:8000/seller/login/")
    return response
    #return render(request,"seller/login.html")

def login_v1(request):
    result = {"error": ""}
    if request.method == "POST" and request.POST:
        username = request.POST.get("username")
        user = Seller.objects.filter(username = username).first()
        if user:
            db_password = user.password
            password = getPassword(request.POST.get("password"))
            if db_password == password:
                response = HttpResponseRedirect("/seller/")
                response.set_cookie("username",user.username)
                return response
            else:
                result["error"] = "密码错误"
        else:
            result["error"] = "用户不存在"
    return render(request,"seller/login.html",{"result": result})


#商品添加视图
from Qshop.settings import MEDIA_ROOT
from Seller.models import *
import datetime
import os
@cookieValid
def goods_add(request):
    doType = ""
    if request.method == "POST" and request.POST:
        g = Goods()
        postData = request.POST
        g.goods_id = postData.get("goods_id")            #商品编号
        g.goods_name = postData.get("goods_name")         #商品名称
        g.goods_price = postData.get("goods_price")      #商品原价
        g.goods_now_price = postData.get("goods_now_price")           #商品现价
        g.goods_num = postData.get("goods_num")       #商品库存
        g.goods_description = postData.get("goods_description")     #商品描述
        g.goods_content = postData.get("goods_content") #商品内容
        g.types = Types.objects.get(id=int(postData.get("types")))
        g.goods_show_time = datetime.datetime.now()
        id = request.COOKIES.get("id")
        if id:
            g.seller = Seller.objects.get(id = int(id))
        else:
            return HttpResponseRedirect("/seller/login/")
        g.save()

        imgs = request.FILES.getlist("img_adress")
        for index,img in enumerate(imgs):
            file_name = img.name
            file_path = "seller/images/%s_%s.%s"%(g.goods_name,index,file_name.rsplit(".",1)[1])
            save_path = os.path.join(MEDIA_ROOT,file_path).replace("/","\\")
            try:
                with open(save_path, "wb") as f:
                    for chunk in img.chunks(chunk_size=1024):
                        f.write(chunk)
                i = Image()
                i.img_adress = file_path
                i.img_label = "%s_%s" % (index, g.goods_name)
                i.img_description = "this is description"
                i.goods = g
                i.save()
            except Exception as e:
                print(e)
    return render(request,"seller/goods_add.html")

@cookieValid
def goods_change(request,id):
    doType = "change"
    g = Goods.objects.get(goods_id = id)
    if request.method == "POST" and request.POST:
        postData = request.POST
        g.goods_id = postData.get("goods_id")            #商品编号
        g.goods_name = postData.get("goods_name")         #商品名称
        g.goods_price = postData.get("goods_price")      #商品原价
        g.goods_now_price = postData.get("goods_now_price")           #商品现价
        g.goods_num = postData.get("goods_num")       #商品库存
        g.goods_description = postData.get("goods_description")     #商品描述
        g.goods_content = postData.get("goods_content") #商品内容
        g.types = Types.objects.get(id=int(postData.get("types")))
        g.goods_show_time = datetime.datetime.now()
        id = request.COOKIES.get("id")
        if id:
            g.seller = Seller.objects.get(id = int(id))
        else:
            return HttpResponseRedirect("/seller/login/")
        g.save()

        imgs = request.FILES.getlist("img_adress")
        if imgs:
            for index, img in enumerate(imgs):
                file_name = img.name
                file_path = "seller/images/%s_%s.%s" % (g.goods_name, index, file_name.rsplit(".", 1)[1])
                save_path = os.path.join(MEDIA_ROOT, file_path).replace("/", "\\")
                try:
                    with open(save_path, "wb") as f:
                        for chunk in img.chunks(chunk_size=1024):
                            f.write(chunk)
                    i = Image()
                    i.img_adress = file_path
                    i.img_label = "%s_%s" % (index, g.goods_name)
                    i.img_description = "this is description"
                    i.goods = g
                    i.save()
                    return HttpResponseRedirect("/seller/goods_list/1/")
                except Exception as e:
                    print(e)
        else:
            return HttpResponseRedirect("/seller/goods_list/1/")
    return render(request, "seller/goods_add.html",locals())

@cookieValid
def goods_del(request,id):
    delgoods = Goods.objects.get(goods_id= id)
    imgs = delgoods.image_set.all()
    imgs.delete()
    delgoods.delete()
    return HttpResponseRedirect("/seller/goods_list/1/")


#商品列表页
from django.core.paginator import Paginator
@cookieValid
def goods_list(request,page):
    goodsList = Goods.objects.all()
    p = Paginator(goodsList,5)
    count = p.count
    p_range = p.page_range
    p_data = p.page(page)
    return render(request,"seller/goods_list.html",{"count":count,"p_range":p_range,"goodsList":p_data})


def logout(request):
    username = request.COOKIES.get("username")
    if username:
        response = HttpResponseRedirect("/seller/login/")
        response.delete_cookie("username")
        del request.session["nickname"]
        return response
    else:
        return HttpResponseRedirect("/seller/login/")


def goods(request,num):
    num = int(num)
    oneGoods = Goods.objects.get(id = num)
    return render(request,"seller/onegoods.html",locals())



# 测试文件
# from Seller.models import Seller,Goods
# import random
def example(request):
#     s = Seller()
#     s.username = 'yangyang'  #卖家账户
#     s.password = getPassword('666666')   #卖家密码
#     s.nickname = '杨洋'    #卖家昵称
#     s.photo = 'image/1.jpg'  #卖家照片
#     s.phone = 18011112222       #卖家电话
#     s.address = '北京'     #卖家地址
#     s.email = 'yangyang@qq.com'                     #卖家邮箱
#     s.id_number = '420116199901014918'
#     s.save()
#     return render(request,"seller/goods_list.html")
#Create your views here.
    return render(request,"seller/iframeExample.html",locals())

from django.views.generic import View
from django.http import JsonResponse

class GoodsApi(View):
    def __init__(self,**kwargs):
        View.__init__(self,**kwargs)
        self.response = {
            "statue":"error",
            "data":""
        }
    def get(self,request):
        if request.GET:
            data = request.GET
            types = data.get("type")
            order = data.get("order")
            all = data.get("all")
            if order and all == "true":
                self.response["data"] = "all参数和order参数冲突，请参考手册修改"
            if all == "true":
                goods_list = []
                goods = Goods.objects.all()
                for good in goods:
                    goods_list.append(
                        {
                            "name":good.goods_name,
                            "price":good.goods_now_price
                        }
                    )
                    self.response["statue"] = "seccess"
                    self.response["data"] = goods_list
            return JsonResponse(self.response)
