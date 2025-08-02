# Simple BMI Calculator with Ranges

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height * height)
bmi = round(bmi, 2)

print("Your BMI is:", bmi)

# Check BMI category
if bmi < 18.5:
    print("Category: Underweight")
elif bmi < 24.9:
    print("Category: Normal weight")
elif bmi < 29.9:
    print("Category: Overweight")
else:
    print("Category: Obese")
