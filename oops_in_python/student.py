class Student:
  def __init__(self, name, house):
    if not name:
      raise ValueError("Missing name")
    if house.title() not in ["Vrindavan", "Ayodhya", "Dwaraka", "Pandharpur"]:
      raise ValueError("Invalid house")
    self.name = name
    self.house = house
  
  def __str__(self):
    return f"Jay Shree Ram dear {self.name} and welcome to in our team!"
  
  def greet(self):
    return f"Jay Shree Ram dear {self.name} and welcome to in our team!"

def main():
  student = get_student()
  # print(f'{name} from {house}')
  # print(f'{student[0]} from {student[1]}')
  # print(f'{student["Name"]} from {student["House"]}')
  print(f'✨ {student.name} from {student.house} ...💥')
  print(student)

def get_student():
  # name = input("Name: ")
  # house = input("House: ")
  # return name, house
  # return [name, house]
  # name = input("Name: ")
  # house = input("House: ")
  # return {"Name": name, "House": house}
  # student = {}
  # student.name = input("Name: ")
  # student.house = input("House: ")

  name = input("Name: ")
  house = input("House: ")
  return Student(name, house)


if __name__ == "__main__":
  main()