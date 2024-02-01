# 
#? define main function 
def main():
  # Get a number from user 
  num = int(input("Enter a number? => "))
  #* display whether it's Even or Odd:
  # if is_even(num):
  #   print(f"Number '{num}' is 'Even' ")
  # else:
  #   print(f"Number '{num}' is 'Odd' ")
  
  #* Another way to write above code
  print(f"Number '{num}' is 'Even' " if is_even(num) else f"Number '{num}' is 'Odd' ")


#? define is_even Fn which returns 'bool (True/False)' value
def is_even(number):
  #* using if_else statement we will return True or False according to whether number is even or not.
  # if number % 2 == 0 :
  #   return True
  # else:
  #   return False
  
  #* Another way of writing if_else statement in short (Ternary operator in Python called Pythonic way of writing if_else statement).
  # return True if number % 2 == 0 else False
  # return (True if number % 2 == 0 else False)

  #* Yet another most precise/elegant way of writing above code
  return number % 2 == 0 #* as we know the result of "number % 2 == 0" is itself bool value (True/False).
  # return (number % 2 == 0)

#? Call main Fn at the end of our code
main()