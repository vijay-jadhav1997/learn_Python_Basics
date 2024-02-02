def main():
    fuel = get_fuel("Fraction: ")
    print(fuel)

# define get_fuel Fn
def get_fuel(fraction):
  while True:
    try:
      numer, denom = input(fraction).split("/")
      numer = int(numer)
      denom = int(denom)
    except ValueError:
      pass
    else:
      if numer > denom or denom == 0:
        pass
      else:
        break
  result = round((numer / denom) * 100)
  if result <= 1 :
    return "E"
  elif result >= 99 :
    return "F"
  else:
    return f"{result}%"

main()
