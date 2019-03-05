import sqlite3
from os import system

class DataBase():
    connect_db = None
    cursor = None
    db  = 'shaken.db'
    def __init__(self):
        self.connect_db = sqlite3.connect(self.db)
        self.cursor = self.connect_db.cursor()

    def changes_db(self, sql):
        # common function of change and commit
        self.cursor.execute(sql)
        self.connect_db.commit()

    def insert_db(self,n,en,ru,th):
        sql = """INSERT INTO {} VALUES ('{}','{}','{}','{}')""".format('words',n,en,ru,th)
        self.changes_db(sql)

    def delete_db(self):
        sql = """DELETE FROM {} WHERE {} = {}""".format('words','en_word',"{}".format('bread'))
        self.changes_db(sql)

    def update_db(self):
        sql = """UPDATE {} SET {} = {} WHERE {} = {}""".format('words', 'ru_word', "'есть'", 'ru_word', "'еда'")
        self.changes_db(sql)

    def select_db(self):
        sql = """SELECT * FROM {}""".format('words')
        self.changes_db(sql)
        print(self.cursor.fetchall())

class Word(DataBase):
    def input_word(self):
        words =[]
        words += input().split()
        print(words)
        self.insert_db(words[0],words[1],words[2],words[3])


dbase = DataBase()
word = Word()
word.input_word()
# dbase.insert_db()
# dbase.delete_db()
# dbase.update_db()
dbase.select_db()
