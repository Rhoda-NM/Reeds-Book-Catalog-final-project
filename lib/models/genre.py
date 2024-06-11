# lib/models/genre.py
from models.__init__ import CURSOR, CONN

class Genre:

    all={}

    def __init__(self, name, category):
        self._id = None
        self.name = name
        self.category = category

    def __repr__(self):
        return f"<Genre: {self.id}: {self.name}: {self.category}>"
    
    @classmethod
    def create_table(cls):
        """Create a new table to persist the attributes of the Genre instances"""
        sql = """
            CREATE TABLE IF NOT EXISTS genres(
                id INTEGER PRIMARY KEY,
                name TEXT,
                category TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

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
            INSERT INTO genres(name, cattegory)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.name, self.category))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, category):
        """Initialize a new Genre instance and save the object to the database"""
        genre = cls(name, category)
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
    def find_by_name(cls, name):
        """Returns Genre object corresponding to first table row matching given name"""
        sql = """
            SELECT *
            FROM genres
            WHERE name is ?
        """
        row = CURSOR.execute(sql, (name, )).fetchone()
        return cls.genre_instance(row) if row else None
    
    @classmethod
    def find_by_category(cls, category):
        """Returns Genre objects corresponding to table rows matching given category"""
        sql = """
            SELECT *
            FROM genres
            WHERE category is ?
        """
        rows = CURSOR.execute(sql, (category, )).fetchall()
        if rows:
            return [cls.genre_instance(row) for row in rows]
        else:
            return None

    