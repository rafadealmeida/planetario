from django.urls import path
from galeria.views import index,contato

#boa prática de programação
urlpatterns = [
    path('', index),
    path("contato", contato)
]