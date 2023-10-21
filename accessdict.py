# accessing key and values
variable = {"name" : "abdr", "age" : 23, "username" : "abdr"}
print(variable)
variable["age"] = 25
print(variable)
print(variable.keys())
print(variable.values())
print(variable["name"])
variable1 = {"name" : "sham"}
print(variable1)
print(variable1.pop("name"))
print(variable1)
variable2 = {"Name" : "shame", "age" : 25, "Name" : "sham"}
print(variable2)
for key, values in variable2.items():
    print(key, values, sep = " - ")
print(variable2.get("age"))
print(variable2.get("age12"))
print(variable2.get("age12","not available"))
print(variable2)
variable3 = {"username" : "sham", "age" : 23, "username" : "sham"}
print(variable3)
print(variable3.items())
variable3.clear()
print(variable3)
variable4 = {}
variable4[0] = 10
variable4[1] = 20
variable4[2] = 30
print(variable4)

