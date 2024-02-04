""" Identity operators """
#? Identity operators are used to compare the objects, not if they are equal, but if they are actually
#? the same object, with the same memory location.

def main():
    # identity_operators()
    is_operator()
    is_not_operator()



def identity_operators():
  """Identity operators"""

  # Let's illustrate identity operators based on the following lists.
  first_fruits_list = ["apple", "banana"]
  second_fruits_list = ["apple", "banana"]
  third_fruits_list = first_fruits_list

  # is
  # Returns true if both variables are the same object.

  # Example:
  # first_fruits_list and third_fruits_list are the same objects.
  print(first_fruits_list is third_fruits_list)

  # is not
  # Returns true if both variables are not the same object.

  # Example:
  # first_fruits_list and second_fruits_list are not the same objects, even if they have
  # the same content
  print(first_fruits_list is not second_fruits_list)
  print(first_fruits_list is second_fruits_list)

  # To demonstrate the difference between "is" and "==": this comparison returns True because
  # first_fruits_list is equal to second_fruits_list.
  print(first_fruits_list == second_fruits_list)
  print(first_fruits_list == third_fruits_list)



#? 1) is :  The is operator checks if two variables refer to the exact same memory location
def is_operator():
  ayodhya = ["jay", "shree", "ram"]
  sharayu = ayodhya

  if ayodhya is sharayu:
    print("Both variables (ayodhya & sharayu) reference the same list in the memory locations.")
    print(f"{ayodhya} == {sharayu} => {sharayu == ayodhya}")
    print(f"{ayodhya} is not {sharayu} => {sharayu is not ayodhya}")
    print(f"{ayodhya} is {sharayu} => {sharayu is ayodhya}")

  
  num1 = 25
  num2 = 25
  if num1 is num2:
    print("Both variables reference the same integer in the memory locations.")
    print("Certain values (like small strings and integers), Python may choose to reuse memory locations to be more efficient.")

#? 2) is not: The is not operator returns True if both operands do not refer to the same object in memory; 
#?      it returns False if they do.

def is_not_operator():
  list1 = [25, "jay", True]
  list2 = [25, "jay", True]

  if list1 is not list2:
    print("The two variables reference different list objects in the memory locations, even though they have same values.")
    print(f"{list1} == {list2} => {list2 == list1}")
    print(f"{list1} is not {list2} => {list2 is not list1}")
    print(f"{list1} is {list2} => {list2 is list1}")


if __name__ == "__main__":
  main()