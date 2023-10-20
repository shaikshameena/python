list1 = [1, 2, 3, 4, 5, 6, "a", "b", "c", "d"]
print(list1)
slicedlist = list1[2 : ]
print(slicedlist)
list2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
slicedlist2 = slice(1, 3) # slice function
print(list2[slicedlist2])
list3 = [10, 20, 30, 40, 50, 60, 70, 80]
print(list3)
slicedlist3 = list3[ : ]
print(slicedlist3)
slicedlist4 = list3[2 : -1]
print(slicedlist4)
reverse_list = list3[:: -1]
print(reverse_list)
