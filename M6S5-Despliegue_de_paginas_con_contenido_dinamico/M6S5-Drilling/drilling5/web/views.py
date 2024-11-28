from django.shortcuts import render

def index(request):
    context = {}
    return render(request, "index.html", context)

def navbar(request):
    context = {}
    return render(request, "navbar.html", context)
