# **Object Oriented Programming**

Object-Oriented Programming (OOP) in Python is a programming paradigm based on the concept of “objects”, which can contain data (attributes) and code (methods). It is used to structure a program into reusable and interconnected objects.

Python supports all four main principles of OOP:

Principle	Meaning
Encapsulation	Bundling data (attributes) and methods (functions) within a class.
Abstraction	Hiding complex implementation details and showing only the essentials.
Inheritance	A class can inherit attributes and methods from another class.
Polymorphism	Methods can behave differently based on the object that calls them.

🧩 2. Key Components in Python OOP
✅ Class
A blueprint for creating objects.

python
Copy
Edit
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says woof!")
✅ Object
An instance of a class.

python
Copy
Edit
my_dog = Dog("Buddy")
my_dog.bark()  # Output: Buddy says woof!
✅ __init__ Method
A special constructor method used to initialize the object.

✅ self
Refers to the current instance of the class.

🧬 3. Inheritance Example
python
Copy
Edit
class Animal:
    def speak(self):
        print("Animal speaks")

class Cat(Animal):
    def speak(self):
        print("Meow")

c = Cat()
c.speak()  # Output: Meow
🔄 4. Polymorphism Example
python
Copy
Edit
class Bird:
    def sound(self):
        print("Chirp")

class Duck:
    def sound(self):
        print("Quack")

def make_sound(animal):
    animal.sound()

make_sound(Bird())  # Chirp
make_sound(Duck())  # Quack
🎁 5. Encapsulation Example
python
Copy
Edit
class BankAccount:
    def __init__(self):
        self.__balance = 0  # private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = BankAccount()
acc.deposit(100)
print(acc.get_balance())  # Output: 100









