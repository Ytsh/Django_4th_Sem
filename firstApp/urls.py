from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name='home'),
    path('helloHtml/',views.helloFromHtmlPage, name='homeHtml'),
    path('add-college', views.addCollege, name = 'add_college'),
    path('add-college-manual', views.addCollegeManual, name = 'add_college_manual'),
    path('add-student', views.addStudent, name = 'addStudent'),
    path('student-list', views.studentList, name = 'studentList'),
    path('testing', views.testing, name='testing'),
    path('homepage', views.homepage, name='homepage'),
]