class Dog:
    def bark(self):
        return "woof!"

def new_bark(self):
    return "new woof!"

Dog.bark = new_bark

dog = Dog()
print(dog.bark())

# Monkey pathcing