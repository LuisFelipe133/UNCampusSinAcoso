use UNcampus;
CREATE VIEW vw_insertUsers AS SELECT 
	usu_cedula,usu_nombre,usu_apellido,usu_correo,usu_telefono,usu_genero,usu_edad,usu_rol,usu_password
	from usuario;

INSERT INTO vw_insertUsers VALUES 
	('1045871234','Maria','Rodriguez','maria@unal.edu.co','15756975369','femenino',21,'estudiante','123'),
	('7502439813','Maria','Gomez','maria.gomez@unal.edu.co','89965739149','femenino',26,'estudiante','123'),
	('3768256912','Juan','Perez','juan.perez@unal.edu.co','57536289106','masculino',20,'estudiante','123'),
	('8135762349','Ana','Rodriguez','ana.rodriguez@unal.edu.co','76841972530','femenino',22,'estudiante','123'),
	('9145632097','Pedro','Gonzalez','pedro.gonzalez@unal.edu.co','69623956370','masculino',25,'estudiante','123'),
	('6358729410','Luis','Lopez','luis.lopez@unal.edu.co','95286713549','masculino',28,'estudiante','123'),
	('7659842103','Maria','Gonzalez','maria.gonzalez@unal.edu.co','71593024826','femenino',18,'estudiante','123'),
	('5893641752','Ana','Lopez','ana.lopez@unal.edu.co','86395901763','femenino',21,'psicologo','123'),
	('9871564230','Juan','Gomez','juan.gomez@unal.edu.co','74560312528','masculino',27,'psicologo','123'),
	('3245987631','Luis','Gonzalez','luis.gonzalez@unal.edu.co','64208957623','masculino',24,'estudiante','123'),
	('4732519068','Maria','Perez','maria.perez@unal.edu.co','43218036209','femenino',23,'psicologo','123');