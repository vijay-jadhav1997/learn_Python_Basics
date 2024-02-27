class MyClass(object):

  @staticmethod
  def make_error():
    print("entering make_error()...💥")
    # zero_division_error = 5/0
    # print(zero_division_error)
    print("     leaving make_error()...✨")


  def do_something(self):
    print("entering do_something()...💥")
    self.make_error()
    print("     leaving do_something()...✨")

def some_util_func():
  print("entering some_util_func()...💥")
  cc = MyClass()
  cc.do_something()
  print("     leaving some_util_func()...✨")

def some_major_func():
  print("entering some_major_func()...💥")
  some_util_func()
  print("     leaving some_major_func()...✨")
    
def main():
  print("entering main()...💥")
  some_major_func()
  print("     leaving main()...✨")


if __name__ == "__main__":
  try:
    main()
  except ZeroDivisionError:
    print("Something went wrong in make_error function...!")
  else:
    print("Everything went as we expecting ...!")
