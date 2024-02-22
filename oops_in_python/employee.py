class Employee:
  # def __init__(self, name, age):
  #   self.name = name
  #   self.age = age
  pass
  
a = Employee()
b = Employee()
c = a

print(a == b, a is b)
print(a == c, a is c)
print(b == c, b is c)
print(a == a, a is a)
