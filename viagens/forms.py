from django import forms
from tempus_dominus.widgets import DatePicker
from datetime import datetime

class ViagemForms (forms.Form):
    origem = forms.CharField(label = 'origem', max_length= 100)
    destino = forms.CharField(label = 'Destino', max_length= 100)
    data_ida = forms.DateField(label = 'Ida', widget=DatePicker())
    data_volta = forms.DateField(label = 'Volta', widget=DatePicker())
    data_pesquisa = forms.DateField(label = 'Data pesquisa', disabled=True, initial=datetime.today)