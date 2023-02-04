from rest_framework import serializers
from .models import *


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = [
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
        ]