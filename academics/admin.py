from django.contrib import admin
from .models import Course,Subject

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin) : 
    list_display = ("name" , "code" , "duration_years")
    search_fields = ("name" , "code")

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin) :
    list_display = ("name" , "code" , "semester" , "credit_hours")
    search_fields = ("name" , "code")
    list_filter = ("semester" , "credit_hours")
