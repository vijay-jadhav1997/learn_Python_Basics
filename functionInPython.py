def square(num):
    return num * num

numSqr = square(5)

# Sprint(numSqr)


def welcomeMsg():
    return "**************\n*           *\n*   WELCOME!    *\n*           *\n**************"


# print(welcomeMsg)

def greeting(userName="user"):
    print(f"Welcome dear, {userName.title()} !")

# userInp = input("Enter your name here => ")


# greeting(userInp)
# greeting()


def main():
    userName = input("what's your name? => ").title()
    hello(userName)
    hello()


def hello(user_name="user"):
    print(f"Jay Hari, dear {user_name}!")


main()