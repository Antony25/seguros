from django.core.management.base import BaseCommand

from django.db import connection



PROCEDURE_CONSULTA_BENEFICIARIO = ['''CREATE PROCEDURE getBeneficiarie @id int
AS
BEGIN
SET NOCOUNT ON
SELECT id, empleado_id, nombre, apellidos, fecha_nacimiento, porcentaje, curp, ssn, numero_telefono, nacionalidad  FROM core_beneficiario WHERE id=@id
END''',

'''CREATE PROCEDURE getBeneficiariesByParticipant @id_empleado int
AS
BEGIN
SET NOCOUNT ON
SELECT id, empleado_id, nombre, apellidos, fecha_nacimiento, porcentaje, curp, ssn, numero_telefono, nacionalidad  FROM core_beneficiario WHERE empleado_id=@id_empleado
END''',

'''CREATE PROCEDURE getBeneficiaries
AS
BEGIN
SET NOCOUNT ON
SELECT id, empleado_id, nombre, apellidos, fecha_nacimiento, porcentaje, curp, ssn, numero_telefono, nacionalidad  FROM core_beneficiario 
END''']

SP_CREACION_BENEFICIARIO = '''
CREATE PROCEDURE addBeneficiary
       @nombre                      NVARCHAR(50) , 
       @apellidos                   NVARCHAR(50), 
       @fecha_nacimiento            DATE , 
       @porcentaje                  INT,
       @curp                        NVARCHAR(18),
       @ssn                         NVARCHAR(20),
       @numero_telefono             NVARCHAR(10),
       @nacionalidad                NVARCHAR(30),
       @empleado_id                 INT
AS 
BEGIN 
       
    IF ((SELECT COALESCE(SUM(porcentaje),0)+@porcentaje from core_beneficiario cb  where cb.empleado_id =@empleado_id) <= 100) 
    
    BEGIN TRY
    
    INSERT INTO core_beneficiario 
          (                    
            nombre,
            apellidos,
            fecha_nacimiento,
            porcentaje,
            curp,
            ssn,
            numero_telefono,
            nacionalidad,
            empleado_id
          ) 
    VALUES 
          ( 
            @nombre,
            @apellidos,
            @fecha_nacimiento,
            @porcentaje,
            @curp,
            @ssn,
            @numero_telefono,
            @nacionalidad,
            @empleado_id
          ) 

    END TRY
    BEGIN CATCH
        DECLARE @ErrorMessage varchar(100)
        DECLARE @ErrorSeverity varchar(100)
        DECLARE @ErrorState varchar(100)
        SET @ErrorMessage  = ERROR_MESSAGE()
        SET @ErrorSeverity = ERROR_SEVERITY()
        SET @ErrorState    = ERROR_STATE()
        
        RAISERROR (@ErrorMessage, @ErrorSeverity, @ErrorState)
        
    END CATCH
       
    ELSE
    BEGIN 
	    DECLARE @customError VARCHAR(50)
	    set @customError= N'Los beneficiarios exceden el 100%'
        SELECT  @customError

        
    END 
    
END 


'''
SP_BORRADO_BENEFICIARIO = '''
CREATE PROCEDURE deleteBeneficiary @id int
AS
BEGIN
SET NOCOUNT ON
 
DELETE FROM core_beneficiario  WHERE id=@id
 
END
'''

SP_ACTUALIZACION_BENEFICIARIO = '''
CREATE PROCEDURE updateBeneficiary
       @id                          INT, 
       @nombre                      NVARCHAR(50)=NULL, 
       @apellidos                   NVARCHAR(50)=NULL,
       @fecha_nacimiento            DATE=NULL,
       @porcentaje                  INT=NULL,
       @curp             			NVARCHAR(18)=NULL,
       @ssn             			NVARCHAR(20)=NULL,
       @numero_telefono             NVARCHAR(10)=NULL,
       @nacionalidad				NVARCHAR(30)=NULL,
       @empleado_id                 INT=NULL 
AS 
BEGIN 
 
    IF ((SELECT COALESCE(SUM(porcentaje),0)+COALESCE(@porcentaje, (SELECT porcentaje FROM core_beneficiario WHERE id=@id)) FROM core_beneficiario cb  WHERE cb.empleado_id =COALESCE(@empleado_id, (SELECT empleado_id FROM core_beneficiario WHERE id=@id)) AND  id!=@id) <= 100) 
    BEGIN
    UPDATE core_beneficiario 
    SET  nombre = IsNull(@nombre, nombre),
    apellidos = IsNull(@apellidos, apellidos),
    fecha_nacimiento = IsNull(@fecha_nacimiento, fecha_nacimiento),
    porcentaje = IsNull(@porcentaje, porcentaje),
    curp = IsNull(@curp, curp),
    ssn = IsNull(@ssn, ssn),
    numero_telefono = IsNull(@numero_telefono, numero_telefono),
    nacionalidad = IsNull(@nacionalidad, nacionalidad),
    empleado_id = IsNull(@empleado_id, empleado_id)
    
    WHERE id = @id
    END
    ELSE
    BEGIN 
    	DECLARE @customError VARCHAR(50)
	    set @customError= N'Los beneficiarios exceden el 100%'
        SELECT  @customError
    END 

END 
'''

