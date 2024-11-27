from django.urls import path
from .views import index

urlpatterns = [
    path("palindromo/<str:palabra>", index, name = "index" ),    
]
