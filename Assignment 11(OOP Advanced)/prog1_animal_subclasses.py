class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

class Dog(Animal):
    def speak(self):
        return f"{self.name} barks: Woof! Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} meows: Meow! Meow!"


def main():
    print("Animal Base Class and Subclasses (Dog & Cat)")
    
    dog = Dog("Dog")
    cat = Cat("Cat")
    
    print(dog.speak())
    print(cat.speak())


if __name__ == "__main__":
    main()
