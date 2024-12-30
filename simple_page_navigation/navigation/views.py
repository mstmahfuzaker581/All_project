from django.shortcuts import render
from django.http import HttpResponse

def about(request):
    return render(request,'navigation/about.html')
def contact(request):
   return render(request,'navigation/contact.html')

