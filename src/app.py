from flask import Flask, render_template,request, redirect, url_for, flash
from flask_mysqldb import MySQL
from config import config
from models.ModelUser import ModelUser
from models.entities.User import User
from flask_login import LoginManager,login_user,logout_user,login_required
from flask_wtf.csrf import CSRFProtect
from data.structures.DynamicArray import DynamicArray
from data.structures.LinkedList import LinkedList
from data.structures.Queue import Queue
from data.structures.NodeTree import NodeTree
from data.structures.BST import BST
from data.structures.AVL import AVL
from data.structures.Heap import Heap
from data.structures.DisjointSet import DisjointSet
from data.structures.HashTable import HashTable

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
    '''hashy = HashTable()
    print(hashy.hashFunctionInt(57))
    print(hashy.hashFunctionString("Blue Sky"))
    hashy.insert(5,"2-5")
    hashy.insert(21,"2-21")
    hashy.insert(37,"2-37")
    hashy.insert(53,"2-53")
    hashy.insert(4,"2-4")
    hashy.insert(16,"2-16")
    hashy.insert(20,"2-20")'''
    hashy2 = HashTable()
    hashy2.insert(4,"hola")
    hashy2.insert(4,"glugluglu")
    hashy2.insert(5,"mark")
    hashy2.insert(10,56)
    hashy2.insert("hello","there")
    #print(hashy2)
    hashy2.printHashTable()
    hashy2.delete(5)
    #print(hashy2)
    hashy2.printHashTable()
    print(hashy2.find("asdas"))

    
    



    
   


