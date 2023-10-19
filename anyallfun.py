list1 = []
list2 = []
for initial in range(1, 11) :
    list1.append(4 * initial)
for initial in range(0, 10):
    list2.append(list1[initial] %5 == 0)
print('See whether at least one number is divisible by 5 in list 1=>')
print(any(list2))

