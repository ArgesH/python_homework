from flask_app import app, render_template, redirect, request
from flask_app.models.medical_record import MedicalRecord
from flask_app.models.patient import Patient


@app.route("/records/")
def get_all_records():
    data = MedicalRecord.get_all()
    return render_template("records.html", all_records=data)

@app.route("/records/create/", methods=["GET"])
def create_record_template():
    return render_template("create_record.html", all_patients=Patient.get_all())


@app.route("/records/create/", methods=["POST"])
def create_record_form():
    data = {
        "condition": request.form["condition"],
        "medication": request.form["medication"],
        "date": request.form["date"],
        "test_results": request.form["test_results"],
        "patient_id": int(request.form["patient_id"]),
    }

    MedicalRecord.create_record(data)
    # redirect
    return redirect("/records/")


