"""test1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

# 导入项目APP中的功能
from p1901_test.views import hello_world, hello_world2
from movie_t1.views import index, index1

from django.views.static import serve
from test1.settings import BASE_DIR, MEDIA_ROOT
import os

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello/', hello_world),
    url(r'^hello2/', hello_world2),
    url(r'^m_index/', index),

    # (?P<path>.*)$

    url(r'^static/(?P<path>.*)$', serve, {'document_root': os.path.join(BASE_DIR, 'static')}),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),


    url(r'^index1/(?P<movie_id>\d+)$', index1, name='single_dog')
]
