
#Create a Rectangle class with width and height attributes, and methods to calculate area and perimeter.

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


# Example usage:
rect = Rectangle(5, 10)
print(rect.area())  # Should return 50
print(rect.perimeter())  # Should return 30

#----------------------------------------------------------------------------------------------------------------

#Create a Counter class that keeps track of a count value. Include methods to increment, decrement, and reset the counter.
class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1

    def decrement(self):
        self.value -= 1

    def reset(self):
        self.value = 0

# Example usage:
counter = Counter()
counter.increment()
counter.increment()
print(counter.value)  # Should return 2
counter.decrement()
print(counter.value)  # Should return 1
counter.reset()
print(counter.value)  # Should return 0

# ---------------------------------------------------------------------------------------------------------------


#Create a Vehicle base class with attributes for make, model, and year. Then create a Car subclass that inherits from Vehicle and adds attributes for number of doors and fuel type.
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

# Car subclass inherits from Vehicle and adds doors and fuel_type
class Car(Vehicle):
    def __init__(self, make, model, year, doors, fuel_type):
        super().__init__(make, model, year)
        self.doors = doors
        self.fuel_type = fuel_type


# Example usage:
car = Car("Toyota", "Corolla", 2020, 4, "Gasoline")
print(car.make)  # Should return "Toyota"
print(car.doors)  # Should return 4
#------------------------------------------------------------------------------------------

#Create a BankAccount class with private attributes for balance and account number. Include methods for deposit, withdrawal, and checking balance.

class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  
        self.__balance = balance                

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

    def get_account_number(self):
        return self.__account_number

# Example usage:
account = BankAccount("123456", 1000)
print(account.get_balance())  # Should return 1000
account.deposit(500)
print(account.get_balance())  # Should return 1500
account.withdraw(200)
print(account.get_balance())  # Should return 1300
print(account.get_account_number())  # Should return "123456"

# Direct access should not be allowed
try:
    account._balance = 2000  # This should be discouraged or prevented
except AttributeError:
    print("Cannot directly access private attribute")