number1 = 24
number2 = 4
print("number1 = ", number1)
print("number2 = ", number2)

#bitwise operations
bitwiseAND = number1 & number2
bitwiseOR = number1 | number2
bitwiseNOT = ~number1
bitwiseXOR = number1 ^ number2
leftshift = number1 << number2
rightshift = number2 >> number1
print("bitwiseAND = ", bitwiseAND)
print("bitwiseOR = ", bitwiseOR)
print("bitwiseNOT = ", bitwiseNOT)
print("leftshift = ", leftshift)
print("rightshift = ", rightshift)
even = number1 & 1
if even == 0 :
    print("number1 is even")
else :
    print("number1 is odd")
odd = number2 & 1 
if odd == 1 :
    print("number2 is odd")
else :
    print("number2 is even")      


