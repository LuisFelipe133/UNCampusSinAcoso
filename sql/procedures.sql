use uncampus;
DELIMITER ??
CREATE PROCEDURE login (IN correo VARCHAR(50))
BEGIN
	SELECT usu_id,usu_correo,usu_password FROM usuario WHERE usu_correo LIKE correo;
END ??
DELIMITER ;