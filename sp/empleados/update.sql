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