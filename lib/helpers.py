# lib/helpers.py
import click
from models.author import Author
from models.book import Book
from models.genre import Genre
from models.lending import Lending

def exit_program():
    click.secho("Goodbye!", fg='blue', bg="white")
    exit()

def list_books():
    books = Book.get_all()
    if books:
        click.echo("retrieving books")
        for book in books:
            print_book(book)
    else:
        click.secho("No books available.", fg='red')      

def list_genres():
    genres = Genre.get_all()
    if genres:
        click.secho("Retrieving genres:", fg='green', bold=True)
        for genre in genres:
            print_genre(genre)
    else:
        click.secho("No genres available.", fg='red')

def list_authors():
    authors = Author.get_all()
    if authors:
        click.secho("Retrieving authors:", fg='green', bold=True)
        for author in authors:
            print_author(author)
    else:
        click.secho("No authors available.", fg='red')

def books_by_genre():
    genre_name = get_input("Enter genre: ", validate_non_empty)
    genre = Genre.find_by_name(genre_name)
    if genre:
        click.echo(genre)
        books = Genre.books(genre)
        if books:
            for book in books:
                print_book(book)
        else:
            click.secho(f"No books found in the genre {genre_name}", fg='red')
    else:
        click.secho(f"{genre_name} genre not found.", fg='red')

def books_by_author():
    author_name = get_input("Enter Author's name: ", validate_non_empty)
    author = Author.find_by_name(author_name)
    if author:
        click.echo(author)
        books = Author.books(author)
        if books:
            for book in books:
                print_book(book)
        else:
            click.secho(F"No books found by this author: {author_name}", fg='red')
    else:
        click.secho(f"No author by the name {author_name} in the catalog", fg='red')

def book_by_title():
    book_title = get_input("Enter book title: ", validate_non_empty)
    book = Book.find_by_title(book_title)
    if book:
        click.secho("Retrieving book:", fg='green', bold=True)
        print_book(book)
    else:
        click.secho(f"No book found by this name {book_title}", fg='red')

def authors_by_genre():
    genre_name  = get_input("Enter genre: ", validate_non_empty)
    genre = Genre.find_by_name(genre_name)
    if genre:
        authors = Genre.authors(genre)
        if authors:
            for author in authors:
                print_author(author)
        else:
            click.secho(f"No authors found in the genre {genre_name}", fg='red')
    else:
        click.secho("Genre not found.", fg='red')

def add_book():
    title = get_input("Book title: ", validate_non_empty)
    author = get_input("Author's name: ", validate_non_empty)
    genre = get_input("Genre: ", validate_non_empty)
    publication_yr = get_input("Year of publication: ", validate_year)
    reading_status = get_input("Reading status: ", validate_non_empty)
    try:
        book = Book.create(title, author, genre, publication_yr, reading_status)
        click.secho(f"{book.title} added successfully", fg='green', bold=True)
    except Exception as exc:
        click.secho(f"Error occurred: {exc}", fg='red')

def borrowed_books():
    books = Lending.borrowed_books()
    if books:
        click.secho("Borrowed books:", fg='green', bold=True)
        for book in books:
            click.secho(f"{book}", fg='cyan', bg='white', bold=True)
    else:
        click.secho("No Books Lent out.", fg='red')

def lend_book():
    book_title = get_input("Book title: ", validate_non_empty)
    book = Book.find_by_title(book_title)
    if book:
        date = get_input("Enter date: ", validate_non_empty)
        name = get_input("Enter borrower's name: ", validate_non_empty)
        lent_book = Lending.create(book_title, date, name)
        click.secho(f"{lent_book} book lent out", fg='green', bold=True)
    else:
        click.secho("Book not found in catalog", fg='red')


def return_book():
    book = get_input("Book to return: ", validate_non_empty)
    returned_book = Lending.find_by_title(book)
    if returned_book:
        Lending.return_book(returned_book)
        click.secho(f"{book} returned successfully", fg='green', bold=True)
    else:
        click.secho("Book not found in catalog", fg='red')

def delete_book():
    book_title = input("Book to remove from catalog: ")
    book = Book.find_by_title(book_title)
    if book:
        Book.delete(book)
        click.secho(f"{book_title} deleted from catalog", fg='green', bold=True)
    else:
        click.secho("Book not in catalog", fg='red')

def print_book(book):
    click.secho(f"Title: {book.title}", fg='green', bold=True)
    click.secho(f"Author: {book.author_name}", fg='blue')
    click.secho(f"Genre: {book.genre_name}", fg='magenta')
    click.secho(f"Publication Year: {book.publication_yr}", fg='yellow')
    click.secho(f"Reading Status: {book.reading_status}", fg='cyan')
    click.echo("-" * 40)

def print_author(author):
    click.secho(f"Author: {author.name}", fg='blue', bg='white', bold=True)
    click.echo("-" * 20)

def print_genre(genre):
    click.secho(f"Genre: {genre.name}", fg='magenta', bold=True)
    click.echo("-" * 20)

def get_input(prompt, validator=None):
    while True:
        value = input(prompt)
        if validator:
            try:
                validator(value)
                return value
            except ValueError as e:
                click.secho(str(e), fg='red')
        else:
            return value

def validate_year(value):
    if not value.isdigit() or not (1000 <= int(value) <= 9999):
        raise ValueError("Please enter a valid year (e.g., 2022).")

def validate_non_empty(value):
    if not value.strip():
        raise ValueError("This field cannot be empty.")