from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
#Function based
def Home(request):
    #print(request.method)
         if(request.method=="GET"):
            return HttpResponse("Welcome to Django")
         
def Index(request):
      if(request.method=="GET"):
            return HttpResponse("Index")