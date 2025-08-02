# Advanced BMI Calculator (CLI Version)

def calculate_bmi(weight, height):
    """Calculate BMI given weight in kg and height in meters."""
    return round(weight / (height ** 2), 2)

def classify_bmi(bmi):
    """Classify BMI based on standard WHO categories."""
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 24.9:
        return "Normal weight"
    elif bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def get_user_input():
    """Safely get user input for weight and height."""
    while True:
        try:
            weight = float(input("Enter your weight in kilograms (kg): "))
            height = float(input("Enter your height in meters (m): "))
            if weight <= 0 or height <= 0:
                print("❌ Height and weight must be positive numbers. Try again.\n")
                continue
            return weight, height
        except ValueError:
            print("❌ Invalid input. Please enter numeric values.\n")

def main():
    """Main function to run the BMI calculator."""
    print("🧮 Welcome to the Advanced BMI Calculator\n")

    while True:
        weight, height = get_user_input()
        bmi = calculate_bmi(weight, height)
        category = classify_bmi(bmi)

        print(f"\n✅ Your BMI is: {bmi}")
        print(f"📊 Category: {category}\n")

        again = input("Would you like to calculate again? (y/n): ").lower()
        if again != 'y':
            print("\n👋 Thank you for using the BMI Calculator!")
            break

# Run the application
if __name__ == "__main__":
    main()
