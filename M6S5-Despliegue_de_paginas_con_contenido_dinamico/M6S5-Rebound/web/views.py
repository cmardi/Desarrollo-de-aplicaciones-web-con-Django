from django.shortcuts import render

def index(request, palabra):
    
    palabra_fix = palabra.replace(" ","").lower()
    reverso = palabra_fix[::-1]

    if palabra_fix == reverso:
        mensaje = f"{palabra} ES PALÍNDROMO"
    else:
        mensaje = f"{palabra} NO ES PALÍNDROMO"    
    
    context = { "respuesta": mensaje }
    
    return render(request, "palindromo.html", context)
