from django.shortcuts import render

def home_view(request):
    return render(request,'home.html')

def about_view(request):
    return render(request,'about.html')

def services_view(request):
    return render(request,'services.html')

def career_view(request):
    return render(request,'careers.html')

def contact_view(request):
    return render(request,'contact.html')

def media_view(request):
    return render(request,'media.html')