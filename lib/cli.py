# lib/cli.py
import click

from helpers import (
    exit_program,
    helper_1
)

@click.command()
def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "00":
            exit_program()
        elif choice == "1":
            helper_1()
        else:
            click.echo("Invalid choice")


def menu():
    click.echo("Browse Catalog:")
    click.echo("00. Exit the catalog")
    click.echo("0. Back>>")
    click.echo("1. Some useful function")


@click.command()
@click.option("--name", prompt="Enter your name ", help="The name of the user")
def hello(name):
    click.echo(f"Hello {name}!")


if __name__ == "__main__":
    main()
