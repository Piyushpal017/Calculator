import art


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 + n2


def calculator(first_number, operation, second_number):
    operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

    result = operations[operation](n1=first_number, n2=second_number)
    print(f"{first_number} {operation} {second_number} =  {result}")

    while input(
            f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower() == "y":
        calculator(result, operation=input("""+
_
*
/
Pick an operation : """), second_number=float(input("What's the second number: ")))
    else:
        print("\n" * 20)
        print(art.logo)
        calculator(first_number=float(input("What's the first number: ")), operation=input("""+
_
*
/
Pick an operation : """), second_number=float(input("What's the second number: ")))


calculator(first_number=float(input("What's the first number: ")), operation=input("""+
_
*
/
Pick an operation : """), second_number=float(input("What's the second number: ")))
