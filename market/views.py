from django.shortcuts import render

def go (request):
    return render(request,'market/go.html')
