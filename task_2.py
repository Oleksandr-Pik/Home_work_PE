# Створіть клас, який описує відгук до книги.
# Додайте до класу книги поле – список відгуків.
# Зробіть так, щоб при виведенні книги на екран за допомогою функції print також виводилися відгуки до неї.

class Review:
    def __init__(self, review: str):
        self.review = review


class Book:
    def __init__(self, author: str, title: str, year_pub: int, genre: str):
        self.author = author
        self.title = title
        self.year_pub = year_pub
        self.genre = genre
        self.reviews = []

    def __str__(self):
        return f"Book (назва: {self.title}, автор: {self.author}, рік видання: {self.year_pub}, жанр: {self.genre}, відгуки: {self.reviews})"

    def add_review(self, review: Review):
        self.reviews.append(review)


book1 = Book(author="Дж. Толкін", title="Гобіт", year_pub=1937, genre="фентезі")
book2 = Book(author="Джейн Остін", title="Гордість і упередження", year_pub=1813, genre="роман")

book1.add_review("Чудова книга")
book1.add_review("Super")
book1.add_review("Дуже затягнуто")
book2.add_review("для тих, хто любить розмірковувати")

print(book1)
print(book2)
