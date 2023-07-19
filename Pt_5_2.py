import csv


def add_books():
    kol = int(input("Сколько записей вы хотите добавить в список? "))
    added_books = []
    for i in range(kol):
        book = input("Введите название книги: ")
        author = input("Введите автора книги: ")
        year = input("Введите год издания книги: ")
        added_books.append([book, author, year])

    with open("books.csv", "a", newline='') as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerows(added_books)


def book_search():
    found_books = []
    author = input("Введите автора книг: ")
    print("Книги данного автора:\n")
    with open("books.csv", newline='') as file:
        reader = csv.DictReader(file, delimiter=";")
        for row in reader:
            if row["Автор"] == author:
                found_books.append(row)

    if not found_books:
        print("В списке нет книг данного автора\n")
    else:
        for row in found_books:
            print(row["Книга"], "|",
                  row["Автор"], "|",
                  row["Год выпуска"], "\n")


while True:
    menu = int(input("Выберите номер опреации:\n"
                     "1. Добавить новые книги\n"
                     "2. Найти книги по автору\n"
                     "3. Выйти\n"))
    if menu == 1:
        add_books()
    elif menu == 2:
        book_search()
    elif menu == 3:
        print("Работа завершена.")
        break
