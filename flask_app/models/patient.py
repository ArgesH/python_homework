from flask_app.config.mysqlconnection import connect_to_mysql
from flask_app import flash
import re
from flask_bcrypt import Bcrypt 

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Patient:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.email = data["email"]
        self.gender = data["gender"]
        self.cel = data["cel"]
        self.birthday = data["birthday"]
        self.records = []

    @classmethod
    def get_all(cls):
        # Query
        query = "select * from patient;"
        # Connect and Excecute query
        result = connect_to_mysql("patient-mr").query_db(query) # [{}, {}...]
        # Transform from dict to Patient objects

        obj_result = []
        for res in result:
            obj_result.append(cls(res))

        return obj_result

    @classmethod
    def create_patient(cls, data):
        query = "insert into patient (name, gender, email, cel, birthday) values (%(nm)s, %(gnd)s, %(em)s, %(c)s, %(bd)s);"
        row_id = connect_to_mysql("patient-mr").query_db(query, data)
        return row_id

    @staticmethod
    def validate_patient(patient):
        is_valid = True # we assume this is true
        if len(patient['nm']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(patient['nm']) > 45:
            flash("Name must be at most 45 characters.")
            is_valid = False
        if len(patient["bd"]) == 0:
            flash("Birthday can not be empty.")
            is_valid = False
        if patient["gnd"] not in ["M", "F"]:
            flash("Gender can be only M or F.")
            is_valid = False

        if len(patient["c"]) == 0:
            flash("Cel can not be empty.")
            is_valid = False

        elif patient["c"][0] != "+":
            flash("Cel should start with +.")
            is_valid = False

        if len(patient["c"]) != 12:
            flash("Cel can only be 12 characters.")
            is_valid = False

        if not EMAIL_REGEX.match(patient["em"]): 
            flash("Invalid email address!")
            is_valid = False

        return is_valid