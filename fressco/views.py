from django.shortcuts import render

def index(request):
    return render(request,'page1/index.html')
# Create your views here.
