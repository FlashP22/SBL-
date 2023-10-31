# Input two numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Swap the numbers
num1, num2 = num2, num1

# Check if the first number is positive, negative, or zero
if num1 > 0:
    print(f"The first number ({num1}) is positive.")
elif num1 < 0:
    print(f"The first number ({num1}) is negative.")
else:
    print("The first number is zero.")
