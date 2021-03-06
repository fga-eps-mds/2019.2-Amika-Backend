from rest_framework import serializers

from .models import *


def ano():
    return date.today().year


def semestre():
    return 1 if date.today().month <= 6 else 2


class TurmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turma
        fields = '__all__'


class FormularioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formulario
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
    formulario = FormularioSerializer(many=True, allow_null=True, default=None)

    class Meta:
        model = Aluno
        fields = ['id', 'username', 'first_name', 'last_name', 'password', 'grupo', 'formulario', 'foto']

    def validate_username(self, matricula):
        if not Registro.objects.filter(matricula=matricula):
            raise serializers.ValidationError("Matrícula não registrada.")
        return matricula

    def validate_grupo(self, nome):
        if nome and not Grupo.objects.filter(nome=nome):
            raise serializers.ValidationError("Grupo não encontrado.")
        return nome

    def create(self, validated_data):
        aluno = Aluno.objects.create_user(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            password=validated_data['password'],
            registro=Registro.objects.get(matricula=validated_data['username']))

        return aluno

    def update(self, aluno, validated_data):
        if validated_data.get('password'):
            aluno.set_password(validated_data['password'])

        if validated_data.get('grupo'):
            aluno.grupo = Grupo.objects.get(nome=validated_data['grupo'])

        if validated_data.get('formulario'):
            formulario = Formulario.objects.filter(tipo=validated_data['formulario'][0]['tipo']).first()
            if formulario:
                formulario.pontuacao = validated_data['formulario'][0]['pontuacao']
                formulario.save()
            else:
                formulario = Formulario.objects.create(tipo=validated_data['formulario'][0]['tipo'],
                                                       pontuacao=validated_data['formulario'][0]['pontuacao'])

            aluno.formulario.add(formulario)

        if validated_data.get('foto'):
            aluno.foto = validated_data['foto']

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
        if kwargs and kwargs.get('data') and kwargs['data'].get('tipo'):
            kwargs['data']['tipo'] = kwargs['data']['tipo'].capitalize()

    def validate(self, data):
        if data['data_disponibilizacao'] > data['data_encerramento']:
            raise serializers.ValidationError({"error": "Data de disponibilização maior do que a de encerramento."})
        return data


class AgendaRealizadaSerializer(serializers.ModelSerializer):
    agenda = serializers.PrimaryKeyRelatedField(read_only=False, queryset=Agenda.objects.all())
    aluno = serializers.PrimaryKeyRelatedField(read_only=False, queryset=Aluno.objects.all())

    class Meta:
        model = AgendaRealizada
        fields = '__all__'

    def update(self, instance, validated_data):
        if validated_data.get('texto'):
            instance.texto = validated_data['texto']
        if validated_data.get('anexo'):
            instance.anexo = validated_data['anexo']

        instance.save()
        return instance


class HumorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Humor
        fields = '__all__'

    def create(self, validated_data):

        print(validated_data['aluno'])
        data = date.today()
        if not Humor.objects.filter(data = data,aluno = Aluno.objects.get(pk=validated_data['aluno'])):
            humor = Humor.objects.create(
                humor_do_dia = validated_data['humor_do_dia'],
                aluno = Aluno.objects.get(pk=validated_data['aluno']),
                data = date.today()
            )
            humor.save()
            return humor
        else:
            raise serializers.ValidationError({"error": "Você já adicionou seu humor hoje!"})


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'
