with open("temperature_output.txt", "a") as file:
    print("----- Temperature Converter -----", file=file)
    print("1. Celsius to Fahrenheit", file=file)
    print("2. Fahrenheit to Celsius", file=file)
    print("3. Celsius to Kelvin", file=file)
    print("4. Kelvin to Celsius", file=file)
    print("5. Fahrenheit to Kelvin", file=file)
    print("6. Kelvin to Fahrenheit", file=file)

    choice = int(input("Enter your choice (1-6): "))
    temp = float(input("Enter temperature: "))

    if choice == 1:
        result = (temp * 9/5) + 32
        unit = "F"
    elif choice == 2:
        result = (temp - 32) * 5/9
        unit = "C"
    elif choice == 3:
        result = temp + 273.15
        unit = "K"
    elif choice == 4:
        result = temp - 273.15
        unit = "C"
    elif choice == 5:
        result = (temp - 32) * 5/9 + 273.15
        unit = "K"
    elif choice == 6:
        result = (temp - 273.15) * 9/5 + 32
        unit = "F"
    else:
        result = "Invalid choice"
        unit = ""

    print(f"Input: {temp}", file=file)
    print(f"Result: {result} {unit}", file=file)
    print("-" * 30, file=file)

print("Temperature result stored in temperature_output.txt")
