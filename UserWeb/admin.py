from django.contrib import admin
from . models import Users, FeedbackUser,AuthDeleteUser,MCQUser,MCQUser,UnitTest,UnitCount,Feedback,OptionalUnit,TimedOut,ResultUser
# Register your models here.

admin.site.register(Users)
admin.site.register(FeedbackUser)
admin.site.register(AuthDeleteUser)
admin.site.register(MCQUser)
admin.site.register(UnitTest)
admin.site.register(UnitCount)
admin.site.register(Feedback)
admin.site.register(OptionalUnit)
admin.site.register(TimedOut)
admin.site.register(ResultUser)