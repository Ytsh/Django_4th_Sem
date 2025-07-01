from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from firstApp.forms import CollegeForm, ProfileForm, StudentForm
from firstApp.models import College, Profile, Student
from firstApp.serializers import StudentSerializer

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
            students = Student.objects.select_related('college').all()
            return render(request, 'student_list.html', {'students':students})
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
    return render(request, 'student_list.html', {'students':students})

def addCollegeManual(request):
    if request.method == "POST":
        name = request.POST.get('name')
        address = request.POST.get('address')
        established_year = request.POST.get('established_year')

        #Validate code here
        college = College(name = name, address = address, established_year = established_year)
        college.save()
        return redirect('studentList')
    return render(request, 'add_college_manual.html')

def testing(request):
    print(request, request.POST.get('name'))

def homepage(request):
    return render(request, 'homePage.html')

def editStudent(request,pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(data = request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('studentList')
    else:
        form = StudentForm(instance=student)
        return render(request, 'edit-student.html', 
                      {'form':form, 'student':student}
                      )
    
def deleteStudent(request,pk):
    if request.method == 'POST':
        student = get_object_or_404(Student, pk = pk)
        student.delete()
        return redirect('studentList')
    
def upload_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show_profiles')
    else:
        form = ProfileForm()
        return render(request, 'upload.html', {'form': form})
    
def show_profiles(request):
    profiles = Profile.objects.all()
    return render(request, 'profile.html',{'profiles':profiles})

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET','POST'])
def students(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many = True)
        return Response(serializer.data) 

# pip install django djangorestframework

