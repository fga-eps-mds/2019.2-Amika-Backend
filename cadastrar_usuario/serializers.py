from rest_framework import serializers
from .models import Registration

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = "__all__"

        def create(self, validated_data):
            matricula = Registration(
                matricula=validated_data['matricula'],
                turma=validated_data['turma'],
            )
            matricula.save()
            return matricula