import operator

number1 = 4
number2 = 3
print ("The addition of numbers is :",end="");
print (operator.add(number1, number2))
print ("The difference of numbers is :",end="");
print (operator.sub(number1, number2))
print ("The product of numbers is :",end="");
print (operator.mul(number1, number2))
print ("The product of numbers is :",end="");
print (operator.mul(number1, number2))
print ("The true division of numbers is : ",end="");
print (operator.truediv(number1, number2))
print ("The floor division of numbers is : ",end="");
print (operator.floordiv(number1, number2))
print ("The exponentiation of numbers is : ",end="");
print (operator.pow(number1, number2))
print ("The modulus of numbers is : ",end="");
print (operator.mod(number1, number2))
if (operator.lt(number1, number2)):
    print("4 is less than 3")
else :
    print ("4 is not less than 3")
if (operator.le(number1, number2)):
    print ("4 is less than or equal to 3")
else : 
    print ("4 is not less than or equal to 3")
if (operator.eq(number1, number2)):
    print ("3 is equal to 3")
else : 
    print ("3 is not equal to 3")
if (operator.gt(number1, number2)): 
    print ("4 is greater than 3") 
else : 
    print ("4 is not greater than 3") 
if (operator.ge(number1, number2)): 
    print ("4 is greater than or equal to 3") 
else : 
    print ("4 is not greater than or equal to 3")
if (operator.ne(number1, number2)): 
    print ("4 is not equal to 3") 
else : 
    print ("4 is equal to 3") 
