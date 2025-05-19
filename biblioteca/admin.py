from django.contrib import admin
from .models import Editora, GeneroLiterario, Livro


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



@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ['nome', 'genero_literario', 'editora']
    autocomplete_fields = ['genero_literario', 'editora']
    list_filter = ['genero_literario', 'editora']