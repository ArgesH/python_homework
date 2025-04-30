# Shopping cart

# Show products
# Show all elements in my shopping cart
# Add/Remove elements
# Login/Logout

from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "shhhh"

my_user = {"email": "test@test.com", "password": "1"}
products = [
    {"id": 1, "name": "Telefon", "price": 100, "quantity": 200},
    {"id": 2, "name": "laptop", "price": 300, "quantity": 50},
    {"id": 3, "name": "charger", "price": 20, "quantity": 300},
    {"id": 4, "name": "tv", "price": 500, "quantity": 20},
]

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        if my_user["email"] == request.form["email"] and my_user["password"] == request.form["password"]:
            session["user_email"] = my_user["email"]
            return redirect("/")
        else:
            return redirect("/login", error_message="Wrong Credentials!")

@app.route("/logout", methods=["POST"])
def logout():
    del session["user_email"]
    del session["my_cart"]
    return redirect("/login")

@app.route("/cart")
def show_cart():
    if "user_email" in session:
        return render_template("my_cart.html", my_items=session.get("my_cart", []))
    else:
        return redirect("/login")

@app.route("/add", methods=["POST"])
def add_to_cart():
    if "user_email" in session:
        for prod in products:
            if prod["id"] == int(request.form["product_id"]):
                my_new_product = {
                    "id": prod["id"],
                    "name": prod["name"],
                    "price": prod["price"],
                    "quantity": 1
                }
                if "my_cart" in session:
                    found = False
                    for element in session["my_cart"]:
                        if prod["id"] == element["id"]:
                            element["quantity"] += 1
                            found = True
                    if not found:
                        session["my_cart"].append(my_new_product)
                else:
                    session["my_cart"] = [my_new_product]
                session["user_messsage"] = "Item Added!"

        return redirect("/")

    return redirect("/login")

@app.route("/remove", methods=["POST"])
def remove_from_cart():
    if "user_email" in session:
        for i in range(len(session["my_cart"])):
            record = session["my_cart"][i]
            if record["id"] == int(request.form["product_id"]):
                if record["quantity"] > 1:
                    session["my_cart"][i]["quantity"] -= 1
                else:
                    session["my_cart"].pop(i) 
        return redirect("/cart")

@app.route("/")
def all_products():
    if "user_email" in session:
        return render_template("products.html", my_products=products)
    else:
        return redirect("/login")

app.run(debug=True)

