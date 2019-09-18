from rest_framework import serializers
from .models import UsuarioAluno, Registration

class UsuarioAlunoSerializer(serializers.ModelSerializer):
	class Meta:
		model = UsuarioAluno
		fields = '__all__'

	def create(self, validated_data):
		aluno = UsuarioAluno(
			nome_aluno=validated_data['nome_aluno'],
			matricula_aluno=validated_data['matricula_aluno'],
			email_aluno=validated_data['email_aluno'],
			senha_aluno=validated_data['senha_aluno'],
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
		model = UsuarioAluno
		fields = "__all__"
