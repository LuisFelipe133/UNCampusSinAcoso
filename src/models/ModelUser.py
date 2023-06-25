from.entities.User import User
from flask_mysqldb import MySQL

class ModelUser():
    @classmethod
    def login(self,db:MySQL,user:User):
        try:
            cursor = db.connection.cursor()
            sql= """ SELECT usu_id,usu_correo,usu_password FROM usuario 
            WHERE usu_correo LIKE '{}' """.format(user.correo)
            cursor.execute(sql)
            row=cursor.fetchone()
            if row != None:
                user=User(row[0],row[1],User.check_password(row[2],user.password))
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def get_by_id(self, db:MySQL, id):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT usu_id, usu_correo FROM usuario WHERE usu_id = {}".format(id)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                return User(row[0], row[1], None)
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def test(self,db):
        try:
            cursor = db.connection.cursor()
            sql= """ SELECT usu_id,usu_correo,usu_password FROM usuario 
            WHERE usu_correo LIKE '{}' """.format("maria@unal.edu.co")
            cursor.execute(sql)
            row=cursor.fetchone()
            print("row: ",row)
        except Exception as ex:
            print("EXCEPTION: ",ex)

    @classmethod
    def comprobar_conexion(self,db:MySQL):
        try:
            cursor = db.connection.cursor()
            cursor.execute("SELECT 1")
            cursor.close()
            return 'Conexión exitosa a la base de datos'
        except Exception as e:
            return 'Error al conectar a la base de datos: ' + str(e)
    @classmethod
    def get_denuncias_curUser(self,db:MySQL,id):
        try:
            cursor = db.connection.cursor()
            cursor.callproc('get_denuncias_curUser',(id,))
            results = cursor.fetchall()
            cursor.close()
            db.connection.commit()
            return results
        except Exception as e:
            print('Error : ' + e)
    @classmethod
    def get_nombreCompleto_curUser(self,db:MySQL,id):
        try:
            cursor = db.connection.cursor()
            cursor.callproc('get_nombreCompleto_curUser',(id,))
            nombreCompleto = cursor.fetchall()
            cursor.close()
            db.connection.commit()
            return nombreCompleto[0]
        except Exception as e:
            print('Error : ' + e)
    
    @classmethod
    def obtenerInformacionEstudiante(self,db:MySQL,id):
        try:
            cursor = db.connection.cursor()
            cursor.callproc('obtenerInformacionEstudiante',(id,))
            info = cursor.fetchall()
            cursor.close()
            db.connection.commit()
            return info[0]
        except Exception as e:
            print('Error : ' + e)
    
    @classmethod
    def get_rol_usuario(self,db:MySQL,id):
        try:
            cursor = db.connection.cursor()
            sql= """ SELECT usu_rol FROM usuario 
            WHERE usu_id = '{}' """.format(id)
            cursor.execute(sql)
            row=cursor.fetchone()
            return row
        except Exception as ex:
            print("EXCEPTION: ",ex.with_traceback)
    
    @classmethod
    def get_all_denuncias(self,db:MySQL):
        try:
            cursor = db.connection.cursor()
            cursor.callproc('get_all_denuncias')
            results = cursor.fetchall()
            cursor.close()
            db.connection.commit()
            return results
        except Exception as e:
            print('Error : ' + e)

    @classmethod 
    def get_user_id_denuncia(self,db:MySQL,id):
        try:
            cursor = db.connection.cursor()
            cursor.callproc('get_user_id_denuncia',(id,))
            results = cursor.fetchall()
            cursor.close()
            db.connection.commit()
            return results[0]
        except Exception as e:
            print('Error : ' + str(e))
    
    @classmethod
    def delete_denuncia(self,db:MySQL,id):
        try:
            cursor = db.connection.cursor()
            sql= """ DELETE FROM denuncia 
            WHERE den_id = '{}' """.format(id)
            cursor.execute(sql)
        except Exception as e:
            print('Error : ' + str(e))