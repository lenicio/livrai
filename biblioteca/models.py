from django.db import models
from django.core.exceptions import ValidationError
from .utils import is_cnpj_valido


class Editora(models.Model):
    nome = models.CharField(
        max_length=200,
        unique=True,
        verbose_name='Nome',
        help_text='Nome da editora'
    )
    cnpj = models.CharField(
        max_length=14,
        unique=True,
        verbose_name='CNPJ',
        help_text='Nº do CNPJ'
    )
    criado_em = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Data de criação',
        help_text='Criado em'
    )
    atualizado_em = models.DateTimeField(
        auto_now=True,
        verbose_name='Data de atualização',
        help_text='Atualizado em'
    )

    def __str__(self):
        return self.nome


    def clean(self):
        super().clean()

        if not is_cnpj_valido(self.cnpj):
            raise ValidationError('O CNPJ não é válido.')

    class Meta:
        verbose_name = 'Editora'
        verbose_name_plural = 'Editoras'


class GeneroLiterario(models.Model):
    nome = models.CharField(
        max_length=200,
        unique=True,
        help_text='Genero Literário',
        verbose_name='Genero Literário'
    )
    criado_em = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Data de criação',
        help_text='Criado em'
    )
    atualizado_em = models.DateTimeField(
        auto_now=True,
        verbose_name='Data de atualização',
        help_text='Atualizado em'
    )

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Genero Literário'
        verbose_name_plural = 'Generos Literários'