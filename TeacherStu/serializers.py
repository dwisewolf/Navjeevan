from rest_framework import serializers
from . models import Student, Video, User, News, Stu_Task, Teach_Task, Feedback

class stuSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'

class videoSerializer(serializers.ModelSerializer):

  class Meta():
    model = Video
    fields = '__all__'

class userSerializer(serializers.ModelSerializer):
	
    class Meta:
        model = User
        fields = '__all__'
        
class newsSerializer(serializers.ModelSerializer):
	
    class Meta:
        model = News
        fields = '__all__'
        
class stuTaskSerializer(serializers.ModelSerializer):

  class Meta():
    model = Stu_Task
    fields = '__all__'
    
class noteSerializer(serializers.ModelSerializer):

  class Meta():
    model = Teach_Task
    fields = '__all__' 
    
class feedbackSerializer(serializers.ModelSerializer):

  class Meta():
    model = Feedback
    fields = '__all__' 
        

        