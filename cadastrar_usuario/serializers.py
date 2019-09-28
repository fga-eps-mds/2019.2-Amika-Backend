from rest_framework import serializers

from .models import Aluno, Registro


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'

    def create(self, validated_data):
        aluno = Aluno.objects.create(
            nome=validated_data['nome'],
            matricula=validated_data['matricula'],
            email=validated_data['email'],
            senha=validated_data['senha'])

        return aluno


class RegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registro
        fields = "__all__"

    def create(self, validated_data):
        registration = Registro.objects.create(
            registration_field=validated_data['matricula'],
            class_field=validated_data['turma'])

        return registration


class EditarAlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = "__all__"
