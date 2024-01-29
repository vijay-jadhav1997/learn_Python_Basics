def main():
  camel = input("camelCase: ")
  convert_to_snake_case(camel)


# def convert_to_snake_case()
def convert_to_snake_case(name):
  snake_case = ' '
  for letter in name:
    if letter.isupper():
      snake_case += f"_{letter.lower()}"
    else:
      snake_case += f"{letter}"

  print(f"snake_case: {snake_case.strip()}")




# call main Fn:
main()
