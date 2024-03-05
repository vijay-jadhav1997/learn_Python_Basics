class MaxSizeList():
  def __init__(self, limit):
    self.limit = limit
    self.mylist = []

  def push(self, element):
    self.mylist.append(element)
    if len(self.mylist) > self.limit:
      self.mylist.pop(0)

    