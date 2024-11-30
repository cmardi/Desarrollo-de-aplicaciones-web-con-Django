from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    fecha_publicacion = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    num_paginas = models.IntegerField(default=100)
    imagen = models.URLField()
    
    def __str__(self):
        return self.titulo


    
