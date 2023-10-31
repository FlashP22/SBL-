# Parent class (superclass)
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass  # This method will be overridden by subclasses

# Subclass 1
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

# Subclass 2
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Subclass 3
class Parrot(Animal):
    def speak(self):
        return f"{self.name} says Squawk!"

# Create instances of the subclasses
dog = Dog("Buddy")
cat = Cat("Whiskers")
parrot = Parrot("Polly")

# Call the speak method on each instance
print(dog.speak())    # Output: Buddy says Woof!
print(cat.speak())    # Output: Whiskers says Meow!
print(parrot.speak()) # Output: Polly says Squawk!
