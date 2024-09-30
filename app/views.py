from django.shortcuts import render,redirect
from .models import *
from django.db.models import Q
# Create your views here.

def insert_Data(request):
    return render(request,"insert.html")

def InsertData(request):
    name_ = request.POST.get('name') 
    email_ = request.POST.get('email')
    city_ = request.POST.get('city')
    number_ = request.POST.get('number')

    image_ = request.FILES.get('image')
    
    if image_ is None:
        print("No image uploaded.")
    

    Student.objects.create(
                Name =  name_,
                Image = image_,
                Email = email_, 
                Number = number_,
                City =  city_, 
                )
    return redirect('showpage')

def showpage(request):
    search = request.GET.get('search')  
    if search:
        all_data = Student.objects.filter(
            Q(Name__icontains=search) |
            Q(Email__icontains=search) |
            Q(id__icontains=search) |
            Q(Number__icontains=search) |
            Q(City__icontains=search) 
        )
    else:
        all_data = Student.objects.all() 
    return render(request, 'add.html', {'key1': all_data})

    
def edit_page(request,pk):
    get_data = Student.objects.get(id=pk)
    return render(request,'edit.html',{'key2':get_data})

def UpdateData(request,pk):
    Udata = Student.objects.get(id=pk)
    Udata.Name = request.POST['name']
    Udata.Image = request.FILES['image']
    Udata.Email = request.POST['email']
    Udata.City = request.POST['city']
    Udata.Number = request.POST['number']
    
    if 'image' in request.FILES:
        Udata.Image = request.FILES['image']
    # query for update 
    Udata.save()
    return redirect('showpage')


def DeleteData(request,pk):
    DData = Student.objects.get(id=pk)
    DData.delete()
    return redirect('showpage')
