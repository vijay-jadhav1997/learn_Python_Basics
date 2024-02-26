from random import choice

class Animal(object):
  def __init__(self, name):
    self.name = name
  
  def eat(self, food):
    print(f"{self.name} is eating {food}")

class Dog(Animal):
  def __init__(self,name):
    super(Dog, self).__init__(name)
    self.breed = choice(['Germen shefferd', 'Indian tiger', 'Russian leo', "italian sharko", "Japanese chinq"])
  def fetch(self, thing):
    print(f"{self.name} goes after the {thing}")

class Cat(Animal):
  def swatstring(self):
    print(f"{self.name} shreds the string!")
  

moti = Dog("Moti")
pinky = Cat("pinky")

moti.fetch("paper")   # op: Moti goes after the paper
pinky.swatstring()   # op: pinky shreds the string!
moti.eat("chapati")   # op: Moti is eating chapati
pinky.eat("milk-chapati")   # op: pinky is eating milk-chapati
# moti.swatstring()    #* op: AttributeError: 'Dog' object has no attribute 'swatstring'

print(moti.breed)