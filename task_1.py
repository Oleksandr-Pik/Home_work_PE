# Створіть клас, який описує автомобіль.
# Які атрибути та методи мають бути повністю інкапсульовані?
# Доступ до таких атрибутів та зміну даних реалізуйте через спеціальні методи (get, set).

class Car:
    def __init__(self, brand: str, model: str, color: str):
        self._brand = brand
        self._model = model
        self._color = color
        self.__price = 0

    def __str__(self):
        return f"Бренд атомобіля: {self._brand}, модель: {self._model}, колір: {self._color} - Ціна: {self.get_price()}$"

    def get_price(self):
        return self.__price

    def set_price(self):
        self.__price = int(input("Вкажіть ціну: "))



car1 = Car("BMW", "X5", "білий")

car1.set_price()

print(car1)

