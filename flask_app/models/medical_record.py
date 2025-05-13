from flask_app.config.mysqlconnection import connect_to_mysql


class MedicalRecord:
    
    def __init__(self, data):
        self.id = data["id"]
        self.condition = data["condition"]
        self.medication = data["medication"]
        self.date = data["date"]
        self.test_results = data["test_results"]
        self.patient_id = None

    @classmethod
    def get_all(cls):
        # Query
        query = "select medical_record.id, medical_record.condition,medical_record.medication,medical_record.date,medical_record.test_results, patient.name as patient_id from medical_record left join patient on patient.id = medical_record.patient_id;"
        # Connect and Excecute query
        result = connect_to_mysql("patient-mr").query_db(query) # [{}, {}...]
        # Transform from dict to Patient objects

        obj_result = []
        for res in result:
            my_obj = cls(res)
            my_obj.patient_id = Patient({})
            obj_result.append(my_obj)
            
        return obj_result

    @classmethod
    def create_record(cls, data):
        query = "insert into medical_record (`condition`, medication, date, test_results, patient_id) values (%(condition)s, %(medication)s, %(date)s, %(test_results)s, %(patient_id)s);"
        row_id = connect_to_mysql("patient-mr").query_db(query, data)
        return row_id




