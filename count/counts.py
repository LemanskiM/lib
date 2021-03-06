def greatest_common_divisor(a, b):
    """
    GCD of 2 numbers
    a - first number to GCD
    b - second number to GCD
    """
    while b:
      a, b = b, a % b
    """
    while b !=0 and % !=0
    a = b
    b = a % b

    """
    return a

def is_prime(number):
  """
  number - number to check
  is checking prime number
  return T/F
  """
  if number == 2:
    return True
  elif number == 0 or number == 1:
    return False
  elif number!=2:
    for i in range (2,number):
      if number % i == 0:
        return False
        break
    else:
      return True

def value_prime(number):
  """
  Is checking n-number of prime numbers
  number - prime number value for number
  """
  i=2
  factor = 0
  while factor != number:
    if is_prime(i) == True:
      factor+=1
      if factor == number:
        break
      else:
        i+=1
    else:
      if factor == number:
        break
      else:
        i+=1
  return(i)

def is_palindrome_bin(number):
  """
  is checking natural and binear palindrome of number
  """
  if str(number) != str(number)[::-1]:
      #    xyz       !=       zyx
    return False
  bin_number = bin(number)[2:]
  return bin_number == bin_number[::-1]

def list_palindromes(start,stop):
  """
  is checkin palindromes in range as atributes
  start - fitst number
  stop - last number to check
  """
  palindromes = []
  for i in range (start,stop):
    if is_palindrome(i) == True:
      palindromes.append(i)
  return palindromes
