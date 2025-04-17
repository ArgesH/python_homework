# 1- Shkruani nje funksion qe kontrollon nese nje string eshte palindrom apo jo

def check_palindrom(palindroma):
    return palindroma == palindroma[::-1]
    # return True
    # return False

def check_palindrom_long_version(palindroma):
    # level
    # adda
    for i in range(len(palindroma)):
        if palindroma[i] != palindroma[len(palindroma)-i-1]:
            return False
    return True

my_testing_var = "ada"
print(check_palindrom(my_testing_var))
print(check_palindrom_long_version(my_testing_var))


def reverse_string(my_string):
    return my_string[::-1]

print(reverse_string("test"))

# 5- Shkruani nje funksion qe gjen numrin e zanoreve te nje stringu.
def gjej_nr_zanore(my_string):
    zanoret = ["a", "e", "i", "o", "y", "u"]
    nr_zanore = 0
    for i in my_string:
        if i in zanoret:
            nr_zanore += 1
            # nr_zanore = nr_zanore + 1
    return nr_zanore

def gjej_zanoret(my_string):
    zanoret = ["a", "e", "i", "o", "y", "u"]
    nr_zanore = 0
    for i in my_string:
        for a in zanoret:
            if i == a:
                nr_zanore += 1
    return nr_zanore


print(gjej_nr_zanore("Sot eshte e premte"))

# 6- Shkruani nje funksion qe gjen shumen e numrave te nje numri 
# (psh 322 duhet te ktheni 7, 543 duhet te ktheni 12)

def find_sum(my_num):
    total_sum = 0
    for i in str(my_num):
        total_sum += int(i)
    return total_sum

print(find_sum(123))

var1 = 1
var2 = 2
var3 = 3

if var1 > var2 and var1 > var3:
    print(var1)
elif var2 > var1 and var2 > var3:
    print(var2)
else:
    print(var3)

def foo(*args, **kwargs):
    # {"c": 1}
    print(max(args))

foo(1,2,3,4,5,6,7,8,4,c=1,d=2,e=3)

def find_hipotenuza(kateti1, kateti2):
    return (kateti1**2 + kateti2**2)**0.5

print(find_hipotenuza(3,4))


# 8- Shkruani nje funksion qe merr nje numer te pacaktuar fjalesh,
# dhe kthen fjalen me te madhe.

def fjala_me_e_gjate(*args):
    var_min = 0
    longest_word = ""
    for i in args:
        word_length = len(i)
        if word_length > var_min:
            var_min = word_length
            longest_word = i
    
    return longest_word, var_min

# print(fjala_me_e_gjate("testing", "1", "2", "3", "44444444444"))

my_word, word_length = fjala_me_e_gjate("1", "22", "333")
print(my_word)
print(word_length)



def numrat_cift(start, finish):
    for i in range(start, finish+1):
        if i % 2 == 0:
            print(i)

# var1 = int(input("Shkruaj fillimin: "))
# var2 = int(input("Shkruaj mbarimin: "))

# numrat_cift(start=var1, finish=var2)


def print_stars(number_of_rows):
    star = "*"
    spaces = " "
    for i in range(1, number_of_rows):
        print(spaces*(number_of_rows-i)+star*i)

print_stars(10)

def return_unique(my_list):
    return list(set(my_list))

def find_if_element_is_in_list(my_list, my_element):
    return my_element in my_list

find_if_element_is_in_list([1,2,3], 4)

# FizzBuzz
# 1- 
# 2- 
# 3- Fizz
# 5- Buzz
# 15- FizzBuzz

# 7- Shkruani nje funksion qe gjen elementet e perbashket te 2 listave.

def element_perbashket(l1, l2):
    list3 = []
    for i in l1:
        for l in l2:
            if l == i:
                list3.append(l)
    return list3

list1 = [1,5,9,11,15,101,"abc"]
list2 = [11,7,"abc",5,23,31]
print(element_perbashket(list1, list2))





print("--------")


my_dict = {"key": "value"}

my_dict["word"] = []

print(my_dict)

del my_dict["key"]

print(my_dict)

my_dict["word"] = {}

print(my_dict)

print(my_dict["word"])



my_dict = {
    "my_employees": [
        {"name": "x", "age": 30, "salary": 100},
    ],
    "my_vacation_days": [
        "2025-01-01", "2025-01-02"
    ],
    "is_manager": True
}

print(my_dict["my_employees"][0]["age"])
print(my_dict["my_vacation_days"][-1])
print(my_dict["is_manager"])
my_dict["my_vacation_days"].append("2025-04-30")
my_dict["is_manager"] = False
my_dict["my_employees"].append({"name": "y", "age": 50, "salary": 1000})
my_dict["my_employees"][1]["department"] = "IT"
print(my_dict)
my_dict["my_employees"][0]["department"] = "IT"

my_list = [{}, {}, {}, {}]

for i in my_list:
    i["deparment"] = "IT"



class Employee:
    def __init__(self, emri, mosha=16, paga=100, departamenti="IT"):
        self.name = emri
        self.age = mosha
        self.salary = paga
        self.department = departamenti

    def __str__(self):
        return f"Employee with name {self.name} with age {self.age} works in department {self.department}"

    def increase_salary(self, new_salary):
        self.salary = new_salary

