import random
from database import DataBase
from utils import *

class Words(DataBase,ChoiceTSMixin,PrintSmthMixin):
    theme_selection = None
    class_name = 'words'
    def theme_init(self):
        self.theme_selection = self.choice_select(__class__.__name__.lower())

    def input_word(self):
        theme = self.choice_theme()
        selection = self.choice_selection()
        while True:
            word_en = input()
            if word_en == 'e' or word_en == 'q':
                break
            word_ru = input()
            self.insert_db(self.class_name,word_en,word_ru,theme,selection)

    def words_en_ru(self):
        # print english - russian words for a theme
        self.print_smth(self.theme_selection,
        self.english_smth_index,self.russian_smth_index)

    def words_ru_en(self):
        # print russian - english words for a theme
        self.print_smth(self.theme_selection,
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
        db = self.select_db(self.theme_selection)
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
                    return f"{words[0]} | {words[1]} | {words[2]}"
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
