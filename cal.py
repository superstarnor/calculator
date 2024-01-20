
def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):  
    return n1/n2


def calculator():
    print("Welcome to Super Calculator, lets do some computing...\n")
    to_continue = True
    total = 0
    n1 = int(input("First, choose a number"))
    
    while to_continue != False:
        
        
        op = int(input("1 - add, 2 - sub, 3 - multply, 4 - divide"))
        n2 = int(input("choose another number"))

        if op == 1:
            total = add(n1,n2)
            print(total)
        elif op == 2:
            total += subtract(n1,n2)
            print(total)
        elif op == 3:
            total += multiply(n1,n2)
            print(total)
        elif op == 4:
            total += divide(n1,n2)
            print(total)
        
        choice = input("Do you wanted to continue? Y or N")
    
        if choice == "N":
            to_continue = False
        

print(calculator())