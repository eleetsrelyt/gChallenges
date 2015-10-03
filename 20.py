## BMI Calculator

print("       BMI Calculator       ")
print("----------------------------")
height_in = float(input("Enter your height in inches: "))
weight_lbs = float(input("Enter your weight in pounds: "))

weight_kg = weight_lbs * 0.45
height_m = height_in * 0.025

height_2 = height_m * height_m
bmi = round(weight_kg / height_2,1)

if bmi<19:
    health = ", which is low."
else:
    if bmi>25:
        health = ", which is high."
    else:
        health = ", which is healthy."

print("Your BMI is",str(bmi) + health)
