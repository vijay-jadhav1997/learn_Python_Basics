import os
import sys

def main():
  try:
    if check_arguments(sys.argv): # only proceed further if arguments are valid
      overlay_shirt()
      # print("We're on right track.....")
  except  FileNotFoundError:
    print("Something went wrong!")



# define validate_arg Fn to validate command-line arguments
def check_arguments(arg):
  if len(arg) < 3:
    sys.exit("Too few command-line arguments")
  elif len(arg) > 3:
    sys.exit("Too many command-line arguments")
  else:
    return isextensions_valid(arg[1], arg[2])
    


# def isextensions_valid fn to check files extensions
def isextensions_valid(input, output):
  # getting the file extension using 'os.path' module 
  input_ext = os.path.splitext(input)[1]
  output_ext = os.path.splitext(output)[1]
  allow_exts = [".png", ".jpg", "jpeg"]
  if not(output_ext.lower() in allow_exts) and not (input_ext.lower() in allow_exts):
    sys.exit("Invalid inputs")
  elif not(output_ext.lower() in allow_exts):
    sys.exit("Invalid output")
  elif not (input_ext.lower() in allow_exts):
    sys.exit("Invalid input")
  else:
    if input_ext != output_ext:
      sys.exit("Input and output have different extensions")
    else:
      return True  # valid extensions

# define overlay_shirt fn 
def overlay_shirt(before, after):
  pass

if __name__ == "__main__":
  main()
