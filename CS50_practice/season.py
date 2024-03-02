from num2words import num2words
from datetime import datetime
import sys


def main():
  date_of_birth = input("Date of Birth: ")
  if is_valid_format(date_of_birth):
    age_in_minutes = get_age_in_minutes(date_of_birth)
    print(age_in_minutes.replace(" and ", " "), "minutes.")


# define is_valid_format function to validate user input date format & return True/False
def is_valid_format(date_str):
  try:
    # validate 'date_str' using 'strptime' method of 'datetime' module
    datetime.strptime(date_str, r"%Y-%m-%d")
  except ValueError:
    sys.exit("Invalid date")
  else:
    return True


# define get_age_in_minutes function to get age in minutes in words
def get_age_in_minutes(birth_date):
  todays_date_obj = datetime.now().date()
  birth_date_obj = datetime.strptime(birth_date, r"%Y-%m-%d").date()

  # Ensure birth date is not in the future
  if todays_date_obj < birth_date_obj:
    sys.exit("Invalid date. Birth date cannot be in the future.")
  # get age in days
  age_in_days = (todays_date_obj - birth_date_obj).days

  # get Age in minutes by multiplying it with 24 hrs * 60 minutes
  age_in_minutes = age_in_days * 24 * 60


  # convert age_in_minutes number to words using 'num2words' module of Python
  age_in_minutes_word = num2words(age_in_minutes)
  print(age_in_minutes_word)
  return age_in_minutes_word


if __name__ == "__main__":
  main()
