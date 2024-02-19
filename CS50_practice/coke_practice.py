# define main Fn
def main():
  change_owed = 0
  amount_due = 50
  prompt_user(change_owed, amount_due)

# define prompt_user fn
def prompt_user(change, amount):

  while amount > 0 :
    print(f"Amount Due: {amount}")
    user_inp = int(input("Insert Coin: "))
    if user_inp == 5 or user_inp == 10 or user_inp == 25:
      amount -= user_inp
  change = abs(amount)
  print(f"Change Owed: {change}")

# call main fn
main()
