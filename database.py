import sqlite3
class DataBase():
    connect_db = None
    cursor = None
    db  = 'shaken.db'
    russian_smth_index = 1
    english_smth_index = 0

    def __init__(self):
        self.connect_db = sqlite3.connect(self.db)
        self.cursor = self.connect_db.cursor()

    def changes_db(self, sql):
        # common function of change and commit
        self.cursor.execute(sql)
        self.connect_db.commit()

    def insert_db(self,table,en,ru,theme,selection):
        self.cursor.execute(f'SELECT * FROM "{table}"')
        id = len(self.cursor.fetchall()) + 1
        sql = f"INSERT INTO {table} VALUES ('{id}','{en}','{ru}','{theme}','{selection}')"
        self.changes_db(sql)

    def delete_db(self,table,theme,selection,smth):
        warn = input('Are you sure? y/n \n')
        if warn == 'y':
            sql = f"DELETE FROM {table} WHERE theme = '{theme}' AND selection = '{selection}' and en_words = '{smth}'"
            self.changes_db(sql)

    def update_db(self):
        sql = """UPDATE {} SET {} = {} WHERE {} = {}""".format('words', 'ru_word', "'есть'", 'ru_word', "'еда'")
        self.changes_db(sql)

    def select_db(self, sql):
        self.changes_db(sql)
        return self.cursor.fetchall()
