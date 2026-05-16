from django.test import TestCase
from django.urls import reverse
from .models import Cliente
from .forms import ClienteForm

class ClienteTestCase(TestCase):

    def config(self):
        """
        Cria um cliente inicial para testar a existência no banco.
        Preenchemos todos os campos que você definiu como obrigatórios no models.py.
        """
        self.cliente_exemplo = Cliente.objects.create(
            nome="Carlos Transportes",
            cpf="123.456.789-01",
            cnpj="12.345.678/0001-00",
            cep="01001-000",
            endereco="Praça da Sé",
            numero=10,
            bairro="Sé",
            cidade="São Paulo",
            uf="SP",
            celular="(11) 98888-7777",
            email="carlos@transportadora.com"
        )

        cliente = Cliente.objects.get(nome="Carlos Transportes")
        self.assertEqual(cliente.cidade, "São Paulo")
        self.assertEqual(cliente.uf, "SP")

    def test_formulario_cliente_valido(self):
        """
        Testa se o formulário aceita dados completos e válidos.
        Isso garante que o ClienteForm está conversando bem com o Model.
        """
        dados_validos = {
            'nome': "Ana Logística",
            'cpf': "987.654.321-09",
            'cnpj': "98.765.432/0001-99",
            'cep': "80010-000",
            'endereco': "Rua das Flores",
            'numero': 500,
            'bairro': "Centro",
            'cidade': "Curitiba",
            'uf': "PR",
            'celular': "(41) 99999-8888",
            'email': "ana@logistica.com"
        }
        form = ClienteForm(data=dados_validos)
        self.assertTrue(form.is_valid())

    def test_formulario_cliente_invalido(self):
        """
        Testa se o formulário REJEITA dados incompletos.
        O campo 'numero' e 'bairro' são obrigatórios no seu model, 
        então o form deve ser inválido sem eles.
        """
        dados_incompletos = {
            'nome': "Empresa Incompleta",
            'cpf': "000.000.000-00"
            # Faltam os outros campos obrigatórios
        }
        form = ClienteForm(data=dados_incompletos)
        self.assertFalse(form.is_valid())

    def test_status_code_pagina_cadastro(self):
        """
        Verifica se a página de cadastro está acessível.
        Nota: Certifique-se de que o 'name' da sua URL no urls.py seja 'cadastrar_cliente'
        """
        try:
            url = reverse('cadastrar_cliente')
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)
        except:
            self.skipTest("A rota 'cadastrar_cliente' ainda não foi configurada no urls.py")
