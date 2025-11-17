# Опишіть свій клас винятку.
# Напишіть функцію, яка викидатиме цей виняток, якщо користувач введе певне значення,
# і перехопіть цей виняток під час виклику функції.

class UserError(Exception):
    pass


class UserNameError(UserError):
    pass


class UserSurnameError(UserError):
    pass


class UserBirthYearError(UserError):
    pass


class User:
    def __init__(self, name: str, surname: str, birth_year: int):
        if not name:
            raise UserNameError("Ім'я не може бути порожнім.")
        if not surname:
            raise UserSurnameError("прізвище не може бути порожнім.")
        if not name.isalpha() or not surname.isalpha():
            raise UserNameError("Ім'я та прізвище повинні містити лише літери.")
        if birth_year < 1900 or birth_year > 2025:
            raise UserBirthYearError("Рік народження має бути в межах 1900–2025.")

        self.name = name
        self.surname = surname
        self.year = birth_year

    def __str__(self):
        return f"{self.name} {self.surname}, {self.year} року народження"

users = []
n = int(input("Скільки кормстувачів ви хочете ввести? "))

for i in range(n):
    print(f"\nВведення даних користувача №{i+1}")
    try:
        name = input("Ім'я: ").strip()
        surname = input("Прізвище: ").strip()
        birth_year = int(input("Рік народження: "))
        user = User(name, surname, birth_year)
        users.append(user)
    except UserError as e:
        print(f"Помилка: {e} Спробуйте ще раз.")
        continue

for user in users:
    print(user)
