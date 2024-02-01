name = (input("what's your name?  => ")).strip().title()
x = int(input("what is x?  => "))
y = int(input("what is y?  => "))

#* print output using 'or' & 'and' logical operators
x > y and  print(f"Hello dear {name} ji, x({x}) is greater than y({y}). ")
x != y or print(f"Hello dear {name} ji, x({x}) is equal to y({y}). ")
# x == y and print(f"Hello dear {name}, x({x}) is equal to y({y}). ")
x < y and print(f"Hello dear {name} ji, y({y}) is greater than x({x}). ")


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
# if x == y:
#   print(f"Hello dear {name}, x({x}) is equal to y({y}). ")
# else:
#   print(f"Hello dear {name}, x({x}) is not equal to y({y}). ")


#* Yet again another way using 'or' & 'and' logical operators
# x == y or print(f"Hello dear {name}, x({x}) is not equal to y({y}). ")
# x == y and print(f"Hello dear {name}, x({x}) is equal to y({y}). ")