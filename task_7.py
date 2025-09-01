# Створіть ієрархію класів транспортних засобів.
# У загальному класі опишіть загальні всім транспортних засобів поля,
# у спадкоємцях – специфічні їм. Створіть кілька екземплярів.
# Виведіть інформацію щодо кожного транспортного засобу.

class Transport:
    def __init__(self, brand: str, model: str, year: int):
        self.brand = brand
        self.model = model
        self.year = year

    def get_info(self):
        return f"{self.year} {self.brand} {self.model}"


class Car(Transport):
    def __init__(self, brand: str, model: str, year: int, fuel_type: str, doors: int):
        super().__init__(brand, model, year)
        self.fuel_type = fuel_type
        self.doors = doors

    def get_info(self):
        base = super().get_info()
        return f"{base} | Fuel: {self.fuel_type}, Doors: {self.doors}"


class Bicycle(Transport):
    def __init__(self, brand: str, model: str, year: int, gear_count: int, is_electric: bool):
        super().__init__(brand, model, year)
        self.gear_count = gear_count
        self.is_electric = is_electric

    def get_info(self):
        base = super().get_info()
        electric = "Electric" if self.is_electric else "Manual"
        return f"{base} | Gears: {self.gear_count}, Type: {electric}"


class Boat(Transport):
    def __init__(self, brand: str, model: str, year: int, length: float, boat_type: str):
        super().__init__(brand, model, year)
        self.length = length
        self.boat_type = boat_type

    def get_info(self):
        base = super().get_info()
        return f"{base} | Length: {self.length}m, Type: {self.boat_type}"


car1 = Car("Toyota", "Corolla", 2020, "Petrol", 4)
car2 = Car("Audi", "Q7", 2023, "Electro", 5)
bike1 = Bicycle("Giant", "Escape 3", 2022, 21, False)
boat1 = Boat("Yamaha", "WaveRunner", 2019, 3.3, "Jet Ski")

print(car1.get_info())
print(car2.get_info())
print(bike1.get_info())
print(boat1.get_info())
