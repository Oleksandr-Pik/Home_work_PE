# Створіть клас, який описує книгу.
# Він повинен містити інформацію про автора, назву, рік видання та жанр.
# Створіть кілька різних книжок. Визначте для нього методи _repr_ та _str_.

class Book:
    def __init__(self, author: str, title: str, year_pub: int, genre: str):
        self.author = author
        self.title = title
        self.year_pub = year_pub
        self.genre = genre

    def __str__(self):
        return f"Book (назва: {self.title}, автор: {self.author}, рік виданн: {self.year_pub}, жанр: {self.genre})"

    def __repr__(self):
        return f"Book({repr(self.title)}, {repr(self.author)}, {repr(self.year_pub)}, {repr(self.genre)})"


book1 = Book(author="Дж. Толкін", title="Гобіт", year_pub=1937, genre="фентезі")
book2 = Book(author="Джейн Остін", title="Гордість і упередження", year_pub=1813, genre="роман")
book3 = Book(author="Джордж Орвелл", title="1984", year_pub=1949, genre="антиутопія")
book4 = Book("Т. Шевченко", "Кобзар", 1832, "збірка віршів")

print(book1)
print(book2)
print(book3)
print(book4)
print()
print(repr(book1))
print(repr(book2))
print(repr(book3))
print(repr(book4))
