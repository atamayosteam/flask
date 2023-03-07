from flask import Flask, render_template, request,redirect


app = Flask(__name__)

bucketlist= ["skydiving","Ear-piercings"]

@app.route("/")
def index():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM `Todos`")

    results = cursor.fetchall()

    return render_template(
        "todo.html.jinja",
        bucketlist=results
    )
@app.route("/add", methods=['POST'])
def add():
    new_todo= request.form['new_todo']

    bucketlist.append(new_todo)
    return redirect(('/todo'))



import pymysql
import pymysql.cursors


connection = pymysql.connect(
    host = "10.100.33.60",
    user = "atamayo",
    password = "220886964",
    database= "todos",
    cursorclass=pymysql.cursors.DictCursor,
    autocommit = True
)
