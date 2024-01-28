def main():
    user_inp = input("Expression: ").split(" ")
    x = float(user_inp[0])
    y = user_inp[1]
    z = float(user_inp[2])
    calc(x , y , z)

# define calc
def calc(num1 = 1 , oper = '+' , num2 = 1):
    match oper:
        case '+':
            print(f"{round(num1 + num2, 1)}")
        case '-':
            print(f"{round(num1 - num2, 1)}")
        case '*':
            print(f"{round(num1 * num2, 1)}")
        case '/':
            print(f"{round(num1 / num2, 1)}")
        # case _:
        #     print("")


main()
