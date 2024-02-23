class Student:
  def __init__(self, name, house):
    self.name = name
    self.house = house
  
  def __str__(self):
    return f"Jay Shree Ram dear {self.name} and welcome to in our team!"
  
  def greet(self):
    return f"Jay Shree Ram dear {self.name} and welcome to in our team!"

  @classmethod
  def get(cls):
    name = input("Name: ")
    house = input("House: ")
    return cls(name, house)

  @property # Getter for name
  def name(self):
    return self._name
  
  @name.setter  # Setter for name
  def name(self, name):
    if not name:
      raise ValueError("Missing name!")
    self._name

  @property # Getter for house
  def house(self):
    return self._house
  
  @house.setter  # Setter for house
  def house(self, house):
    if house.title() not in ["Vrindavan", "Ayodhya", "Pandharpur", "Kashi", "Kanchi"]:
      raise ValueError("Invalid house")
    self._house = house


def main():
  student = Student.get()
  print(f'✨ {student.name} from {student.house} ...💥')



if __name__ == "__main__":
  main()