PROCEDURE_CONSULTA_EMPLEADO = ['''CREATE PROCEDURE getEmploye @id int
AS
BEGIN
SET NOCOUNT ON
 
SELECT *  FROM core_empleado WHERE id=@id
 
END''',

'''
CREATE PROCEDURE getEmployes
AS
BEGIN
SET NOCOUNT ON
 
SELECT *  FROM core_empleado ce 
 
END'''] 

SP_CREACION_EMPLEADO= '''
CREATE PROCEDURE addEmploye
       @nombre                      NVARCHAR(50) , 
       @apellidos                   NVARCHAR(50), 
       @fecha_nacimiento            DATE , 
       @numero_empleado             INT,
       @curp             			NVARCHAR(18),
       @ssn             			NVARCHAR(20),
       @numero_telefono             NVARCHAR(10),
       @nacionalidad				NVARCHAR(30)
AS 
BEGIN 
 

     INSERT INTO core_empleado
          (                    
            nombre,
            apellidos,
            fecha_nacimiento,
            numero_empleado,
            curp,
            ssn,
            numero_telefono,
            nacionalidad
          ) 
     VALUES 
          ( 
            @nombre,
            @apellidos,
            @fecha_nacimiento,
            @numero_empleado,
            @curp,
            @ssn,
            @numero_telefono,
            @nacionalidad
          ) 

END 
'''

SP_BORRADO_EMPLEADO = '''
CREATE PROCEDURE deleteEmploye @id int
AS
BEGIN
SET NOCOUNT ON
 
DELETE FROM core_empleado WHERE id=@id
 
END
'''
SP_ACTUALIZACION_EMPLEADO = '''
CREATE PROCEDURE updateEmploye
       @id                          INT, 
       @nombre                      NVARCHAR(50)=NULL, 
       @apellidos                   NVARCHAR(50)=NULL,
       @fecha_nacimiento            DATE=NULL,
       @numero_empleado             INT=NULL,
       @curp             			NVARCHAR(18)=NULL,
       @ssn             			NVARCHAR(20)=NULL,
       @numero_telefono             NVARCHAR(10)=NULL,
       @nacionalidad				NVARCHAR(30)=NULL 
AS 
BEGIN 
 

    UPDATE core_empleado 
    SET  nombre = IsNull(@nombre, nombre),
    apellidos = IsNull(@apellidos, apellidos),
    fecha_nacimiento = IsNull(@fecha_nacimiento, fecha_nacimiento),
    numero_empleado = IsNull(@numero_empleado, numero_empleado),
    curp = IsNull(@curp, curp),
    ssn = IsNull(@ssn, ssn),
    numero_telefono = IsNull(@numero_telefono, numero_telefono),
    nacionalidad = IsNull(@nacionalidad, nacionalidad)
    
    WHERE id = @id

END 

'''
class Command(BaseCommand):
    help = 'Add Rpocedustes'



    def handle(self, *args, **options):
        print("PRocedures")

        try:
            with connection.cursor() as cursor:
                for item in PROCEDURE_CONSULTA_BENEFICIARIO:
                    try:
                        cursor.execute(item)

                        print ("agregado procedure")
                    except Exception as e:
                        print("error al agregar=>", str(e))
                print("Seagregaron SP de consulta para beneficiario")
                try:
                    cursor.execute(SP_CREACION_BENEFICIARIO)
                    print ("agregado procedure")
                except Exception as e:
                    print("error al agregar=>", str(e))
                print("Seagregaron SP de creacion para beneficiario")
                try:
                    cursor.execute(SP_BORRADO_BENEFICIARIO)
                    print ("agregado procedure")
                except Exception as e:
                    print("error al agregar=>", str(e))
                print("Seagregaron SP de borrado para beneficiario")
                try:
                    cursor.execute(SP_ACTUALIZACION_BENEFICIARIO)
                    print ("agregado procedure")
                except Exception as e:
                    print("error al agregar=>", str(e))
                print("Seagregaron SP de actualizacion para beneficiario")
            
                for item in PROCEDURE_CONSULTA_EMPLEADO:
                    try:
                        cursor.execute(item)

                        print ("agregado procedure")
                    except Exception as e:
                        print("error al agregar=>", str(e))
                print("Seagregaron SP de consulta para beneficiario")
                try:
                    cursor.execute(SP_CREACION_EMPLEADO)
                    print ("agregado procedure")
                except Exception as e:
                    print("error al agregar=>", str(e))
                print("Seagregaron SP de creacion para beneficiario")
                try:
                    cursor.execute(SP_BORRADO_EMPLEADO)
                    print ("agregado procedure")
                except Exception as e:
                    print("error al agregar=>", str(e))
                print("Seagregaron SP de borrado para beneficiario")
                try:
                    cursor.execute(SP_ACTUALIZACION_EMPLEADO)
                    print ("agregado procedure")
                except Exception as e:
                    print("error al agregar=>", str(e))
                print("Seagregaron SP de actualizacion para beneficiario")



                print("PROCESO FINALIZADO SP CREADOS")

        except Exception as e:
            print(str(e))