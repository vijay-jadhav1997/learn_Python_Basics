class GetSet(object):
  instance_count = 0

  __mangled_name = "no privacy!"
  
  def __init__(self, value):
    self.instance_attr = value
    GetSet.instance_count += 1

  @property
  def instance_attr(self):
    print("getting the 'instance_attr' attribute")
    return self._instance_attr

  @instance_attr.setter
  def instance_attr(self, value):
    print("setting the 'instance_attr' attribute")
    self._instance_attr = value
  
  @instance_attr.deleter
  def instance_attr(self):
    print("deleting the 'instance_attr' attribute")
    self._instance_attr = None
    

test = GetSet(20)
test = GetSet(10)
test = GetSet(5)
print(test.instance_count)
print(test.__mangled_name)
# test.instance_attr = "Jay Shree Ram"
# print(test.instance_attr)
# test.instance_attr = "Jay Shree Radhe Radhe Krushna"
# print(test.instance_attr)
