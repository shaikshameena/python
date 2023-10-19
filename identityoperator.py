def overlapping(list1, list2):
    number1 = 0
    number2 = 0
    for initial in list1:
        number1 += 1
    for initial in list2:
        number2 += 1
    for initial in range(0, number1):
        for secondinitial in range(0, number2):
            if list1[initial] == list2[secondinitial]:
                return 1
    return 0

number1 = 10
number2 = 20
list1 = [10, 20, 30, 40, 60]
list2 = [12, 13, 14, 15, 16, 17]

if overlapping(list1, list2):
    print("overlapping")
else:
    print("not overlapping")
if number1  not in list1 :
    print("number1 is not present in list1")
else :
    print("number1 is present in list1")
if number2  in list2 :
    print("number2 is present in list2")
else :
    print("number2 is present in list2")
number1 = number2    
print(number1 is number2)

