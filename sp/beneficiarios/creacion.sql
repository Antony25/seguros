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
        PRINT  N'Los beneficiarios exceden el 100%'
        RETURN RAISERROR (N'Los beneficiarios exceden el 100 porciento', 16, 1)
    END
    
END 

GO