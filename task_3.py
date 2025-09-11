# Опишіть клас співробітника, який вміщує такі поля: ім'я, прізвище, відділ і рік початку роботи.
# Конструктор має генерувати виняток, якщо вказано неправильні дані.
# Введіть список працівників із клавіатури. Виведіть усіх співробітників, які були прийняті після цього року.

class Employee:
    def __init__(self, name: str, surname: str, department: str, year: int):
        if not name:
            raise ValueError("Ім'я не може бути порожнім.")
        if not surname:
            raise ValueError("прізвище не може бути порожнім.")
        if not name.isalpha() or not surname.isalpha():
            raise ValueError("Ім'я та прізвище повинні містити лише літери.")
        if not department:
            raise ValueError("Відділ не може бути порожнім.")
        if year < 2000 or year > 2025:
            raise ValueError("Рік початку роботи має бути в межах 2000–2025.")

        self.name = name
        self.surname = surname
        self.department = department
        self.year = year

    def __str__(self):
        return f"{self.name} {self.surname}, відділ: {self.department}, працює з {self.year} року"



employees = []
n = int(input("Скільки співробітників ви хочете ввести? "))

for i in range(n):
    print(f"\nВведення даних для співробітника №{i+1}")
    try:
        name = input("Ім'я: ").strip()
        surname = input("Прізвище: ").strip()
        department = input("Відділ: ").strip()
        year = int(input("Рік початку роботи: "))
        emp = Employee(name, surname, department, year)
        employees.append(emp)
    except ValueError as e:
        print(f"Помилка: {e} Спробуйте ще раз.")
        continue

for emp in employees:
    print(emp)
