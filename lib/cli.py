# lib/cli.py
import click

from helpers import (
    exit_program,
    list_books,
    list_genres,
    list_authors,
    books_by_author,
    book_by_title,
    books_by_genre,
    authors_by_genre,
    add_book,
    borrowed_books,
    lend_book,
    return_book,
    delete_book
)
@click.group()
def main():
    """Library Catalog CLI"""
    pass

@click.command()
def browse_catalog():
    """Browse the book catalog"""
    while True:
        menu()
        choice = input("> ").strip()
        if choice == "00":
            exit_program()
        elif choice == "0":
            click.echo("Back to main menu")
            break
        elif choice == "1":
            list_books()
        elif choice == "2":
            add_book()
        elif choice == "3":
            list_genres()
        elif choice == "4":
            list_authors()
        elif choice == "5":
            book_by_title()
        elif choice == "6":
            books_by_author()
        elif choice == "7":
            books_by_genre()
        elif choice == "8":
            authors_by_genre()
        elif choice == "9":
            lend_book()
        elif choice == "10":
            borrowed_books()
        elif choice == "11":
            return_book()
        else:
            click.echo("Invalid choice")


def menu():
    click.echo("Browse Catalog:")
    click.echo("00. Exit the catalog")
    click.echo("0. Back>>")
    click.echo("1. View books in catalog")
    click.echo("2. Add a Book to Catalog")
    click.echo("3. Browse genres")
    click.echo("4. View Authors")
    click.echo("5. Search Book by Title")
    click.echo("6. Search Books by Author ")
    click.echo("7. Search Books by Genre")
    click.echo("8. Search Authors in a genre")
    click.echo("9. Lend a Book to a Friend")
    click.echo("10. View borrowed Books From Catalog")
    click.echo("11. Return Borrowed Book")



@click.command()
@click.option("--name", prompt="Enter your name ", help="The name of the user")
def hello(name):
    click.echo(f"Hello {name}!")

main.add_command(browse_catalog)
main.add_command(hello)

if __name__ == "__main__":
    main()
