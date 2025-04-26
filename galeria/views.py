from django.shortcuts import render
from django.http import HttpResponse
from galeria.models import Fotografia

def index(request):
    fotos = Fotografia.objects.all()
    # fotos = Fotografia.objects.order_by("-data_fotografia")
    return render(request, 'galeria/index.html', {'cards': fotos})

def imagem(request,id):
    try:
        foto = Fotografia.objects.get(id=id)
    except Fotografia.DoesNotExist:
        return HttpResponse("Imagem não encontrada", status=404)
    
    return render(request, 'galeria/imagem.html',{"card":foto})



