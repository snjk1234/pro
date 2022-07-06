from django.shortcuts import render

def index(request):
    return render(request,'fressco/index.html')
# Create your views here.

def dashboard(request):
    return render(request, 'fressco/dashboard.html')

def login(request):
    return render(request, 'fressco/login.html')
    
def test(request):
    return render(request, 'fressco/test.html')
    #omar