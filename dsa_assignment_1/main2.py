import logging

class Book:
    def __init__(self, isbn, title, publisher, language, num_copies, availability):
        self.isbn = isbn
        self.title = title
        self.publisher = publisher
        self.language = language
        self.num_copies = num_copies
        self.availability = availability

    def __str__(self):
        return (f"ISBN: {self.isbn}, Title: {self.title}, Publisher: {self.publisher}, "
                f"Language: {self.language}, Number of Copies: {self.num_copies}, "
                f"Availability: {self.availability}")

book_records = []


logging.basicConfig(filename='library.log', level=logging.INFO)

def log_action(action):
    logging.info(action)


#Main Requirements
def display_menu():
    print("\nLibrary Book Management System")
    print("1. Display all book records")
    print("2. Add new book record")
    print("3. Sort books by Publisher (Bubble Sort)")
    print("4. Sort books by Number of Copies (Insertion Sort)")
    print("5. Exit")

def display_books(books):
    if not books:
        print("No books available.")
    else:
        for book in books:
            print(book)

def add_book():
    isbn = int(input("Enter ISBN: "))
    title = input("Enter Title: ")
    publisher = input("Enter Publisher: ")
    language = input("Enter Language: ")
    num_copies = int(input("Enter Number of Copies: "))
    availability = input("Enter Availability (True/False): ").strip().lower() == 'true'
    book = Book(isbn, title, publisher, language, num_copies, availability)
    book_records.append(book)
    log_action(f"Book added: {book}")
    print("Book added successfully!")

    
def bubble_sort_books_by_publisher(books):
    n = len(books)
    for i in range(n):
        for j in range(0, n-i-1):
            if books[j].publisher > books[j+1].publisher:
                books[j], books[j+1] = books[j+1], books[j]
    print("Books sorted by publisher (ascending order).")

def insertion_sort_books_by_copies(books):
    for i in range(1, len(books)):
        key = books[i]
        j = i-1
        while j >= 0 and key.num_copies > books[j].num_copies:
            books[j + 1] = books[j]
            j -= 1
        books[j + 1] = key
    print("Books sorted by number of copies (descending order).")

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    return username == "admin" and password == "password"

def main():
    if not login():
        print("Access Denied!")
        return

    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            display_books(book_records)
        elif choice == '2':
            add_book()
        elif choice == '3':
            bubble_sort_books_by_publisher(book_records)
            display_books(book_records)
        elif choice == '4':
            insertion_sort_books_by_copies(book_records)
            display_books(book_records)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

