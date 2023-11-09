
CREATE PROCEDURE getBeneficiarie @id int
AS
BEGIN
SET NOCOUNT ON
SELECT id, empleado_id, nombre, apellidos, fecha_nacimiento, porcentaje, curp, ssn, numero_telefono, nacionalidad  FROM core_beneficiario WHERE id=@id
END

CREATE PROCEDURE getBeneficiariesByParticipant @id_empleado int
AS
BEGIN
SET NOCOUNT ON
SELECT id, empleado_id, nombre, apellidos, fecha_nacimiento, porcentaje, curp, ssn, numero_telefono, nacionalidad  FROM core_beneficiario WHERE empleado_id=@id_empleado
END


CREATE PROCEDURE getBeneficiaries
AS
BEGIN
SET NOCOUNT ON
SELECT id, empleado_id, nombre, apellidos, fecha_nacimiento, porcentaje, curp, ssn, numero_telefono, nacionalidad  FROM core_beneficiario 
END