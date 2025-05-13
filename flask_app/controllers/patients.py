from flask_app import app, render_template, redirect, request
from flask_app.models.patient import Patient


# Get all patients
@app.route("/patients/")
def get_all_patients():
    # Get the data
    data = Patient.get_all()
    return render_template("patients.html", all_patients=data)

@app.route("/patients/create/", methods=["GET"])
def create_patient_template():
    return render_template("create_patient.html")

@app.route("/patients/create/", methods=["POST"])
def create_patient_form():
    # Query DB (insert)

    data = {
        "nm": request.form["name"],
        "em": request.form["email"],
        "bd": request.form["birthday"],
        "gnd": request.form["gender"],
        "c": request.form["cel"],
    }
    if not Patient.validate_patient(data):
        return redirect("/patients/create/")

    Patient.create_patient(data)

    # redirect
    return redirect("/patients/")

