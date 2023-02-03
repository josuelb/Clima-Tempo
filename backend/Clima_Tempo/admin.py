
from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Cliente)
class Clientes(admin.ModelAdmin):
    list_display = (
        'id',
        'nome',
        'data_Nasc',
        'sexo',
        'cpf',
        'email',
        'senha',
        'situacao',
        'data_insc',
        'cep_principal'
     )

    list_display_links = (
        'id',
        'nome',
        'cpf',
        'email'
    )
    search_fields = (
        'id',
        'nome',
        'cpf',
        'email'

    )