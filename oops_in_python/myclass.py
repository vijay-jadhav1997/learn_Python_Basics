class MyClass(object):

  def __enter__(self):
    print("We have entered 'with'")
    return self

  def __exit__(self, type, value, traceback):
    print("we are leaving 'with'")
  
  def greet(self):
    print(f"Jay Hari! instance {self}")
  

with MyClass() as testing:
  testing.greet()

print("after the 'with' block")