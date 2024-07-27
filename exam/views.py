from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def testpaper(request):
    que= "who developed python ?"
    a= "Dennis Ritche "
    b= "Guido van Russan "
    c= "ken thompson "
    d= "Bjarre Stroustrap "
    template=loader.get_template('testpaper.html')
    context= {
       'que': que , 
        'a': a, 
        'b': b,
        'c': c , 
        'd':d }
      
    
    res=template.render(context,request)
    return HttpResponse(res)

def result(request):
   template=loader.get_template('hello.html')
   res1=template.render()
   return HttpResponse(res1)


def template_tags(request):
   template=loader.get_template('child.html')
   res1=template.render()
   return HttpResponse(res1)

