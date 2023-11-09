CREATE PROCEDURE getAllEmployes
AS
BEGIN
SET NOCOUNT ON
 
SELECT *  FROM core_empleado
 
END

CREATE PROCEDURE getEmploye @id int
AS
BEGIN
SET NOCOUNT ON
 
SELECT *  FROM core_empleado WHERE id=@id
 
END





CREATE PROCEDURE addEmploye
       @nombre                      NVARCHAR(50), 
       @apellidos                   NVARCHAR(50), 
       @fecha_nacimiento            DATE , 
       @numero_empleado             INT,
       @curp             			NVARCHAR(18),
       @ssn             			NVARCHAR(20),
       @numero_telefono             NVARCHAR(10),
       @nacionalidad				NVARCHAR(30)
AS 
BEGIN 
     SET NOCOUNT ON 

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