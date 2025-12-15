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

print("-- Calculator Menu --")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice = int(input("Enter your choice (1-4): "))
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == 1:
    operation = "Addition"
    result = add(num1, num2)
elif choice == 2:
    operation = "Subtraction"
    result = subtract(num1, num2)
elif choice == 3:
    operation = "Multiplication"
    result = multiply(num1, num2)
elif choice == 4:
    operation = "Division"
    result = divide(num1, num2)
else:
    operation = "Invalid Choice"
    result = "No result"

#  Store EVERYTHING
with open("calculator_output.txt", "a") as file:
    print(" //Calculator Record// ", file=file)
    print(f"Choice Entered : {choice}", file=file)
    print(f"Operation     : {operation}", file=file)
    print(f"Number 1      : {num1}", file=file)
    print(f"Number 2      : {num2}", file=file)
    print(f"Result        : {result}", file=file)
    print("-" * 35, file=file)

print("Result stored in calculator_output.txt")
