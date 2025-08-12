from django import forms
from firstApp.models import College, CustomUser, Profile, Student

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
from django.contrib.auth.forms import UserCreationForm
class CustomUserSignupForm(UserCreationForm):
    ROLE_CHOICES = [
        ('Student', 'Student'),
        ('College', 'College'),
        ('Admin', 'Admin'),
    ]
    full_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    role = forms.ChoiceField(choices=ROLE_CHOICES)
    class Meta:
        model = CustomUser
        fields = ['email','full_name', 'role', 'password1', 'password2']

class IndependentForm(forms.Form):
    full_name = forms.CharField(max_length=100)
    email = forms.EmailField()