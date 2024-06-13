#!/usr/bin/env python
# lib/cli.py
import click
from colorama import Fore, Back, Style, init
from models.book import Book

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

# Initialize Colorama
init(autoreset=True)

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
            click.echo(Fore.YELLOW + "Back to main menu") 
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
        elif choice == "12":
            delete_book()
        
        else:
            click.echo(Fore.RED + "Invalid choice")


def menu():
    click.echo(Fore.GREEN + "Browse Catalog:")
    click.echo(Fore.CYAN +  "00. Exit the catalog")
    click.echo(Fore.CYAN + Back.LIGHTWHITE_EX +  "0. Back>>")
    click.echo(Fore.CYAN +  "1. View books in catalog")
    click.echo(Fore.CYAN +  "2. Add a Book to Catalog")
    click.echo(Fore.CYAN +  "3. Browse genres")
    click.echo(Fore.CYAN + "4. View Authors")
    click.echo(Fore.CYAN + "5. Search Book by Title")
    click.echo(Fore.CYAN + "6. Search Books by Author ")
    click.echo(Fore.CYAN + "7. Search Books by Genre")
    click.echo(Fore.CYAN + "8. Search Authors in a genre")
    click.echo(Fore.CYAN + "9. Lend a Book to a Friend")
    click.echo(Fore.CYAN + "10. View borrowed Books From Catalog")
    click.echo(Fore.CYAN + "11. Return Borrowed Book")
    click.echo(Fore.CYAN + "12. Delete a Book From Catalog")



@click.command()
@click.option("--name", prompt="Enter your name ", help="The name of the user")
def greet_user(name):
    """Say hello to the user"""
    click.echo(Fore.CYAN +  f"Hello {name}!")

@click.command()
def mark_book_as_read():
    """Mark a book as read."""
    book_title = input("Enter the title of the book you want to mark as read: ")
    book = Book.find_by_title(book_title)
    if book:
        book.mark_as_read()
        click.echo(Fore.GREEN + f"{book.title} has been marked as read.")
    else:
        click.echo(Fore.RED +"Book not found.")

@click.command()
def mark_book_as_unread():
    """Mark a book as unread."""
    book_title = input("Enter the title of the book you want to mark as unread: ")
    book = Book.find_by_title(book_title)
    if book:
        book.mark_as_unread()
        click.echo(Fore.GREEN + f"{book.title} has been marked as unread.")
    else:
        click.echo(Fore.RED +"Book not found.")

main.add_command(browse_catalog)
main.add_command(mark_book_as_read)
main.add_command(mark_book_as_unread)
main.add_command(greet_user)

if __name__ == "__main__":
    main()
