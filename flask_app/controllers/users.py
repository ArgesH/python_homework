from flask_app import app, request, session, flash, render_template
from flask_app.models.user import User

@app.route("/user/login", methods=["POST"])
def user_login():
    email = request.form["email"]
    password = request.form["password"]

    my_user = User.get_by_email({"email": email})
    if my_user:
        if my_user.password == password:
            session["user_id"] = my_user.id
        else:
            flash("Incorrect password/email!")
            return redirect("/user/login")
    else:
        flash("Incorrect password/email!")
        return redirect("/user/login")


@app.route("/user/login", methods=["GET"])
def user_login_form():
    if "user_id" in session:
        return redirect("/")
    return render_template("user_login.html")

@app.route("/user/logout", methods=["POST"])
def logout():
    if "user_id" in session:
        del session["user_id"]
    
    return redirect("/user/login")
