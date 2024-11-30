from django.shortcuts import render
from .models import Libro

def index(request):
    libros = Libro.objects.all()
    
    print(libros)
    
    context = { "libros": libros }
    return render(request, "index.html", context)
