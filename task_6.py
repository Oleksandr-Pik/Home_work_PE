# Використовуючи код example_10, створіть класовий метод
# ( для створення використовуйте декоратор @classmethod ).
# Метод має підраховувати кількість об'єктів цього класу які досягли повноліття,
# для вирішення задачі використовуйте статичний метод створенний в завданні 5

class User:
    __counter = 0

    def __init__(self, name: str):
        self.name = name
        self.count_user()

    @classmethod
    def count_user(cls):
        cls.__counter += 1

    @classmethod
    def get_counter(self):
        return self.__counter

    def getName(self):
        return self.name


user1 = User("Alex")
user2 = User("John")
user3 = User("Max")

print(User.get_counter())
