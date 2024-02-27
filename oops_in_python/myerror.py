class MyError(Exception):
  def __init__(self, *args):
    print("Calling __init__() ✨")
    if args:
      self.message = args[0]
    else:
      self.message = None
  
  def __str__(self):
    print("Calling __str__() ✨")
    if self.message:
      return f"Here's a MyError exception with a message: {self.message}"
    else:
      return "Here's a MyError exception!"


# raise MyError

raise MyError("Heey, we have a problem")

