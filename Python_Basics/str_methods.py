date_inp = input("Date: ")

# if inp[0].isdigit():
#   print(f"Valid: ✅ => {int(inp)}")
# else:
#   print("Invalid: ❌")

#! str methods that returns True/False
date_inp.isalpha()
date_inp.isdigit()
date_inp.isspace()
date_inp.isnumeric()
date_inp.islower()
date_inp.isupper()
date_inp.isalnum()
date_inp.istitle()
date_inp.isidentifier()

#! str that returns index number
date_inp.index()
date_inp.find("substring")

#! str that returns copy of str
# date_inp[i : j]
date_inp.capitalize()
date_inp.title()
date_inp.lower()
date_inp.upper()
date_inp.endswith("substring")
date_inp.startswith("substring")
# date_inp.center(width, _fill_character)
# date_inp.rjust(width, _fill_character)
# date_inp.ljust(width, _fill_character)
date_inp.join(["str1", "str2", "str3"])
date_inp.format()
date_inp.encode()


if date_inp[0].isdigit():
  month, day, year = date_inp.split("/")
  month = int(month)
  day = int(day)
  print(day)
  print(year.isspace())