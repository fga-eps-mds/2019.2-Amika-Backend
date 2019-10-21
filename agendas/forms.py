from django import forms
from uploads.core.models import Document
from . models import AgendaRealizar

class DocumentoForm (forms.ModelForm):
    class Meta: 
        model = AgendaRealizar
        fields = ('texto', 'anexo')