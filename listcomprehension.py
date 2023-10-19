list1 = [10, 20, 30, 40, 50, 60]
print(list1)
squared = [ x ** 2 for x  in list1]
print(squared)
list2 = [list1 for list1 in [10, 20, 30]]
print(list2)
list3 = ["even number" if i % 2 == 0 else "odd number" for i in range(10)]
print(list3)
