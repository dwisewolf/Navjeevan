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
    url(r'^Taskhome/$', views.TaskHome, name='TaskHome'),  
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
    # url(r'^empanellist(?P<id>\d+)/edit/$', views.update_view, name='update'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name="login.html"), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name="userlogout.html"), name='logout'),
    path('userlogin/', views.Userdata,name='userlogin'),
    path('userlogout/', views.userlogout,name='userlogout'),
# Student's Task URL's
    path('home/allTask', views.stuTaskList,name='allTaskList'), 
    path('home/addTask', views.create_Taskview,name='createTask'),  
    url(r'^home/tasklist(?P<id>\d+)/edit/$', views.update_Taskview, name='updateTask'), 
    url(r'^home/tasklist(?P<id>\d+)/delete/$', views.delete_Taskview, name='deleteTask'), 
    url(r'^home/clasSearch/(?P<clas>[\w\-]+)/search/$', views.clasSearch, name='clasSearch'),
    path('Taskhome/authallTask', views.authStuTaskList,name='authallTaskList'),
    path('Taskhome/allTechTask', views.stuTaskList2,name='allTaskList2'),
    path('Taskhome/techaddTask', views.create_Taskview2,name='techcreateTask'),
    url(r'^Taskhome/techtasklist(?P<id>\d+)/edit/$', views.update_Taskview2, name='techupdateTask'), 
    url(r'^Taskhome/techtasklist(?P<id>\d+)/delete/$', views.delete_Taskview2, name='techdeleteTask'), 
    url(r'^Taskhome/techclasSearch/(?P<clas>[\w\-]+)/search/$', views.clasSearch2, name='techclasSearch'),    
# Teacher's Details URL's
    path('home/addTeachTask', views.create_Teachview,name='createTeachview'), 
    path('home/allTeachTask', views.teachTaskList,name='allTeachTaskList'), 
    url(r'^home/techtasklist(?P<id>\d+)/edit/$', views.update_TechTaskview, name='updateTechTask'), 
    url(r'^home/techtasklist(?P<id>\d+)/delete/$', views.delete_TechTaskview, name='deleteTechTask'),
    url(r'^home/clasTechSearch/(?P<clas>[\w\-]+)/search/$', views.clastechSearch, name='clastechSearch'), 
# Feedback URL's
    path('home/allFeedback', views.feedList,name='feedList'), 
    url(r'^home/feedlist(?P<id>[\w\-]+)/edit/$', views.update_feedview, name='updateFeed'), 
    # url(r'^home/feedlist(?P<id>[\w\-]+)/delete/$', views.delete_feedview, name='deleteFeed'), 
]
