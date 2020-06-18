from rest_framework import serializers
from . models import Student, Video, User, News

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
        

        