from django import forms
from firstApp.models import College, Profile, Student

class CollegeForm(forms.ModelForm):
    class Meta:
        model = College
        fields = ['name', 'address', 'established_year']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'age', 'college']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'picture']