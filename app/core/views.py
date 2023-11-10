from django.shortcuts import render
from rest_framework import status, viewsets
from .serializers import BeneficiarioSerializer
from .serializers import EmpleadoSerializer
from .models import Beneficiario
from .models import Empleado
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from .queryset import Employes
from .queryset import Beneficiaries


from rest_framework.response import Response
# Create your views here.
from pdb import set_trace

# Estas vistas Usan el metodo tradicional CREACION,CONSULTA, ACTUALIZACION y ELIMINACION
class EmpleadoViewSet(viewsets.ModelViewSet):
    
    serializer_class = EmpleadoSerializer
    def get_queryset(self):
        
        queryset =  Empleado.objects.filter(**self.request.GET.dict())
        return queryset

class BeneficiarioViewSet(viewsets.ModelViewSet):
    
    serializer_class = BeneficiarioSerializer
    def get_queryset(self):
        
        queryset =  Beneficiario.objects.filter(**self.request.GET.dict())
        return queryset
    

# Estas Vistas hacer lo anterio pero apollandose de STORE PROCEDURES
    
@permission_classes((permissions.AllowAny,))
class EmpleadoProcedureViewSet(APIView):
    def get(self, request, pk=None, format=None):
        if pk:
            employe =  Employes.get_employe(pk)
            return Response(employe, status=status.HTTP_200_OK)
        else:
            employes =  Employes.get_all_employes()
            return Response(employes, status=status.HTTP_200_OK)
        
    def post(self, request):
        serializer=EmpleadoSerializer(data=request.data)
        if serializer.is_valid():
            employe=  Employes(request.data)
            result = employe.create()
        else:
            result = serializer.errors
        
        return Response(result, status=status.HTTP_201_CREATED if result.get('success') else status.HTTP_400_BAD_REQUEST)


    def delete(self,request, pk=None, format=None):
        result =  Employes.delete_employe(pk)
        return Response(result, status=status.HTTP_204_NO_CONTENT if result.get('success') else status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk=None, format=None):
        employe=  Employes(request.data)
        result = employe.update(pk)
        
        return Response(result, status=status.HTTP_200_OK if result.get('success') else status.HTTP_400_BAD_REQUEST)

        

@permission_classes((permissions.AllowAny,))
class BeneficiarioProcedureViewSet(APIView):
    def get(self, request, pk=None, format=None):
        if pk:
            beneficiary =  Beneficiaries.get_beneficiary(pk)
            return Response(beneficiary, status=status.HTTP_200_OK)
        else:
            if request.GET.get('id_empleado'):
                beneficiaries =  Beneficiaries.get_beneficiaries_by_participant(request.GET.get('id_empleado'))
            else:
                beneficiaries =  Beneficiaries.get_all_beneficiaries()
            return Response(beneficiaries, status=status.HTTP_200_OK)
        
    def post(self, request):
        serializer=BeneficiarioSerializer(data=request.data)
        if serializer.is_valid():
            beneficiary=  Beneficiaries(request.data)
            result = beneficiary.create()
        else:
            result = serializer.errors

        
        return Response(result, status=status.HTTP_201_CREATED if result.get('success') else status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request, pk=None, format=None):
        result =  Beneficiaries.delete_beneficiarie(pk)
        return Response(result, status=status.HTTP_204_NO_CONTENT if result.get('success') else status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk=None, format=None):
        beneficiary=  Beneficiaries(request.data)
        result = beneficiary.update(pk)
        
        return Response(result, status=status.HTTP_200_OK if result.get('success') else status.HTTP_400_BAD_REQUEST)