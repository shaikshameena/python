
# working of AND gate

def AND (number1, number2):

	if number1 == 1 and number2 == 1:
		return True
	else:
		return False

# Driver code
if __name__=='__main__':
	print(AND(1, 1))

	print("+---------------+----------------+")
	print(" | AND Truth Table | Result |")
	print(" A = False, B = False | A AND B =",AND(False,False)," | ")
	print(" A = False, B = True | A AND B =",AND(False,True)," | ")
	print(" A = True, B = False | A AND B =",AND(True,False)," | ")
	print(" A = True, B = True | A AND B =",AND(True,True)," | ")
# working of NAND gate

def NAND (number1, number2):
	if number1 == 1 and number2 == 1:
		return False
	else:
		return True

# Driver code
if __name__=='__main__':
	print(NAND(1, 0))

	print("+---------------+----------------+")
	print(" | NAND Truth Table | Result |")
	print(" A = False, B = False | A AND B =",NAND(False,False)," | ")
	print(" A = False, B = True | A AND B =",NAND(False,True)," | ")
	print(" A = True, B = False | A AND B =",NAND(True,False)," | ")
	print(" A = True, B = True | A AND B =",NAND(True,True)," | ")
# working of OR gate

def OR(number1, number2):
	if number1 == 1 or number2 ==1:
		return True
	else:
		return False

# Driver code
if __name__=='__main__':
	print(OR(0, 0))

	print("+---------------+----------------+")
	print(" | OR Truth Table | Result |")
	print(" A = False, B = False | A OR B =",OR(False,False)," | ")
	print(" A = False, B = True | A OR B =",OR(False,True)," | ")
	print(" A = True, B = False | A OR B =",OR(True,False)," | ")
	print(" A = True, B = True | A OR B =",OR(True,True)," | ")
# working of Xor gate

def XOR (number1, number2):
	if number1 != number2:
		return 1
	else:
		return 0

# Driver code
if __name__=='__main__':
	print(XOR(5, 5))

	print("+---------------+----------------+")
	print(" | XOR Truth Table | Result |")
	print(" A = False, B = False | A XOR B =",XOR(False,False)," | ")
	print(" A = False, B = True | A XOR B =",XOR(False,True)," | ")
	print(" A = True, B = False | A XOR B =",XOR(True,False)," | ")
	print(" A = True, B = True | A XOR B =",XOR(True,True)," | ")
# working of Not gate

def NOT(number):
	return not number
# Driver code
if __name__=='__main__':
	print(NOT(0))

	print("+---------------+----------------+")
	print(" | NOT Truth Table | Result |")
	print(" A = False | A NOT =",NOT(False)," | ")
	print(" A = True, | A NOT =",NOT(True)," | ")

# working of NOR gate

def NOR(number1, number2):
	if(number1 == 0) and (number2 == 0):
		return 1
	elif(number1 == 0) and (number2 == 1):
		return 0
	elif(number1 == 1) and (number2 == 0):
		return 0
	elif(number1 == 1) and (number2 == 1):
		return 0

# Driver code 
if __name__=='__main__':
	print(NOR(0, 0))

	print("+---------------+----------------+")
	print(" | NOR Truth Table | Result |")
	print(" A = False, B = False | A NOR B =",NOR(False,False)," | ")
	print(" A = False, B = True | A NOR B =",NOR(False,True)," | ")
	print(" A = True, B = False | A NOR B =",NOR(True,False)," | ")
	print(" A = True, B = True | A NOR B =",NOR(True,True)," | ")
# working of Not gate

def XNOR(number1,number2):
	if(number1 == number2):
		return 1
	else:
		return 0
# Driver code
if __name__=='__main__':
	print(XNOR(1,1))

	print("+---------------+----------------+")
	print(" | XNOR Truth Table | Result |")
	print(" A = False, B = False | A XNOR B =",XNOR(False,False)," | ")
	print(" A = False, B = True | A XNOR B =",XNOR(False,True)," | ")
	print(" A = True, B = False | A XNOR B =",XNOR(True,False)," | ")
	print(" A = True, B = True | A XNOR B =",XNOR(True,True)," | ")

