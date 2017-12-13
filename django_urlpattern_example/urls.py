"""django_urlpattern_example URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from mynewsite import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # 字符串前面的'r'是表示要求Python解释器保持后面字符串的原貌，不要试图去处理任何转义字符的符号，
    # 这是使用Regular Expression解析的字符串都会开的'保险'
    # '^' 符号表示接下来的字符要定义开头的字符串，而'$'表示结尾字符串
    # 开始和结尾放在一起，中间没有任何字符的设置r'^$'就表示首页'/'
    # 特别需要注意的是，如果在^和$之间加入一个'/'，那么反而会出错，要使用localhost:8000//才能匹配上，
    # 原因是在输入网址时会自动加上/
    # 传统上用来查询特定数据(POST和GET)的一些网址格式(如'localhost:8000/?page=10')，
    # Django会把它忽视不予处理，它的结果和'localhost:8000/'是一样的

    # 匹配localhost:8000//
    re_path(r'^/$', views.homepage),

    # 因为输入网址时会自动加上'/'，所以下面的'/'匹配最后的'/'，
    # '/$'表示匹配最后的'/'并且后面没有字符了，如果有就不是我们要解析的网址了
    re_path(r'^about/$', views.about),

    # 表示匹配如下4个：
    # localhost:8000/about/0/
    # localhost:8000/about/1/
    # localhost:8000/about/2/
    # localhost:8000/about/3/
    re_path(r'about/[1|2|3|4]/$', views.about),

    # 传递参数小括号括起来就行
    # re_path(r'^list/([0|1|2|3])/$', views.listing),

    # 设置参数的名字(?P<name>pattern)，设置名字的话，在view对应的函数中就一定要使用相同的名称才可以
    re_path('^list/(?P<type>[0|1|2|3])/$', views.listing),
    # 这里没有没有参数，views.listing的参数变量加上了一个默认值，所以没有参数就会以默认参数值处理
    re_path('^list/$', views.listing),

    # 例子取出年，月，日，以及文章的编号
    re_path(r'^post/(\d{4})/(\d{1,2})/(\d{1,2})/(\d{1,3})/$', views.post, name='post-url'),
    # 通过reverse也可以反解出url
    # reverse('post-url', args=(yr, mon, day, post_num)))



    # 手动传递数据过去，只需要在处理函数后面加上一个字典类型的数据就行,同时在在views.homepage里面设置一个名字为'mode'的参数接收
    path('manual/', views.manual, {'mode': 'manual'}),

    # include 可以用来去掉多余的部分，比如：
    # urlpatterns = [
    #     path('<page_slug>-<page_id>/history/', views.history),
    #     path('<page_slug>-<page_id>/edit/', views.edit),
    #     path('<page_slug>-<page_id>/discuss/', views.discuss),
    #     path('<page_slug>-<page_id>/permissions/', views.permissions),
    # ]
    # 可以变成
    # urlpatterns = [
    #     path('<page_slug>-<page_id>/', include([
    #         path('history/', views.history),
    #         path('edit/', views.edit),
    #         path('discuss/', views.discuss),
    #         path('permissions/', views.permissions),
    #     ])),
    # ]

    # 可以把部分模块的urlpatterns单独设置，然后包含进来
    re_path(r'^mynewsite/', include('mynewsite.urls')),

    # An included URLconf receives any captured parameters from parent URLconfs.
    # 变量也可以传递到包含的urls里
    re_path(r'^mynewsite(\d{3})/', include('mynewsite.urls')),

    # 如果在字符串中什么都不加那么默认会匹配任何网址，如果在网站中不打算让用户看到找不到的指定页面，
    # 而是输入错误就让它转到首页，那就可以在最后一行加上这个
    re_path('', views.homepage),
]
