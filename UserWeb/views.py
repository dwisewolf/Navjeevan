from .forms import StuForm, UserForm, UsersLoginForm, StuTaskForm,DateForm, TeachForm, FeedbackForm
from TeacherStu.models import Student, User, Stu_Task, Teach_Task, Feedback
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

# @login_required(login_url="/login/")
def home(request): 
    query = request.GET.get("q", None)
    template = "index.html"
    context = {"object_list": query}
    return render(request, template,context)

# Create a New Student
# @login_required(login_url="/login/") 
def create_view(request):
    query = request.GET.get("q", None)
    # print (query)
    form = StuForm(request.POST,request.FILES)
    template = "createUser.html"
    context = {"form": form,"code":query}
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        return HttpResponseRedirect("/home/create/?q="+query)
    else: 
        form = StuForm()   
    return render(request, template, context)


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
    query = request.GET.get("q", None)
    print (query)
    obj = get_object_or_404(Student, userid=userid)
    template = "updateUser.html"
    form = StuForm(request.POST or None, instance=obj)
    context = {"form": form,"code":query}
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        messages.success(request, "Updated post!")
        return HttpResponseRedirect("/home/stuTeachList?q="+query)
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
        return HttpResponseRedirect("/home/")
    return render(request, template, context)


# Can Delete the Student Data
# @login_required(login_url="/admin/")
def delete_view(request , userid=None):
    query = request.GET.get("q", None)
    print (query)
    obj = get_object_or_404(Student, userid=userid)
    context = {"object": obj,"code":query}
    template = "delete.html"
    if request.method == 'POST':
        obj.delete()
        messages.success(request, "Post Deleted...!")
        return HttpResponseRedirect("/home/stuTeachList?q="+query)
    return render(request, template, context)


def delete_view_user(request , id=None):
    obj = get_object_or_404(User, id=id)
    context = {"object": obj}
    if request.method == 'POST':
        obj.delete()
        messages.success(request, "Post Deleted...!")
        return HttpResponseRedirect("/home/")

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
    # print(query)
    # user = User.objects.get(username=request.user.username)
    # print("User NAme" , user )
    enable=Student.objects.filter(Enable="True")
    obj = enable.filter(userid__contains=query
            ).values("userid","category","clas","name","mobileNum",'Enable').order_by('-clas')
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

def create_Taskview(request):
    query = request.GET.get("q", None)
    form = StuTaskForm(request.POST,request.FILES)
    template = "addNewTask.html"
    context = {
            "form" : form,
            "code":query
        }
    context2 = {"form" : form,"code":query}
        # redirect('post_details', id=post_id)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        return HttpResponseRedirect('/home/addTask?q='+query)
    else: 
        form = StuTaskForm()   
    return render(request, template, context)
    # return HttpResponseRedirect('/thanks/')

def stuTaskList(request):
    query = request.GET.get("q", None)
    obj = Stu_Task.objects.filter(school_code=query
            ).values().order_by('-date')
    # print(obj)
    obj_class = Student.objects.order_by().values('clas').distinct()
    context = {
            "object_clist" : obj_class,
            "object_list" : obj,
            "code":query
        }
    template = "allTaskList.html"    
    return render(request, template, context)

def update_Taskview(request, id=None):
    query = request.GET.get("q", None)
    print (query)
    obj = get_object_or_404(Stu_Task, id=id)
    template = "updateTask.html"
    form = StuTaskForm(request.POST or None, instance=obj)
    context = {"form": form,"code":query}
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        messages.success(request, "Updated post!")
        return HttpResponseRedirect("/home/allTask?q="+query)
    return render(request, template, context)

def delete_Taskview(request , id=None):
    query = request.GET.get("q", None)
    # query1=str(query)
    print (query)
    obj = get_object_or_404(Stu_Task, id=id)
    context = {"object": obj,"code":query}
    template = "deleteTask.html"
    if request.method == 'POST':
        obj.delete()
        messages.success(request, "Post Deleted...!")
        return HttpResponseRedirect("/home/?q="+query)
    return render(request, template, context)

def clasSearch(request, clas=None):
    query = request.GET.get("q", None)
    # print(query)
    # print(clas)
    obj = Stu_Task.objects.filter(school_code=query,clas=clas).values().order_by('-date')
    print(obj)
    obj_class = Student.objects.order_by().values('clas').distinct()
    context = {
            "object_clist" : obj_class,
            "object_list" : obj,
            "code":query
        }
    template = "allTaskList.html"    
    return render(request, template, context)

