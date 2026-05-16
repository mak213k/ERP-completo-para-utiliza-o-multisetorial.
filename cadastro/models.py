#models.py
from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)
    cnpj = models.CharField(max_length=18)
    cep = models.CharField(max_length=9)
    endereco = models.CharField(max_length=200)
    numero = models.IntegerField()
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)
    celular = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.nome

class Entrega(models.Model):
    remetente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='envios')
    destinatario = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='recebimentos')
    descricao_carga = models.CharField(max_length=200)
    peso = models.DecimalField(max_digits=10, decimal_places=2)
    valor_frete = models.DecimalField(max_digits=10, decimal_places=2)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Entrega {self.id}"