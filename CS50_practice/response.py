from validator_collection import checkers


def main():
  email_address = input("What's your email address? ")
  validation = validate(email_address)
  print(validation)


# define validate function to validate input email address and return valid/Invalid accordingly
def validate(email):
  try:
    is_email_id = checkers.is_email(email)
    return ("Valid" if is_email_id else "Invalid")
  except ValueError:
    return "Invalid"


if __name__ == "__main__":
  main()