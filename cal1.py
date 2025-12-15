def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

with open("calculator_output.txt", "a") as file:
    print("----- Calculator Menu -----", file=file)
    print("1. Addition", file=file)
    print("2. Subtraction", file=file)
    print("3. Multiplication", file=file)
    print("4. Division", file=file)

    choice = int(input("Enter your choice (1-4): "))
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == 1:
        result = add(num1, num2)
    elif choice == 2:
        result = subtract(num1, num2)
    elif choice == 3:
        result = multiply(num1, num2)
    elif choice == 4:
        result = divide(num1, num2)
    else:
        result = "Invalid choice"

    print(f"Result: {result}", file=file)
    print("-" * 30, file=file)

print("Result stored in calculator_output.txt")
