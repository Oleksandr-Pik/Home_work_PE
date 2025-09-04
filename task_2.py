# Створіть 2 класи мови, наприклад, англійська та іспанська.
# В обох класів має бути метод greeting().
# Обидва створюють різні привітання.
# Створіть два відповідні об'єкти з двох класів вище
# та викличте дії цих двох об'єктів в одній функції (функція hello_friend).

class Language:
    def greeting(self):
        print("Hello")

class English(Language):
    def greeting(self):
        print("Hello my friend")

class Spanish(Language):
    def greeting(self):
        print("Hola mi amiga")

speak_en = English()
speak_spa = Spanish()

def hello_friend(lang: str):
    if lang == "en":
        speak_en.greeting()
    elif lang == "spa":
        speak_spa.greeting()

hello_friend("en")
hello_friend("spa")

