use UNcampus;
CREATE VIEW vw_insertUsers AS SELECT 
	usu_cedula,usu_nombre,usu_apellido,usu_correo,usu_telefono,usu_genero,usu_edad,usu_rol,usu_password
	from usuario;

INSERT INTO vw_insertUsers VALUES 
	('1045871234','Maria','Rodriguez','maria@unal.edu.co','15756975369','femenino',21,'estudiante','pbkdf2:sha256:600000$FddyXnIUXIxQ6gVV$ce3c3a0f7c9676465989a8caa68a8d15b7a18752d20477ec98ef887da53ad041'),
	('7502439813','Maria','Gomez','maria.gomez@unal.edu.co','89965739149','femenino',26,'estudiante','pbkdf2:sha256:600000$FddyXnIUXIxQ6gVV$ce3c3a0f7c9676465989a8caa68a8d15b7a18752d20477ec98ef887da53ad041'),
	('3768256912','Juan','Perez','juan.perez@unal.edu.co','57536289106','masculino',20,'estudiante','pbkdf2:sha256:600000$FddyXnIUXIxQ6gVV$ce3c3a0f7c9676465989a8caa68a8d15b7a18752d20477ec98ef887da53ad041'),
	('8135762349','Ana','Rodriguez','ana.rodriguez@unal.edu.co','76841972530','femenino',22,'estudiante','pbkdf2:sha256:600000$FddyXnIUXIxQ6gVV$ce3c3a0f7c9676465989a8caa68a8d15b7a18752d20477ec98ef887da53ad041'),
	('9145632097','Pedro','Gonzalez','pedro.gonzalez@unal.edu.co','69623956370','masculino',25,'estudiante','pbkdf2:sha256:600000$FddyXnIUXIxQ6gVV$ce3c3a0f7c9676465989a8caa68a8d15b7a18752d20477ec98ef887da53ad041'),
	('6358729410','Luis','Lopez','luis.lopez@unal.edu.co','95286713549','masculino',28,'estudiante','pbkdf2:sha256:600000$FddyXnIUXIxQ6gVV$ce3c3a0f7c9676465989a8caa68a8d15b7a18752d20477ec98ef887da53ad041'),
	('7659842103','Maria','Gonzalez','maria.gonzalez@unal.edu.co','71593024826','femenino',18,'estudiante','pbkdf2:sha256:600000$FddyXnIUXIxQ6gVV$ce3c3a0f7c9676465989a8caa68a8d15b7a18752d20477ec98ef887da53ad041'),
	('5893641752','Ana','Lopez','ana.lopez@unal.edu.co','86395901763','femenino',21,'psicologo','pbkdf2:sha256:600000$FddyXnIUXIxQ6gVV$ce3c3a0f7c9676465989a8caa68a8d15b7a18752d20477ec98ef887da53ad041'),
	('9871564230','Juan','Gomez','juan.gomez@unal.edu.co','74560312528','masculino',27,'psicologo','pbkdf2:sha256:600000$FddyXnIUXIxQ6gVV$ce3c3a0f7c9676465989a8caa68a8d15b7a18752d20477ec98ef887da53ad041'),
	('3245987631','Luis','Gonzalez','luis.gonzalez@unal.edu.co','64208957623','masculino',24,'estudiante','pbkdf2:sha256:600000$FddyXnIUXIxQ6gVV$ce3c3a0f7c9676465989a8caa68a8d15b7a18752d20477ec98ef887da53ad041'),
	('4732519068','Maria','Perez','maria.perez@unal.edu.co','43218036209','femenino',23,'psicologo','pbkdf2:sha256:600000$FddyXnIUXIxQ6gVV$ce3c3a0f7c9676465989a8caa68a8d15b7a18752d20477ec98ef887da53ad041');