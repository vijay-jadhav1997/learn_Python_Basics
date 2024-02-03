""" Arithmatic Operators"""
#? Addition Operator => +
#? Substraction Operator => -
#? Multiplication Operator => *
#? Division Operator => /
#? Modulus Operator => %
#? Floor Division Operator => //

def main():
  try:
    num1, num2 = get_num("Enter two integers having space between (ex. 20 5) => ")
  except IndexError or ValueError :
    num1, num2 = get_num("Enter two integers having space between (ex. 20 5) => ")
  else:
    add_numb(num1, num2)
    sub_numb(num1, num2)
    multiply_numb(num1, num2)
    division_numb(num1, num2)
    modulus_numb(num1, num2)
    exp_of_numb(num1, num2)
    foor_division_numb(num1, num2)

# define get_num 
def get_num(msg):
  while True:
    try:
      numb1, numb2 = input(msg).strip().split(" ")
      numb1 = int(numb1)
      numb2 = int(numb2)
    except ValueError or EOFError :
      pass
    else:
      return (numb1, numb2)


#* Addition
def add_numb(num1, num2):
  try:
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
    return result
  except ValueError or EOFError:
    pass


#* Substraction 
def sub_numb(num1, num2):
  try:
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
    return result
  except ValueError or EOFError:
    pass



#* Multiplication
def multiply_numb(num1, num2):
  try:
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
    return result
  except ValueError or EOFError:
    pass


#* Division
# result of division is always float
def division_numb(num1, num2):
  try:
    result = num1/ num2
    print(f"{num1} / {num2} = {result}")
    return result
  except ValueError or ZeroDivisionError:
    pass



#* Modulus
def modulus_numb(num1, num2):
  try:
    result = num1 % num2
    print(f"{num1} % {num2} = {result}")
    return result
  except ValueError or EOFError:
    pass


#* Exponentiation
def exp_of_numb(num1, num2):
  try:
    if num2 < 10 :
      result = num1 ** num2
      print(f"{num1} ** {num2} = {result}")
      return result
    else:
      print(f"{num1} ** {num2} => out of range, '{num2}' 2nd value should be less than 10")
  except ValueError or EOFError:
    print("Out of the range")


#* Floor dividion
def foor_division_numb(num1, num2):
  try:
    result = num1 // num2
    print(f"{num1} // {num2} = {result}")
    return result
  except ValueError or EOFError:
    pass

if __name__ == "__main__":
  main()