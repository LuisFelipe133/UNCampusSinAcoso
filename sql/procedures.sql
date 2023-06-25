use uncampus;
DELIMITER ??
CREATE PROCEDURE login (IN correo VARCHAR(50))
BEGIN
	SELECT usu_id,usu_correo,usu_password FROM usuario WHERE usu_correo LIKE correo;
END ??
DELIMITER ;

DELIMITER ??
CREATE PROCEDURE get_denuncias_curUser(IN id INT)
BEGIN
	select den_id,den_lugar,den_victimario from denuncia where den_usu_id=id;
END ??
DELIMITER ;

DELIMITER ??
CREATE PROCEDURE get_all_denuncias()
BEGIN
	SELECT * from vw_denuncia_usuarios;
END ??
DELIMITER ;