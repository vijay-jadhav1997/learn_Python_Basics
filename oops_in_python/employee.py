class Employee:
  office_brance = "India"
  def __init__(self, name, experience):
    self.name = name
    self.experience = experience
  
  def __str__(self):
    return f"We welcome you, dear {self.name} in our Indian office branch"
  
  def greeting(self):
    return f"Jay Shree Radhe Krushna"

  
# shree = Employee("Damodar", "Jay Jay Shree Dnyanoba Mauli Tukaram...!")

# print(shree)


class Parent:
  personality = "Introvert"
  languages_speak = ["English"]

  def __init__(self, name , age):
    self.name = name
    self.age = age
  
  def speak(self, language="Marathi"):
    return f"{self.name} speaks {language}!"

class Child(Parent):
  personality = "Extrovert"
  languages_speak = ["English", "Hindi"]
  # def __init__(self):
  #   super().__init__()
  #   self.seaks.append("Marathi")

  def speak(self, language="Sanskrut"):
    return super().speak(language)

child = Child("Raghavendra", 30)
parent = Parent("Madhav", 125)

# print(child.personality, child.speak())
# print(isinstance(child, Parent))
# print(isinstance(child, Child))
print(child.speak())
print(child.speak("English"))
print(parent.speak("Bruj dialect"))
print(parent.speak())


