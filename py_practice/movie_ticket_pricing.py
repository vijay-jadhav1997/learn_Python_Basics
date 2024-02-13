from datetime import datetime
def main():
  try:
    age_inp = int(input("How old are you? => "))
    ticket_price = get_price(age_inp)
  except ValueError:
    print("Please enter valid age in integer!")
  else:
    print(f"Movie Ticket Price is ${ticket_price}")
# define get_price() fn which return the discount
def get_price(age):
  price = 12 if age >= 18 else 8
  
  if datetime.now().strftime("%A") == 'Wednesday': 
    price -= 2

  leap_year = int(datetime.now().strftime("%Y"))
  if leap_year % 4 == 0 and leap_year%100 != 0:
    print(f"{leap_year} is leap year.")
  
  return price

if __name__ == "__main__":
  main()