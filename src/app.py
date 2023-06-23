from flask import Flask, render_template,request, redirect, url_for, flash
from flask_mysqldb import MySQL
from config import config
from models.ModelUser import ModelUser
from models.entities.User import User
from flask_login import LoginManager,login_user,logout_user,login_required
from flask_wtf.csrf import CSRFProtect
from data.structures.DynamicArray import DynamicArray
from data.structures.NodeList import NodeList
from data.structures.LinkedList import LinkedList
from data.structures.Queue import Queue

app = Flask(__name__) 

csrf = CSRFProtect()

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
                return redirect(url_for('home'))
            else:
                flash("Invalid Password")
                return render_template('auth/login.html')
        else:
            flash("User not found")
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/home')
@login_required
def home():
    return render_template('home.html')



def status_401(error):
    return redirect(url_for('login'))

def status_404(error):
    return "<h1>Página no encontrada</h1>",404


if __name__ == '__main__':
    ''''app.config.from_object(config['development'])
    csrf.init_app(app)
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    app.run()'''
    lista = LinkedList()
    print(lista.isEmpty())
    lista.pushBack(1)
    lista.pushBack(2)
    lista.pushBack(3)
    lista.pushBack(4)
    lista.pushFront(5)
    lista.pushFront(6)
    lista.pushFront(7)
    lista.pushFront(8)
    lista.printList()
    print(lista.topFront())
    print(lista.topBack())
    lista.popBack()
    lista.popFront()
    lista.printList()
    print(lista.contains(5))
    print(lista.findPosition(5))
    print(lista.findNode(2))
    lista.update(2,56)
    lista.printList()



