# Define main fn
def main():
  user_inp = input("Input: ")
  remove_vowals(user_inp)

# define remove_vowals fn
def remove_vowals(input):
  output = ""
  for letter in input :
    match letter :
      case "A" | "a" | "E" | "e" | "I" | "i" | "O" | "o" | "U" | "u" :
        output
      case _ :
        output += letter

    # if letter != "A" or letter != "a" 
  print(f"Output: {output}")
# call main Fn
main()
