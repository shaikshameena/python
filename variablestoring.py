number = 10
print(" id of a : ", id(10) ," Value : ", number )
number = number + 10 # Modifying value of variable creates new object
print(" id of a : ", id(number) ," Value : ", number  )

number += 10 # Modifying value of variable creates new object
print(" id of a : ", id(number) ," Value : ", number  )
list1 = [5, 4, 3, 2, 1]
list2 = list1
list1 = list1 + [1, 2, 3, 4]
print(list1)
print(list2)
list1 = [5, 4, 3, 2, 1]
list2 = list1
list1 += [1, 2, 3, 4] # modifying value in current reference

print(list1)
print(list2) # as on line 4 it modify the value without creating new object
			# variable list2 which is pointing to list1 gets changes



