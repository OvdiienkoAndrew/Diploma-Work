# -*- coding: utf-8 -*-

import sqlite3
import tkinter as tk
from tkinter import messagebox 
import pyperclip

from tkinter import font 
def errors_menu(root, name_db):

    conn = sqlite3.connect(name_db)
    cursor = conn.cursor()

    from src.settings.settings import clear_window, on_enter, on_leave

    from src.data_base.error.check.main import check_db

    from src.menus.exit import on_escape

    from src.menus.main import main_menu

    from src.menus.main import main_menu

    from src.menus.request import requests_menu
    from src.menus.settings import settings_menu

    clear_window(root)

    second_window = tk.Toplevel(root)
    second_window.title("Результат")
    second_window.attributes('-fullscreen', True)

    second_window.bind("<Escape>", lambda event: (second_window.destroy(),on_escape(event, root, name_db)))

    menubar = tk.Menu(second_window)

    filemenu = tk.Menu(menubar, tearoff=0)
    filemenu.add_command(label="Головне меню", command=lambda: (second_window.destroy(),main_menu(root, name_db)))
    filemenu.add_command(label="Налаштування", command=lambda: (second_window.destroy(),settings_menu(root, name_db)))
    filemenu.add_command(label="Запити", command=lambda: (second_window.destroy(),requests_menu(root, name_db)))
    filemenu.add_separator()
    filemenu.add_command(label="Вихід", command=lambda: (second_window.destroy(),on_escape(None, root, name_db)))
   
    menubar.add_cascade(label="Файл", menu=filemenu)

    if check_db(root, name_db):
        errormenu = tk.Menu(menubar, tearoff=0)
        errormenu.add_command(label="Помилки", command=lambda: (second_window.destroy(),errors_menu(root, name_db)))
        menubar.add_cascade(label="Помилки", menu=errormenu)

    second_window.config(menu=menubar)

    class ErrorPerson:
         
        def __init__(self, surname, name, patronomic, position, sign, department, years, error, npp_pp):
           
            self.__surname = str(surname).replace(' ','')
            self.__name = str(name).replace(' ','')
            self.__patronomic = str(patronomic).replace(' ','')

            position = str(position).lower().replace(' ','')

            if position: 
                if position[0] == 'з':
                    self.__position = "заф. кафедри"
                elif position[0].lower() == 'п':
                    self.__position = "професор"
                elif position[0].lower() == 'д':
                    self.__position = "доцент"
                elif position[0].lower() == 'с':
                    self.__position = "ст. викладач"
                elif position[0].lower() == 'а':
                    self.__position = "асистент"
                elif position[0].lower() == 'в':
                    if position[1].lower()  == '.':
                        self.__position = "в.о. заф. кафедри"
                    elif position[1].lower() == 'и':
                        self.__position = "викладач"
                    else:
                       self.__position = ""
                else:
                    self.__position = ""
            else:
                self.__position = ""

            self.__sign = str(sign).replace(' ','')
            
            self.__department = str(department).replace(' ','')

            self.__years = str(years).lower().replace(' ','')

            self.__error = str(error)

            self.__npp_pp = "НПП" if str(npp_pp)[0].lower() == 'н' else "ПП"
           
        def get_person(self):
            return f"{str(self.__surname).replace(' ','')} {str(self.__name).replace(' ','')} {str(self.__patronomic).replace(' ','')}"

        def get_position(self):
            return str(self.__position).replace(' ','')

        def get_sign(self):
            return str(self.__sign).replace(' ','')

        def get_department(self):
            return str(self.__department).replace(' ','')

        def get_years(self):
            return str(self.__years).replace(' ','')

        def get_error(self):
            return str(self.__error)

        def get_npp_pp(self):
            return str(self.__npp_pp)

        def get(self):
            if self.get_sign():
                return f"{self.get_person()}, {self.get_npp_pp()}, {self.get_sign()}, {self.get_position()}, ({self.get_department()}) {self.get_years()}: \"{self.get_error()}\""
            return f"{self.get_person()}, {self.get_npp_pp()}, знак сумісності відсутній, {self.get_position()}, ({self.get_department()}) {self.get_years()}: \"{self.get_error()}\""
           

    class ErrorVacancy:
        def __init__(self, name, number, position, sign, department, years, error, npp_pp):
           
            self.__name = str(name).replace(' ','')
            self.__number = int(str(number).replace(' ','') or 0)

            position = str(position).lower().replace(' ','')

            if position: 
                if position[0] == 'з':
                    self.__position = "заф. кафедри"
                elif position[0].lower() == 'п':
                    self.__position = "професор"
                elif position[0].lower() == 'д':
                    self.__position = "доцент"
                elif position[0].lower() == 'с':
                    self.__position = "ст. викладач"
                elif position[0].lower() == 'а':
                    self.__position = "асистент"
                elif position[0].lower() == 'в':
                    if position[1].lower()  == '.':
                        self.__position = "в.о. заф. кафедри"
                    elif position[1].lower() == 'и':
                        self.__position = "викладач"
                    else:
                       self.__position = ""
                else:
                    self.__position = ""
            else:
                self.__position = ""

            self.__sign = str(sign).replace(' ','')
            
            self.__department = str(department).replace(' ','')

            self.__years = str(years).lower().replace(' ','')

            self.__error = str(error)

            self.__npp_pp = "НПП" if str(npp_pp)[0].lower() == 'н' else "ПП"

        def get_vacancy(self):
            return f"{str(self.__name).replace(' ','')} {int(str(self.__number).replace(' ',''))}"

        def get_position(self):
            return str(self.__position).replace(' ','')

        def get_sign(self):
            return str(self.__sign).replace(' ','')

        def get_department(self):
            return str(self.__department).replace(' ','')

        def get_years(self):
            return str(self.__years).replace(' ','')

        def get_error(self):
            return str(self.__error)

        def get_npp_pp(self):
            return str(self.__npp_pp)


        
        def get(self):
            if self.get_sign():
                return f"{self.get_vacancy()}, {self.get_npp_pp()}, {self.get_sign()}, {self.get_position()}, ({self.get_department()}) {self.get_years()}: \"{self.get_error()}\""
            return f"{self.get_vacancy()}, {self.get_npp_pp()}, знак сумісності відсутній, {self.get_position()}, ({self.get_department()}) {self.get_years()}: \"{self.get_error()}\""
           
     
    assistant_error = []

    cursor.execute("""
        SELECT DISTINCT
        
            person."прізвище",
            person."ім_я",
            person."по-батькові",

            job."посада",

            job."знак_сумісності",

            code_year."назва_кафедри",
            code_year."роки",

            check_assistant_teacher."помилка",

            job.'НПП_ПП'

            FROM check_assistant_teacher

            JOIN job ON check_assistant_teacher."job_id" = job.id 
            JOIN code_year ON job."код_рік_id" = code_year.id
            JOIN person ON job.id = person."job_id" 
            ORDER BY check_assistant_teacher."помилка" ASC
           
        """,())

  
    for value in cursor.fetchall():
        assistant_error.append(ErrorPerson(value[0],value[1],value[2],value[3],value[4],value[5],value[6],value[7],value[8]))

    cursor.execute("""
        SELECT DISTINCT
        
            vacancy."назва",
            vacancy."номер",

            job."посада",

            job."знак_сумісності",

            code_year."назва_кафедри",
            code_year."роки",

            check_assistant_teacher."помилка",

            job.'НПП_ПП'

            FROM check_assistant_teacher

            JOIN job ON check_assistant_teacher."job_id" = job.id 
            JOIN code_year ON job."код_рік_id" = code_year.id
            JOIN vacancy ON job.id = vacancy."job_id" 
            ORDER BY check_assistant_teacher."помилка" ASC
           
        """,())

    for value in cursor.fetchall():
        assistant_error.append(ErrorVacancy(value[0],value[1],value[2],value[3],value[4],value[5],value[6],value[7]))

    class ErrorPersonTime:
         
        def __init__(self, surname, name, patronomic, position, sign, department, years, min_local, max_local,min_global,max_global,npp_pp):
           
            self.__surname = str(surname).replace(' ','')
            self.__name = str(name).replace(' ','')
            self.__patronomic = str(patronomic).replace(' ','')

            position = str(position).lower().replace(' ','')

            if position: 
                if position[0] == 'з':
                    self.__position = "заф. кафедри"
                elif position[0].lower() == 'п':
                    self.__position = "професор"
                elif position[0].lower() == 'д':
                    self.__position = "доцент"
                elif position[0].lower() == 'с':
                    self.__position = "ст. викладач"
                elif position[0].lower() == 'а':
                    self.__position = "асистент"
                elif position[0].lower() == 'в':
                    if position[1].lower()  == '.':
                        self.__position = "в.о. заф. кафедри"
                    elif position[1].lower() == 'и':
                        self.__position = "викладач"
                    else:
                       self.__position = ""
                else:
                    self.__position = ""
            else:
                self.__position = ""

            self.__sign = str(sign).replace(' ','')
            
            self.__department = str(department).replace(' ','')

            self.__years = str(years).lower().replace(' ','')

            self.__min_local = str(min_local).replace(' ','').replace('None','')
            self.__max_local = str(max_local).replace(' ','').replace('None','')
            self.__min_global = str(min_global).replace(' ','').replace('None','')
            self.__max_global = str(min_global).replace(' ','').replace('None','')

            self.__npp_pp = "НПП" if str(npp_pp)[0].lower() == 'н' else "ПП"
           
        def get_person(self):
            return f"{str(self.__surname).replace(' ','')} {str(self.__name).replace(' ','')} {str(self.__patronomic).replace(' ','')}"

        def get_position(self):
            return str(self.__position).replace(' ','')

        def get_sign(self):
            return str(self.__sign).replace(' ','')

        def get_department(self):
            return str(self.__department).replace(' ','')

        def get_years(self):
            return str(self.__years).replace(' ','')

        def get_min_local(self):
            return (str(self.__min_local).replace(' ',''))

        def get_max_local(self):
            return (str(self.__max_local).replace(' ',''))

        def get_min_global(self):
            return (str(self.__min_global).replace(' ',''))

        def get_max_global(self):
            return (str(self.__max_global).replace(' ',''))

        def get_npp_pp(self):
            return str(self.__npp_pp)

        def get(self):
            if self.get_sign():
                return f"{self.get_person()}, {self.get_npp_pp()}, {self.get_sign()}, {self.get_position()}, ({self.get_department()}) {self.get_years()}: \"Мінімум: {self.get_min_local()}; максимум: {self.get_max_local()}; загальний мінімум: {self.get_min_global()}; загальний максимум: {self.get_max_global()}.\""
            return f"{self.get_person()}, {self.get_npp_pp()}, знак сумісності відсутній, {self.get_position()}, ({self.get_department()}) {self.get_years()}: \"Мінімум: {self.get_min_local()}; максимум: {self.get_max_local()}; загальний мінімум: {self.get_min_global()}; загальний максимум: {self.get_max_global()}.\""
         
            
    class ErrorVacancyTime:
         
        def __init__(self, name, number, position, sign, department, years, min_local, max_local,min_global,max_global, npp_pp):
           
            self.__name = str(name).replace(' ','')
            self.__number = int(str(number).replace(' ','') or 0)

            position = str(position).lower().replace(' ','')

            if position: 
                if position[0] == 'з':
                    self.__position = "заф. кафедри"
                elif position[0].lower() == 'п':
                    self.__position = "професор"
                elif position[0].lower() == 'д':
                    self.__position = "доцент"
                elif position[0].lower() == 'с':
                    self.__position = "ст. викладач"
                elif position[0].lower() == 'а':
                    self.__position = "асистент"
                elif position[0].lower() == 'в':
                    if position[1].lower()  == '.':
                        self.__position = "в.о. заф. кафедри"
                    elif position[1].lower() == 'и':
                        self.__position = "викладач"
                    else:
                       self.__position = ""
                else:
                    self.__position = ""
            else:
                self.__position = ""

            self.__sign = str(sign).replace(' ','')
            
            self.__department = str(department).replace(' ','')

            self.__years = str(years).lower().replace(' ','')

            self.__min_local = str(min_local).replace(' ','').replace('None','')
            self.__max_local = str(max_local).replace(' ','').replace('None','')
            self.__min_global = str(min_global).replace(' ','').replace('None','')
            self.__max_global = str(min_global).replace(' ','').replace('None','')

            self.__npp_pp = "НПП" if str(npp_pp)[0].lower() == 'н' else "ПП"
           
        def get_vacancy(self):
            return f"{str(self.__name).replace(' ','')} {str(self.__number).replace(' ','')}"

        def get_position(self):
            return str(self.__position).replace(' ','')

        def get_sign(self):
            return str(self.__sign).replace(' ','')

        def get_department(self):
            return str(self.__department).replace(' ','')

        def get_years(self):
            return str(self.__years).replace(' ','')

        def get_min_local(self):
            return (str(self.__min_local).replace(' ',''))

        def get_max_local(self):
            return (str(self.__max_local).replace(' ',''))

        def get_min_global(self):
            return (str(self.__min_global).replace(' ',''))

        def get_max_global(self):
            return (str(self.__max_global).replace(' ',''))

        def get_npp_pp(self):
            return str(self.__npp_pp)

        def get(self):
            if self.get_sign():
                return f"{self.get_vacancy()}, {self.get_npp_pp()}, {self.get_sign()}, {self.get_position()}, ({self.get_department()}) {self.get_years()}: \"Мінімум: {self.get_min_local()}; максимум: {self.get_max_local()}; загальний мінімум: {self.get_min_global()}; загальний максимум: {self.get_max_global()}.\""
            return f"{self.get_vacancy()}, {self.get_npp_pp()}, знак сумісності відсутній, {self.get_position()}, ({self.get_department()}) {self.get_years()}: \"Мінімум: {self.get_min_local()}; максимум: {self.get_max_local()}; загальний мінімум: {self.get_min_global()}; загальний максимум: {self.get_max_global()}.\""
           
    cursor.execute("""
        SELECT DISTINCT
        
            person."прізвище",
            person."ім_я",
            person."по-батькові",

            job."посада",

            job."знак_сумісності",

            code_year."назва_кафедри",
            code_year."роки",

            check_db."мінімум",
            check_db."максимум",
            check_db."загальний_мінімум",
            check_db."загальний_максимум",

            job.'НПП_ПП'


            FROM check_db

            JOIN job ON check_db."job_id" = job.id 
            JOIN code_year ON job."код_рік_id" = code_year.id
            JOIN person ON job.id = person."job_id" 
            ORDER BY check_db."мінімум" ASC,
            check_db."максимум" ASC,
            check_db."загальний_мінімум" ASC,
            check_db."загальний_максимум" ASC
           
        """,())

    for value in cursor.fetchall():
        assistant_error.append(ErrorPersonTime(value[0],value[1],value[2],value[3],value[4],value[5],value[6],value[7],value[8],value[9],value[10],value[11]))

    cursor.execute("""
        SELECT DISTINCT
        
            vacancy."назва",
            vacancy."номер",

            job."посада",

            job."знак_сумісності",

            code_year."назва_кафедри",
            code_year."роки",

            check_db."мінімум",
            check_db."максимум",
            check_db."загальний_мінімум",
            check_db."загальний_максимум",

            job.'НПП_ПП'


            FROM check_db

            JOIN job ON check_db."job_id" = job.id 
            JOIN code_year ON job."код_рік_id" = code_year.id
            JOIN vacancy ON job.id = vacancy."job_id" 
            ORDER BY check_db."мінімум" ASC,
            check_db."максимум" ASC,
            check_db."загальний_мінімум" ASC,
            check_db."загальний_максимум" ASC
           
        """,())

    for value in cursor.fetchall():
        assistant_error.append(ErrorVacancyTime(value[0],value[1],value[2],value[3],value[4],value[5],value[6],value[7],value[8],value[9],value[10]))

    big_text = ""
    for value in assistant_error:
       big_text += f"{value.get()}\n" 


    frame = tk.Frame(second_window)
    frame.pack(fill="both", expand=True)

    my_font = font.Font(family="Arial", size=24)

    text = tk.Text(frame, wrap="none", font=my_font, state="normal")
    text.pack(side="left", fill="both", expand=True)

    scroll_y = tk.Scrollbar(frame, orient="vertical", command=text.yview)
    scroll_y.pack(side="right", fill="y")

    scroll_x = tk.Scrollbar(second_window, orient="horizontal", command=text.xview)
    scroll_x.pack(side="bottom", fill="x")

    text.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
    text.insert("1.0", big_text)

    # Кнопка "Копировать"
    copy_button = tk.Button(second_window, text="Копіювати текст", font=my_font,
                            command=lambda: copy_text_to_clipboard(root, text))
    copy_button.pack(pady=20)

    def copy_text_to_clipboard(root, text_widget):
        text = text_widget.get("1.0", "end-1c")  # Получаем весь текст без последнего \n
        pyperclip.copy(text)  # Копируем текст с помощью pyperclip
        #second_window.destroy()
        #main_menu(root, name_db)

    def paste_from_clipboard(text_widget):
        try:
            clipboard_text = pyperclip.paste()  # Получаем текст из буфера обмена
            text_widget.insert(tk.INSERT, clipboard_text)  # Вставляем в текущее место курсора
        except Exception as e:
            messagebox.showwarning("Помилка", f"Помилка при вставці: {e}")

    root.update()
    conn.close()
