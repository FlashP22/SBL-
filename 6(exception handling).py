def divide_numbers():
    try:
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        result = num1 / num2
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
    except ZeroDivisionError:
        print("You cannot divide by zero.")
    else:
        print(f"Result of division: {result:.2f}")
    finally:
        print("Execution completed.")

if __name__ == "__main__":
    divide_numbers()
