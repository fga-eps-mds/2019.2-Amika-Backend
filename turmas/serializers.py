from .models import Turma, Periodo
from rest_framework import serializers
import datetime

class TurmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turma
        fields = ['nome']

    def create(self, validated_data):
        return Turma.objects.get_or_create(
            nome=validated_data['nome'],
            periodo=Periodo.objects.get_or_create(
                ano=datetime.date.today().year,
                semestre=1 if datetime.date.today().month <= 6 else 2)[0])[0]

class TurmaPeriodoSerializer(serializers.ModelSerializer):
    ano = serializers.ReadOnlyField(source='periodo.ano')
    semestre = serializers.ReadOnlyField(source='periodo.semestre')

    class Meta:
        model = Turma
        fields = ('nome', 'ano', 'semestre')