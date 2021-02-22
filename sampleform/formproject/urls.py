

from django.contrib import admin
#includeを追加
from django.urls import path, include







from django.conf.urls import url
from django.contrib import admin
from accounts import views

#from django.contrib.auth.views import login, auth_logout
from django.contrib.auth.views import auth_logout




urlpatterns = [
    path('admin/', admin.site.urls),
    #追加
    path('', include('formapp.urls')),

#ふたつめのアプリ ログイン機能

    #url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^create/$', views.create_account, name='create_account'),
    url(r'^login/$', views.account_login, name='login'),
    url(r'^logout/$', auth_logout, {'template_name': 'index.html'}, name='logout'),

]




















