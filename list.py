students = ['JaY Shree Ram', 'Jay Shree Krushna', 'Jay Shree Vitthal', 'Jay Hari']

for i in students:
  print(i.replace(" ", "_").lower(), end=" ")

for i in range(len(students)):
  print(i ,students[i].replace(" ", "_").lower(), end=" ")


while True :
  n = int(input("\n Enter n => "))
  if n > 0 :
    break

# for _ in range(n):
#   print(f"{n}) Jay hari...🙏🏻")