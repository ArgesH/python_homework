storage = [
    {
        "name": "Rroba",
        "sasia": 10,
        "cmimi": 100,
    },
    {
        "name": "Metrazhe",
        "sasia": 20,
        "cmimi": 15,
    },
]

storage.append({
    "name": "tuta",
    "sasia": 30,
    "cmimi": 30,
})

def count_storage(my_storage):
    sasia = 0
    for i in my_storage:
        sasia += i["sasia"]
    
    return sasia

print(count_storage(storage))

# name = input("Jepni emrin e produktit: ")
# sasia = input("Jepni sasine: ")
# cmimi = input("Cmimi: ")

# storage.append({
#     "name": name,
#     "sasia": int(sasia),
#     "cmimi": float(cmimi),
# })

# print(count_storage(storage))

i = 0
while i != 1:
    name = input("Jepni emrin e produktit: ")
    sasia = input("Jepni sasine: ")
    cmimi = input("Cmimi: ")
    storage.append({
        "name": name,
        "sasia": int(sasia),
        "cmimi": float(cmimi),
    })

    i = int(input("Nese deshiron te mbyllesh sistemin, jep vleren 1"))

print(count_storage(storage))
