def main():
  plate = input("Plate: ")
  if is_valid(plate):
    print("Valid : ✅")
  else:
    print("Invalid: ❌")


def is_valid(s):
  if 2 <= len(s) <= 6 and s[0:2].isalpha() and s.isalnum():
    output = "a"
    for l in s:
      if l.isalpha() and output.isalpha():
        output += l
      elif l == "0" and output[-1].isalpha():
        output
      elif l.isdigit():
        output += l
    output = output[1:len(output)]
    print(output)
    if len(s) == len(output):
        return True
    else:
        return False
  else:
    return False
# call main Fn
main()
