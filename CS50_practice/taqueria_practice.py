def main():
   get_total()

items = {
  "Baja Taco": 4.25,
  "Burrito": 7.50,
  "Bowl": 8.50,
  "Nachos": 11.00,
  "Quesadilla": 8.50,
  "Super Burrito": 8.50,
  "Super Quesadilla": 9.50,
  "Taco": 3.00,
  "Tortilla Salad": 8.00
}

# define get_total Fn
def get_total():
  total = 0.00
  while True:
    try:
      item = input("Item: ").strip().title()
      if item in items:
        total += items[item]
        print(f"Total: ${round(total, 2)}")
      
    except EOFError:
      break
    # except KeyError:
    #   pass
     


main()
