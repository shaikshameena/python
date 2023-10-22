variable1 = {10, 20, 30, 49, "abdr", 9.8}
print(variable1)
variable2 = {10, 2, 30, 49, "abdr", 9.8,"sham", 7, 5}
print(variable2)
print(variable1.union(var2))
variable3 = {1, 2, 3, 49, "abdr", 9.8}
print(variable3)
variable4 = {10, 20, 30, 49, "abdr", 9.8, "sham", 7, 5}
print(variable4)
print(variable3.intersection(var4))
print(variable1 & variable3)
print(variable1 | variable3)
print(variable1.difference(variable2))
print(variable2 - variable1)
print(variable1.symmetric_difference(variable2))
