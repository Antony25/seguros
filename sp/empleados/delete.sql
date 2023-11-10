CREATE PROCEDURE deleteEmploye @id int
AS
BEGIN
SET NOCOUNT ON
 
DELETE FROM core_empleado WHERE id=@id
 
END