from random import choices
from secrets import choice
from django import forms
from django.forms import Textarea
from tempus_dominus.widgets import DatePicker
from datetime import datetime
from viagens.classe_viagem import tipos_de_classe
from viagens.validar import campo_temNumero, origem_destino_iguais
from viagens.validar import *
from viagens.models import Viagem, ClasseViagem, Pessoa



class ViagemForms(forms.ModelForm):
    data_pesquisa = forms.DateField(label='Data da pesquisa', disabled=True, initial=datetime.today)

    class Meta:
        model = Viagem
        fields = '__all__'
        labels = {'data_ida': 'Data de Ida', 'data_volta':'Data de volta','informacoes': 'Informações', 'classe_viagem': 'Tipo de Voo'}

    widgets = {

        'data_ida ': DatePicker(),
        'data_volta': DatePicker()

    }

    
    

    def clean(self):
        origem = self.cleaned_data.get('origem')
        destino = self.cleaned_data.get('destino')
        data_ida = self.cleaned_data.get('data_ida')
        data_volta = self.cleaned_data.get('data_volta')
        data_pesquisa = self.cleaned_data.get('data_pesquisa')

        listaErros = {}
        campo_temNumero(origem, 'origem', listaErros)
        campo_temNumero(destino, 'destino', listaErros)
        origem_destino_iguais(origem, destino, listaErros)
        compara_data_ida_volta(data_ida, data_volta, listaErros)
        compara_data_ida_pesquisa(data_ida, data_pesquisa, listaErros)
        if listaErros is not None:
            for erro in listaErros:
                mensagem_erro = listaErros[erro]
                self.add_error(erro, mensagem_erro)
        return self.cleaned_data

class PessoaForms(forms.ModelForm):
    class Meta:
        model = Pessoa
        exclude = ['nome']