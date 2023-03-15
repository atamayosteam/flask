from flask import Flask, render_template, request,redirect
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash



app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "Anthony": generate_password_hash("hello"),
    "Tamayo": generate_password_hash("bye")
}

@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username

todos= ["read more","learn tennis"]

@app.route("/todo")
def index():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM `todos`")
    cursor.execute("SELECT * FROM `todos` ORDER BY `Complete`")
    results = cursor.fetchall()

    return render_template(
        "todo.html.jinja",
        todos=results
    )
@app.route("/add", methods=['POST'])
@auth.login_required
def add():
    new_todo= request.form['new_todo']
    cursor = connection.cursor()

    return redirect(('/todo'))

app.route("/Complete", methods=["POST"])
@auth.login_required
def complete():
    todo_id = request.form['todo_id']

    cursor= connection.cursor()

    cursor.execute(f"UPDATE `todos` SET `Complete` =1 WHERE `id` ={todo_id}")

    return redirect("/todo")



import pymysql
import pymysql.cursors


connection = pymysql.connect(
    host = "10.100.33.60",
    user = "atamayo",
    password = "220886964",
    database="atamayo_flask",
    cursorclass=pymysql.cursors.DictCursor,
    autocommit = True
)


