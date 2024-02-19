import csv

students = []

# for _ in range(5):
#   student_info = input("Enter your info => ")

#   with open("users.csv", "a") as file:
#     file.write(f"{student_info}\n")


with open("users.csv") as file:
  reader = csv.DictReader(file)
  for row in reader:
    student = {"name": row["name"], "address": row["address"]}
    students.append(student)

for student in sorted(students, key=lambda student: student["name"]):
  print(f"Name: {student["name"]}, Address: {student["address"]}")