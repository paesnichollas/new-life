from django.contrib import admin
from .models import Categoria, Produto, Depoimento, Contato


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'slug']
    prepopulated_fields = {'slug': ('nome',)}


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'categoria', 'destaque', 'lancamento', 'mais_vendido']
    list_filter = ['categoria', 'destaque', 'lancamento', 'mais_vendido']
    search_fields = ['nome', 'descricao']
    list_editable = ['destaque', 'lancamento', 'mais_vendido']


@admin.register(Depoimento)
class DepoimentoAdmin(admin.ModelAdmin):
    list_display = ['nome_cliente', 'video_youtube_id', 'ativo']
    list_filter = ['ativo']
    list_editable = ['ativo']


@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'assunto', 'data_envio']
    list_filter = ['data_envio']
    readonly_fields = ['data_envio']
    search_fields = ['nome', 'email', 'assunto']

