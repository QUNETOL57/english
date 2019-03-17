class Texts(DataBase,ChoiceTSMixin,PrintSmthMixin):
    def text_en_ru(self):
        self.print_smth(self.choice_selection(self.choice_theme('texts')),
        self.english_smth_index,self.russian_smth_index)

    def text_ru_en(self):
        self.print_smth(self.choice_selection(self.choice_theme('texts')),
        self.russian_smth_index,self.english_smth_index)
