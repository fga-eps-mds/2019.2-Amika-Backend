from rest_framework import serializers
from .models import formulario_felicidade

class FormuarioFelicidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = formulario_felicidade
        fields = '__all__'