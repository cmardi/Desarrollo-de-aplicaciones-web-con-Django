from django.urls import path
from .views import index, navbar

urlpatterns = [
    path("", index, name = "index" ),
    path("navbar/", navbar, name = "navbar" ),    
]