var1 = Employee(emri="x", mosha=20, paga=100, departamenti="IT")
var2 = Employee(emri="y")

my_dict = {
    "my_employees": [var1, var2],
}

print(var1.name)
print(var1.age)
print(var2.age)
var2.vacation_days = []
print(var2.vacation_days)

my_employee_list = []
for i in range(1000):
    my_employee_list.append(Employee(emri="z"))

print(len(my_employee_list))

print(var2)
print(var1)

var2.increase_salary(250)
var2.increase_salary(200000)






class Ushqime:
    def __init__(self, lloji, cmimi, sasia, cilesia, data_skadences):
        self.type = lloji
        self.price = cmimi
        self.quantity = sasia
        self.quality = cilesia
        self.expiration_date = data_skadences

    def foo(self):
        self.quantity += 1
        return self

    def expense(self):
        return self.price * self.quantity

    def __str__(self):
        return f"Ushqimi {self.type} ka cilesine {self.quality}"

    def __repr__(self):
        return f"Ushqimi {self.type} ka cilesine {self.quality}"

first_food = Ushqime("makarona", 120, 150, 1, "2026-04-30")
second_food = Ushqime("domate", 120, 15, 1, "2026-04-30")

my_shopping_list = [first_food, second_food]

print(first_food.type)
print(second_food.type)
print(second_food.quality)

print(first_food.expense())
print(second_food.expense())

for i in my_shopping_list:
    print(f"Ushqimi: {i.type}: expense: {i.expense()}")

print(first_food)
print(my_shopping_list)

print(first_food.foo().quantity)
# return of this call is, first_food


class Animal:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def noise(self):
        return ""

    def __str__(self):
        return "This is Animal Class!"


class Dog(Animal):
    
    def __init__(self, name, age, race):
        super().__init__(name, age)
        self.race = race

    def noise(self):
        return "HAM"

    def calculate_age(self):
        return self.age * 7

    def __str__(self):
        parent_str = super().__str__()
        return parent_str + " And Dog Class!"
    
    def __str__(self):
        return ""

a1 = Animal("x", 3)
d1 = Dog("y", 2, "husky")

print(a1.noise())
print(d1.noise())
print(d1.calculate_age())



class PrepareCatFood:

    @classmethod
    def prepare_food(cls):
        return ["buy it", "cook it", "serve it"]

class Cat(Animal):

    def __init__(self, name, age, color):
        super().__init__(name, age)

        self.color = color
        self.prepare_food = PrepareCatFood.prepare_food()

    def noise(self):
        return "Mjau"

    @staticmethod
    def food_description():
        return "Cats eat mice!"

    @classmethod
    def describe_cats(cls):
        return ""


c1 = Cat("pisika", 7, "portokalli")
print(c1.food_description())
Cat.describe_cats()


class Employee:

    net_percentage = 0.8

    def __init__(self, paga):
        self.paga = paga

    def calculate_net(self):
        return self.paga * self.net_percentage

    @classmethod
    def describe_tax(cls):
        return f"Tax is {cls.net_percentage}"

e1 = Employee(100)
Employee.net_percentage
Employee.describe_tax()




class Vehicles:

    def __init__(self, brand, year, fuel, color):
        self.brand = brand
        self.year = year
        self.fuel = fuel
        self.color = color

    def horn(self):
        return "NO HORN!"

    def fuel_consumption(self):
        pass

    @staticmethod
    def describe():
        return ""

class Makina(Vehicles):
    fuel_efficency = 0.01

    def __init__(self, brand, year, fuel, color, motori, ndotja):
        super().__init__(brand, year, fuel, color)
        self.motori = motori
        self.ndotja = ndotja
    
    def horn(self):
        return "Bip!"

    def fuel_consumption(self):
        return self.fuel * self.fuel_efficency

    @staticmethod
    def describe():
        return "Makina ecen shpejt"

    def display_attributes(self):
        return f"{self.brand}"

class Bicycle(Vehicles):
    def __init__(self, brand, year, fuel, color, EV):
        super().__init__(brand, year, fuel, color)
        self.ev = EV
    
    def horn(self):
        return "Tring"

    def fuel_consumption(self):
        if self.ev == True:
            return 100
        return 0

    @staticmethod
    def describe():
        return "Bicikleta nuk ecen shpejte"


m1 = Makina("BENC", 1999, "BENCIN", "ZEZ", 5000, "SHUM")
m2 = Makina("FIAT", 2010, "NAFT", "ZEZ", 1400, "PAK")
b1 = Bicycle("BMX", 2025, "", "RED", False)

m1.horn()
m2.horn()
b1.horn()


class Fiat(Makina):
    def __init__(self, brand="Fiat", year, fuel, color, motori, ndotja):
        super().__init__(brand, year, fuel, color)
        self.motori = motori
        self.ndotja = ndotja
    

f1 = Fiat(year=2000, fuel="", color="", motori="", ndotja="")





class TEG:
    def __init__(self, brandi, kati, lloji):
        pass


class Dyqani(TEG):
    def __init__(self, brandi, kati, lloji, qeraja):
        super().__init__(brandi, kati, lloji)




