import math

def main():
  # num = int(input("Enter any positive integer => "))
  # nums = get_sum_of_even_nums(num)
  # print(f"💥 Sum of even numbers up to {num} is {nums} ✨")
  
  # input_list = input("Enter numbers like 4,-5,10,43,-100,20,33,-4,... =>").strip().split(",")
  # nums, counts = get_positive_numbers(input_list)
  # print(f"{counts} & positive nums list = {nums}")
  
  # print_table(num)
  # calc_factorial(num)

  # string = input("Enter any word =>") 
  # reverse_string(string)

  # find_1st_nonrepeated_char(string)

  # validate_input()

  check_prime_number()
  

def get_positive_numbers(numbers):
  try:
    nums = []
    count = 0
    for num in numbers:
      # print(num)
      num = int(num)
      if abs(num) == num:
        nums.append(num)
        count += 1
  except ValueError:
    raise ValueError
  else:
    return nums, count

# define get_sum_of_even_nums which return sum of even numbers up to nth number
def get_sum_of_even_nums(nth):
  try:
    result = 0
    for num in range(0,abs(nth)+1,2):
      result += num
  except ValueError:
    raise ValueError
  else:
    return result

# define print_table func that print the multiplication table of given number skipping 5th row
def print_table(num):
  try:
    for i in range(1,11):
      if i == 5:
        continue
      print(f"{num} X {i} = {num * i}")
  except ValueError:
    print("Something went wrong!")

# define reverse_string(string) which return the string having reverse ordered characters
def reverse_string(word):
  try:
    reverse_str = ""
    for ch in word:
      reverse_str = ch + reverse_str
  except ValueError:
    print("Something went wrong...")
  else:
    print(reverse_str)
    return reverse_str

# define find_1st_nonrepeated_char fun that raturn 1st non-repeated character
def find_1st_nonrepeated_char(word):
  try:
    for ch in word:
      if word.count(ch) == 1 and ch != " ":
        print(ch)
        return ch
  except ValueError:
    print("Something went wrong...")

# define calc_factorial fn to calculate factorial of given +ve intger
def calc_factorial(num):
  count = 2
  factorial = 1
  while count <= num:
    factorial *= count
    count += 1
  #? Alternate Solution:
  # while num > 0:
  #   factorial *= num
  #   num -= 1
  print(f"{num}! = {factorial}")
  return factorial
    
# define function that promt user for a number until user enter a number between 1 and 10
def validate_input():
  while True:
    try:
      num = int(input("Enter a number b/w 1 & 10 => "))
    except ValueError:
      print("Enter valid number")
    else:
      if 1 <= num <= 10 :
        print(f"Congrats! You have entered number {num}")
        break
      else:
        print("Inavlid number! Please, try again")

# define function that promt user for 10 times, to enter a number and tells the whether number is prime number or not.
def check_prime_number():
  for i in range(10):
    try:
      num = int(input("Enter any +ve integer => "))
    except ValueError:
      print("Please, enter valid number")
    else:
      is_prime = True
      sqroot = round(math.sqrt(num))
      for j in range(2, sqroot+1):
        if (num % j) == 0 :
          is_prime = False
          break
      if is_prime :
        print(f"Yes! ✨Number {num} is a prime number.")
      else:
        print(f"Oh ho! ✨Number {num} is not a prime number.")





if __name__ == "__main__":
  main()