from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.template import Template, Context

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