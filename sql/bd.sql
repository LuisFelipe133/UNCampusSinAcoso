CREATE SCHEMA UNcampus;
use UNcampus;
-- DROP SCHEMA UNcampus;
CREATE TABLE usuario(
    usu_id INT PRIMARY KEY auto_increment, 
    usu_cedula VARCHAR(10),
    usu_nombre VARCHAR(50),
    usu_apellido VARCHAR(50),
    usu_correo VARCHAR(50),
    usu_telefono VARCHAR(12),
    usu_genero VARCHAR(10),
    usu_edad INT,
    usu_rol VARCHAR(10),
    usu_password CHAR(102)
);
CREATE TABLE denuncia(
    den_id INT PRIMARY KEY auto_increment,
    den_usu_id INT,
    den_tipo VARCHAR(50),
    den_frecuencia VARCHAR(50),
    den_victimario VARCHAR(50),
    den_descripcion VARCHAR(300),
    den_fecha DATE,
    den_isAtendido BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (den_usu_id) REFERENCES usuario(usu_id)
);
