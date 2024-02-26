import random

class Myclass:
  #* class attributes => devotion, love
  devotion = "Shree Radhe Krushna"
  love = "Shree Dnyanoba Mauli Tukaram"

  def __init__(self, name, state):
    #* Instance attributes => name, state, random_int
    print("Calling __init__")
    self.name = name
    self.state = state
    self.random_int = random.randint(1,10)

  #* Instance method
  def greet(self):
    print("Jay Jay Ram Krushna Hari...!")
  
  def __str__(self):
    return f"🙏🏻 Jay Hari Maharaj ji from {self.name}"
  
  def magic_num(self):
    return  random.random.choice(["Jay Hari", "Radhe Radhe", "Ram Krushna Hari", "Har Har Mahadev", "Namo Narayan"])
    

  @property #* getter for name
  def name(self):
    print("Calling getter fn for name")
    # print("Jay Shree Radhe Krushna")
    return self.__name

  @name.setter #* setter for name
  def name(self, name):
    print("Calling setter fn for name")
    # print("Shree Dnyanoba Mauli Tukaram")
    self.__name = name





# instance = Myclass("Madhav", "devotee")
# instance.greet()
# print(instance.__str__())
# print(instance)
# instance.name = "Raghav"
# print(instance.random_int)
# print(instance.greet())
# instance.name

class MyNum():
  def __init__(self, num):
    print("Calling __init__")
    self.num = num
  
  def __str__(self):
    return "This class has number of instance method for math"

  @property  #* getter for num 
  def num(self):
    print("Calling getter fn for num")
    return self._num
  
  @num.setter #* setter for num
  def num(self, num):
    print("Calling setter fn for num")
    self._num = num
  
  #* Increment fun
  def increment(self, add=1):
    print("Calling Increment fun")
    self.num += add
    print("incremented")
    return  self._num 



mynum = MyNum(10)
print(mynum.num)
mynum.increment(10)
print(mynum.num)