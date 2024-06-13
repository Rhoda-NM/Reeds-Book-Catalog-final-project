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
    else:
        print("no books")
    for book in books:
        print_book(book)

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
    genre_name = input("Enter genre: ")
    genre = Genre.find_by_name(genre_name)
    if genre:
        click.echo(genre)
        books = Genre.books(genre)
        if books:
            for book in books:
                print_book(book)
        else:
            click.secho("No books found in this genre.", fg='red')
    else:
        click.secho("Genre not found.", fg='red')

def books_by_author():
    author_name = input("Enter Author's name: ")
    author = Author.find_by_name(author_name)
    if author:
        click.echo(author)
        books = Author.books(author)
        if books:
            for book in books:
                print_book(book)
        else:
            click.secho("No books found by this author.", fg='red')
    else:
        click.secho("Author not found.", fg='red')

def book_by_title():
    book_title = input("Enter book title: ")
    book = Book.find_by_title(book_title)
    if book:
        click.secho("Retrieving book:", fg='green', bold=True)
        print_book(book)
    else:
        click.secho("Book not found.", fg='red')

def authors_by_genre():
    genre_name  = input("Enter genre: ")
    genre = Genre.find_by_name(genre_name)
    if genre:
        authors = Genre.authors(genre)
        if authors:
            for author in authors:
                print_author(author)
        else:
            click.secho("No authors found in this genre.", fg='red')
    else:
        click.secho("Genre not found.", fg='red')

def add_book():
    title = input("Book title: ")
    author = input("Author's name")
    genre = input("Genre: ")
    publication_yr = input("Year of publication: ")
    reading_status = input("Reading status: ")
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
            print_book(book)
    else:
        click.secho("No borrowed books.", fg='red')

def lend_book():
    book_title = input("Book title: ")
    book = Book.find_by_title(book_title)
    if book:
        date = input("Enter date: ")
        name = input("Enter borrower's name: ")
        lent_book = Lending.create(book_title, date, name)
        click.secho(f"{lent_book} book lent out", fg='green', bold=True)
    else:
        click.secho("Book not found in catalog", fg='red')


def return_book():
    book = input("Book to return: ")
    returned_book = Lending.find_by_title(book)
    Lending.return_book(returned_book)

def delete_book():
    book_title = input("Book to remove from catalog: ")
    book = Book.find_by_title(book_title)
    if book:
        Book.delete(book)
        print(f"{book_title} deleted from catalog")
    else:
        print("book not in catalog")

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