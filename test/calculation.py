def main():
  while True:
    try:
      x = int(input("what's x? "))
    except ValueError:
      pass
    else:
      print(f"square of x is {square(x)}")
      break


def square(n):
  return n * n


if __name__ == "__main__":
  main()