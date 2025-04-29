from flask import Flask, render_template, request, redirect, session
# Tasks app
# First page: Display all tasks 90%
# Second page: Possibility to add a new task 90%
# Login + Logout

app = Flask(__name__)
app.secret_key = "secret string"

my_tasks = ["t1", "t2"]
my_user = {"email": "test@test.com", "password": "123"}

@app.route("/")
def home_page():
    if "user_email" not in session:
        return redirect("/login")
    return render_template("tasks.html", our_tasks=my_tasks)

@app.route("/new", methods=["GET", "POST"])
def new_tasks():
    if request.method == "GET":
        if "user_email" not in session:
            return redirect("/")

        return render_template("add_task.html")
    
    if request.method == "POST":
        user_task = request.form["emri"]  # {"emri": "my_homework"}
        my_tasks.append(user_task)
        return redirect("/")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    
    if request.method == "POST":
        user_email = request.form["email"]
        user_password = request.form["password"]
        if user_email == my_user["email"] and user_password == my_user["password"]:
            session["user_email"] = user_email
            return redirect("/")
        else:
            return render_template("login.html", error_message="Wrong credentials!")

@app.route("/logout", methods=["POST"])
def logout_user():
    del session["user_email"]
    return redirect("/")

app.run(debug=True)
