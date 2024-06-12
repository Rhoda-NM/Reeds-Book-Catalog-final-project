#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.author import Author
from models.book import Book
from models.genre import Genre
from models.lending import Lending

def seed_database():
    Book.drop_table()
    Book.create_table()
    Author.drop_table()
    Author.create_table()
    Genre.drop_table()
    Genre.create_table()
    Lending.drop_table()
    Lending.create_table()

    #create table data
seed_database()
print("Seeded database")
