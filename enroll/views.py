from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms import StudentForm
from .models import Student, Teacher


# Create your views here.
def home(request):
    return render(request,'index.html')

def add_show(request):
    if request.method == 'POST':
        fm = StudentForm(request.POST)
        if fm.is_valid():
            '''nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pwd = fm.cleaned_data['name']
            print(nm,em,pwd)'''
            fm.save()
            '''reg = Student(name=nm, email=em, password=pwd)
            reg.save()'''
            fm = StudentForm()

    else:
        fm = StudentForm()
    stud = Student.objects.all()
    return render(request, 'addandshow.html',{'form':fm,'stu':stud})

def addsht(request):
    if request.method == 'POST':
        nm = request.POST['tname']
        em = request.POST['temail']
        pwd = request.POST['pwd']
        print(nm,em,pwd)
        tmodel = Teacher(name=nm, email=em, password=pwd)
        tmodel.save()
    return render(request, 'addandshow.html')

def delete_rec(request, id):
    if request.method == 'POST':
        pi = Student.objects.get(pk=id)
        pi.delete()
        return redirect('addshow')

def update_rec(request, id):
    pi = Student.objects.get(pk=id)
    if request.method == 'POST':        
        fm = StudentForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        fm = StudentForm(instance=pi, render=True)
    return render(request,'updatestudent.html',{'form':fm})

