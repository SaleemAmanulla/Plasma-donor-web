from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('login.html')

@app.route("/login")
def donate():
     return render_template('login.html')

@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/adminLogin")
def adminlogin():
    return render_template('Admin/adminLogin.html')

@app.route("/adminindex")
def adminindex():
    return render_template('Admin/adminindex.html')