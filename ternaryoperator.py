number1 = 10
number2 = 20
minimum = number1 if number1 < number2 else number2
print("minimum =", minimum)
print("both are equal " if number1 == number2 else "number1 greater than number2 " if number1 > number2 else "number1 is not greater than number2")
# using ternary opertor in tuple
print((number2, number1) [number1 < number2])
print({True : number1, False : number2} [ number1 < number2])
print((lambda : number2, lambda : number1) [number1 < number2]())
print("number1 is greater") if number1 > number2 else print("number2 is greater")
