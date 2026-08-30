from django.contrib import admin
from .models import Student

@admin.register(Student)
class Studentadmin(admin.ModelAdmin) : 
    list_display = ("name", "email", "phone", "course")
    list_filter = ("course",)
    search_fields = ("name" , "email")
>>>>>>> 1dc98b9 (Save my work)
