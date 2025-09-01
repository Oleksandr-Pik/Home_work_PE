# Створіть клас Editor, який містить методи view_document та edit_document.
# Нехай метод edit_document виводить на екран інформацію про те,
# що редагування документів недоступне для безкоштовної версії.
# Створіть підклас ProEditor, у якому цей метод буде перевизначено.
# Введіть ліцензійний ключ із клавіатури
# і, якщо він коректний, створіть екземпляр класу ProEditor, інакше Editor.
# Викликайте методи перегляду та редагування документів.

class Editor:
    def __init__(self, name):
        self.name = name

    def view_document(self):
        return "Перегдяд документів дозволено"

    def edit_document(self):
        return "Редагування документів недоступне для безкоштовної версії"


class ProEditor(Editor):
    def __init__(self, licence_key: str = ""):
        self.licence_key = licence_key

    def edit_document(self):
        return "Редагування документів дозволено"


license_key = input("Введіть ліцензійний ключ: ")

user_name = "Alex"

user = ProEditor(user_name) if license_key == "qwerty" else Editor(user_name)

print(user.edit_document())
