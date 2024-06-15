class Book:
    def __init__(self, author: str, name: str, year: int):
        self.author = author
        self.name = name
        self.year = year

    def get_information_book(self):
        return f"Title: {self.title},Author: {self.author}"

    def change_info(self,name = None, author = None):
        if name:
            self.name = name
            if author:
                self.author = author



class Library:
    def __init__(self, author: str, worker: str,books= None):
        self.author = author
        self.books = books
        self.worker = worker
    def add_book(self, book: str):
        self.books.append(book)
        print("Книга успешно добавлена")
    def remove_book(self, book: str):
        if book in self.books:
            self.books.remove(book)
            print('вы удалили книгу')
        else:
            print('нет такой книги в библиотеке')


    def list_book_count(self):
        return f"Number of books in the libruary: [len(self.books)]"


book1 = Book("book1", "Harry Potter", 1897)
book2 = Book("book2", "1984",2024)
book3 = Book("book3", "Port Artur", 1905)
library = Library("Tolkin", "Tatyana",[])
library.add_book(book1)
library.remove_book(book2)
book3.change_info(author = "London")
