def main():
  create_list()




def create_list():
  items = {}
  while True:
    try:
      item = input("").upper()
    except EOFError:
      items = {item: items[item]  for item in sorted(items)}
      for item in items:
        print(f"{items[item]} {item}")
      break
    except KeyError:
      pass
    else:
      if item in items :
        items[item] += 1
      else:
        items[item] = 1

# call main Fn
main()
