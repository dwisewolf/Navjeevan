from django import forms  
from . models import Users
from TeacherStu.models import Student, User, Stu_Task, Teach_Task, Feedback

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

class StuTaskForm(forms.ModelForm):  

    # Enable = forms.BooleanField(widget=forms.CheckboxInput, default=False)

    # def clean(self): 
  
    #     # data from the form is fetched using super function 
    #     super(StuTaskForm, self).clean() 
          
    #     # extract the username and text field from the data 
    #     school_code = self.cleaned_data.get('school_code') 
    #     clas = self.cleaned_data.get('clas') 
    #     subject = self.cleaned_data.get('subject') 
    #     date = self.cleaned_data.get('date') 
    #     video = self.cleaned_data.get('video') 
    #     textbook = self.cleaned_data.get('textbook') 
    #     Notes = self.cleaned_data.get('Notes') 
  
    #     # conditions to be met for the username length 
    #     if date < 5: 
    #         self._errors['username'] = self.error_class([ 
    #             'Minimum 5 characters required']) 
    #     if len(text) <10: 
    #         self._errors['text'] = self.error_class([ 
    #             'Post Should Contain a minimum of 10 characters']) 
  
    #     # return any errors if found 
    #     return self.cleaned_data 


    class Meta:
        model = Stu_Task
        fields = '__all__'

        labels = {
            'school_code': ('School-Code'),
            'clas':('Class'),
            'subject':("Subject"),
            'date':('Choose Date'),
            'video':('Video'),
            'textbook':('TextBook'),
            'Notes':('Notes'),
        }

        widgets = {
            'school_code': forms.TextInput(attrs={'placeholder': 'Enter School-Code','class':'form-control'}),
            'clas': forms.Select(attrs={'id':'choicewa','class':'form-control'}),
            'subject': forms.Select(attrs={'id':'choicewa','class':'form-control'}),
            'date': forms.DateInput( attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'video': forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter Video Description'}),
            'textbook': forms.TextInput(attrs={'class':'form-control','placeholder': 'TextBook'}),
            'Notes': forms.Textarea(attrs={'cols':10,'rows':5,'placeholder': 'Note','class':'form-control'}),
        }

class TeachForm(forms.ModelForm):  

    class Meta:
        model = Teach_Task
        fields = '__all__'

        labels = {
            'school_code': ('School-Code'),
            'clas':('Class'),
            'Notes':('Notes'),
        }

        widgets = {
            'school_code': forms.TextInput(attrs={'placeholder': 'Enter School-Code','class':'form-control'}),
            'clas': forms.Select(attrs={'id':'choicewa','class':'form-control'}),
            'Notes': forms.Textarea(attrs={'cols':10,'rows':5,'placeholder': 'Note','class':'form-control'}),
        } 

class FeedbackForm(forms.ModelForm):  

    class Meta:
        model = Feedback
        fields = '__all__'

        labels = {
            'school_code': ('School-Code'),
            'userid':('User-Id'),
            
            'reply':('Reply'),
            'feedback':('Feedback'),
        }

        widgets = {
            'school_code': forms.TextInput(attrs={'placeholder': 'Enter School-Code','class':'form-control'}),
            'userid': forms.TextInput(attrs={'placeholder': 'Enter User-Id','class':'form-control'}),
            
            'reply': forms.TextInput(attrs={'placeholder': 'Reply','class':'form-control'}),
            'feedback': forms.Textarea(attrs={'cols':10,'rows':5,'placeholder': 'Enter Your Feedback','class':'form-control'}),
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

class DateForm(forms.ModelForm):  

    class Meta:
        model = Stu_Task
        fields = ['video']

        widgets = {
        'date': forms.DateInput(format=('%m/%d/%Y'), attrs={'placeholder':'Select a date', 'type':'date'}),
        }


