import abc

#* Abstract class
class GetterSetter(object):
  __metaclass__ = abc.ABCMeta

  @abc.abstractmethod
  def set_value(self, input):
    """ Set a Value in the instance"""
    return

  @abc.abstractmethod
  def get_value(self):
    """Get and return a value from the instance..."""
    return


class MyClass(GetterSetter):
  # def set_valu(self, value):
  #   self.value = value
  
  def get_value(self):
    return self.value
  
myclass = GetterSetter()  
print(myclass)

