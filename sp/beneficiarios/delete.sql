CREATE PROCEDURE deleteBeneficiary @id int
AS
BEGIN
SET NOCOUNT ON
 
DELETE FROM core_beneficiario  WHERE id=@id
 
END