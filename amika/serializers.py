from rest_framework import serializers

from .models import *


class TurmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turma
        fields = '__all__'


class RegistroSerializer(serializers.ModelSerializer):
    turma = serializers.CharField(max_length=2, min_length=1)
    ano = serializers.ReadOnlyField(source='periodo.ano')
    semestre = serializers.ReadOnlyField(source='periodo.semestre')

    class Meta:
        model = Registro
        fields = ['id', 'matricula', 'turma', 'ano', 'semestre']

    def validate_turma(self, descricao):
        if not Turma.objects.filter(descricao=descricao):
            raise serializers.ValidationError("Turma não encontrada.")
        return descricao

    def create(self, validated_data):
        return Registro.objects.get_or_create(
            matricula=validated_data['matricula'],
            turma=Turma.objects.get(descricao=validated_data['turma']),
            periodo=Periodo.objects.get_or_create(ano=ano(), semestre=semestre())[0])[0]


class AlunoSerializer(serializers.ModelSerializer):
    grupo = serializers.CharField(max_length=100, allow_null=True, default=None)

    class Meta:
        model = Aluno
        fields = ['id', 'username', 'first_name', 'last_name', 'password', 'grupo']

    def validate_grupo(self, nome):
        if nome and not Grupo.objects.filter(nome=nome):
            raise serializers.ValidationError("Grupo não encontrado.")
        return nome

    def create(self, validated_data):
        aluno = Aluno.objects.get_or_create(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            registro=Registro.objects.get(matricula=validated_data['username']),
            grupo=None)[0]
        aluno.set_password(validated_data['password'])
        aluno.save()

        return aluno

    def update(self, aluno, validated_data):
        if validated_data.get('password'):
            aluno.set_password(validated_data['password'])

        if validated_data.get('grupo'):
            aluno.grupo = Grupo.objects.get(nome=validated_data['grupo'])

        aluno.save()
        return aluno


class GrupoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grupo
        fields = '__all__'


class AgendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agenda
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if kwargs:
            kwargs['data']['tipo'] = kwargs['data']['tipo'].capitalize()

    def validate(self, data):
        if data['data_disponibilizacao'] > data['data_encerramento']:
            raise serializers.ValidationError({"error": "Data de disponibilização maior do que a de encerramento."})
        return data

def ano():
    return date.today().year


def semestre():
    return 1 if date.today().month <= 6 else 2

class AgendaRealizarSerializer(serializers.ModelSerializer):
    agenda_relacionada = serializers.ReadOnlyField(source='agenda.nome')
    class Meta:
        model = AgendaRealizar
        fields = '__all__'