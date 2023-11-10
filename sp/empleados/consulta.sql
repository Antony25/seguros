CREATE PROCEDURE getEmploye @id int
AS
BEGIN
SET NOCOUNT ON
 
SELECT *  FROM core_empleado WHERE id=@id
 
END


CREATE PROCEDURE getEmployes
AS
BEGIN
SET NOCOUNT ON
 
SELECT *  FROM core_empleado ce 
 
END