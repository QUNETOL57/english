import sqlite3
import random

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

    def insert_db(self,en,ru,th,sel):
        self.cursor.execute(f'SELECT * FROM "words"')
        id = len(self.cursor.fetchall()) + 1
        sql = """INSERT INTO {} VALUES ('{}','{}','{}','{}','{}')""".format('words',id,en,ru,th,sel)
        self.changes_db(sql)

    def delete_db(self):
        sql = """DELETE FROM {} WHERE {} = {}""".format('words','en_word',"{}".format('bread'))
        self.changes_db(sql)

    def update_db(self):
        sql = """UPDATE {} SET {} = {} WHERE {} = {}""".format('words', 'ru_word', "'есть'", 'ru_word', "'еда'")
        self.changes_db(sql)

    def select_db(self, sql = """SELECT * FROM {}""".format('words')):
        self.changes_db(sql)
        return self.cursor.fetchall()

class ChoiceTSMixin:
    #choice theme from the database
    def choice_theme(self,table):
        theme = input('Theme: ')
        if theme == 'all' or theme == '*':
            sql = f'SELECT "en_{table}","ru_{table}" FROM {table}'
        else:
            sql = f'SELECT "en_{table}","ru_{table}" FROM {table} WHERE theme="{theme}"'
        return sql
    #choice selectin from the database
    def choice_selection(self,sql):
        selection = input('Selection: ')
        if selection == 'all' or selection == '*':
            return sql
        else:
            return sql + f' AND selection="{selection}"'

class PrintSmthMixin:
    def print_smth(self,theme,index1,index2):
        db = self.select_db(theme)
        for line in db:
            print(f"{line[index1]} - {line[index2]}")

class Word(DataBase,ChoiceTSMixin,PrintSmthMixin):
    def input_word(self):
        #input word to the database
        # words =[]
        # words += input().split()
        # self.insert_db(words[0],words[1],words[2],words[3])
        theme = input('Theme: ')
        selection = input('Selection: ')
        while True:
            word_en = input()
            if word_en == 'e' or word_en == 'q':
                break
            word_ru = input()
            self.insert_db(word_en,word_ru,theme,selection)



    def words_en_ru(self):
        # print english - russian words for a theme
        self.print_smth(self.choice_selection(self.choice_theme('words')),
        self.english_smth_index,self.russian_smth_index)

    def words_ru_en(self):
        # print russian - english words for a theme
        self.print_smth(self.choice_selection(self.choice_theme('words')),
        self.russian_smth_index,self.english_smth_index)

    def test_random_word(self,index1,index2):
        # print random word for a theme
        db = self.select_db(self.choice_selection(self.choice_theme('words')))
        line = db[random.randint(0,len(db)-1)]
        print(f"{line[index1]} - {line[index2]}")

    def test_random_en(self):
        self.test_random_word(self.english_smth_index,self.russian_smth_index)

    def test_random_ru(self):
        self.test_random_word(self.russian_smth_index,self.english_smth_index)

    def test_input(self, index1, index2):
        db = self.select_db(self.choice_selection(self.choice_theme('words')))
        random.shuffle(db)
        for line in db:
            answer = input(f"{line[index1]} : ")
            if answer.strip() == line[index2]:
                print("+")
            else:
                print("-")

    def test_input_ru(self):
        self.test_input(self.english_smth_index,self.russian_smth_index)

    def test_input_en(self):
        self.test_input(self.russian_smth_index,self.english_smth_index)

    def test_one_three(self, index1,index2):
        # print 1 word and 3 another words
        db = self.select_db(self.choice_selection(self.choice_theme('words')))
        random.shuffle(db)
        def make_word(db,index1,index2,word1):
            words_from_db = []
            for i in db:
                words_from_db.append(i[index1])
            while True:
                word2 = random.choice(words_from_db)
                word3 = random.choice(words_from_db)
                if word1 != word2 and word1 != word3 and word2 != word3:
                    words = [word1,word2,word3]
                    random.shuffle(words)
                    return f"{words[0]} {words[1]} {words[2]}"
        for line in db:
            print(f"{line[index2]}\n{make_word(db,index1,index2,line[index1])}")
            answer = input()
            if answer.strip() == line[index1]:
                print("+")
            else:
                print("-")

    def test_one_three_ru(self):
        self.test_one_three(self.russian_smth_index,self.english_smth_index)

    def test_one_three_ru(self):
        self.test_one_three(self.english_smth_index, self.russian_smth_index)


class Text(DataBase,ChoiceTSMixin,PrintSmthMixin):
    def text_en_ru(self):
        self.print_smth(self.choice_selection(self.choice_theme('texts')),
        self.english_smth_index,self.russian_smth_index)

    def text_ru_en(self):
        self.print_smth(self.choice_selection(self.choice_theme('texts')),
        self.russian_smth_index,self.english_smth_index)

word = Word()
# word.input_word()
# word.words_en_ru()
word.test_input_ru()
