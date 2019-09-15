from rest_framework import serializers
from .models import UsuarioAluno

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