# Invoice Generator for Employees
# Two types of Employees: Full time or Hourly based
# Create classes to handle this structure
# Write a function to calculate the salary of each Employee


class InvGen:

    def __init__(self, employee_name, amount, date):
        self.employee_name = employee_name
        self.amount = amount
        self.date = date

    def calculate_salary(self):
        return self.amount * 176
    
class InvGenHB(InvGen):

    def __init__(self, employee_name, amount, date, hours_worked):
        super().__init__(employee_name, amount, date)

        self.hours_worked = hours_worked
    
    def calculate_salary(self):
        return self.amount * hours_worked

class InvGenFT(InvGen):
    pass
    
class InvGenPT(InvGen):

    def calculate_salary(self):
        return self.amount * 176 / 2



import datetime


class SmartDevice:

    def __init__(self, name, serial_number, lloji):
        self.name = name
        self.serial_number = serial_number
        self.lloji = lloji
    
    def power_on(self):
        pass

    def power_off(self):
        pass
    
    def calculate_expense(self):
        pass
    
    def time_on(self):
        pass

class AC(SmartDevice):

    def __init__(self, name, serial_number, lloji, btu, power, ac_class):
        super().__init__(name, serial_number, lloji)
        self.btu = btu
        self.power = power
        self.ac_class = ac_class
        self.temp = 0
        self.on_time = 0
    
    def power_on(self):
        self.on_time = datetime.datetime.now()
        print("AC is on!")
        return True

    def power_off(self):
        self.on_time = 0
        print("AC is off!")
        return False
    
    def calculate_expense(self):
        return btu * ac_class * 0.05

    def time_on(self):
        if self.on_time != 0:
            return datetime.datetime.now() - self.on_time

    def update_temp(self, value):
        if self.power_on():
            self.temp = value
        else:
            print("AC is Off!")
        



class Appointment:

    def __init__(self, date, name, email):
        self.date = date
        self.name = name
        self.email = email

class DailyClients(Appointment):

    def __init__(self, date, name, email):
        super().__init__(date, name, email)
        self.sent_reminder = False
        self.last_reminder_time = None # 2025-04-17 12:30:30

    def print_info(self):
        # if self.sent_reminder == False:
        #     print("Daily remainder for check-up")
        #     self.sent_reminder = True
        #     self.last_reminder_time = datetime.datetime.now()

        # elif datetime.datetime.now() - self.last_reminder_time > 24*60*60:
        #     print("Daily remainder for check-up")
        #     self.sent_reminder = True
        #     self.last_reminder_time = datetime.datetime.now()
        
        if self.sent_reminder == False or (datetime.datetime.now() - self.last_reminder_time > 24*60*60):
            print("Daily remainder for check-up")
            self.sent_reminder = True
            self.last_reminder_time = datetime.datetime.now()
        else:
            print("Remainder already sent!")



class RandomClients(Appointment):

    def __init__(self, date, name, email):
        super().__init__(date, name, email)

    


class Event:
    def __init__(self, name, event_type):
        self.name = name
        self.type = event_type

    @classmethod
    def create_meeting_event(cls, name):
        return cls(name, "meeting")

    @classmethod
    def create_lunch_event(cls, name):
        return cls(name, "lunch")

e1 = Event("123", "Meeting")
e2 = Event("x", "meeting")

e3 = Event.create_meeting_event("My meeting")
e4 = Event.create_meeting_event("My meeting 1")
e5 = Event.create_lunch_event("Lunch!")




class User:
    number_of_users = 0

    def __init__(self, username):
        self.username = username
        User.number_of_users += 1

    @classmethod
    def get_number_of_users(cls):
        return cls.number_of_users

print(User.number_of_users) # 0

u1 = User("u1")
u2 = User("u2")

print(User.number_of_users) # 2
print(u1.number_of_users) # 2

u3 = User("u3")
print(u3.number_of_users) # 3

User.number_of_users = 10












