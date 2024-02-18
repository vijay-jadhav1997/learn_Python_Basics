import math
import re

def main():
  # email = input("What's your email?\t").strip()
  # # print( f"Your email '{email}' is valid✔" if validate_email(email) else f"Your email '{email}' is invalid❌")
  # omkar = shree(5)
  # print(omkar(2))
  # print(greet("Raghav"))
  # print(greet())
  print("Jay Hari...!")
  # sum_all(1,2,3,4,5)
  # while True:
  #   try:
  #     end = int(input("Enter a +ve integer => "))
  #   except ValueError:
  #     print("Enter a valid integer...")
  #   else:
  #     for i in even_generator(end):
  #       print(i)
  #     break

  print(factorial(1))
  print(factorial(2))
  print(factorial(3))
  print(factorial(4))
  print(factorial(5))



def validate_email(email_id):
  # return True if "@" in email_id and email_id.endswith(".com") else False
  # if "@" in email_id and email_id.endswith(".com"):
  #   return True
  # else:
  #   pass

  return True if re.search("@", email_id) else False


def shree(num):
  def om(sqr):
    return num ** sqr
  return om

names = [
  {
    "fname": "Rameshwar",
    "age": 20,
    "is_educated": True,
  },
  {
    "fname": "Meena",
    "age": 22,
    "is_educated": True,
  },
  {
    "fname": "Aadesh",
    "age": 25,
    "is_educated": False,
  },
  {
    "fname": "Geeta",
    "age": 21,
    "is_educated": True,
  },
  {
    "fname": "Raghav",
    "age": 30,
    "is_educated": True,
  },
  {
    "fname": "Mahesh",
    "age": 15,
    "is_educated": True,
  },
]
# for name in sorted(names, key=lambda name: name["age"], reverse=True):
#   print(name)

def greet(name="Mohan"):
  return (f"✨Hello dear {name}, welcome in Python community! 👨🏻‍💻")

numbers = list(range(1,11))
# for number in numbers:
#   cube = lambda num: num**3
#   print(f"The cube of number {number} is {cube(number)}. 🎉")


square = lambda num: math.sqr(num)

def sum_all(*args):
  print(args)
  result = 0
  for num in args:
    result += num
  print(result)
  return result

def even_generator(num):
  for i in range(2, num+1, 2):
    yield i

def factorial(num):
  if num == 1:
    return 1
  else:
    return num * factorial(num-1)

if __name__ == "__main__":
  main()