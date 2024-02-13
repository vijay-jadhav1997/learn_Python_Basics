import sys
import requests

# define main fn
def main():
  if len(sys.argv) == 2 and sys.argv[1].isnumeric():
      num = float(sys.argv[1])
      get_bitcoin(num)
  elif len(sys.argv) == 1 :
      sys.exit("Missing command-line argument")
  elif len(sys.argv) > 2:
      sys.exit("More Command-line arguments!")
  elif not(sys.argv[1].isnumeric()):
      sys.exit("Command-line argument is not a number")

# define get_user_input fn
def get_bitcoin(dollar):
  try:
      response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
  except requests.RequestException:
      pass
  else:
      data = response.json()
      rate = data["bpi"]["USD"]["rate_float"]
      bitcoin = rate * dollar
  print(f"${'{:,}'.format(bitcoin)}")

# call main fn
if __name__ == "__main__":
  main()
