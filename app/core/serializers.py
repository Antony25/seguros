from .models import Beneficiario
from .models import Empleado

from rest_framework import serializers
from .utils import getAge
from pdb import set_trace


class EmpleadoSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    def validate(self, data):
        age = getAge(data.get('fecha_nacimiento'))
        if age <18:
            raise serializers.ValidationError({"fecha_nacimiento": "Es menor a 18 años"})
        if len(data.get('numero_telefono'))<10:
            raise serializers.ValidationError({"numero_telefono": "La longitud del numero de telefono debe ser de 10"})
        return data

    class Meta:
        model= Empleado
        fields = '__all__'

class BeneficiarioSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    def validate(self, data):
        age = getAge(data.get('fecha_nacimiento'))
        if age <18:
            raise serializers.ValidationError({"fecha_nacimiento": "Es menor a 18 años"})
        if len(data.get('numero_telefono'))<10:
            raise serializers.ValidationError({"numero_telefono": "La longitud del numero de telefono debe ser de 10"})
        return data

    class Meta:
        model= Beneficiario
        fields = '__all__'