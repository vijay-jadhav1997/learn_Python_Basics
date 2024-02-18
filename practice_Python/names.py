#**************##### Jay Jay Ram Krushna hari #####***************#

# names = []

# for _ in range(3):
#   name = input("What's your name => ")
#   names.append(name)

# for name in sorted(names):
#   print(name)

#?
# name = input("What's your name => ")
# file = open("names.txt", "a")
# file.write(f"{name}\n")
# file.close()
# for _ in range(3):
#   name = input("What's your name => ")
#   with open("names.txt", "a") as file:
#     file.write(f"{name}\n")

#? 
# with open("names.txt", "r") as file:
#   lines = file.readlines()

# for line in sorted(lines):
#   print(line.rstrip())

# with open("names.txt", "r") as file:
#   for line in file:
#     print(line.rstrip())

# for _ in range(3):
#   name = input("What's your name & address => ")
#   with open("names.csv", 'a') as file:
#     file.write(f"{name}\n")
  
# with open("names.csv", "r") as file:
#   for line in sorted(file):
#     namee,address = line.rstrip().split(",")
#     print(f"name: {namee}, address: {address}")
students = []
with open("names.csv", "r") as file:
  for line in file:
    name, address = line.rstrip().split(",")
    student = {"name": name, "address": address}
    students.append(student)

# print(str(students))
#? passing 'key' (2nd argument)= a function (get_name fn) to sorted() fn
# def get_name(student):
#   return student["name"]

# for student in sorted(students, key=get_name):
#   print(f"name: {student['name']}, address: {student["address"]}")

#? passing 'key' (2nd argument)= lambda fn 
for student in sorted(students, key=lambda student: student["name"]):
  print(f"Name: {student["name"]}, Address: {student["address"]}")