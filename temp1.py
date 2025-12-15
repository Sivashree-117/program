print("--Temperature Converter--")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Celsius to Kelvin")
print("4. Kelvin to Celsius")
print("5. Fahrenheit to Kelvin")
print("6. Kelvin to Fahrenheit")

choice = int(input("Enter your choice (1-6): "))
temp = float(input("Enter temperature: "))

if choice == 1:
    conversion = "Celsius to Fahrenheit"
    result = (temp * 9/5) + 32
    unit = "F"
elif choice == 2:
    conversion = "Fahrenheit to Celsius"
    result = (temp - 32) * 5/9
    unit = "C"
elif choice == 3:
    conversion = "Celsius to Kelvin"
    result = temp + 273.15
    unit = "K"
elif choice == 4:
    conversion = "Kelvin to Celsius"
    result = temp - 273.15
    unit = "C"
elif choice == 5:
    conversion = "Fahrenheit to Kelvin"
    result = (temp - 32) * 5/9 + 273.15
    unit = "K"
elif choice == 6:
    conversion = "Kelvin to Fahrenheit"
    result = (temp - 273.15) * 9/5 + 32
    unit = "F"
else:
    conversion = "Invalid Choice"
    result = "No result"
    unit = ""

#  Store EVERYTHING
with open("temperature_output.txt", "a") as file:
    print("--Temperature Record--", file=file)
    print(f"Choice Entered : {choice}", file=file)
    print(f"Conversion    : {conversion}", file=file)
    print(f"Input Temp    : {temp}", file=file)
    print(f"Result        : {result} {unit}", file=file)
    print("-" * 35, file=file)

print("Temperature result stored in temperature_output.txt")
