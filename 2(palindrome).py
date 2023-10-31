def is_palindrome_number(num):
    num_str = str(num)
    return num_str == num_str[::-1]

def is_palindrome_string(input_str):
    input_str = input_str.lower()
    input_str = ''.join(filter(str.isalnum, input_str))
    return input_str == input_str[::-1]

def main():
    while True:
        print("Palindrome Checker")
        print("1. Check if a number is a palindrome")
        print("2. Check if a string is a palindrome")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            num = int(input("Enter a number: "))
            if is_palindrome_number(num):
                print(f"{num} is a palindrome number.")
            else:
                print(f"{num} is not a palindrome number.")
        elif choice == '2':
            input_str = input("Enter a string: ")
            if is_palindrome_string(input_str):
                print(f'"{input_str}" is a palindrome string.')
            else:
                print(f'"{input_str}" is not a palindrome string.')
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
