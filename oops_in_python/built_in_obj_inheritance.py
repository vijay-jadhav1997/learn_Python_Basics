class MyDict(dict):
  def get_keys(self):
    # print(self.keys())
    return self.keys()
  pass

dd = MyDict()    
dd['c'] = 20
dd['d'] = 200
for ky in dd.keys():
  print(ky,"=",dd[ky])
# dd.get_keys({'Jay':25, 'shree':52, 'om': 100, 'namo': 200, 'narayan': 400})
print(dd.get_keys())
