from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name='home'),
    path('helloHtml/',views.helloFromHtmlPage, name='homeHtml'),
    path('add-college', views.addCollege, name = 'add_college'),
    path('add-college-manual', views.addCollegeManual, name = 'add_college_manual'),
    path('add-student', views.addStudent, name = 'addStudent'),
    path('edit-student/<int:pk>', views.editStudent, name = 'editStudent'),
    path('delete-student/<int:pk>', views.deleteStudent, name = 'deleteStudent'),
    path('student-list', views.studentList, name = 'studentList'),
    path('testing', views.testing, name='testing'),
    path('homepage', views.homepage, name='homepage'),
    path('upload_profile', views.upload_profile, name='upload_profile'),
    path('show_profiles', views.show_profiles, name='show_profiles'),
    path('students', views.students),
    path('signup/', views.signup_view , name='signup'),
    path('login/', views.login , name='login'),
    path('logout/', views.logout , name='logout'),
]