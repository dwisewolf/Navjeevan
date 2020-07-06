from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [

    path('data/', views.stulist.as_view()),
    path('videoFile/', views.FileView.as_view(),name='Get/Post-File'),
    path('getuserData/', views.getUserData, name='POST-Get-UserData-with-userid'),
    path('stuUpload/', views.addShipmentAPIView, name='AddShipmentAPIView'), 
    path('userData/', views.userData, name='userData'),
    path('checkNum/', views.checkMobileNum, name='checkMobileNum'),
    path('newsData/', views.NewsView.as_view(),name='Get/Post-File'), 
    path('newsUpload/', views.addNews, name='addNews'), 
    path('stuListSchool/', views.stuListSchool, name='Student_Data_BasedOn_School_code'),
    # path('videoFile/<int:id>/', views.FileView.as_view()),
    path('stuTaskData/', views.stuTaskList.as_view()), 
    path('notesData/', views.notesList.as_view()),
    path('feedBackData/', views.feedBackList.as_view()),

]


