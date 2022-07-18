from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

#def login(request):
    #return HttpResponseRedirect(reverse('login'))
def index(request):
    return render(request,'fressco/index.html')
def dashboard(request):
    return render(request, 'fressco/dashboard.html')

def login(request):
    return render(request, 'fressco/login.html')
    
def test(request):
    return render(request, 'fressco/test.html')