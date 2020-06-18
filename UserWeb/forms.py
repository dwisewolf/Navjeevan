from django import forms  
from . models import Users
from TeacherStu.models import Student, User

class StuForm(forms.ModelForm):  

    # Enable = forms.BooleanField(widget=forms.CheckboxInput, default=False)

    class Meta:
        model = Student
        fields = '__all__'

        labels = {
            'userid': ('User-Id'),
            'name':('Name'),
            'fatherName':("Father Name"),
            'clas':('Choose Class'),
            'section':('Section'),
            'houseName':('HouseName'),
            'address':('Address'),
            'mobileNum':('Mobile Number'),
            'category':("Choose Category"),
        }

        widgets = {
            'userid': forms.TextInput(attrs={'placeholder': 'Enter User-Id','class':'form-control'}),
            'name': forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter Name'}),
            'fatherName': forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter Father Name'}),
            'clas': forms.Select(attrs={'id':'choicewa','class':'form-control'}),
            'section': forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter Section'}),
            'houseName': forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter House Name'}),
            'address': forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter Home Address'}),
            'mobileNum': forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter Mobile Number'}),
            'category': forms.Select(attrs={'id':'choicewa','class':'form-control'}),
        }

class UserForm(forms.ModelForm):  

    class Meta:
        model = User
        fields = '__all__'

        labels = {
            'mobileNum': ('Mobile Number'),
            'password':('Password'),
        }
        
        attrs = {
        "type": "password"
    }        

        widgets = {
            'mobileNum': forms.TextInput(attrs={'placeholder': 'Enter Mobile Number','class':'form-control'}),
            'password': forms.PasswordInput(attrs={"type": "password", 'class':'form-control'}),
            #'password': forms.PasswordInput(attrs={'placeholder':'********','autocomplete': 'off','data-toggle': 'password'}),
        }

class UsersLoginForm(forms.ModelForm):  

    class Meta:
        model = Users
        fields = ['name','password']

        password = forms.CharField(widget=forms.PasswordInput)
        widgets = {
            'password': forms.PasswordInput(attrs={'class': 'input-text with-border', 'placeholder': 'Enter Password'}),
            'name': forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter User Name'}),
        }
        labels = {
            'name': ('User Name'),
            'password':('Password'),
            }
