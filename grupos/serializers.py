from rest_framework import serializers
from .models import Grupo

class GrupoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grupo
        fields = ['nome']

    def create(self, validated_data):
        return Grupo.objects.create(
            nome=validated_data['nome']
        )