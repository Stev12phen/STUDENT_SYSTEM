from . models import Student, Lecture
from django import forms

class StudentForm(forms.ModelForm):
    class Meta:
        model= Student
        fields= '__all__'

        