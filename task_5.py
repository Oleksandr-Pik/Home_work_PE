# Створіть програму спортивного комплексу, у якій передбачене меню:
# 1 - перелік видів спорту,
# 2 - команда тренерів,
# 3 - розклад тренувань,
# 4 - вартість тренування.
# Дані зберігати у словниках.
# Також передбачити пошук по прізвищу тренера, яке вводиться з клавіатури у відповідному пункті меню.
# Якщо ключ не буде знайдений, створити відповідний клас-Exception, який буде викликатися в обробнику виключень.


sports_list = [
    {
        "sport": "бокс",
        "trainer": "Усик",
        "schedule": "Вт, Чт, Сб",
        "cost": "600"
    },
    {
        "sport": "футбол",
        "trainer": "Шевченко",
        "schedule": "Пн, Ср",
        "cost": "400"
    },
    {
        "sport": "баскетбол",
        "trainer": "Петрович",
        "schedule": "Ср, Пт, Нд",
        "cost": "500"
    },
    {
        "sport": "теніс",
        "trainer": "Ганна",
        "schedule": "Вт, Нд",
        "cost": "350"
    },
]


class UserError(Exception):
    pass


def get_sports():
    for idx, item in enumerate(sports_list):
        print(f"{idx+1} - {item["sport"]}")



def get_trainers():
    for idx, item in enumerate(sports_list):
        print(f"{idx + 1} - {item["trainer"]} - {item["sport"]}")


def get_schedule():
    for idx, item in enumerate(sports_list):
        print(f"{idx + 1} - {item["sport"]} - {item["schedule"]}")


def get_cost():
    for idx, item in enumerate(sports_list):
        print(f"{idx + 1} - {item["sport"]} - {item["cost"]}")


def get_info_by_trainer():
    trainer_name = input("Вкажіть ім'я тренера: ")
    if not trainer_name:
        raise UserError("Ім'я тренера не може бути порожнім.")
    if not trainer_name.isalpha():
        raise UserError("Ім'я тренера повинно містити лише літери.")
    for idx, item in enumerate(sports_list):
        if item["trainer"] == trainer_name:
            print(f"Тренер: {item["trainer"]}")
            print(f"Вид спорту: {item["sport"]}")
            print(f"Розклад тренувань: {item["schedule"]}")
            print(f"Вартість: {item["cost"]}")
            break
        else:
            raise UserError(f"Тренера {trainer_name} не знайдено")


while True:
    print("Програма спортивного комплексу")
    print("1 - перелік видів спорту")
    print("2 - команда тренерів")
    print("3 - розклад тренувань")
    print("4 - вартість тренування")
    print("5 - пошук по прізвищу тренера")
    print("0 - вихід\n")
    print("Зробіть ваш вибір:")
    punct = input()

    match punct:
        case "1":
            get_sports()
        case "2":
            get_trainers()
        case "3":
            get_schedule()
        case "4":
            get_cost()
        case "5":
            try:
                get_info_by_trainer()
            except UserError as e:
                print(f"Помилка: {e}")
        case "0":
            break
        case _:
            print("Помилка вводу!")
