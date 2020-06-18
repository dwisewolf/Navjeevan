from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse, HttpResponse
from .models import Student, Video, User, News
from django.shortcuts import render #Default
from django.http import *
from django.shortcuts import get_object_or_404 #get object(error) when object not exist
from rest_framework.views import APIView #API data
from rest_framework.response import Response #Successful 200 response
from rest_framework import status #send back status 
from . import services
from rest_framework.decorators import api_view
from django.http import JsonResponse, HttpResponse
import json
from django.db.models import Q
from . serializers import stuSerializer, videoSerializer, userSerializer, newsSerializer
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status


class stulist(APIView):

    def get(self, request):
        stu_list=Student.objects.all()
        serializer=stuSerializer(stu_list,many=True)
        return Response(serializer.data)


    def post(self, request):
        data=self.request.data

        mobileNum = data.get('mobileNum')
        # if (Student.objects.filter(mobileNum=mobileNum).exists()):
        if (User.objects.filter(mobileNum=mobileNum).exists()):
            return services.UserLogin(request)
        else:
            password = data.get('password',None)
            paswd = len(str(password))
            print(paswd)
            # print(paswd)
            # import pdb
            # pdb.set_trace()

            if password is None or len(password)==0:
                return services.MesgResponse(mobileNum,mesg="Please Enter Password.",status=204) 
            
            else:
                # return services.MesgResponse(mobileNum,mesg=" Password.",status=204) 
                saveQuerySet = User.objects.create(mobileNum=mobileNum,password=password)
                saveQuerySet.save()
                return services.LoginDataSuccessResponse(mobileNum,status=200) 
        # else:
            # return services.MesgResponse(mobileNum,mesg='Enter Valid Mobile Number...',status=204)


class FileView(APIView):
	parser_classes = (MultiPartParser, FormParser)

	def get(self, request):
		stu_list=Video.objects.all()
		serializer=videoSerializer(stu_list,many=True)
		return Response(serializer.data)

	def post(self, request, *args, **kwargs):
	 	file_serializer = videoSerializer(data=request.data)
	 	if file_serializer.is_valid():
	 		file_serializer.save()
	 		return Response(file_serializer.data, status=status.HTTP_201_CREATED)
	 	else:
	 		return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
             
class NewsView(APIView):

	def get(self, request):
		news_list=News.objects.all()
		serializer=newsSerializer(news_list,many=True)
		return Response(serializer.data)

	def post(self, request):
		data=self.request.data
		user_code = data.get('user_code')
		ucode = user_code[0:3]
		tcode = user_code[-3:]
		stuCls = News.objects.filter(user_code=user_code).values_list('class_code',flat=True)[0]
		if (News.objects.filter(user_code=user_code).exists()):
			stuList = News.objects.filter(school_code=ucode)
			tecList = News.objects.filter(school_code=tcode)
			if (stuList.filter(user_code=user_code).exists()):
				news_list= (stuList.filter(user_code=user_code).values() | stuList.filter(Q(user_code='All')|Q(user_code='ALL')).values()) | stuList.filter(user_code=stuCls).values()
				serializer=newsSerializer(news_list,many=True)
				return Response(serializer.data)
			elif (tecList.filter(user_code=user_code).exists()):
				news_list= (tecList.filter(user_code=user_code).values() | tecList.filter(Q(user_code='All')|Q(user_code='ALL')).values()) | tecList.filter(user_code=stuCls).values()
				serializer=newsSerializer(news_list,many=True)
				return Response(serializer.data)
			# elif (News.objects.filter(user_code=user_code).exists()):
			# 	news_list= (News.objects.filter(class_code=user_code).values() | News.objects.filter(user_code='All').values())
			# 	serializer=newsSerializer(news_list,many=True)
			# 	return Response(serializer.data)
			else:
				return services.MesgResponse(user_code, mesg='Something is Wrong', status=status.HTTP_400_BAD_REQUEST)
		else:
			return services.MesgResponse(user_code, mesg='User-Code is Not Exist', status=status.HTTP_400_BAD_REQUEST) 


@api_view(['POST',])
def stuListSchool(request):
      school_code = request.data.get('school_code',None)
      # school_code = Student.objects.filter(userid__icontains=school_code)
      if (Student.objects.filter(userid__icontains=school_code).exists()):
      	stu_list= Student.objects.filter(userid__icontains=school_code).values()
      	serializer=stuSerializer(stu_list,many=True)
      	return Response(serializer.data)
      else:
          return services.MesgResponse(school_code,mesg='School Code is Invalid...',status=status.HTTP_400_BAD_REQUEST)    
    

@api_view(['POST',])
def checkMobileNum(request):
    mobileNum = request.data.get('mobileNum',None)
    if (Student.objects.filter(mobileNum=mobileNum).exists()):
        return services.MesgResponse(mobileNum,mesg='Mobile Number is Valid...',status=status.HTTP_201_CREATED)
    else:
        return services.MesgResponse(mobileNum,mesg='Mobile Number is Invalid...',status=status.HTTP_400_BAD_REQUEST)      
          
@api_view(['GET',])
def userData(request):
      stu_list=User.objects.all()
      serializer=userSerializer(stu_list,many=True)
      return Response(serializer.data)
    
@api_view(['POST',])
def addNews(request):
  	 	file_serializer = newsSerializer(data=request.data)
  	 	if file_serializer.is_valid():
  	 		file_serializer.save()
  	 		return Response(file_serializer.data, status=status.HTTP_201_CREATED)
  	 	else:
  	 		return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST',])
def getUserData(request):
  	userid = request.data.get('userid',None)
  	if (Video.objects.filter(userid=userid).exists()):
  		stu_list=Video.objects.filter(userid=userid).values()
  		mesg=list(stu_list)
  		return Response(mesg)
  	else:
  		return services.MesgResponse(userid,mesg="Mobile Number Not Exist",status=204)

@api_view(['POST',])
def addShipmentAPIView(request):
      stuItems = {}
      stuItemList = []
  
      userid = request.data.get('userid', None)
      name = request.data.get('name', None)
      fatherName = request.data.get('fatherName', None)
      clas = request.data.get('clas', None)
      mobileNum = request.data.get('mobileNum ',None)
      category = request.data.get('category',None)
      saveQuerySet = Student.objects.create(userid=userid,name =name,fatherName = fatherName,clas = clas,mobileNum =mobileNum,category =category)
      saveQuerySet.save()
      stuItemList.append({
              "userid":saveQuerySet.userid,
              "name": saveQuerySet.name,
              "fatherName": saveQuerySet.fatherName,
              "clas": saveQuerySet.clas,
              "mobileNum": saveQuerySet.mobileNum,
              "category": saveQuerySet.category,
          })
      stuItems["stuItems"] = stuItemList
      return services.SuccessResponse(stuItems, status=200)	