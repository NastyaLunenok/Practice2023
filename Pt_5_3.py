import csv


def is_valid_year(year):
    try:
        year = int(year)
        if year >= 0:
            return True
        else:
            return False
    except ValueError:
        return False


def search_books(from_year, to_year):
    books = []
    with open("books.csv", newline='') as file:
        reader = csv.DictReader(file, delimiter=";")
        for row in reader:
            for year in range(from_year, to_year + 1):
                year = str(year)
                if year == row["Год выпуска"]:
                    books.append(row)
      
    if not books:
        print("В списке нет книг этих лет")
    else:
        for row in books:
            print(row["Книга"], "|", row["Автор"], "|", row["Год выпуска"])


fl = True
while fl:
    start_year = input("Введите нижнюю границу диапазона годов: ")
    end_year = input("Введите верхнюю границу диапазона годов: ")
    if (not is_valid_year(start_year) or
        not is_valid_year(end_year) or
        start_year > end_year):
        print("Некорректный ввод годов. Введите еще раз.")
    else:
        search_books(int(start_year), int(end_year))
        fl = False
