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
    1. View books in the catalog: View the books in the database
    2. Add a Book to the Catalog: Add a book to the catalog database
    3. Browse genres: View the genres in the table genres in the db
    4. View Authors: View the Authors in the table authors in the db
    5. Search Book by Title: Search for a book by its title
    6. Search Books by Author: Search for books by the author's name
    7. Search Books by Genre: Search for books in a specific genre
    8. Search Authors in a genre: Search for authors with books in a certain genre
    9. Lend a Book to a Friend: Take a record of a book lent out
    10. View borrowed Books From Catalog: View the books that user is currently lending out
    11. Return Borrowed Book: Record a book when it's returned
    12. Delete a Book From Catalog: Remove a book from one's catalog

   ### CLI working
    Viewing books:
    ![Screenshot from 2024-06-13 14-02-45](https://github.com/Rhoda-NM/Reeds-Book-Catalog-final-project/assets/56297292/dc1a4b09-dd27-4e85-b268-57cd4b9df45f)
    Adding books:
    ![Screenshot from 2024-06-13 14-02-45](https://github.com/Rhoda-NM/Reeds-Book-Catalog-final-project/assets/56297292/5d8a0ee0-e8c6-42d6-bd3b-906e8a5673e4)




## File structure
The project folder contains:

├── Pipfile
├── Pipfile.lock
├── README.md
├── LICENSE.md
├── gitignore
├── catalog.db
└── lib
    ├── models
    │   ├── __init__.py
    |   ├── author.py 
    |   ├── book.py 
    |   ├── genre.py 
    │   └── lending.py 
    ├── cli.py 
    ├── debug.py 
    └── helpers.py 
    ├── seed.py 

## Models and Fuctions in the CLI
 ### CLI Script
The main entry point of the application is cli.py. It contains commands and functionality to interact with the book catalog, manage lending, and perform various operations related to books, authors, and genres.

### Models
 1. Book
 Represents a book in the catalog with attributes such as title, author, genre, publication year, and reading status. Provides methods for updating the reading status, marking as read or unread, and saving changes to the database.
 2. Author
 Represents an author of a book with attributes like name and potentially other details. Provides methods for finding authors, creating author instances, and managing author data in the database.
 3. Genre
 Represents a genre of books with attributes like name and potentially other details. Provides methods for finding genres, creating genre instances, and managing genre data in the database.
 4. Lending
 Manages lending information, including borrower details, lending dates, and return dates. Provides methods for creating lending instances, retrieving borrowed books, and handling lending data in the database.



### Functions
- list_books()
This function retrieves and lists all books currently in the catalog. It provides detailed information about each book, including the title, author, genre, publication year, and reading status.

- add_book()
Allows users to add a new book to the catalog by providing the title, author, genre, publication year, and reading status.

- borrowed_books()
Displays a list of books that are currently borrowed, along with information about the borrowers and return dates.

- lend_book()
Enables users to lend a book to a friend by specifying the book title, borrower's name, and lending date.

- return_book()
Allows users to return a borrowed book by entering the book title. The book is then marked as returned in the catalog.

## Tech Stack
**PYTHON
** SQL
** Libraries: 
            -sqlite
            -click
            -colorama



## License
Learn.co Educational Content License: (http://learn.co/content-license) (http://learn.co/content-license)
