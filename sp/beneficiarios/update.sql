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