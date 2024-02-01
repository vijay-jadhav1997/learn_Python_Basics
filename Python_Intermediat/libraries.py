import sys
def main():
  get_name()

def get_name():
  # try:
  #   print(f"My name is {sys.argv[1]}")
  # except IndexError:
  #   print(IndexError)
  if len(sys.argv) < 2:
    sys.exit("Too few arguments...!")
  
  for arg in sys.argv[1:]:
    print(f"{sys.argv.index(arg)}) {arg}")


main()