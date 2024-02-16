import sys
import os
from PIL import Image, ImageOps

def main():
  # process_img()
  resize_img(sys.argv[1], sys.argv[2])

def process_img():
  # for img in sys.argv[1:]:
  try:
    img = Image.open(sys.argv[1])
    cropped_img = img.crop((200,100,400,400))
    cropped_img.save("tukoba.png")
  except (FileNotFoundError,OSError):
    sys.exit("Something went wrong...!")


# Merging Images 
def resize_img(img1, img2):
  try:
    img1 = Image.open(img1)
    shirt = Image.open("shirt.png")
    # print(shirt.size)
    cropped_img = ImageOps.fit(img1, shirt.size, method=0, bleed=0.0,centering=(0.5, 0.5))
    cropped_img.paste(shirt, (0,0), shirt)
    cropped_img.save(img2)
  except (FileNotFoundError, OSError):
    sys.exit("Something went wrong! in resize_img fun")

if __name__ == "__main__":
  main()