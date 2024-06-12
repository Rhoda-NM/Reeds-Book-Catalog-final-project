# lib/helpers.py
from models.author import Author
from models.book import Book
from models.genre import Genre
from models.lending import Lending

def exit_program():
    print("Goodbye!")
    exit()

def list_books():
    books = Book.get_all()
    for book in books:
        print(book)

def list_genres():
    genres = Genre.get_all()
    for genre in genres:
        print(genre)

def books_by_genre():
    genre_name = input("Enter genre: ")
    if genre := Genre.find_by_name(genre_name):
        books = Genre.books(genre)
        for book in books:
            print(book)

def books_by_author():
    author_name = input("Enter Author's name: ")
    if author := Author.find_by_name(author_name):
        books = Author.books(author)
        for book in books:
            print(book)

def book_by_title():
    book_title = input("Enter book title: ")
    Book.find_by_title(book_by_title)

def authors_by_genre():
    genre_name  = input("Enter genre: ")
    if genre := Genre.find_by_name(genre_name):
        authors = Genre.authors(genre)
        for author in authors:
            print(author)

def add_boook():
    title = input("Book title: ")
    author = input("Author's name")
    genre = input("Genre: ")
    publication_yr = input("Year of publication: ")
    reading_status = input("Reading status: ")
    try:
        book = Book.create(title, author, genre, publication_yr, reading_status)
        print(f"{book} added successfully")
    except Exception as exc:
        print("Error occurred: ", exc)