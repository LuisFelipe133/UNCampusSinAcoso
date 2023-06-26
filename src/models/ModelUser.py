from.entities.User import User
from flask_mysqldb import MySQL
from data.structures.HashTable import HashTable
from data.structures.Queue import Queue

class ModelUser():
    @classmethod
    def login(self,db:MySQL,user:User):
        try:
            cursor = db.connection.cursor()
            sql= """ SELECT usu_id,usu_correo,usu_password FROM usuario 
            WHERE usu_correo LIKE '{}' """.format(user.correo)
            cursor.execute(sql)
            row=cursor.fetchone()
            user_atributes = HashTable()
            user_atributes.insert("id",row[0])
            user_atributes.insert("correo",row[1],)
            user_atributes.insert("password",row[2])
            if row != None:
                user=User(user_atributes.get("id"),user_atributes.get("correo"),User.check_password(user_atributes.get("password"),user.password))
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
            key_atributes = HashTable()
            key_atributes.insert("usr_id",row[0])
            key_atributes.insert("usr_correo",row[1])
            if row != None:
                return User(key_atributes.get("usr_id"), key_atributes.get("usr_correo"), None)
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
    def get_denuncias_curUser(self,db:MySQL,id)->Queue:
        try:
            cursor = db.connection.cursor()
            cursor.callproc('get_denuncias_curUser',(id,))
            results = cursor.fetchall()
            cursor.close()
            db.connection.commit()
            user_denuncias = Queue()
            for j in range(len(results)):
                for i in results[j]:
                    user_denuncias.enqueue(i)
            user_denuncias.printQueue()
            return user_denuncias
        except Exception as e:
            print('Error : ' + e)
    @classmethod
    def get_nombreCompleto_curUser(self,db:MySQL,id)->HashTable:
        try:
            cursor = db.connection.cursor()
            cursor.callproc('get_nombreCompleto_curUser',(id,))
            nombreCompleto = cursor.fetchall()
            cursor.close()
            db.connection.commit()
            nombre = HashTable()
            nombre.insert("nombre",nombreCompleto[0][0])
            return nombre
        except Exception as e:
            print('Error : ' + e)
    
    @classmethod
    def obtenerInformacionEstudiante(self,db:MySQL,id)->HashTable:
        try:
            cursor = db.connection.cursor()
            cursor.callproc('obtenerInformacionEstudiante',(id,))
            info = cursor.fetchall()
            cursor.close()
            db.connection.commit()
            informacion = HashTable()
            informacion.insert("cedula",info[0][0])
            informacion.insert("telefono",info[0][1])
            informacion.insert("genero",info[0][2])
            informacion.insert("edad",info[0][3])
            informacion.printHashTable()
            return informacion
        except Exception as e:
            print('Error : ' + e)
    
    @classmethod
    def get_rol_usuario(self,db:MySQL,id)->HashTable:
        try:
            cursor = db.connection.cursor()
            sql= """ SELECT usu_rol FROM usuario 
            WHERE usu_id = '{}' """.format(id)
            cursor.execute(sql)
            row=cursor.fetchone()
            rol = HashTable()
            rol.insert("rol",row[0])
            print(rol.get("rol"))
            return rol
        except Exception as ex:
            print("EXCEPTION: ",ex.with_traceback)
    
    @classmethod
    def get_all_denuncias(self,db:MySQL)->Queue:
        try:
            cursor = db.connection.cursor()
            cursor.callproc('get_all_denuncias')
            results = cursor.fetchall()
            cursor.close()
            db.connection.commit()
            denuncias = Queue()
            for j in range(len(results)):
                for i in results[j]:
                    denuncias.enqueue(i)
            return denuncias
        except Exception as e:
            print('Error : ',e)

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
            print('Error : ',str(e))