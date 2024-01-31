import random

# define main fn
def main():
  level = get_level()
  generate_integer(level)


# define get_level fn
def get_level():
  while True:
      try:
          level_inp = int(input("Level: "))
      except ValueError or KeyError:
          pass
      else:
          if 0 < level_inp <= 3:
              return level_inp

# define generate_integer fn
def generate_integer(level):
  score = 0
  if level == 1:
      low = 0
      high = 9
  elif level == 2:
      low = 10
      high = 99
  elif level == 3:
      low = 100
      high = 999

  for j in range(10):
      try:
          x = random.randint(low, high)
          y = random.randint(low, high)
      except ValueError:
          raise ValueError
      else:
          result = check_problem(x, y, score)
          if result :
              score += 1
          if j == 9:
              print(f"Score: {score}")

# define check_problem fn
def check_problem(a, b, score):
  for i in range(3):
      try:
          answer = input(f"{a} + {b} = ")
      except ValueError:
          pass
      else:
          if answer.isdigit() and int(answer) == (a + b):
              return True
          else:
              print("EEE")
              if i == 2:
                  print(f"{a} + {b} = {a+b}")
                  return False




# call main fn
if __name__ == "__main__":
  main()
