from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User
from django.shortcuts import HttpResponse
# Create your views here.

# this funtion will add new items
def add_show(request):
    if request.method == "POST":
     fm =StudentRegistration(request.POST)
     if fm.is_valid():
      nm = fm.cleaned_data['name']
      em = fm.cleaned_data['email']
      pw = fm.cleaned_data['password']
      reg = User(name=nm, email=em, password=pw)
      reg.save()
     fm =StudentRegistration()
 
    else:
     fm =StudentRegistration()
    stud= User.objects.all()
    return render(request, 'enroll/addandshow.html',{'form':fm,'stu':stud})

# this function will update and edit

def update_data(request ,id):
  if request.method=='POST':
    pi=User.objects.get(pk=id)
    fm= StudentRegistration(request.POST,instance=pi)
    if fm.is_valid():
     fm.save()
  

  else:
      pi=User.objects.get(pk=id)
      fm= StudentRegistration(instance=pi)
  return render(request,'enroll/update.html',{'form':fm})

# this function will delete data
def delete_data(request,id):
  if request.method=='POST':
    pi = User.objects.get(pk=id)
    pi.delete()
    return HttpResponseRedirect('/')
  

def filter(request):
   stud= User.objects.all()
   if request.method=='POST':
     st=request.Post.get("")
     if st!=None:
        stud= User.objects.filter(name=st)
   data={
     'stud':stud

    }
   return render(request,'addandshow.html',data)
