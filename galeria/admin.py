from django.contrib import admin
from .models import Fotografia

@admin.register(Fotografia)
class FotografiaAdmin(admin.ModelAdmin):
    list_display = ("id","nome","legenda","descricao","foto","publicada","data_fotografia")
    list_display_links = ("nome","foto")
    search_fields = ("nome",)
    list_filter = ("categoria",)
    list_per_page = 4
    list_editable = ("publicada",)


# from django.contrib import admin

# # Register your models here.
# # todas as configuracoes ao django admin
# from galeria.models import Fotografia # importe a fotografia
# class ListandoFotografias(admin.ModelAdmin):
#     list_display = ("id","nome","legenda","descricao","foto")
#     list_display_links = ("nome","foto")
#     search_fields = ("nome",)

# admin.site.register(Fotografia,ListandoFotografias) #registre nosso banco de dados no admin
# # carregue agora.