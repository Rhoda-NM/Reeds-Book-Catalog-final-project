# lib/models/genre.py
from models.__init__ import CURSOR, CONN

class Genre:

    all={}

    def __init__(self, name):
        self._id = None
        self.name = name
        self._books = []

    def __repr__(self):
        return f"<Genre: {self.id}: {self.name}>"
    
    @classmethod
    def create_table(cls):
        """Create a new table to persist the attributes of the Genre instances"""
        sql = """
            CREATE TABLE IF NOT EXISTS genres(
                id INTEGER PRIMARY KEY,
                name TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """Drop the table that persists Genre instances"""
        sql = """
            DROP TABLE IF EXISTS genres
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """Insert a new row with the name values of the current genre instance. Update object id attribute with the primary key value of the new row"""
        sql = """
            INSERT INTO genres(name)
            VALUES (?)
        """
        CURSOR.execute(sql, (self.name,))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name):
        """Initialize a new Genre instance and save the object to the database"""
        genre = cls(name)
        genre.save()
        return genre
    @classmethod
    def genre_instance(cls, row):

        """Returns a Genre object having attributes from the genres table row"""
        genre = cls.all.get(row[0])
        if genre:
            genre.name = row[1]
        else:
            genre = cls(row[1])
            genre.id = row[0]
            cls.all[genre.id] = genre
        return genre
    
    @classmethod
    def get_all(cls):
        """Return a list containing a Genre object per row in the table"""
        sql = """
            SELECT *
            FROM genres
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.genre_instance(row) for row in rows]
    
    @classmethod
    def find_by_name(cls, name):
        """Returns Genre object corresponding to first table row matching given name"""
        sql = """
            SELECT *
            FROM genres
            WHERE name is ?
        """
        row = CURSOR.execute(sql, (name, )).fetchone()
        return cls.genre_instance(row) if row else None
    
    def books(self):
        """Return books in the given genre"""
        genre = self.name
        from models.book import Book
        sql = """
            SELECT * FROM books
            WHERE genre_name = ?
        """

        rows = CURSOR.execute(sql, (genre,)).fetchall()
        return [
            Book.instance_from_db(row) for row in rows
        ]

    def authors(self):
        """Return authors in a certain genre"""
        from models.author import Author
        genre_authors  = []
        for book in self.books():
            if book.author_name not in genre_authors:
                genre_authors.append(book.author_name)
        
        authors = [Author.find_by_name(name) for name in genre_authors]
        return authors
            

    