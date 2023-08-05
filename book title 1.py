class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False
        self.borrower = None

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        for book in self.books:
            status = "Borrowed" if book.is_borrowed else "Available"
            print(f"{book.title} by {book.author} (ISBN: {book.isbn}) - Status: {status}")

    def borrow_book(self, isbn, borrower):
        for book in self.books:
            if book.isbn == isbn:
                if book.is_borrowed:
                    print("Book is already borrowed.")
                else:
                    book.is_borrowed = True
                    book.borrower = borrower
                    print(f"{book.title} is now borrowed by {borrower}.")
                return
        print("Book with the given ISBN not found.")

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.is_borrowed:
                    book.is_borrowed = False
                    book.borrower = None
                    print(f"{book.title} is returned.")
                else:
                    print("Book is not currently borrowed.")
                return
        print("Book with the given ISBN not found.")


def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            title = input("Enter the book title: ")
            author = input("Enter the author: ")
            isbn = input("Enter the ISBN: ")
            book = Book(title, author, isbn)
            library.add_book(book)
            print("Book added successfully!")

        elif choice == '2':
            print("\nBooks in the library:")
            library.display_books()

        elif choice == '3':
            isbn = input("Enter the ISBN of the book you want to borrow: ")
            borrower = input("Enter your name: ")
            library.borrow_book(isbn, borrower)

        elif choice == '4':
            isbn = input("Enter the ISBN of the book you want to return: ")
            library.return_book(isbn)

        elif choice == '5':
            print("Thank you for using the Library Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

