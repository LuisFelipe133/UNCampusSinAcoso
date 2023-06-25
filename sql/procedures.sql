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

DELIMITER //
CREATE PROCEDURE get_nombreCompleto_curUser(IN estudiante_id INT)
BEGIN
    DECLARE nombre_estudiante VARCHAR(50);
    DECLARE apellido_estudiante VARCHAR(50);

    SELECT usu_nombre INTO nombre_estudiante
    FROM usuario
    WHERE usu_id = estudiante_id;
    
    SELECT usu_apellido INTO apellido_estudiante
    FROM usuario
    WHERE usu_id = estudiante_id;

    SELECT CONCAT(nombre_estudiante, ' ', apellido_estudiante) AS nombre_completo;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE obtenerInformacionEstudiante(IN estudiante_id INT)
BEGIN
    SELECT usu_cedula AS Cedula, usu_telefono AS Telefono, usu_genero AS Genero, usu_edad AS Edad
    FROM usuario
    WHERE usu_id = estudiante_id;
END //
DELIMITER ;
DELIMITER ??
CREATE PROCEDURE get_user_id_denuncia(in id INT)
BEGIN
	select den_id,concat(usu_nombre,' ',usu_apellido),den_cantPersonas,den_lugar,
    den_tipo,den_frecuencia,den_victimario,den_descripcion 
    FROM usuario JOIN denuncia ON (usu_id=den_usu_id) WHERE den_id=id;
END ??
DELIMITER ;
