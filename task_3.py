# Використовуючи посилання наприкінці цього уроку,
# ознайомтеся з таким засобом інкапсуляції, як властивості.
# Ознайомтеся з декоратором property у Python.
# Створіть клас, що описує температуру і дозволяє задавати та отримувати температуру за шкалою Цельсія та Фаренгейта,
# причому дані можуть бути задані в одній шкалі, а отримані в іншій.

class Temperature:
    def __init__(self, degree_celsius=0):
        self._degree_celsius = degree_celsius

    @property
    def celsius(self):
        return self._degree_celsius

    @celsius.setter
    def celsius(self, value):
        self._degree_celsius = value

    @property
    def fahrenheit(self):
        return self._degree_celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self._degree_celsius = (value - 32) * 5 / 9


t = Temperature()
t.celsius = float(input("Вкажіть температуру в градусах Цельсія: "))
print(f"{t.celsius}°C = {t.fahrenheit}°F")

t.fahrenheit = float(input("Вкажіть температуру в градусах Фаренгейта: "))
print(f"{t.fahrenheit}°F = {t.celsius:.2f}°C")
