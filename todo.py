from flask import Flask, render_template, request,redirect


app = Flask(__name__)

todos= ["read more","learn tennis"]

@app.route("/")
def index():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM `todos`")

    results = cursor.fetchall()

    return render_template(
        "todo.html.jinja",
        todoss=results
    )
@app.route("/add", methods=['POST'])
def add():
    new_todo= request.form['new_todo']

    todos.append(new_todo)
    return redirect(('/'))

app.route("/complete", methods=["POST"])
def complete():
    todo_id = request.form['todo_id']

    cursor= connection.cursor()

    cursor.execute(f"UPDATE `todos` SET `complete` =1 WHERE `id` ={todo_id}")

    return redirect("/")



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


