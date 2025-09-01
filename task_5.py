# Використовуючи код example_10, створіть статичний метод класу
# ( для створення використовуйте декоратор @staticmethod ),
# метод має приймати вік людини та перевіряти чи досягла вона повноліття, метод має повертати True або False

class User:
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    @staticmethod
    def isAdult(age):
        return True if age >= 18 else False


user1 = User("Alex")

print(user1.isAdult(46))