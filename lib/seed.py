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
    Book.create("Pride and Prejudice", "Jane Austeen", "Romance", 1813, "Unread")
    Book.create("Clockwork Angel", "Cassandra Clare", "Fantasy Fiction", 2012, "Read")
    Book.create("The gilded ones", "Namina Forna", "Fantasy Fiction", 2021, "read")
    Book.create("The Pivot Year", "Brianna West", "Self growth", 2023, "Unread")
    Book.create("The Symposium", "Plato", "Philosophy", 2008, "Read")
    Book.create("It ends with us", "Collen Hoover", "Romance", 2016, "Unread")
    Book.create("Jane Eyre", "Charlotte Bronte", "Romance", 1847, "Read")
    Book.create("The Stranger", "Albert Camus", "Philosophy", 1942, "Read")
    Book.create("The Mountain is You", "Brianna West", "Self growth", 2020, "Unread")
    

seed_database()
print("Seeded database")
