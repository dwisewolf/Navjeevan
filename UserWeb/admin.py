from django.contrib import admin
from . models import Users, FeedbackUser,AuthDeleteUser
# Register your models here.

admin.site.register(Users)
admin.site.register(FeedbackUser)
admin.site.register(AuthDeleteUser)