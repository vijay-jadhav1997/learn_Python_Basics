# Define main Fn
def main():
  # Get user input
  user_inp = input("Enter how you're feeling today with emoticons => ")
  # Replace emoticons with emoji
  result = user_inp.replace(":)", "🙂").replace(":(", "🙁")
  displayRes(result)




#define displayRes Fn
def displayRes(res):
  # print result:
  print(res)

main()