from calculation import square

def main():
  test_calc()


def test_calc():
  #? 1st way
  # if square(2) != 4:
  #   print(" 2 square was not 4")
  # if square(-3) != 9:
  #   print(" -3 square was not 9")
  # if square(5) != 25:
  #   print(" 5 square was not 25")
  # if square(100) != 10000:
  #   print(" 100 square was not 10000")

  #? 2nd way using assert keyword with try_except exception handling statement
  # try:
  #   assert square(2) == 4
  # except AssertionError:
  #   print(" 2 square was not 4")
  # try:
  #   assert square(-3) == 9
  # except AssertionError:
  #   print("-3 square was not 9")
  # try:
  #   assert square(10) == 1000
  # except AssertionError:
  #   print("10 square was not 1000")

  #? most excellent way using assert keyword with "pytest" 3rd party library
  assert square(2) == 4
  assert square(-5) == 25
  assert square(0) == 0
  assert square(-10) == 100
  assert square(25) == 625


if __name__ == "__main__":
  main()