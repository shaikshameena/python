number1 = 10
number2 = 20
number3 = 30
# logical operators
if number1 > 0 and number2 > 0 :
    print("number1 and number2 greater than zero")
if number1 > 0 and number2 > 0 and number3 > 0 :
    print("all numbers are greater than zero")
else :
    print(" atleast one number greater than zero")
if number1 and number2 and number3:
    print("all numbers are boolean as true")
else :
    print("all numbers are boolean as false")
if number1 > 0 or number2 > 0 :
    print("Either of the number is greater than 0")
else : 
    print("No number is greater than 0")
if number1 > 0 or number2 > 0 or number3 > 0:
    print("Either of the number is greater than 0")
else :
   print("No number is greater than 0")
if number1 or number2 or number3:
    print("At least one number has a boolean value as True")
else:
    print("Atleast one number has boolean value as False")
if not number1 :
    print("Boolean value of a is True")
if not (number1 % 5 == 0 or number1 % 10 == 0) :
    print("number1 is not divisible by either 5 or 10")
else :
    print("number1 is divisible by either 5 or 10")
def order(number2) :
    print("Method called for value:", number2)
    return True if number2 > 0 else False
variable1 = order
variable2 = order
variable3 = order
if variable1(-1) or variable2(5) or variable3(10):
    print("At least one of the numbers is positive")

    
