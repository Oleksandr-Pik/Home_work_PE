# Створіть ієрархію класів із використанням множинного успадкування.
# Виведіть на екран порядок вирішення методів для кожного класу.
# Поясніть, чому лінеаризація даних класів виглядає саме так.

class Animal:
    def sound(self):
        print("Animal makes a sound")

class Mammal(Animal):
    def sound(self):
        print("Mammal sound")

class Bird(Animal):
    def sound(self):
        print("Bird sound")

class Bat(Mammal, Bird):
    pass



print("MRO для класу Bat:", Bat.mro())


bat = Bat()
bat.sound()