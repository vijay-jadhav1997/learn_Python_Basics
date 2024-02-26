from random import randint

class InstanceCounter(object):
  count = 0

  def __init__(self, val):
    self.val = val
    value = InstanceCounter.count
    value += 1
    InstanceCounter.count = value


  @property
  def val(self) :
    return self._val

  @val.setter 
  def val(self, newval):
    self._val = newval

# a = InstanceCounter(5)
# b = InstanceCounter(13)
# c = InstanceCounter(17)

for i in range(5) :
  obj = InstanceCounter(randint(1,20))
  print(f"Value of obj: {obj.val}")
  print(f"Instance count : {obj.count}")


