# ----------- import statements  ------------

from ast import Assign
from flask import Flask,flash, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime 


# ------------ app initialisation -------------------

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= "sqlite:///ozidesk.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
db=SQLAlchemy(app)

#--------------- models ------------------------------


class Role(db.Model):
    _tablename = "role"
    role_id = db.Column(db.Integer, primary_key=True, unique=True)
    role_name = db.Column(db.String)
    
    def __repr__(self) -> str:
        return f" {self.role_id}-{self.role_name}"
        
class Login(db.Model):
    _tablename="login"
    login_id = db.Column(db.Integer, primary_key=True,unique=True)
    email =db.Column(db.String,unique=True)
    password=db.Column(db.String,unique=True) 
    name=db.Column(db.String)
    mobile=db.Column(db.String)
    role_id=db.Column(db.Integer, db.ForeignKey(Role.role_id))
    type=db.Column(db.String)  

    def __repr__(self) -> str:
        return f" {self.login_id }-{self.email}-{self.password}-{self.name}-{self.mobile}-{self.role_id}-{self.type}"        

class Application(db.Model):
    _tablename="application"
    application_id = db.Column(db.Integer,primary_key=True,unique=True)
    login_id = db.Column(db.Integer, db.ForeignKey(Login.login_id)) 
    start_status=db.Column(db.Integer) 
    submit_status=db.Column(db.Integer)
    hire_status=db.Column(db.Integer)
    score=db.Column(db.Integer)
    
    def __repr__(self) -> str:
        return f" {self.application_id }-{self.login_id}-{self.start_status}-{self.submit_status}-{self.hire_status}-{self.score}"
    
class Question(db.Model):
    _tablename = "question"
    question_id = db.Column(db.Integer, primary_key=True, unique=True)
    question = db.Column(db.String)
    
    def __repr__(self) -> str:
        return f" {self.question_id}-{self.question}"


class Role_question(db.Model):
    _tablename="role_question"
    role_id = db.Column(db.Integer, db.ForeignKey(Role.role_id),primary_key=True) 
    question_id = db.Column(db.Integer, db.ForeignKey(Question.question_id),primary_key=True) 

    def __repr__(self) -> str:
        return f" {self.role_id }-{self.question_id}"        


class Intern_care(db.Model):
    _tablename = "intern_care"
    login_id = db.Column(db.Integer, db.ForeignKey(Login.login_id),primary_key=True) 
    application_id = db.Column(db.Integer, db.ForeignKey(Application.application_id),primary_key=True) 
    qualification = db.Column(db.String)
    city = db.Column(db.String)
    state = db.Column(db.String)
    country = db.Column(db.String)
    source = db.Column(db.String)
    linkedin = db.Column(db.String)

    def __repr__(self) -> str:
        return f" {self.login_id}-{self.application_id}-{self.qualification}-{self.city}-{self.state}-{self.country}-{self.source}-{self.linkedin}"
    

#-------------- Controllers ------------------------------

@app.route("/")
def index():
    return render_template('master.html')

@app.route("/contact", methods=["GET","POST"])
def contact():
    return render_template('contact.html')

@app.route("/about",methods=["GET","POST"])
def about():
    return render_template("about.html")

@app.route("/internships",methods=["GET","POST"])
def internships():
    return render_template("internships.html")

@app.route("/loginrender",methods=["GET","POST"])
def loginrender():
    return render_template('login.html')

@app.route("/login",methods=["GET","POST"])
def login():
    email=request.form['email']
    password=request.form['password']
    f1=Login.query.all()
    for f in f1:
        if email==f.email and password==f.password:
            return render_template('test.html')
    return render_template('login_error.html')


@app.route("/register",methods=["GET","POST"])
def register():
    return render_template("registration.html")

@app.route("/applypage",methods=["GET","POST"])
def applypage():
    return render_template("applypage.html")

#---------------- final application run ------------------

if __name__=="__main__":
    #app.run(debug=True)
    app.run(host='0.0.0.0',port=8080)    

