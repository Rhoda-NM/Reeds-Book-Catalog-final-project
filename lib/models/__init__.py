import sqlite3

CONN = sqlite3.connect('catalog.db')
CURSOR = CONN.cursor()
