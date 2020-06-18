from django.contrib import admin
from .models import Student, Video, User, News
from import_export.admin import ImportExportModelAdmin
# Register your models here.

@admin.register(Student, Video, User, News)
class ViewAdmin(ImportExportModelAdmin):
    search_fields = ('userid', 'name','category', 'mobileNum', 'clas')
    odering = ['name']
    

    