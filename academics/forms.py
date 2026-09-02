from django import forms

from .models import Course, Subject


class CourseForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = ['name', 'code', 'duration_years']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 border border-slate-200 rounded-lg outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500',
                'placeholder': 'Enter course name'
            }),

            'code': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 border border-slate-200 rounded-lg outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500',
                'placeholder': 'Enter course code'
            }),

            'duration_years': forms.NumberInput(attrs={
                'class': 'w-full px-4 py-3 border border-slate-200 rounded-lg outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500',
                'placeholder': 'Enter duration in years'
            }),
        }


class SubjectForm(forms.ModelForm):

    class Meta:
        model = Subject
        fields = ['course', 'name', 'code', 'semester', 'credit_hours']

        widgets = {
            'course': forms.Select(attrs={
                'class': 'w-full px-4 py-3 border border-slate-200 rounded-lg outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500'
            }),

            'name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 border border-slate-200 rounded-lg outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500',
                'placeholder': 'Enter subject name'
            }),

            'code': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 border border-slate-200 rounded-lg outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500',
                'placeholder': 'Enter subject code'
            }),

            'semester': forms.NumberInput(attrs={
                'class': 'w-full px-4 py-3 border border-slate-200 rounded-lg outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500',
                'placeholder': 'Enter semester'
            }),

            'credit_hours': forms.NumberInput(attrs={
                'class': 'w-full px-4 py-3 border border-slate-200 rounded-lg outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500',
                'placeholder': 'Enter credit hours'
            }),
        }