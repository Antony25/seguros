from django.db import connection
from .models import Empleado
from .serializers import EmpleadoSerializer

from .models import Beneficiario
from .serializers import BeneficiarioSerializer
from .utils import ResultResponse

from pdb import set_trace

cursor =  connection.cursor()

class Employes:
    def __init__(self, data):
        print(data)
        self.data = data


    def create(self ):
        result = ResultResponse()
        
        try:
            with connection.cursor() as cursor:
                query = '''addEmploye @nombre="{nombre}", @apellidos="{apellidos}", \
                @fecha_nacimiento="{fecha_nacimiento}", @numero_empleado={numero_empleado},\
                @curp="{curp}", @ssn="{ssn}", @numero_telefono="{numero_telefono}", @nacionalidad="{nacionalidad}"'''.format(**self.data)

                value= cursor.execute(query)
                if value.rowcount>0:
                    result.success = True
                    result.message = "Creacion Exitosa"
        except Exception as e:
            print(str(e))
            result.message =  str(e)

        return result.to_dict()
        

    @staticmethod
    def get_all_employes() -> list:
        result = []
        try:
            cursor.execute('getEmployes')
            response = cursor.fetchall()
            for element in response:
                result.append(Empleado(*element))
        except Exception as e:
            print(str(e))

        print(result)
        return EmpleadoSerializer(result, many=True).data
    
    @staticmethod
    def get_employe(id) -> dict:
        result = {}
        try:
            cursor.execute(f'getEmploye @id={id}')
            response = cursor.fetchone()
            result=Empleado(*response)
        except Exception as e:
            print(str(e))

        print(result)
        return EmpleadoSerializer(result, many=False).data
        
    
    @staticmethod
    def delete_employe(id) -> dict:
        result = ResultResponse()
        try:
            cursor.execute(f'deleteEmploye @id={id}')
            
            if cursor.rowcount>0:
                result.success = True
                result.message = "Proceso Exitoso"
            else:
                result.message = "Error al eliminar el empleado"
            
        except Exception as e:
            print(str(e))
            result.message = str(e)

        return result.to_dict()
    
    def update(self, id ):
        result = ResultResponse()
        
        try:
            self.data.update({"id":id})
            with connection.cursor() as cursor:
                query = '''updateEmploye @id={id}, @nombre="{nombre}", @apellidos="{apellidos}", \
                @fecha_nacimiento="{fecha_nacimiento}", @numero_empleado={numero_empleado},\
                @curp="{curp}", @ssn="{ssn}", @numero_telefono="{numero_telefono}", @nacionalidad="{nacionalidad}"'''.format(**self.data)

                value= cursor.execute(query)
                if value.rowcount>0:
                    result.success = True
                    result.message = "Actualizacion Exitosa"
                else:
                    result.message =  "Error al realizar la actualizacion"
        except Exception as e:
            print(str(e))
            result.message =  str(e)

        return result.to_dict()


class Beneficiaries:

    def __init__(self, data):
        self.data = data


    def create(self )-> dict:
        result = ResultResponse()
        
        try:
            with connection.cursor() as cursor:
                query = '''addBeneficiary @nombre="{nombre}", @apellidos="{apellidos}", \
                @fecha_nacimiento="{fecha_nacimiento}", @porcentaje={porcentaje},\
                @curp="{curp}", @ssn="{ssn}", @numero_telefono="{numero_telefono}", @nacionalidad="{nacionalidad}",
                @empleado_id={empleado}'''.format(**self.data)
                print(query)

                if cursor.rowcount>0:
                    result.success = True
                    result.message = "Creacion Exitosa"
                else:
                    result.message =  cursor.fetchval()
        except Exception as e:
            print(str(e))
            result.message =  str(e)

        return result.to_dict()


    @staticmethod
    def get_all_beneficiaries() -> list:
        result = []
        try:
            cursor.execute('getBeneficiaries')
            response = cursor.fetchall()
            for element in response:
                result.append(Beneficiario(*element))
        except Exception as e:
            print(str(e))

        print(result)
        return BeneficiarioSerializer(result, many=True).data
    
    @staticmethod
    def get_beneficiary(id) -> dict:
        result = {}
        try:
            cursor.execute(f'getBeneficiarie @id={id}')
            response = cursor.fetchone()
            result=Beneficiario(*response)
        except Exception as e:
            print(str(e))

        print(result)
        return BeneficiarioSerializer(result, many=False).data
    
    @staticmethod
    def get_beneficiaries_by_participant(id) -> list:
        result = []
        try:
            cursor.execute(f'getBeneficiariesByParticipant @id_empleado={id}')
            response = cursor.fetchall()
            for element in response:
                result.append(Beneficiario(*element))
        except Exception as e:
            print(str(e))

        print(result)
        return BeneficiarioSerializer(result, many=True).data
    
    @staticmethod
    def delete_beneficiarie(id) -> dict:
        result = ResultResponse()
        try:
            cursor.execute(f'deleteBeneficiary @id={id}')
            
            if cursor.rowcount>0:
                result.success = True
                result.message = "Proceso Exitoso"
            else:
                result.message = "Error al eliminar el empleado"
            
        except Exception as e:
            print(str(e))
            result.message = str(e)

        return result.to_dict()

    def update(self, id )-> dict:
        result = ResultResponse()
        
        try:
            self.data.update({"id":id})
            with connection.cursor() as cursor:
                query = '''updateBeneficiary @id={id}, @nombre="{nombre}", @apellidos="{apellidos}", \
                @fecha_nacimiento="{fecha_nacimiento}", @porcentaje={porcentaje},\
                @curp="{curp}", @ssn="{ssn}", @numero_telefono="{numero_telefono}", @nacionalidad="{nacionalidad}",\
                @empleado_id={empleado}'''.format(**self.data)
                print(query)
                cursor.execute(query)

                if cursor.rowcount>0:
                    result.success = True
                    result.message = "Actualizacion Exitosa"
                else:
                    try:
                        result.message = cursor.fetchval()
                    except:
                        result.message =  "Error al realizar la actualizacion"
                        
        except Exception as e:
            print(str(e))
            result.message =  str(e)

        return result.to_dict()

