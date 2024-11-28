from django.shortcuts import HttpResponse

def index(request):
    return HttpResponse("Bienvenido a mi sitio de libros")
