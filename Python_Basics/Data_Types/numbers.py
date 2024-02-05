""" Numbers """
#?    There are three numeric types in Python:
#?     int (e.g. 2, 4, 20)
#?     bool (e.g. False and True, acting like 0 and 1)
#?     float (e.g. 5.0, 1.6)
#?     complex (e.g. 5+6j, 4-3j)


#? 1) int :
def integer_numbers():
  """Integer type:
    Int, or integer, is a whole number (without decimals), positive or negative,
    of unlimited length.
  """

  positive_integer = 1
  negative_integer = -3255522
  big_integer = 35656222554887711

 # Another way to declare integer using 'int()' Fn.
  num = int(56)
  num2 = int('56')
  print(num2, type(num2))
  print(num)

#? 2) bool :
def booleans():
  """Boolean: Booleans represent the truth values False and True. The two objects representing the values
  False and True are the only Boolean objects. The Boolean type is a subtype of the integer type,
  and Boolean values behave like the values 0 and 1, respectively, in almost all contexts, the
  exception being that when converted to a string, the strings "False" or "True" are returned,
  respectively.
  """

  true_boolean = True
  false_boolean = False

  print(true_boolean, false_boolean)

  # Let's try to cast boolean to string.
  assert str(true_boolean) == "True"
  assert str(false_boolean) == "False"


#? float:
def float_numbers():
  """Float type: Float, or "floating point number" is a number, positive or negative,
  containing one or more decimals.
  """

  float_number = 7.0
  # Another way of declaring float is using float() function.
  float_number_via_function = float(7)
  float_negative = -35.59
  print(float_number, float_negative, float_number_via_function)
  
  # Float can also be scientific numbers with an "e" to indicate
  # the power of 10.
  float_with_small_e = 35e3
  float_with_big_e = 12E4

  print(float_with_big_e, float_with_small_e)


#? 4) complex numbers:  
def complex_numbers():
  """Complex Type"""

  complex_number_1 = 5 + 6j
  complex_number_2 = 3 - 2j

  print(complex_number_1)
  print(complex_number_2)
  print(complex_number_1 * complex_number_2 == 27 + 8j)


def number_operators():
  """Basic operations"""

  # Addition.
  print(2 + 4) 

  # Multiplication.
  print(2 * 4) 

  # Division always returns a floating point number.
  print(12 / 3) 
  print(12 / 5) 
  print(17 / 3) 

  # Modulo operator returns the remainder of the division.
  print(12 % 3) 
  print(13 % 3) 

  # Floor division discards the fractional part.
  print(17 // 3) 

  # Raising the number to specific power.
  print(5 ** 2)   # 5 squared
  print(2 ** 7)   # 2 to the power of 7

  # There is full support for floating point; operators with
  # mixed type operands convert the integer operand to floating point.
  print(4 * 3.75 - 1)