from .forms import StuForm, UserForm, UsersLoginForm
from TeacherStu.models import Student, User
# from django.contrib.auth.models import User
from . models import Users
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse,JsonResponse
from rest_framework import compat
from django.views import View
from rest_framework.response import Response 
from rest_framework import status 
from rest_framework.views import APIView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import json

# @login_required(login_url="/home/userlogin/")
# @login_required(login_url="/login/")
def home(request): 
    query = request.GET.get("q", None)
    template = "index.html"
    context = {"object_list": query}
    return render(request, template,context)

# Create a New Student
# @login_required(login_url="/login/")
def create_view(request):
    form = StuForm(request.POST,request.FILES)
    template = "createUser.html"
    context = {"form": form}
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        return HttpResponseRedirect("/home/")
    else: 
        form = StuForm()   
    return render(request, template, context)

# def create_view_user(request):
#     form = UserForm(request.POST,request.FILES)
#     template = "createUser.html"
#     context = {"form": form}
#     if form.is_valid():
#         obj = form.save(commit=False)
#         obj.save()
#         return HttpResponseRedirect("/home/")
#     else: 
#         form = UserForm()   
#     return render(request, template, context)

# Get Infomation of Particular Student According to Id 
# @login_required(login_url="/login/")
def detail_view(request, userid=None):
    qs = get_object_or_404(Student, userid=userid)
    context = {"object" : qs}
    template = "getUserData.html"
    return render(request, template, context) 

def detail_view_user(request, id=None):
	# pass
    qs = get_object_or_404(User, id=id)
    context = {"object" : qs}
    template = "getAuthUserData.html"
    return render(request, template, context) 


# Can Upadate the Student Data
# @login_required(login_url="/login/")
def update_view(request, userid=None):
    obj = get_object_or_404(Student, userid=userid)
    template = "updateUser.html"
    form = StuForm(request.POST or None, instance=obj)
    context = {"form": form}
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        messages.success(request, "Updated post!")
        return HttpResponseRedirect("/home/")
    return render(request, template, context)

def update_view_user(request, id=None):
    obj = get_object_or_404(User, id=id)
    template = "updateAuthUser.html"
    form = UserForm(request.POST or None, instance=obj)
    context = {"form": form}
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        messages.success(request, "Updated post!")
        return HttpResponseRedirect("/home/usersList/")
    return render(request, template, context)


# Can Delete the Student Data
# @login_required(login_url="/admin/")
def delete_view(request , userid=None):
    obj = get_object_or_404(Student, userid=userid)
    context = {"object": obj}
    if request.method == 'POST':
        obj.delete()
        messages.success(request, "Post Deleted...!")
        return HttpResponseRedirect("/home/")

    template = "delete.html"
    return render(request, template, context)

def delete_view_user(request , id=None):
    obj = get_object_or_404(User, id=id)
    context = {"object": obj}
    if request.method == 'POST':
        obj.delete()
        messages.success(request, "Post Deleted...!")
        return HttpResponseRedirect("/home/usersList/")

    template = "deleteAuth.html"
    return render(request, template, context)


# Get Infomation of Particular Student According to Id 
# @login_required(login_url="/home/userlogin/")
def Userdata(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        name = request.POST.get('name')        
        form = UsersLoginForm(request.POST)
        qs = Users.objects.filter(name=name)
        if Users.objects.filter(name=name).exists():
            if (qs.filter(password=password).exists()):
                if form.is_valid():
                    obj = Users.objects.filter(name__iexact=name).values("name")[0]["name"] 
                    context = {"object_list" : obj}
                    template = "index.html" 
                    # print("obj"*12,obj)  
                    # messages.success(request, 'Login successfully!') 
                    # return HttpResponseRedirect("/home/", context)
                    return render(request, template, context) 
            else:
                messages.info(request, 'Enter the Correct Password!')
                return HttpResponseRedirect("/userlogin/")
        else:
            messages.info(request, 'Enter the Correct Name!')
            return HttpResponseRedirect("/userlogin/") 
    else: 
        form = UsersLoginForm()   
    return render(request, "userlogin.html", {"form": form})

def userlogout(request):
    return HttpResponseRedirect("/userlogin/")


# Show List of All Data
# @login_required(login_url="/home/userlogin/")
def stuTeachList(request):
    # print(paswd)
    # import pdb
    # pdb.set_trace()

    query = request.GET.get("q", None)
    print(query)
    # user = User.objects.get(username=request.user.username)
    # print("User NAme" , user )
    obj = Student.objects.filter(userid__contains=query
            ).values("userid","category","clas","section","name","mobileNum").order_by('userid')
    # print(obj)
    context = {
            "object_list" : obj,
            "code":query
        }
    template = "allList.html"    
    return render(request, template, context)

@login_required(login_url="/login/")
def usersList(request):
    query = request.GET.get("q", None)
    obj = User.objects.all().values()
    context = {
            "object_list" : obj,
            "code":query
        }
    template = "allauthList.html"    
    return render(request, template, context)
 