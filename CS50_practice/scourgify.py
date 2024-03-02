import csv
import sys

def main():
  if validate_arg(sys.argv):
    data = get_csvfile_data(sys.argv[1])
    write_csvfile(sys.argv[2],data)
    # print(str(data))

# define validate_arg Fn to validate command-line arguments
def validate_arg(arg):
  if len(arg) == 3:
      if arg[1].endswith(".csv") and arg[2].endswith(".csv"):
          return True  # valid csv file
      else:
          sys.exit("Not a CSV file")
  elif len(arg) < 3:
      sys.exit("Too few command-line arguments")
  elif len(arg) > 3:
      sys.exit("Too many command-line arguments")


# define get_table fn to get list of row list of csv_file
def get_csvfile_data(csv_file):
  try:
    listed_data = []
    with open(csv_file, "r") as file:
      reader = csv.DictReader(file)
      for row in reader:
        last, first = row["name"].strip().split(",")  # unpacking "first" & "last" name from "name".
        row_dict = {"first": first, "last": last, "house": row["house"]} # creat dict with "first", "last" & "house" keys.
        listed_data.append(row_dict)
    return listed_data # returns the listed data of row_dict list of csv_file
  except FileNotFoundError:
    sys.exit(f"Could not read {csv_file}")

# define write_csvfile to create csv file of expected format
def write_csvfile(after_csvfile, obj_list):
  try:
    for obj in obj_list:
      last_name, first_name = obj["name"].strip().split(",")
      with open(after_csvfile, "a") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writerow({"first": first_name, "last": last_name, "house": obj["house"]})
  except ValueError:
     print(ValueError, "line 44")

if __name__ == "__main__":
  main()
