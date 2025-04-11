var_a = 10
var_b = 5

print(var_a)

var_a = var_a + var_b

print(var_a)

my_list = [1,2,3,4,"test"]
my_tuple = ("a", "b", "c")
my_dict = {"first_key": 10, "second_key": 20, "first_key": 30, my_tuple: 30}
my_set = {1,2,3,4,4,4,4,4}

# for i in my_list:
#     print(i)
    
# for x in my_tuple:
#     print(x)

# print("test")

# for i in range(10):
#     print(i)
# print('--------')
# for a in range(len(my_tuple)):
#     print(my_tuple[a])

# for i in my_list:
#     print(2*i)

# for i in range(len(my_list)):
#     if type(my_list[i]) == int:
#         print(2*i)

#     elif type(my_list[i]) == str:
#         print("this is string")

#     else:
#         print("This is not a number")

#     print("test")


# my_dict = {"first_key": 10, "second_key": 20, "first_key": 30, my_tuple: 30}
# for i in my_dict.values():
#     print(i)

# for key, value in my_dict.items():
#     print(key, value)

# my_list = [10,20,30]

# my_dict = {0: 10, "1":20, 2:30, 1:40, "3": " ",}

# print(my_list[1])

# print(my_dict["1"])

# my_list.append("test")
# my_dict["3"] = "tresh"

# print(my_dict["3"])
# print(my_list[1])

# my_set = {1,2,3,4,4,4,4,4}

# for i in my_set:
#     print(i)

# print(my_set[-1])

# list()
# dict()
# set()
# tuple()



# my_list = []
# for i in range(2, 11, 2):
#     my_list.append(i)

# for i in range(1, 11):
#     if i % 2 != 0:
#         my_list.append(i)

# # Iteroni tek lista my_list, dhe printoni cdo element ne katror
# for i in my_list:
#     print(i*i)

# # iteroni tek lista my_list, dhe shtoni ne nje dict: key do jete cdo elemetn i listes,
# # value do jete elementi ne katror

# my_dict = {}
# for i in my_list:
#     my_dict[i] = i**2

# {1:1, 2:4, 3:9}

# def foo():
#     print("test")

# foo()

# def find_sum(a, b):
#     print(a+b)
#     return a + b

# my_sum = find_sum(5, 3)
# print(my_sum)
# my_sum = find_sum(6, 6)


# def prodhimi(a, b):
#     return a * b

# Shkruani nje funksion qe merr si parameter nje liste me numra, 
# dhe gjen prodhimin e ketyre numrave

my_list = [2,5,8,12]
def prodhimi_i_numrave_te_nje_liste(my_l):
    prodhimi = 1 # 2, 10, 80
    for i in my_l:
        prodhimi = prodhimi * i

    return prodhimi

prodhimi_i_numrave_te_nje_liste(my_l=my_list)
print(prodhimi_i_numrave_te_nje_liste(my_l=[1,2,3,4]))

print(prodhimi_i_numrave_te_nje_liste(my_list))
