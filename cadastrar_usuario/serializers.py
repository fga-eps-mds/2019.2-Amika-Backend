from rest_framework import serializers
from .models import Registration

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