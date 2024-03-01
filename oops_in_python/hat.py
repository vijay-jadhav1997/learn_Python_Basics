import random

class Hat:
  houses = ["Vrindavan", "Pandharpur", "Alandi", "Dehu", "Ayodhya"]

  @classmethod
  def sort(cls, name):
    house = random.choice(cls.houses)
    print(name, "is in", house)
  

hat = Hat()

# hat.sort("Jay Shree Radhe")
Hat.sort("Jay Shree Dnyanoba Mauli")
Hat.sort("Jay Shree Tukoba")
Hat.sort("Jay Shree Vitthal Rakhumai")
Hat.sort("Jay Shree Ram Lakshman Janaki Jay Bolo Hanuman ki!")