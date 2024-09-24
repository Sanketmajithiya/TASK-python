
from django.shortcuts import render, redirect
from .forms import studentform
from .models import student
from django.utils import timezone


def dashboard(request):
    search = request.GET.get("search")
    if search:
        students = student.objects.filter(first_name__icontains=search)
    else:
        students = student.objects.all()
    context = {
        'students': students
    }
    
    return render(request,"web/data.html",context)

def add(request):
    if request.method == 'POST':
        form = studentform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = studentform()        
        
    context = {
        'form': form,
    }
    
    return render(request, 'web/add.html',context)
    
def index(request):
    search = request.GET.get("search")
    if search:
        students = student.objects.filter(first_name__icontains=search)
        print(students)
        
        

def delete(request,student_id):
    get_stu = student.objects.get(id=student_id)
    get_stu.delete()
    return redirect('dashboard') 

       
def edit(request,student_id):
    get_stu = student.objects.get(id=student_id)
    
    if request.method == 'POST':
        edit_stu = studentform(request.POST, instance=get_stu)
        if edit_stu.is_valid():
            edit_stu.save()
            return redirect('dashboard')        
    
    context = {
        'form':studentform(instance=get_stu)
    }
    return render(request, 'web/edit.html', context)    
        
        