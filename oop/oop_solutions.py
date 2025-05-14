#Easy question 1:
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

rect = Rectangle(5, 10)
print("Area:", rect.area())
print("Perimeter:", rect.perimeter())
print()

#Easy question 2:
class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1

    def decrement(self):
        self.value -= 1

    def reset(self):
        self.value = 0

counter = Counter()
counter.increment()
counter.increment()
print(counter.value)
counter.decrement()
print(counter.value)
counter.reset()
print(counter.value)
print()

#Medium Question 1:
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class Car(Vehicle):
    def __init__(self, make, model, year, doors, fuel_type):
        super().__init__(make, model, year)
        self.doors = doors
        self.fuel_type = fuel_type

car = Car("Toyota", "Corolla", 2020, 4, "Gasoline")
print("Make:", car.make)
print("Doors:", car.doors)
print()

#Medium Question 2:
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
    
account = BankAccount("123456", 1000)
print("Initial Balance:", account.get_balance())
account.deposit(500)
print("After Deposit:", account.get_balance())
account.withdraw(200)
print("After Withdrawal:", account.get_balance())
print("Account Number:", account.get_account_number())

try:
    account.__balance = 999999
except AttributeError:
    print("Cannot directly access private attribute")

print("Final Balance:", account.get_balance())
