from .models import Turma
from rest_framework import serializers

class TurmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turma
        fields = ['id','nome_turma', 'ano_turma', 'periodo_turma']

    def create(self, validated_data):
    	turma_atual = Turma(
    		nome_turma = validated_data['nome_turma'],
      		ano_turma = validated_data['ano_turma'],
      		periodo_turma = validated_data['periodo_turma'],
    	)
    	turma_atual.save()
    	return turma_atual