def dateSearch(request):
    query = request.GET.get("q", None)
    print(query)
    date = request.POST.get('date')  
    print(date)      
    form = DateForm(request.POST)
    obj = Stu_Task.objects.filter(school_code=query,date=date).values().order_by('-date')
    print(obj)
    obj_class = Student.objects.order_by().values('clas').distinct()
    context = {
            "object_clist" : obj_class,
            "object_list" : obj,
            "code":query
        }
    template = "allDateTaskList.html"    
    return render(request, template, context)

def create_Teachview(request):
    query = request.GET.get("q", None)
    form = TeachForm(request.POST,request.FILES)
    template = "addNewTeachTask.html"
    context = {
            "form" : form,
            "code":query
        }
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        return HttpResponseRedirect('/home/allTeachTask?q='+query)
    else: 
        form = TeachForm()   
    return render(request, template, context) 

def teachTaskList(request):
    query = request.GET.get("q", None)
    obj = Teach_Task.objects.filter(school_code=query
            ).values().order_by('id')
    # print(obj)
    obj_class = Student.objects.order_by().values('clas').distinct()
    context = {
            "object_clist" : obj_class,
            "object_list" : obj,
            "code":query
        }

    template = "allTechTaskList.html"    
    return render(request, template, context)

def update_TechTaskview(request, id=None):
    query = request.GET.get("q", None)
    print (query)
    obj = get_object_or_404(Teach_Task, id=id)
    template = "updateTask.html"
    form = TeachForm(request.POST or None, instance=obj)
    context = {"form": form,"code":query}
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        messages.success(request, "Updated post!")
        return HttpResponseRedirect("/home/allTeachTask?q="+query)
    return render(request, template, context)

def delete_TechTaskview(request , id=None):
    query = request.GET.get("q", None)
    # query1=str(query)
    print (query)
    obj = get_object_or_404(Teach_Task, id=id)
    context = {"object": obj,"code":query}
    template = "deleteTechTask.html"
    if request.method == 'POST':
        obj.delete()
        messages.success(request, "Post Deleted...!")
        return HttpResponseRedirect("/home/allTeachTask?q="+query)
    return render(request, template, context)

def clastechSearch(request, clas=None):
    query = request.GET.get("q", None)
    # print(query)
    # print(clas)
    obj = Teach_Task.objects.filter(school_code=query,clas=clas).values().order_by('id')
    print(obj)
    obj_class = Student.objects.order_by().values('clas').distinct()
    context = {
            "object_clist" : obj_class,
            "object_list" : obj,
            "code":query
        }
    template = "allTechTaskList.html"    
    return render(request, template, context)

def createFeedview(request):
    query = request.GET.get("q", None)
    form = FeedbackForm(request.POST,request.FILES)
    template = "addFeedback.html"
    context = {
            "form" : form,
            "code":query
        }
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        return HttpResponseRedirect('/home/allFeedback?q='+query)
    else: 
        form = FeedbackForm()   
    return render(request, template, context) 

def feedList(request):
    query = request.GET.get("q", None)
    obj = Feedback.objects.filter(school_code=query
            ).values().order_by('id')
    # print(obj)
    # obj_class = Student.objects.order_by().values('clas').distinct()
    context = {
            # "object_clist" : obj_class,
            "object_list" : obj,
            "code":query
        }

    template = "allfeedList.html"    
    return render(request, template, context)

def update_feedview(request, id=None):
    query = request.GET.get("q", None)
    print (query)
    obj = get_object_or_404(Feedback, id=id)
    template = "updateTask.html"
    form = FeedbackForm(request.POST or None, instance=obj)
    context = {"form": form,"code":query}
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        messages.success(request, "Updated post!")
        return HttpResponseRedirect("/home/allFeedback?q="+query)
    return render(request, template, context)

def delete_feedview(request , id=None):
    query = request.GET.get("q", None)
    # query1=str(query)
    print (query)
    obj = get_object_or_404(Feedback, id=id)
    context = {"object": obj,"code":query}
    template = "deletefeed.html"
    if request.method == 'POST':
        obj.delete()
        messages.success(request, "Post Deleted...!")
        return HttpResponseRedirect("/home/allFeedback?q="+query)
    return render(request, template, context)

# def stuTeachList(request):
#     query = request.GET.get("q", None)
#     print(query)
#     obj = Student.objects.filter(userid__startswith=query,category="STUDENT"
#             ).values("userid","category","name","mobileNum").order_by('-id')
#     context = {
#             "object_list" : obj,
#             "code":query
#         }
#     template = "allList.html"    
#     return render(request, template, context)
 