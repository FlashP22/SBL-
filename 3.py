# Initialize empty lists
even_list = []
odd_list = []
merged_list = []

# Function to display the menu
def display_menu():
    print("Menu:")
    print("1. Put even and odd elements into two different lists")
    print("2. Merge and sort the two lists")
    print("3. Update first element with X value and delete the middle element of list")
    print("4. Find max and min element from the list")
    print("5. Add N names into the existing number list and check if 'python' is present")
    print("6. Exit")

# Function to input a list of numbers
def input_numbers():
    num_list = input("Enter a list of numbers separated by spaces: ").split()
    num_list = [int(num) for num in num_list]
    return num_list

# Function to put even and odd elements into two different lists
def separate_even_odd(numbers):
    for num in numbers:
        if num % 2 == 0:
            even_list.append(num)
        else:
            odd_list.append(num)

# Function to merge and sort two lists
def merge_and_sort_lists():
    global merged_list
    merged_list = even_list + odd_list
    merged_list.sort()

# Function to update the first element with X value and delete the middle element
def update_and_delete_elements():
    if len(merged_list) >= 1:
        x = int(input("Enter the value to update the first element with: "))
        merged_list[0] = x

    if len(merged_list) >= 3:
        middle_index = len(merged_list) // 2
        merged_list.pop(middle_index)

# Function to find max and min elements from the list
def find_max_min_elements():
    if merged_list:
        max_value = max(merged_list)
        min_value = min(merged_list)
        print(f"Max Element: {max_value}")
        print(f"Min Element: {min_value}")
    else:
        print("The list is empty.")

# Function to add N names into the existing number list and check if 'python' is present
def add_names_and_check_python():
    n = int(input("Enter the number of names to add: "))
    names = []
    for i in range(n):
        name = input(f"Enter name {i + 1}: ")
        names.append(name)

    merged_list.extend(names)
    if 'python' in merged_list:
        print("'python' is present in the list.")
    else:
        print("'python' is not present in the list.")

# Main program
while True:
    display_menu()
    choice = input("Enter your choice (1/2/3/4/5/6): ")

    if choice == '1':
        numbers = input_numbers()
        separate_even_odd(numbers)
        print("Even List:", even_list)
        print("Odd List:", odd_list)
    elif choice == '2':
        merge_and_sort_lists()
        print("Merged and Sorted List:", merged_list)
    elif choice == '3':
        update_and_delete_elements()
        print("Updated List:", merged_list)
    elif choice == '4':
        find_max_min_elements()
    elif choice == '5':
        add_names_and_check_python()
    elif choice == '6':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
