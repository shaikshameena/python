# using function adding two elements
def addition(number1 : int, number2 : int) -> int :
    result = number1 + number2
    return result
  
number1, number2 = 19, 12
result = addition(number1, number2) # calling function
print("addition of two numbers = ", result)
