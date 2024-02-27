import abc

class GetSetParent(object):
  __metaclass__ = abc.ABCMeta

  def __init__(self):
    self.value = 0

  def get_value(self):
    return self.value
  
  def set_value(self, value):
    self.value = value
  
  @abc.abstractmethod
  def showdocument(self):
    return


class GetSetInt(GetSetParent):
  
  def get_value(self):
    return self.value
  
  def set_value(self, value):
    if not isinstance(value, int):
      value = 0
    super(GetSetInt, self).set_value(value)
  
  # Parent's class @abc.abstractmethod
  def showdocument(self):
    print(f"GetSetInt object ({self.value}), only accepts integer values.")

class GetSetList(GetSetParent):
  def __init__(self, value=0):
    self.values_list = [value]
  
  def get_value(self):
    return self.values_list[-1]

  def get_values(self):
    return self.values_list
  
  def set_value(self, value):
    self.values_list.append(value)
  
  def showdocument(self):
    print(f"GetSetList object, length {len(self.values_list)}, stores history of values set.")



test = GetSetInt()
print(test.get_value())

test.set_value(25)
print(test.get_value())

test.set_value("100")
print(test.get_value())
test.showdocument()


test_getsetlist = GetSetList()
print(test_getsetlist.get_value())

test_getsetlist.set_value(25)
print(test_getsetlist.get_value())

test_getsetlist.set_value("100")
test_getsetlist.set_value(25)
print(test_getsetlist.get_values())
test_getsetlist.showdocument()
