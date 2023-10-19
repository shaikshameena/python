def is_prime(number):
    if number in [2, 3] :
        return True
    if (number == 1) or (number % 2 == 0) :
        return False
    number1 = 3
    while number1 * number1 <= number:
      if number % number1 == 0 :
          return False
      number += 2
      return True

print(is_prime(78), is_prime(79))
