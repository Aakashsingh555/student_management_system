from django.shortcuts import render
from students.models import Student


def dashboard(request):
    students = Student.objects.all()

    return render(request, 'dashboard.html', {
        'students': students
    })