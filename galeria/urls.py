from django.urls import path
from galeria.views import index
from galeria.views import imagem
from galeria.views import buscar

urlpatterns = [
    path('', index,name='index'),
    path('imagem/<int:id>/', imagem, name='imagem'),
    path('buscar/', buscar, name='buscar'),
]