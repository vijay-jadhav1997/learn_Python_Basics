import os

class ConfigDict(dict):
  def __init__(self, filename):
    self._filename = filename
    if os.path.isfile(self._filename):
      with open(self._filename) as file:
        for line in file:
          line = line.rstrip()
          key, value = line.split("=", 1)
          dict.__setitem__(self, key, value)
        
  def __setitem__(self, key, value):

    dict.__setitem__(self, key, value)
    with open(self._filename, 'w') as file:
      for key, value in self.items():
        file.write(f"{key} = {value}\n") 

  @property
  def filename(self):
    return self._filename
  


cd = ConfigDict('log.txt')

print(cd.filename)
print(cd)