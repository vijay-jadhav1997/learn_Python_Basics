""" Logical operators """
#? Logical operators are used to combine conditional statements.

def main():
  logical_operators()

def logical_operators():
  """Logical operators"""

  # Let's work with these number to illustrate logic operators.
  first_number = 5
  second_number = 10

  # and
  # Returns True if both statements are true.
  print(first_number > 0 and second_number < 20)

  # or
  # Returns True if one of the statements is true
  print(first_number > 5 or second_number < 20)

  # not
  # Reverse the result, returns False if the result is true.
  # pylint: disable=unneeded-not
  print(not first_number == second_number)
  print(first_number != second_number)



#? 1) and :  The and operator returns True if both operands are true; otherwise, it returns False.

age = 25
is_student = False

if age > 18 and not is_student:
  print("Eligible for voting")





#? 2) or : The or operator returns True if at least one of the operands is true; 
#?          it returns False if both operands are false.
is_weekend = True
is_holiday = False

if is_weekend or is_holiday:
  print("Time to relax!")




#? 3)not: The not operator is a unary operator that returns the opposite of the operand's boolean value. 
#?    If the operand is True, not returns False; if the operand is False, not returns True.
is_raining = False

if not is_raining:
  print("No need for an umbrella")

if __name__ == "__main__":
  main()