class ChoiceTSMixin:
    #choice theme from the database
    def choice_theme(self):
        return input('Theme: ')

    def choice_selection(self):
        return input('Selection: ')

    def choice_theme_select(self,table):
        theme = self.choice_theme()
        if theme == 'all' or theme == '*':
            sql = f'SELECT "en_{table}","ru_{table}" FROM {table}'
        else:
            sql = f'SELECT "en_{table}","ru_{table}" FROM {table} WHERE theme="{theme}"'
        return sql
    #choice selectin from the database
    def choice_selection_select(self,sql):
        selection = self.choice_selection()
        if selection == 'all' or selection == '*':
            return sql
        else:
            return sql + f' AND selection="{selection}"'

    def choice_select(self,table):
        sql = self.choice_selection_select(self.choice_theme_select(table))
        return sql

class PrintSmthMixin:
    def print_smth(self,theme,index1,index2):
        db = self.select_db(theme)
        for line in db:
            print(f"{line[index1]} - {line[index2]}")
