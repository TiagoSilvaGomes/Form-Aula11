from django import forms
from django.shortcuts import render
from viagens.forms import ViagemForms, PessoaForms

def index(request):
    form= ViagemForms()
    pessoa_form = PessoaForms()
    contexto={'form': form, 'pessoa_form':pessoa_form}
    return render(request, 'index.html', contexto)

def revConsulta(request):
    if request.method =='POST':
        form = ViagemForms(request.POST)
        pessoa_form = PessoaForms(request.POST)
        if form.is_valid():
            contexto={'form': form, 'pessoa_form':pessoa_form}
            return render(request, 'consulta.html', contexto)
        else: 
            print('Form inválido')
            contexto = {'form': form, 'pessoa_form':pessoa_form}
            return render(request, 'index.html', contexto)
