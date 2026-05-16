from django.shortcuts import render, redirect
from .forms import ClienteForm, EntregaForm
from .models import Cliente, Entrega

def cadastrar_cliente(request):
    print('chegou aqui')
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadastro')
    else:
        form = ClienteForm()
    return render(request, 'cadastro/cadastro.html', {'form': form})

def gerar_entrega(request):
    if request.method == 'POST':
        form = EntregaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_entregas')
    else:
        form = EntregaForm()
    return render(request, 'cadastro/entrega_form.html', {'form': form})

def lista_entregas(request):
    entregas = Entrega.objects.all().order_by('-data_criacao')
    return render(request, 'cadastro/lista_entregas.html', {'entregas': entregas})