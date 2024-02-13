def main():
  try:
    start_num, nth_term = input("Enter start number and number for nth_term (Example-> 25,11) => ").strip().split(",")
    nth_term = int(nth_term)
    number = find_nth_term(start_num, nth_term)
    print(f"{nth_term}th term of number {start_num} is {number}")
  except ValueError:
    print("Please, enter valid numbers in valid format!")

def find_nth_term(initial_num, nth):
  prev_num = str(initial_num)
  next_num = ""
  for i in range(nth):
    count = 0
    last_digits = ''
    for digit in prev_num:
      last_digits += digit
      if last_digits == prev_num:
        if len(prev_num) == 1:
          next_num += f"1{digit}"
        elif digit != last_digits[-2]:
          next_num += f"{count}{last_digits[-2]}1{digit}"
        else:
          count += 1
          next_num += f"{count}{digit}"

        prev_num = next_num 
        next_num = ""
      else:
        if last_digits == prev_num[0]: 
          count += 1
        elif digit == last_digits[-2]: 
          count += 1
        elif digit != last_digits[-2] and count == 0:
          next_num += f"1{last_digits[-2]}"
        elif digit != last_digits[-2] and count != 0:  
          next_num += f"{count}{last_digits[-2]}"
          count = 1
      
    print(f"{i + 1})",prev_num)
  return prev_num   



if __name__ == "__main__":
  main()