from django import forms
from . models import AgendaRealizar

class DocumentoForm(forms.ModelForm):
    class Meta: 
        model = AgendaRealizar
        fields = ('titulo', 'texto', 'anexo')