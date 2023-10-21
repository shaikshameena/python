number1 = 5
number2 = 10
divisor = 6.7
divident = 2
print("quoitent =",number1 // number2)
print("quoitent = ", divisor // divident)
print(- 5 // 2)  # floor division
print( 5 // 2)
print (5.0/2)
print (-5.0/2)
#division operator on Boolean values
class MyClass:
	def __init__(self, value):
		self.value = value

	def __truediv__(self, other):
		return MyClass(self.value and other.value)
 
number1 = MyClass(True)
number2 = MyClass(False)
result = number1 / number2 # c.value is False
print(result.value)

