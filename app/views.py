
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from app.forms import *
# Create your views here.
def Fbv_string(request):
    return HttpResponse('Fbv_string  view is created')

class Cbv_string(View):
    def get(self,request):
        return HttpResponse('Cbv_string view is created')
    
# handling with html page as response('string')

def Fbv_html(request):
    return render(request,'Fbv_html.html')

class Cbv_html(View):
    def get(self,request):
        return render(request,'Cbv_html.html')
    

# handling forms

def Fbv_form(request):
    TFO=TopicForm()
    d={'TFO':TFO}
    if request.method=="POST":
        TFD=TopicForm(request.POST)
        if TFD.is_valid():
            TFD.save()
            return HttpResponse('Data is inserted successfully')
    return render(request,'Fbv_form.html',d)




class Cbv_form(View):
    def get(self,request):
        TFO=TopicForm()
        d={'TFO':TFO}
        return render(request,'Cbv_form.html',d)
    

    def post(self,request):
        TFD=TopicForm(request.POST)
        if TFD.is_valid():
            TFD.save()
            return HttpResponse('Data is submitted successfully')

