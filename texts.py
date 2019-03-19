import random
from database import DataBase
from utils import *

class Texts(DataBase,ChoiceTSMixin,PrintSmthMixin):
    theme_selection = None
    class_name = 'texts'
    def theme_init(self):
        self.theme_selection = self.choice_select(self.class_name)

    def text_en_ru(self):
        self.print_smth(self.theme_selection,
        self.english_smth_index,self.russian_smth_index)

    def text_ru_en(self):
        self.print_smth(self.theme_selection,
        self.russian_smth_index,self.english_smth_index)

    def input_text(self):
        theme = self.choice_theme()
        selection = self.choice_selection()
        while True:
            text_en = input()
            if text_en == 'e' or text_en == 'q':
                break
            text_ru = input()
            self.insert_db(self.class_name,text_en,text_ru,theme,selection)
