# ai_calc_converter.py

# 📌 A simple calculator and weight converter

# 🧠 Built by Shriram | Year: 2023 (reuploaded in 2025)

# 🛠 Functions: Performs basic arithmetic or converts pounds ↔ kilograms

# Choose functionality

choice = input("Choose mode: (e = calculator, d = weight converter): ")

if choice == "e":
    # Calculator mode
    num1 = float(input("Enter first number: "))
   
    num2 = float(input("Enter second number: "))
    
    operator = input("Choose operation (+, -, *, /, //): ")

    if operator == "+":
        print("Result:", num1 + num2)
    elif operator == "-":
        print("Result:", num1 - num2)
    elif operator == "*":
        print("Result:", num1 * num2)
    elif operator == "/":
        print("Result:", num1 / num2)
    elif operator == "//":
        print("Result:", num1 // num2)
    else:
        print("Invalid operator.")

elif choice == "d":
    # Weight converter mode
    weight = float(input("Enter weight: "))
   
    unit = input("Unit (lb or kg): ").lower()

    if unit == "lb":
        print("Weight in kg:", round(weight / 2.20462, 2))
    elif unit == "kg":
        print("Weight in lb:", round(weight * 2.20462, 2))
    else:
        print("Invalid unit.")
else:
    print("Invalid choice.")
    
  Add AI calculator + weight converter script (2023 project)

