from flask import Flask, render_template,request, redirect, url_for, flash, session, get_flashed_messages
from datetime import date
from flask_mysqldb import MySQL
from config import config
from models.ModelUser import ModelUser
from models.entities.User import User
from flask_login import LoginManager,login_user,logout_user,login_required
from data.structures.DynamicArray import DynamicArray
from data.structures.LinkedList import LinkedList
from data.structures.Queue import Queue
from data.structures.NodeTree import NodeTree
from data.structures.BST import BST
from data.structures.AVL import AVL
from data.structures.Heap import Heap
from data.structures.DisjointSet import DisjointSet
from data.structures.HashTable import HashTable
from data.structures.Graph import Graph

app = Flask(__name__) 

db = MySQL(app)
login_manager_app=LoginManager(app)


@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(db,id)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method=='POST':
        user = User(0,request.form['username'],request.form['password'])
        logged_user = ModelUser.login(db,user)
        if logged_user!=None:
            if logged_user.password:
                login_user(logged_user)
                session['user_id'] = logged_user.id
                rol:HashTable = ModelUser.get_rol_usuario(db,session['user_id'])
                role = rol.get("rol")
                User.setUserRol(role)

                if role == 'estudiante':
                    return redirect(url_for('home'))
                elif role == 'psicologo':
                    return redirect(url_for('homeDoc'))
            else:
                flash("Invalid Password")
                return render_template('auth/login.html')
        else:
            flash("User not found")
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')

@app.route('/perfil',methods=['POST'])
@login_required
def perfil():
    if request.method=='POST':
        user_id = session['user_id']
        results:Queue=ModelUser.get_denuncias_curUser(db,user_id)
        nombreCompleto=ModelUser.get_nombreCompleto_curUser(db,user_id)
        info:HashTable=ModelUser.obtenerInformacionEstudiante(db,user_id)
        return render_template('auth/perfil.html',denuncias=results, nombreCompleto=nombreCompleto,info=info)

        
    
@app.route('/delete',methods=['POST'])
@login_required
def deleteDen():
    if request.method=='POST':
        id_den = request.form["id_denuncia_del"]
        ModelUser.delete_denuncia(db,id_den)
        user_id = session['user_id']
        results=ModelUser.get_denuncias_curUser(db,user_id)
        nombreCompleto:HashTable=ModelUser.get_nombreCompleto_curUser(db,user_id)
        info=ModelUser.obtenerInformacionEstudiante(db,user_id)
        return render_template('auth/perfil.html',denuncias=results, nombreCompleto=nombreCompleto,info=info)

@app.route('/deletePsi',methods=['POST'])
@login_required
def deleteDenPsi():
    if request.method=='POST':
        id_den = request.form["id_denuncia_del"]
        ModelUser.delete_denuncia(db,id_den)
        user_id = session['user_id']
        results:Queue=ModelUser.get_all_denuncias(db)
        return render_template('auth/denunciasDoc.html',denuncias=results)
        

@app.route('/verDen',methods=['POST'])
@login_required
def verInfo_denuncias():
    if request.method=="POST":
        den_id = request.form["id_denuncia"]
        denuncia_id=den_id
        results2:Queue=ModelUser.get_user_id_denuncia(db,den_id)
        return render_template('auth/denWin.html',detalles=results2)
    

@app.route('/denuncias',methods=['POST'])
@login_required
def denuncias():
    if request.method=='POST':
        user_id = session['user_id']
        results=ModelUser.get_all_denuncias(db)
        print(results)
        return render_template('auth/denunciasDoc.html',denuncias=results)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/home', methods=['GET', 'POST'])
@login_required
def home():
        messages = get_flashed_messages()
        return render_template('home.html', messages=messages)

@app.route('/homeDoc', methods=['GET', 'POST'])
@login_required
def homeDoc():
        messages = get_flashed_messages()
        return render_template('homeDoc.html', messages=messages)

@app.route('/backHome')
def backHome():
    messages = get_flashed_messages()
    if User.getUserRol() == 'estudiante':
        return render_template('home.html', messages=messages)
    elif User.getUserRol() == 'psicologo':
        return render_template('homeDoc.html', messages=messages)


@app.route('/enviar', methods=['POST'])
def enviar():
    cantPersonas = request.form['cantPersonas']
    lugar = request.form['lugar']
    tipoDeAgresion = request.form['tipoDeAgresion']
    frecuencia = request.form['frecuencia']
    ejercidoPor = request.form['ejercidoPor']
    descripcion = request.form['descripcion']

    cursor = db.connection.cursor()
    user_id = session['user_id']
    logged_user = ModelUser.get_by_id(db, user_id)
    sql = ("INSERT into denuncia(den_usu_id,den_cantPersonas, den_lugar, den_tipo, den_frecuencia, den_victimario, den_descripcion) VALUES (%s,%s, %s, %s, %s, %s, %s)")
    valores = (int(logged_user.id),int(cantPersonas), lugar, tipoDeAgresion, frecuencia, ejercidoPor, descripcion)
    cursor.execute(sql, valores)
    db.connection.commit()
    cursor.close()
    db.connection.close()
    flash('El formulario ha sido enviado correctamente', 'success')

    if User.getUserRol() == 'estudiante':
        return redirect(url_for('home'))
    elif User.getUserRol() == 'psicologo':
        return redirect(url_for('homeDoc'))

    




def status_401(error):
    return redirect(url_for('login'))

def status_404(error):
    return "<h1>Página no encontrada</h1>",404




if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    app.run()

    
    



    
   


