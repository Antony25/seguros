from .models import Beneficiario
from .models import Empleado

from rest_framework import serializers


class EmpleadoSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model= Empleado
        fields = '__all__'

class BeneficiarioSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model= Beneficiario
        fields = '__all__'