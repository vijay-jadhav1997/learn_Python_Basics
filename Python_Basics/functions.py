def greet():
  print("Jay Jay Ram Krushna Hari ✨")

# greet()  

def add(num1, num2) -> int:
  res = num1 + num2
  print(f" {num1} + {num2} = {res}")
  return res


# add(5, 5)

def multiargs(*args):
  print(args)

# multiargs(2,3,5,8,9,6)
# multiargs()

def sum_of_all_num(*nums):
  res = 0
  for num in nums:
    res += num
  print(res)
  return res

# sum_of_all_num(1,2,3,4,5,6,7,8,9,10)
# sum_of_all_num()

def keyargs(**kwargs):
  print(kwargs)
  print(type(kwargs))

# keyargs(first= "Jay", last="Hari")
# keyargs()