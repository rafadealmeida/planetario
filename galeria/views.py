from django.shortcuts import render

def index(request):
    return render(request,'galeria/index.html')

def contato(request):
    return render(request,'galeria/contato.html')

