class Library:
    books_available = 100

    @classmethod
    def lend_books(cls, num_books: int) -> None:
        cls.books_available -= num_books
    
    @classmethod
    def return_books(cls, num_books: int) -> None:
        cls.books_available += num_books


print(f"Initial status: {Library.books_available} books available")
Library.lend_books(30)
print(f"After lending: {Library.books_available} books available")
Library.return_books(10)
print(f"After return: {Library.books_available} books available")
