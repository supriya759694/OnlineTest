from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
def greeting(request):
    s="<h1>hello welcome to first view</h1>"
    return HttpResponse(s)

def about(request):
    s="<h1>abouit Me</h1>"
    return HttpResponse(s)

def contact(request):
    s="<h1>contact us</h1>"
    return HttpResponse(s)

def custom_tags(request):
   template=loader.get_template('todayfile.html')
   res1=template.render()
   return HttpResponse(res1)
    
def custom_filter(request):
       template=loader.get_template('cusfilter.html')
       test= "python"
       context={
           'test':test
       }
       res1=template.render(context,request)
       return HttpResponse(res1)
    
# Create your views here.
