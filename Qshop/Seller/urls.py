from django.urls import path,re_path
from Seller.views import *

urlpatterns = [
    re_path('^$',index),
    path('index/', index,),
    path('goods_add/', goods_add,name='goods_add'),
    re_path('goods_list/(\d+)/', goods_list),
    path('login/', login,name="login"),
    path('logout/', login,name="logout"),
    re_path('goods/(\d+)/', goods),
    re_path('goods_change/(?P<id>\d+)/',goods_change,name='goods_change'),
    re_path('goods_del/(?P<id>\d+)/',goods_del,name='goods_del'),
    # re_path('example',example),

    path('example/', example),
]