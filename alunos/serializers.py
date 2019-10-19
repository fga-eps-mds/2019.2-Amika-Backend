import datetime

from rest_framework import serializers

from .models import Registro, Periodo, Aluno


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['username', 'first_name', 'last_name', 'password']

    def create(self, validated_data):
        aluno = Aluno.objects.get_or_create(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            registro=Registro.objects.get(
                matricula=int(validated_data['username'])))[0]
        aluno.set_password(validated_data['password'])
        aluno.save()

        return aluno


class RegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registro
        fields = ['matricula', 'turma']

    def create(self, validated_data):
        return Registro.objects.get_or_create(
            matricula=validated_data['matricula'],
            turma=validated_data['turma'],
            periodo=Periodo.objects.get_or_create(
                ano=datetime.date.today().year,
                semestre=1 if datetime.date.today().month <= 6 else 2)[0])[0]
