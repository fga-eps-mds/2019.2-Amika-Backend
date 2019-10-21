from django.db import models
from django.db.models import PROTECT, CASCADE

# Create your models here.
class AgendaRealizar(models.Model):
    titulo = models.CharField(max_length=100)   
    texto = models.TextField()
    anexo = models.FileField(upload_to='arquivos')