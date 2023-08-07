# OBJECT ORIENTED PROGRAMMING (OOP)

# - Key concepts in oop
#     -class
#     -objects
#     -encapsulation
#     -inheritance
#     -polymorpism
#     -Abstracion

# CLASSES
# A class is a blue print for creating objects.


# class Car:
#     def __init__(self, name, model, year):
#         self.name = name
#         self.model = model
#         self.year = year

#     def start_engine(self):
#         print('Engine srarted')

#     def stop_engine(self):
#         print('Engine stopped')

# car1 = Car('Bugatti', 'veyron', 2020)
# print(car1.name)
# car1.start_engine()

# car2 = Car('Bugatti', 'Chiron', 2021)
# print (car2.name, car2.model, car2.year)

# Example 2 bank acccount

# class BankAccount:
#     def __init__(self, account_number, balance):
#         self.account_number = account_number
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount

#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount

#         else:
#             print('insufficient funds')

#     def get_balance(self):
#         print(self.balance)


# acc = BankAccount(346487, 0)
# acc.deposit(500000)
# acc.get_balance()

# acc.withdraw(200000)
# acc.get_balance()

# acc.withdraw(400000)


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * self.width + 2 * self.height


r1 = Rectangle(4, 3)
r1.calculate_perimeter()
r1.calculate_area()


# example3
# class Student:
#     def __init__(self, name, year, course):
#         self.name = name
#         self.year = year
#         self.course = course

#     def display_details(self):
#         print('name:', self.name)
#         print('year:', self.year)
#         print('course:', self.course)


# st1 = Student('Frank', 3, 'BSSE')
# st1.display_details()


# # excercise

# # calculate the area and circumference of a circle
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_cicumference(self):
        return 2 * 3.14 * self.radius

    def calculate_area(self):
        return 3.14 * self.radius**2


c1 = Circle(7)
print(c1.calculate_area())


# # Exercise2: Calculate and display employee bonuses
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def calculate_bonus(self):
#         bonus = 0.15*self.salary
#         print(bonus)


# emlpoyee1 = Employee('Brian', 150000)
# emlpoyee1.calculate_bonus()

# employee2 = Employee('martha', 230000)
# employee2.calculate_bonus()


# # encapsulation
# # used to hide implementations of an object
# # protect objets from shanges
# # protect objects from external changes
# # code mudulality and organization

# # Example With bank account
# class BankAcount:
#     def __init__(self, account_number, balance):
#         self.account_number = account_number
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount

#     def withdraw(self, amount):
#         if self.balance >= amount:
#             self.balance -= amount
#         else:
#             print('insufficient funds')

#     def show_balance(self):
#         print(self.balance)


# my = BankAcount(123, 300000)
# my.show_balance()
# my.deposit(100000)
# my.show_balance()
# my.withdraw(200000)
# my.show_balance()

# Example convert temperature from celcius to fahrenheit

# class Converter:
#     def __init__(self, temp):
#         self.temp = temp

#     def convert_to_fahrenheit(self):
#         print(self.temp*1.8 + 32)


# temp1 = Converter(37)
# temp1.convert_to_fahrenheit()


# Assignment 1: Show encapsulation with employee information to give a pay incrementation from 850000 to 1000000


class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    def increase_salary(self):
        self._salary += 150000
        print(self._salary)


employee1 = Employee('Brian', 850000)
employee1.increase_salary()
