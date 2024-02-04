"""  Membership operators  """
#? Membership operators are used to test if a sequence is presented in an object.
#? Membership operators are commonly used in scenarios where you need to check whether a value exists or does not exist in a collection, list, tuple, set, or other iterable data structures.


def membership_operators():
  """Membership operators"""

  # Let's use the following fruit list to illustrate membership concept.
  fruit_list = ["apple", "banana", "mango", "orange"]

  # in
  # Returns True if a sequence with the specified value is present in the object.

  # Returns True because a sequence with the value "banana" is in the list
  print("banana" in fruit_list)

  # not in
  # Returns True if a sequence with the specified value is not present in the object

  # Returns True because a sequence with the value "pineapple" is not in the list.
  print("pineapple" not in fruit_list)

  # Returns False because a sequence with the value "pineapple" is not in the list.
  print("pineapple" in fruit_list)


#? 1) in Operator: The 'in' operator returns True if a specified value is found in the sequence, and False otherwise.

def in_operator():
  registered_usernames = ["user1", "user2", "user3"]

  username = input("Enter your username: ")

  if username in registered_usernames:
    print("Access granted!")
  else:
    print("Invalid username. Access denied.")


#? 2) not in Operator: The 'not in' operator returns 'True' if a specified value is not found in the sequence, and 'False' otherwise.
def not_in_operator():
  blocked_emails = ["spam@example.com", "phishing@example.com", "junk@example.com"]

  email = input("Enter your email address: ")

  if email not in blocked_emails:
    print("Email accepted!")
  else:
    print("Sorry, this email is blocked.")
