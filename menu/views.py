from django.shortcuts import render

def about(request):
    return render(request, 'about.html')

def index(request):
    return render(request, 'index.html')

def missions(request):
    return render(request,'missions.html')