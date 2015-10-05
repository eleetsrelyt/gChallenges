## Temperature Converter

print(" Temperature Converter ")
print("------------------------")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

option = input("Select a conversion")
tempinit = float(input("Starting Temperature:"))

if option == 1:
    tempout = ((tempinit * 9) / 5) + 32
    print(tempout, "F")
else:
    tempout = ((tempinit - 32) / 9) * 5
    print(tempout, "C")
