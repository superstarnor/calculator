


def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):  
    return n1/n2


def calculator():
    print("welcome to our homemade calculator")
    print("You would choose two number and choose an operation")
    num1 = int(input("Choose a number"))
    num2 = int(input("chose another number"))
    op = input("choose 1 - add, 2 - subtract, 3 - multiply, 4 - divide")
    if op == "1":
        return add(num1,num2)
    elif op == "2":
        return subtract(num1,num2)
    elif op == "3":
        return multiply(num1,num2)
    elif op == "4":
        return divide(num1,num2)

    else:
        return "Not chosen valid operation"

print(calculator())