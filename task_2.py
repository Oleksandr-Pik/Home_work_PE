# Опишіть класи графічного об'єкта, прямокутника та об'єкта, який може обробляти натискання миші.
# Опишіть клас кнопки. Створіть об'єкт кнопки та звичайного прямокутника.
# Викличте метод натискання на кнопку.

class Figure:
    TYPE = "Графічний об'єкт"

    def get_info(self):
        print(f"Це: {self.TYPE}")


class Rectangle(Figure):
    TYPE = "Прямокутник"


class ClickedFigure:
    def on_click(self):
        print("Ви клікнули мишею")


class MyButton(ClickedFigure, Rectangle):
    TYPE = "Кнопка"

    def on_click(self):
        super().on_click()
        print("по об'єкту,")
        super().get_info()


rect = Rectangle()
rect.get_info()
print()
btn = MyButton()
btn.on_click()
