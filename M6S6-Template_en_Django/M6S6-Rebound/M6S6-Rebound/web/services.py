class Libro(object):
    def __init__(self, titulo, autor, valoracion):
        self.titulo = titulo
        self.autor = autor
        self.valoracion = valoracion
        
libro1 = Libro("Django 3 Web Development Cookbook Fourth Edition", "Aidas Bendoraitis", 3250)
libro2 = Libro("Two Scoops of Django 3.x", "Daniel Feldroy", 1570)
libro3 = Libro("El libro de Django", "Adrian Holovaty", 1400)
libro4 = Libro("Python Web Development with Django", "Jeff Forcier", 1450)
libro5 = Libro("Django for Professionals", "William S. Vincent", 2100)
libro6 = Libro("Django for APIs", "William S. Vincent", 2540)



lista_libros = [libro1, libro2, libro3, libro4, libro5, libro6]