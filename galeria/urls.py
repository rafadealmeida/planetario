from django.urls import path
from galeria.views import index

#boa prática de programação
urlpatterns = [
    path('', index),
]