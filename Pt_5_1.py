import csv

books = [("Книга", "Автор", "Год выпуска"),
         ["Murder on the Orient Express", "Agatha Christie", "1934"],
         ["The Kite Runner", "Khaled Hosseini", "2003"],
         ["A Game of Thrones", "George R. R. Martin", "1996"],
         ["Atonement", "Ian McEwan", "2001"],
         ["A Brief History of Time", "Stephen Hawking", "1988"]]

with open("books.csv", "w", newline='') as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerows(books)
