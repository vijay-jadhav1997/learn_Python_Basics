# Simple Calculator using Python
#* get user inputs
# x = input("enter 1st number!  => ")
# y = input("enter 2nd number!  => ")
# x = int(input("enter 1st number!  => "))
# y = int(input("enter 2nd number!  => "))
# x = float(input("enter 1st number!  => "))
# y = float(input("enter 2nd number!  => "))

#* perform addition
# result = int(x) + int(y)
# result = float(x) + float(y)
# result = round(x + y) # it will round floating number to integer.
# result = round(x + y, 2) # it will round the number up to 2 digit after decimal point.

#* print result to the screen:
# print(f"Sum =>  {result}")
#? formatting float
# print(f"Sum =>  {result:,}")

# def main():
#   num = round(float(input("Enter a integer number => ")))
#   print(f"Square of number {num} is {suare(num)}")


# def suare(n):
#   return pow(n, 2)


# main()

# define main Function
def main():
    greeting = input("Greeting: ").strip().lower()

    howGreeting(greeting)

# define howGreeting Fn
def howGreeting(greet):
    if greet.startswith('hello'):
        print("$0")
    elif greet.startswith('h'):
        print("$20")
    else:
        print("$100")

# call main Fn at the end
main()
