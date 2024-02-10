import csv

students = []

# for _ in range(5):
#   student_info = input("Enter your info => ")

#   with open("students.csv", "a") as file:
#     file.write(f"{student_info}\n")


with open("students.csv") as file:
  reader = csv.reader(file)
  for name, address in reader:
    student = {"name": name, "address": address}
    students.append(student)

for student in sorted(students, key=lambda student: student["name"]):
  print(f"Name: {student["name"]}, Address: {student["address"]}")