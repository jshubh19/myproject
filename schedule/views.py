from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import Template, Context


from django.http import Http404,HttpResponse,HttpResponseRedirect, BadHeaderError
#from schedule.forms import ContactForm
from .forms import *
from django.core.mail import send_mail, get_connection
from .models import *

import datetime

from django.views.generic import ListView

from django.contrib.auth.models import User
from django.contrib import messages

# for message for userregistration on same page



class Myview(ListView):
    def get (self,request):
        return HttpResponse("<h1>welcome to Django classbased views</h1>")




def data_fetch(request):
    obj=Doctor.objects.all()
    return render(request,'doctor.html',{'doc':obj})






def Temp(request):
    c=Context({'Name':'Shubham','lname':'Jangid'})
    t=Template("<h1>Welcome to your Template {{Name}}-{{lname}}</h1>")
    x=t.render(c)
    return HttpResponse(x)


def curdate(request):
    dt=datetime.datetime.now()
    c=Context({'name':dt})
    t=Template("<h1>this is {{name}}</h1>")
    x=t.render(c)
    return HttpResponse(x)

def hoursahead(request,offset):
    offset = int(offset)
    dt=datetime.datetime.now()
    time=datetime.timedelta(hours=offset)
    rs=dt+time
    c=Context({'name':dt,'ntime':time,'nrs':rs})
    t=Template("<h1>this is {{name}}, after adding time {{ntime}}, result is {{nrs}}</h1>")
    x=t.render(c)
    return HttpResponse(x)

def input(request):
    return render(request,'basic.html')

def inputb(request):
    return render(request,'index.html')

def contact(request):




    if request.method =='POST':
        form=StudentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save(commit=True)

            name = form.cleaned_data['name']
            last_name=form.cleaned_data['last_name']
            location=form.cleaned_data['location']
            email=form.cleaned_data['email']
            image=form.cleaned_data['image']
            file=form.cleaned_data['file']
            return HttpResponseRedirect('/contact/completed/')

            #try:
             #   send_mail('name','last_name','location','email',['abc@mail.com'],'image','file')
            #except:
             #   return HttpResponse('Error sending mail')
            #return redirect('completed')
    else:
        form=StudentForm()
    return render(request,'Contact_form.html',{'form':form})



def completed(request):
    return HttpResponse('<h1> Thank you</h1>')


def user_registration(request): # user creation for admin panel
    if request.method=='POST':
        obj=UserForm(request.POST)
        if obj.is_valid():
            username=obj.cleaned_data['username']
            first_name=obj.cleaned_data['first_name']
            last_name=obj.cleaned_data['last_name']
            email=obj.cleaned_data['email']
            password=obj.cleaned_data['password']
            User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)

            messages.success(request,'User Registration Successfully!')
            return HttpResponseRedirect('/user/')

    else:
        obj=UserForm()
    return render(request,'registration.html',{'obj':obj})


#def user_creation_succesfully(request):
  #  return HttpResponse("User Create Successfully")