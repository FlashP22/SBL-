# Define a class called 'Person'
class Person:
    # Constructor (Initializer) method
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method to display information about the person
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Create objects of the 'Person' class
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

# Call the 'display_info' method to display information about the persons
person1.display_info()
person2.display_info()
