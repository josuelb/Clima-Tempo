import email
from django.db import models

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length= 100, null = False)
    data_Nasc = models.DateField(null = False)
    sexo = models.CharField(max_length = 1)
    cpf = models.CharField(max_length = 11 , unique= True, null= False)
    email = models.EmailField(null = False)
    senha = models.CharField(max_length = 15 , null = False)

    class Meta:
        abstract = True


class Cliente(Pessoa):
    situacao = models.CharField(null = False, max_length = 6)
    data_insc = models.DateTimeField(auto_now_add = True, null = False)
    cep_principal = models.CharField(max_length = 8 ,null = False)



