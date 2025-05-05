def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2


print("Welcome to calculator !")


# if ops not in ("+", "-", "*", "/"):
#     print("invalid operator")
# elif ops=="+":
#     result=add(n1,n2)
# elif ops=="-":
#     result=subtract(n1,n2)
# elif ops=="*":
#     result=multiply(n1, n2)
# elif ops=="/":
#      result=divide(n1, n2)
# print(f"Result is:{result}") 
should_contunue=True
while should_contunue:
    operator = {"+": add,
                "-": subtract,
                "*": multiply,
                "/": divide,
                }
    num1 = int(input("Please enter first number:"))
    for symbol in operator:
        print(symbol)
    ops = input("Please choose an operator from above list: '+' or '-' or '*' or '/':")
    num2 = int(input("Please enter second number:"))
    result=operator[ops](num1,num2)
    print(f"{num1} {ops} {num2} = {result}")
    choice=input("Wish to continue calculator?: Types Yes or No").lower()
    if choice == "no":
        should_contunue=False
        print("exiting calculator")


