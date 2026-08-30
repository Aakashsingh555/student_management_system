from django import forms

from .models import Student


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ['name', 'email', 'phone', 'course']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 border border-slate-200 rounded-lg outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500',
                'placeholder': 'Enter student name'
            }),

            'email': forms.EmailInput(attrs={
                'class': 'w-full px-4 py-3 border border-slate-200 rounded-lg outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500',
                'placeholder': 'Enter email address'
            }),

            'phone': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 border border-slate-200 rounded-lg outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500',
                'placeholder': 'Enter phone number'
            }),

            'course': forms.Select(attrs={
                'class': 'w-full px-4 py-3 border border-slate-200 rounded-lg outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500'
            }),
        }