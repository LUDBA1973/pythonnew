books = {
    "harry potter": True,
    "alex ferguson": True,
    "american predator": True,
    "nobody's women": True
}
borrowed_books = {}

def display_books():
    print("Available books:")
    for book, available in books.items():
        if available:
            print(f"- {book}")


def borrow_book(book_title):
    if book_title in books and books[book_title]:
        books[book_title] = False
        borrowed_books[book_title] = True
        print(f"\nYou have borrowed '{book_title}'.")
    elif book_title in books and not books[book_title]:
        print(f"\nSorry, '{book_title}' is already borrowed.")
    else:
        print("\nBook not found in the library.")


def return_book(book_title):
    if book_title in borrowed_books:
        books[book_title] = True
        del borrowed_books[book_title]
        print(f"\nYou have returned '{book_title}'.")
    else:
        print("\nYou cannot return a book you haven't borrowed.")



while True:
        print("\nOptions: \n1. Display Books \n2. Borrow Book \n3. Return Book \n4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            display_books()
        elif choice == "2":
            book_title = input("Enter the book title to borrow: ").lower()
            borrow_book(book_title)
        elif choice == "3":
            book_title = input("Enter the book title to return: ").lower()
            return_book(book_title)
        elif choice == "4":
            print("\nThank you for using the Library System. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please enter a valid option.")


