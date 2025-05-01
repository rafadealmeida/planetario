from django.shortcuts import render
from django.http import HttpResponse
from galeria.models import Fotografia

def index(request):
    # fotos = Fotografia.objects.all()
    # fotos = Fotografia.objects.order_by("-data_fotografia")
    fotografia = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True)
    return render(request, 'galeria/index.html', {'cards': fotografia})

def imagem(request,id):
    try:
        foto = Fotografia.objects.get(id=id)
    except Fotografia.DoesNotExist:
        return HttpResponse("Imagem não encontrada", status=404)
    
    return render(request, 'galeria/imagem.html',{"card":foto})


def buscar(request):
    try:
        query = request.GET.get('search') 
        resultados = Fotografia.objects.filter(nome__icontains=query) if query else []
    except Fotografia.DoesNotExist:
        return HttpResponse("Imagem não encontrada", status=404)

    return render(request, 'galeria/buscar.html', {'resultados': resultados, 'query': query})
