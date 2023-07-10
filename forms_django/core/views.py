from django.shortcuts import render

def home(request):
    return render(request, "core/home.html")

def contact(request):
    return render(request, "core/contact.html")

def about_us(request):
    return render(request, "core/about_us.html")

def servicios(request):
    return render(request, "core/servicios.html")
