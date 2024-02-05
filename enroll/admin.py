from django.contrib import admin
from .models import Student, Teacher
# Register your models here.

class ModelAdminStudent(admin.ModelAdmin):
    list_display = ('id','name','email','password')

class ModelAdminTeacher(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(Student, ModelAdminStudent)
admin.site.register(Teacher, ModelAdminTeacher)