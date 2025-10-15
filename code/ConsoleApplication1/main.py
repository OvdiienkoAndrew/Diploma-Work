import os
import tkinter as tk
import tkinter.font as tkFont
import ctypes
import sqlite3

def hide_folder(path):
   FILE_ATTRIBUTE_HIDDEN = 0x02
   FILE_ATTRIBUTE_SYSTEM = 0x04
   attributes = FILE_ATTRIBUTE_HIDDEN | FILE_ATTRIBUTE_SYSTEM

   ctypes.windll.kernel32.SetFileAttributesW(path, attributes)

def creat_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)


def input_load_db_rules(name_db):
    conn = sqlite3.connect(name_db)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT 1
    FROM load
    LIMIT 1
    """, ())

    if cursor.fetchone():
        return

    names = ["Середнє навантаження", "Максимум перевищення у %", "Максимум", "Мінімум", "Зас. дек. з навчальної роботи", "Зас. дек. з наукової роботи", "Зас. дек. з виховної роботи", "Зас. дек. з міжнародної роботи", "Гаранти ОП акредитуються", "Гаранти ОП не акредитуються", "Редактори журналів Скопус", "Керівники аспірантів", "Рівномірність розподілу"]

    values = [580, 4.3, 600, 460, 100, 60, 60, 60, 100, 0, 100, 20, 20.5]

    for i, name in enumerate(names):

        cursor.execute("""
            INSERT INTO load (name, npp_pp, value)
            VALUES (?, ?, ?)
            """, (str(names[i]), "НПП", float(values[i])))

        conn.commit()

    names = ["Середнє навантаження", "Максимум перевищення у %", "Максимум", "Мінімум", "Зас. дек. з навчальної роботи", "Зас. дек. з наукової роботи", "Зас. дек. з виховної роботи", "Зас. дек. з міжнародної роботи","Рівномірність розподілу"]

    values = [580, 4.3, 600, 460, 100, 60, 60, 60,  20.5]

    for i, name in enumerate(names):

        cursor.execute("""
            INSERT INTO load (name, npp_pp, value)
            VALUES (?, ?, ?)
            """, (str(names[i]), "ПП", float(values[i])))

        conn.commit()

    conn.close()
   
 
def main():
    if __name__=="__main__":
        from src.data_base.create.main import create_db
        from src.menus.main import main_menu

        

        root = tk.Tk()
        root.attributes('-fullscreen', True)

        creat_folder("resources\\data base\\working")
        creat_folder("resources\\data base\\archive")
        hide_folder("resources\\data base")

        name_db = "resources\\data base\\working\\file.db"

        create_db(name_db)
        input_load_db_rules(name_db)

        creat_folder("resources\\Середнэ навантаження\\НПП\\Загальне")
        creat_folder("resources\\Середнэ навантаження\\НПП\\Лекційне")
        creat_folder("resources\\Середнэ навантаження\\НПП\\Аудиторне")

        creat_folder("resources\\Середнэ навантаження\\ПП\\Загальне")
        creat_folder("resources\\Середнэ навантаження\\ПП\\Лекційне")
        creat_folder("resources\\Середнэ навантаження\\ПП\\Аудиторне")


        big_font = tkFont.Font(family="Times New Roman", size=22)
        root.option_add("*Button.Font", big_font)
        root.option_add("*Label.Font", big_font)
        root.option_add("*Entry.Font", big_font)
        root.option_add("*Menu.Font", big_font)

        main_menu(root, name_db)

main()