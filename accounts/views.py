from django.shortcuts import render
from students.models import Student
from academics.models import Course


def dashboard(request):
    students = Student.objects.all()
    total_students = Student.objects.count()
    total_course = Course.objects.count()

    return render(request, 'dashboard.html', {
        'students': students,
        'total_students': total_students,
        'total_course' : total_course,
    })