# Reeds Book Catalog CLI

### About:
 Welcome to Reeds Book Catalog CLI! This command-line interface (CLI) application is a book catalog application that allows book enthusiasts to organize, track, and manage their collections more efficiently and seamlessly.  
 
 Date: 13/06/2024

## Application Features
- Book management: Users can add new books to their catalogs
- Genre classification: Books can be categorized into different genres enabling easier organization, as well as being able to choose a book easily from a predefined category.
- Search and Filtering: Users can search for books by title, author, or genre quickly
- Lending tracking: Users can easily keep track of the books borrowed from their collections
- Reading status: Users can update their reading status for their books

## Authors

- [@Rhoda Muya](https://www.github.com/Rhoda-NM)

## Installation
1. Clone this repository to your local machine:
    ``````bash
    git clone https://github.com/Rhoda-NM/Reeds-Book-Catalog-final-project.git
    ```

2. Navigate to the project directory
    cd  Reeds-Book-Catalog-final-project

3. Install virtual environment
    run: pipenv install then pipenv she

3. Install the required dependencies
   pip install click
   pip install colorama

4. Run the CLI appliccation
   python cli.py

## Usage
Once running the CLI application presents a menu with different navigation options:
  ### --help: shows options present
  ### greet-user: says hello to the user
  ### browse-catalog: shows main menu
   
   ### Library Catalog Menu
    1. View books in catalog: View the books in the database
    2. Add a Book to Catalog: Add a book to the catalog database
    3. Browse genres: View the genres in the table genres in the db
    4. View Authors: View the Authors in the table authors in the db
    5. Search Book by Title: Search for a book by its title
    6. Search Books by Author: Search for books by the author name
    7. Search Books by Genre: Search for books in a specific genre
    8. Search Authors in a genre: Search for authors with books in        certain genre
    9. Lend a Book to a Friend: Take record of a book lent out
    10. View borrowed Books From Catalog: View the books that user is currently lending out
    11. Return Borrowed Book: Record a book when it's returned
    12. Delete a Book From Catalog: Remove a book from one's catalog


## File structure
The project folder contains:
|-lib-|-
       |- models-|-
                 |- author.py- Contains class object Author and its methods and attribute
                 - book.py Contains class object Book and its methods and attributes
                 - genre.py- Contains class object Genre and its methods and attributes
                 - lending.py- Contains class object Lending and its methods and attributes
        |-cli.py- Main function for the implementation of the CLI
        |-debug.py - Sets up the ipdn
        |-helpers.py - contains the functions to be executed in the cli
        |-seed.py - Contains data from the classes used to create db and add data to it
|-gitignore
|-catalog.db
|-LICENSE.md
|-Pipfile
|-{}Pipfile.lock
|-README.md

## Tech Stack
**PYTHON
** SQL
** Libraries: 
            -sqlite
            -click
            -colorama



## License
Learn.co Educational Content License: (http://learn.co/content-license) (http://learn.co/content-license)