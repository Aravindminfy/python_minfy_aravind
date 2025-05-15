print("******************* Welcome to the calculator**************************")

import math



def add(x,y):
    return x+y

def sub(x,y):
    return x-y

multi = lambda x,y : x*y

def div(x,y):
    try:
        return x/y
    except ZeroDivisionError as e:
        return "cannot divide by zero"
    except Exception as e:
        return f"error {e}"



while True:

    operation = input("enter the operations(+,-,*,/ ) : ")

    valid_operator = ['+','-','*','/']

    if operation in valid_operator:

        n1= int(input("Enter a number : "))
        n2 = int(input("Enter a number : "))

        if operation == '+':
            print(add(n1,n2))

        if operation == '-':
            print(sub(n1,n2))

        if operation == '*':
            print(multi(n1,n2))

        if operation == '/':
            print(div(n1,n2))

        cont = input("enter quit to end the calculation or press enter to continue : ")

        if cont == "quit":
            print("thank you")
            break
    else:
        print("Enter valid operation")