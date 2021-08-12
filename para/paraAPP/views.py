from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, "index.html")

def about_us(request):
    return render(request, "about_us.html")

def press(request):
    return render(request, "press.html")
