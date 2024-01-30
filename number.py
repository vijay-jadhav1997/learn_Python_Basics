######## PYTHON #######
#! LEARN ERROR handling
#* prompt user for x 
# try:
#   x = int(input("Enter integer as x => "))
# except ValueError:
#   print("❌ Please, enter valid integer as x")
# else:
#   print(f"✨ x is {x} 💥")

#* prompt user for 'x' until user input correct value using "while" loop with "break" statement:
# while True:
#   try:
#     x = int(input("Enter integer as x => "))
#   except ValueError:
#     print("❌ Please, enter valid integer as x")
#   else:
#     break

# print(f"✨ x is {x} 💥")

#* another way to excute same logic 
# while True:
#   try:
#     x = int(input("Enter integer as x => "))
#     break
#   except ValueError:
#     print("❌ Please, enter valid integer as x")

# print(f"✨ x is {x} 💥")

#? Now we do above task creating fn:
def main():
  x = get_int() # here we calling get_int Fn which eventually return value, then it wiil be assigned to x.
  print(f"✨ x is {x} 💥")

def get_int():
  # while True:
  #   try:
  #     x = int(input("Enter a integer number  => "))
  #   except ValueError:
  #     print("❌ Please, enter correct integer number.")
  #   else:
  #     break
  # return x
  #* another way 
  # while True:
  #   try:
  #     x = int(input("Enter a integer number  => "))
  #   except ValueError:
  #     print("❌ Please, enter correct integer number.")
  #   else:
  #    return x
  #* Yet another way:
  # while True:
  #   try:
  #     x = int(input("Enter a integer number  => "))
  #     return x
  #   except ValueError:
  #     print("❌ Please, enter correct integer number.")
  #* again most concise way :
  while True:
    try:
      return int(input("Enter a integer number  => "))
    except ValueError:
      # print("❌ Please, enter correct integer number.")
      pass  # here, we just passing the line without doing/printing anything. 
      # i.e. if we don't want to show what is going wrong to user then we could use "pass" keyword instead "print"/other
     
  

# call main fn
main()