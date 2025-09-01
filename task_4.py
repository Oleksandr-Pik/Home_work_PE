# Створіть клас, який описує автомобіль.
# Створіть клас автосалону, що містить в собі список автомобілів, доступних для продажу,
# і функцію продажу заданого автомобіля.

class Car:
    def __init__(self,brand: str, model: str, color: str, price: int):
        self.brand = brand
        self.model = model
        self.color = color
        self.price = price

    def __str__(self):
        return f"Бренд атомобіля: {self.brand}, модель: {self.model}, колір: {self.color} - Ціна: {self.price}$"

    def __repr__(self):
        return f"Бренд атомобіля: {self.brand}, модель: {self.model}, колір: {self.color} - Ціна: {self.price}$"

class CarDealership:
    def __init__(self, name: str="Херсон-авто", adr: str="м.Херсон"):
        self.name = name
        self.adr = adr
        self.cars = []

    def __str__(self):
        return f"Автосалон (назва: {self.name}, адреса: {self.adr}, доступні авто для продажу: {str(self.cars)})"

    def add_car(self, car: Car):
        self.cars.append(car)

    def get_cars(self):
        return self.cars


car1 = Car("BMW", "X5", "білий", 30000)
car2 = Car("BMW", "X3", "чорний", 25000)
car3 = Car("Audi", "Q7", "чорний", 50000)

car_dealership = CarDealership()
car_dealership.add_car(car1)
car_dealership.add_car(car2)
car_dealership.add_car(car3)

print(car_dealership)
print()
print("Автомобілі:")
for car in car_dealership.get_cars():
    print(car)