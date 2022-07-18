from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

def go(request):
    return render(request,'market/go.html')
def menu(request):
    return render(request,'market/menu.html')
