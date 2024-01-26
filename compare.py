name = (input("what's your name?  => ")).strip().title()
x = int(input("what is x?  => "))
y = int(input("what is y?  => "))

#? define if_else statement :
# if x > y:
#   print(f"Hello dear {name}, x({x}) is greater than y({y}). ")
# elif x < y:
#   print(f"Hello dear {name}, y({y}) is greater than x({x}). ")
# else:
#   print(f"Hello dear {name}, x({x}) is equal to y({y}). ")


#? another way
# if x > y or x < y:
#   print(f"Hello dear {name}, x({x}) is not equal to y({y}). ")
# else:
#   print(f"Hello dear {name}, x({x}) is equal to y({y}). ")

#? Yet another way
if x == y:
  print(f"Hello dear {name}, x({x}) is equal to y({y}). ")
else:
  print(f"Hello dear {name}, x({x}) is not equal to y({y}). ")
