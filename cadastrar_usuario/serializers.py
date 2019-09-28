from rest_framework import serializers
from .models import Aluno, Registration

class AlunoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Aluno
		fields = '__all__'

	def create(self, validated_data):
		aluno = Aluno(
			nome=validated_data['nome'],
			matricula=validated_data['matricula'],
			email=validated_data['email'],
			senha=validated_data['senha'],
		)
		aluno.save()
		return aluno

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = "__all__"

        def create(self, validated_data):
            registration = Registration(
                registration_field=validated_data['matricula'],
                class_field=validated_data['turma'],
            )
            registration.save()
            return registration

class EditarAlunoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Aluno
		fields = "__all__"
