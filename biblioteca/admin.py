from django.contrib import admin
from .models import Editora, GeneroLiterario


@admin.register(Editora)
class EditoraAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cnpj', 'criado_em']
    search_fields = ['nome', 'cnpj']
    ordering = ['nome']
    readonly_fields = ['criado_em', 'atualizado_em']


@admin.register(GeneroLiterario)
class GeneroLiterarioAdmin(admin.ModelAdmin):
    list_display = ['nome', 'criado_em']
    search_fields = ['nome']
    ordering = ['nome']
    readonly_fields = ['criado_em', 'atualizado_em']
