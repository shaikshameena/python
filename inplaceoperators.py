import operator

number1 = 10
number2 = 20
number3 = 10
number4 = 20
result = operator.add(number1, number2)
result1 = operator.iadd(number3,number4)
print ("Value after adding using normal operator : ",end="")
print (result)
print ("Value after adding using Inplace operator : ",end="")
print (result1)
print ("Value of first argument using normal operator : ",end="")
print (number1)
print ("Value of first argument using Inplace operator : ",end="")
print (number3) 
list1 = [1, 2, 4, 5]
result3 = operator.add(list1,[1, 2, 3])
print ("Value after adding using normal operator : ",end="")
print (result3)
print ("Value of first argument using normal operator : ",end="")
print (number1)
result4 = operator.iadd(list1,[1, 2, 3]) #inplace operator
print ("Value after adding using Inplace operator : ",end="")
print (result4)
print ("Value of first argument using Inplace operator : ",end="")
print (number1) 
string1 = "geeks"
string2 = "forgeeks"
string1 = operator.iconcat(string1, string2)
print ("The string after concatenation is : ", end="")
print (string1)
output = operator.isub(2, 3)
print ("The value after subtracting and assigning : ", end="")
print(output) 
output = operator.imul(2, 3)
print ("The value after multiplying and assigning : ", end="")
print (output)
output = operator.imod(10, 6)
print ("The value after modulus and assigning : ", end="")
print (output)
output = operator.ixor(10,5)
print ("The value after xoring and assigning : ",end="")
print (output) 
output = operator.ipow(5,4)
print ("The value after exponentiating and assigning : ",end="")
print (output) 
output = operator.ior(10,5)
print ("The value after bitwise or, and assigning : ",end="")
print (output)
output = operator.iand(5,4)
print ("The value after bitwise and, and assigning : ",end="")
print (output) 
output = operator.ilshift(8,2)
print ("The value after bitwise left shift and assigning : ",end="")
print (output)
output = operator.irshift(8,2);
print ("The value after bitwise right shift and assigning : ",end="")
print (output) 
