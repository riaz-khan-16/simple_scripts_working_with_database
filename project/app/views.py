from django.shortcuts import render

# Create your views here.

from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import User



def index(request):
    x=User.objects.all()
    context = {
    'x':x
     }
    return render(request,"index.html",context )

def add(request):

    if request.method=='POST':
        name=request.POST['name']
        age=request.POST['age']
        salary=request.POST['salary']
      
        
        print(name,age,salary)
        x=User.objects.create(name=name,age=age,salary=salary)
        x.save()
        return redirect('index')

    return render(request,"add.html")


    
def update(request,id):
    
    if request.method=='POST':
        x=User.objects.get(id=id)
        name=request.POST['name']
        age=request.POST['age']
        salary=request.POST['salary']
        x.name=name
        x.age=age
        x.salary=salary
        x.save()
        return redirect('index')

    
    x=User.objects.get(id=id)
   
    context = {
    'x':x
     }
    

    return render(request,"update.html",context )

    # x.name='updated Name'
    # x.salary='updated Salry'
    # x.save()
    # return redirect('index')

def delete(request,id):
   x=User.objects.get(id=id)
   x.delete()
   print('Deleted')

   return redirect('index')


