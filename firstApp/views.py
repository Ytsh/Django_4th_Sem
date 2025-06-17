from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from firstApp.forms import CollegeForm, StudentForm
from firstApp.models import College, Student

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
    return render(request, 'student_list.html', {'students':students})

def addCollegeManual(request):
    if request.method == "POST":
        name = request.POST.get('name')
        address = request.POST.get('address')
        established_year = request.POST.get('established_year')

        #Validate code here
        college = College(name = name, address = address, established_year = established_year)
        college.save()
        return redirect('add_college')
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
