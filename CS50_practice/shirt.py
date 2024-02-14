import os
import sys
from PIL import Image, ImageOps


def main():
  if check_arguments(sys.argv):  # only proceed further if arguments are valid
    overlay_shirt(sys.argv[1], sys.argv[2])


# define validate_arg Fn to validate command-line arguments
def check_arguments(arg):
  if len(arg) < 3:
    sys.exit("Too few command-line arguments")
  elif len(arg) > 3:
    sys.exit("Too many command-line arguments")
  else:
    return isextensions_valid(arg[1], arg[2])


# define isextensions_valid fn to check files extensions.
def isextensions_valid(input, output):
  # getting the file extension using 'os.path' module.
  input_ext = os.path.splitext(input)[1]
  output_ext = os.path.splitext(output)[1]
  allow_exts = [".png", ".jpg", "jpeg"]
  if not (output_ext.lower() in allow_exts) and not (input_ext.lower() in allow_exts):
    sys.exit("Invalid inputs")  # exit if both files have invalid extensions.
  elif not (output_ext.lower() in allow_exts):
    sys.exit("Invalid output")  # exit if output file has invalid extension.
  elif not (input_ext.lower() in allow_exts):
    sys.exit("Invalid input")  # exit if input file has invalid extension.
  else:
    if input_ext != output_ext:
      sys.exit("Input and output have different extensions")
    else:
      return True  # files have allowed extensions.


# define  overlay_shirt function to overlay shirt.png
def overlay_shirt(before, after):
  try:
    image = Image.open(before)
    shirt = Image.open("../practice_Python/shirt.png")
  except FileNotFoundError:
    sys.exit("Input does not exist")  # exit if input file doesn't exist.

  else:
    resized_img = ImageOps.fit(image, shirt.size, bleed=0.0,centering=(0.5,0.5)) # resize input image to be the same size of shirt.png
    resized_img.paste(shirt, shirt)  # overlay shirt.png over resized_img
    resized_img.save(after, format="png")  # save
    if resized_img.size == shirt.size:
      print("They are of same size!")
    else:
      print("They arer't of same size!")


if __name__ == "__main__":
  main()
