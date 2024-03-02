import sys

# Define the main function
def main():
  # Check command-line arguments and retrieve the number of lines of code
  if check_arg(sys.argv):
    line_of_code = get_lines_of_code(sys.argv[1])
    print(f"Number of non-empty lines of code: {line_of_code}")

# Define the check_arg function to validate command-line arguments
def check_arg(arg):
  if len(arg) == 2:
    if arg[1].endswith(".py"):
      return True  # Valid Python file
    else:
      sys.exit("Not a Python file")  # Exit if the specified file is not a Python file
  elif len(arg) < 2:
    sys.exit("Too few command-line arguments")  # Exit if too few command-line arguments
  elif len(arg) > 2:
    sys.exit("Too many command-line arguments")  # Exit if too many command-line arguments

# Define the get_lines_of_code function to count non-empty lines of code
def get_lines_of_code(py_file):
  try:
    with open(py_file, "r") as file:
      lines = 0
      for line in file:
        if not (line.strip().startswith("#")) and not (line.strip() == ""):
          # Count lines that are not comments and are not empty
          lines += 1
      return lines
  except FileNotFoundError:
    sys.exit(f"File '{py_file}' does not exist")  # Exit if the specified file does not exist

if __name__ == "__main__":
  main()
