from django.http import HttpResponse
from django.shortcuts import redirect, render

from firstApp.forms import CollegeForm, StudentForm
from firstApp.models import Student

# Create your views here.

def home(request):
    return HttpResponse("Hellow from firstApp")

def helloFromHtmlPage(request):
    context = {
        'title':'Welcome!',
        'message':'This template is loaded'
    }
    return render(request,'home.html',context)

def addCollege(request):
    if request.method == 'POST':
        form = CollegeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('studentList')
    else:
        form = CollegeForm()
    return render(request,'add_college.html', {'form':form})

def addStudent(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('studentList')
    else:
        form = StudentForm()
    return render(request,'add_student.html', {'form':form})

def studentList(request):
    students = Student.objects.select_related('college').all()
    print(students[0].college.name)
    return render(request, 'student_list.html', {'students':students})

