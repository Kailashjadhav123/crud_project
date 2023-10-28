from django import forms
from .models import Student


class Add_student(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'