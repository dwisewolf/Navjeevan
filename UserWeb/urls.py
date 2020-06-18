from django.urls import path
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.base import TemplateView

urlpatterns = [
    #Admin Panel
    #url(r'^home/$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^home/$', views.home, name='home'),
    path('home/create/', views.create_view,name='createUser'), 
    # path('home/createAuth/', views.create_view_user,name='createAuthUser'),
    url(r'^home/stuTeachList$', views.stuTeachList, name='UsersList'),
    url(r'^home/usersList/$', views.usersList, name='AuthUsersList'),
    url(r'^home/stulist(?P<userid>[\w-]+)/$', views.detail_view,name='stulistUser'), 
    url(r'^home/usersList/stulistAuth(?P<id>\d+)/$', views.detail_view_user,name='stulistAuthUser'), 
    url(r'^home/stulist(?P<userid>[\w-]+)/edit/$', views.update_view, name='updateUser'), 
    url(r'^home/usersList/stulistAuth(?P<id>\d+)/edit/$', views.update_view_user, name='updateAuthUser'),
    url(r'^home/stulist(?P<userid>[\w-]+)/delete/$', views.delete_view, name='deleteUser'), 
    url(r'^home/usersList/stulistAuth(?P<id>\d+)/delete/$', views.delete_view_user, name='deleteAuthUser'),
    # url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    #Student Panel
    url(r'^login/$', auth_views.LoginView.as_view(template_name="login.html"), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name="userlogout.html"), name='logout'),
    path('userlogin/', views.Userdata,name='userlogin'),
    path('userlogout/', views.userlogout,name='userlogout'),
]
