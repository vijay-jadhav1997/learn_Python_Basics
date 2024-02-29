import sys
import csv
from tabulate import tabulate
# define main Fn
def main():
   if validate_arg(sys.argv):
      table = get_table(sys.argv[1])
      print(tabulate(table, headers="firstrow", tablefmt="grid"))


# define validate_arg Fn to validate comman-line arguments
def validate_arg(arg):
  if len(arg) == 2:
    if arg[1].endswith(".csv"):
      return True  # valid csv file
    else:
      sys.exit("Not a CSV file")
  elif len(arg) < 2:
    sys.exit("Too few command-line arguments")
  elif len(arg) > 2:
    sys.exit("Too many command-line arguments")

# define
def get_table(csv_file):
  try:
    pizza_list = []
    with open(csv_file, "r") as file:
      reader = csv.reader(file)
      for row in reader:
        pizza_list.append(row)
    return pizza_list
  except FileNotFoundError:
    sys.exit("File does not exist")

if __name__ == "__main__":
  main()
