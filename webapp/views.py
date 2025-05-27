from django.shortcuts import render
# from dashboard.models import *

# Create your views here.
def home(request):
    return render(request,'webapp/home.html')


def about(request):
    return render(request,'webapp/about.html')    


def term(request):
    return render(request,'webapp/term.html') 

def privacy(request):
    return render(request,'webapp/privacy.html')     