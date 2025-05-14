from flask_app import app, request, session, flash, render_template, redirect
from flask_app.models.user import User
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)


@app.route("/user/login", methods=["POST"])
def user_login():
    email = request.form["email"]
    password = request.form["password"]

    data = {
        "email": email,
        "password": password,
    }

    if not User.validate_login_data(data):
        return redirect("/user/login")

    my_user = User.get_by_email({"email": email})
    if my_user:
        if not bcrypt.check_password_hash(my_user.password, request.form['password']):
            flash("Incorrect password/email!")
            return redirect("/user/login")
        else:
            session["user_id"] = my_user.id
            return redirect("/tweets/all")
    else:
        flash("Incorrect password/email!")
        return redirect("/user/login")


@app.route("/user/login", methods=["GET"])
def user_login_form():
    if "user_id" in session:
        return redirect("/tweets/all")
    return render_template("user_login.html")

@app.route("/user/logout", methods=["POST"])
def logout():
    if "user_id" in session:
        del session["user_id"]
    
    return redirect("/user/login")


@app.route("/user/register", methods=["GET"])
def register_form():
    if "user_id" in session:
        return redirect("/tweets")
    return render_template("register.html")


@app.route("/user/register", methods=["POST"])
def register():
    if "user_id" in session:
        return redirect("/tweets/all/")

    # create a data dict
    data = {
        "email": request.form["email"],
        "password": request.form["password"],
        "name": request.form["name"],
    }

    # Validate data
    if not User.validate_data(data):
        return redirect("/user/register")

    # Hash password
    hashed_password = bcrypt.generate_password_hash(request.form["password"])
    data["password"] = hashed_password

    # call model for data
    user_id = User.register_user(data)
    session["user_id"] = user_id

    # redirect
    return redirect("/tweets/all/")
    

