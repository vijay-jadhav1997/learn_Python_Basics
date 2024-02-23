# Parent class for 'Student' and 'Professor' classes
class Wizard:
  def __init__(self, name):
    self.name = name


# child class of 'Wizard' class
class Student(Wizard):
  def __init__(self, name, house):
    super().__init__(name) 
    self.house = house

# child class of 'Wizard' class
class Professor(Wizard):
  def __init__(self, name, subj):
    super().__init__(name)
    self.subject = subj


wizard = Wizard("Jay Shree Narayan")
student = Student("Raghav", "Ayodhya")
math_prof = Professor("Chanakya", "ArthaShastras")

print(wizard.name)
print(student.house)
print(math_prof.subject)