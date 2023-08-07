# INHERITANCE

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def eat(self):
#         print(f'{self.name} is eating')


# class Cat(Animal):
#     def meow(self):
#         print('meeoow')


# class Dog(Animal):
#     def bark(self):
#         print('barking...')


# animal = Animal('big animal')
# cat = Cat('mart')
# dog = Dog('Sam')

# animal.eat()
# cat.eat()
# dog.eat()
# dog.bark()

# # example 2


# class Vehicle:
#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color

#     def display_info(self):
#         print('Brand:', self.brand)
#         print('Color:', self.color)


# class Car(Vehicle):
#     def __init__(self, brand, color, num_wheels):
#         super().__init__(brand, color)
#         self.num_wheels = num_wheels

#     def honk(self):
#         print('Honking the horn..')


# car1 = Car('Toyota', 'black', 4)
# car1.color = 'red'
# car1.display_info()


# exercise 1
# use inheritance to calculate area and perimeter of a circle and rectangle

# class Shape:
#     def __init__(self, area, perimeter):
#         self.area = area
#         self.perimeter = perimeter

#     def display(self):
#         print(f"the area is {self.area} ")
#         print(f"the perimeter is {self.perimeter}")


# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#         # self.area /= area

#     def calculteArea(self):
#         self.area = 3.14 * self.radius ** 2

#     def calculatePerimeter(self):
#         self.perimeter = 2 * 3.14 * self.radius


# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def calculteArea(self):
#         self.area = self.length * self.width

#     def calculatePerimeter(self):
#         self.perimeter = (2*self.length) + (2 * self.width)


# c1 = Circle(7)
# c1.calculatePerimeter()
# c1.calculteArea()
# c1.display()

# r1 = Rectangle(4, 3)
# r1.calculatePerimeter()
# r1.calculteArea()
# r1.display()

# # Example3
# # Multiple inheritance


# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def eat(self):
#         print(f'{self.name} is eating')


# class Flyable:
#     def fly(self):
#         print(f'{self.name} is flying')


# class Bird(Animal, Flyable):
#     def __init__(self, name, species):
#         self.species = species
#         self.name = name

#     def display_info(self):
#         print(f'Species: {self.species}')
#         print(f'Name: {self.name}')


# my_bird = Bird('pigeon', 'bird')


# my_bird.eat()
# my_bird.fly()


# Method overidding
# class Animal:
#     def make_sound(self):
#         print('Animal is making sound')


# class Cat(Animal):
#     def make_sound(self):
#         print('Cat is meowing...')


# class Dog(Animal):
#     def make_sound(self):
#         print('Dog is barking...')


# def make_animal_sound(animal):
#     animal.make_sound()


# cat = Cat()
# dog = Dog()
# animal = Animal()

# make_animal_sound(cat)
# make_animal_sound(dog)
# make_animal_sound(animal)


# polymorphism
# writing code that can run with different objects

# Method overriding
# method overloading
# class Shape:
#     def calculate_area(self):
#         return self.length * self.width


# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width


# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def calculate_area(self):
#         return 3.14 * self.radius ** 2

#     def calculate_circumference(self):
#         return 2 * 3.14 * self.radius


# rectangle = Rectangle(4, 6)
# circle = Circle(14)

# print('area of rectangle', rectangle.calculate_area())
# print('area of circle', circle.calculate_area())
# print('Circumference of circle', circle.calculate_circumference())

# Abstraction

# from abc import ABC, abstractmethod


# class Vehicle(ABC):
#     @abstractmethod
#     def start(self):
#         pass

#     @abstractmethod
#     def stop(self):
#         pass


# class Car(Vehicle):
#     def start(self):
#         print('Starting the car...')

#     def stop(self):
#         print('Stopping the car...')


# class Truck(Vehicle):
#     def start(self):
#         print('Starting the truck...')

#     def stop(self):
#         print('Stopping the truck...')


# car = Car()
# truck = Truck()

# car.start()
# car.stop()

# truck.start()
# truck.stop()


# Exercise 2
# demostrate abstraction calculating area of a circle and rectangle
# from abc import ABC, abstractmethod


# class Shape(ABC):
#     @abstractmethod
#     def calculate_area(self):
#         pass

#     @abstractmethod
#     def display(self):
#         pass


# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def calculate_area(self):
#         self.area = self.length*self.width

#     def display(self):
#         print(f'area is {self.area}')


# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def calculate_area(self):
#         self.area = 3.14 * self.radius ** 2

#     def calculate_circumference(self):
#         self.circumference = 2 * 3.14 * self.radius

#     def display(self):
#         print(f'area is {self.area}')
#         print(f'circumference is {self.circumference}')


# rectangle = Rectangle(4, 6)
# circle = Circle(14)
# circle.calculate_area()
# circle.calculate_circumference()
# circle.display()

# rectangle.calculate_area()
# rectangle.display()

# assignment
# create a receipt printing program using GUI interface
import tkinter as tk


class ReceiptSystem:
    def __init__(self):
        self.items = []

        self.window = tk.Tk()
        self.window.title("Brian Boutique Receipt System")

        self.item_label = tk.Label(self.window, text="Item:")
        self.item_label.grid(row=0, column=0, padx=10, pady=5)

        self.item_entry = tk.Entry(self.window)
        self.item_entry.grid(row=0, column=1, padx=10, pady=5)

        self.price_label = tk.Label(self.window, text="Price:")
        self.price_label.grid(row=1, column=0, padx=10, pady=5)

        self.price_entry = tk.Entry(self.window)
        self.price_entry.grid(row=1, column=1, padx=10, pady=5)

        self.add_button = tk.Button(
            self.window, text="Add Item", command=self.add_item)
        self.add_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        self.item_list_label = tk.Label(self.window, text="Items:")
        self.item_list_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")

        self.item_list_text = tk.Text(self.window, height=5, width=40)
        self.item_list_text.grid(
            row=4, column=0, columnspan=2, padx=10, pady=5)

        self.clear_button = tk.Button(
            self.window, text="Clear Items", command=self.clear_items)
        self.clear_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        self.receipt_text = tk.Text(self.window, height=10, width=40)
        self.receipt_text.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

        self.print_button = tk.Button(
            self.window, text="Print Receipt", command=self.print_receipt)
        self.print_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

        self.window.mainloop()

    def add_item(self):
        item = self.item_entry.get()
        price = float(self.price_entry.get())
        self.items.append((item, price))
        self.item_list_text.insert(tk.END, f"{item}: shs.{price}\n")
        self.item_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)

    def clear_items(self):
        self.items = []
        self.item_list_text.delete(1.0, tk.END)

    def print_receipt(self):
        self.receipt_text.delete(1.0, tk.END)
        total_cost = 0.0
        self.receipt_text.insert(tk.END, "Receipt:\n\n")
        for i, (item, price) in enumerate(self.items, start=1):
            self.receipt_text.insert(tk.END, f"{i}. {item}: shs.{price}\n")
            total_cost += price
        self.receipt_text.insert(tk.END, f"\nTotal: shs.{total_cost}")


ReceiptSystem()
