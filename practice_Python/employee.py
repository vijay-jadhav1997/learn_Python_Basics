import csv

employees = []

# for _ in range(5):
#   name = input("Enter your name => ")
#   address = input("Enter your address => ")

#   with open("employees.csv", "a") as file:
#     writer = csv.writer(file)
#     writer.writerow([name, address])

for _ in range(3):
  name = input("Enter your name => ")
  address = input("Enter your address => ")

  with open("employees.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "address"])
    writer.writerow({"name": name, "address": address})


with open("employees.csv") as file:
  reader = csv.DictReader(file)
  for row in reader:
    employee = {"name": row["name"], "address": row["address"]}
    employees.append(employee)

for employee in sorted(employees, key=lambda employee: employee["name"]):
  print(f"Name: {employee["name"]}, Address: {employee["address"]}")