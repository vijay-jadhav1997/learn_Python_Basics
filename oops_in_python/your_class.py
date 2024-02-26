import sys
class YourClass:
  class_attribute = 10
  classy = "class value!"

  def __init__(self):
    self.instance_attribute = 100
    self.insty = 50

inst = YourClass()

print(inst.classy) #* Here, 'classy' is class attribute/variable

inst.classy = "instance value!" #* we can set new instance attribue having same name of class attribute/variable
print(inst.classy) #* Here, 'classy' is instance attribute, bcs Python first look up to'instance attributes', if not found, then to 'class attributes'
print(YourClass.classy) #* Here, 'classy' is class attribute, Now Python look up to 'class attributes' directly

del inst.classy #* we can delete "instance attribute", Now there is no instance attribute of named 'classy'
print(inst.classy) #* Here, 'classy' is class attribute/variable, bcs we deleted 'classy' instance attribute

# del inst.class_attribute  #! We can't delete class attribute
print(inst.class_attribute)

inst.mess = [20, 10, 5, 0]  #* we are setting altogether a new instance attribute to instance object, named 'mess'
inst.var = {"greet":"Jay Hari" }  #* we are setting altogether a new instance attribute to instance object, named 'var'
print(inst.mess, inst.var)
# print(dir(inst))  #* 'dir()' a built-in function