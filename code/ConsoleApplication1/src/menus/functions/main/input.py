import tkinter as tk
from tkinter import filedialog, messagebox

import sqlite3
import pandas as pd
import threading


def on_click_input(root, name_db):
    
   
    def read_files(root, name_db, files_path, loading):

        def get_cell_str(i,j):
            return str(df.iloc[i, j])

        def get_cell_float(i,j):

            value = str(df.iloc[i, j]).replace(' ','').replace(',','.')

            if value == "nan":
                return 0.00

            try:
                value = float(value)
               
                return value
            except Exception:
                return 0.00

        def get_cells_float(i):
            value = []

            total = 0

            for j in range(8,27):
                value.append(get_cell_float(i, j))
                total += get_cell_float(i, j)
            
            value.append(total)
            return value   

        def bid_and_sign_of_madness(i):

            number = 0.00
            string = ""

            value = get_cell_str(i, 3).lower().replace(' ', '').replace(',', '.')

            index = 0

            while index < len(value) and (
            value[index] == '.' or value[index] == '0' or value[index] == '1' or value[index] == '2' or value[
            index] == '3' or value[index] == '4' or value[index] == '5' or value[index] == '6' or value[
            index] == '7' or value[index] == '8' or value[index] == '9'):

                index += 1

            if index == 0:
                return 0.00, ""

            number = float(value[:index])
            string = value[index:]

            if string:
                string = "сум."

            return number, string

        conn = sqlite3.connect(name_db)
        cursor = conn.cursor()

        for file_path in files_path:

            xls = pd.ExcelFile(file_path)

            if "Загальна" not in xls.sheet_names:
                messagebox.showinfo("Помилка", f'Лист "Загальна" не знайдено у файлі: {file_path}.')
                continue

            df = pd.read_excel(xls, sheet_name="Загальна",engine="openpyxl")

            fullname = get_cell_str(1,0)

            code = ""
            years = ""

            i = 0
            while i < len(fullname):
                if fullname[i] == '(':
                    i += 1
                    while fullname[i] != ')':
                        code += fullname[i]
                        i += 1

                if fullname[i] == '-' or fullname[i] == '0' or fullname[i] == '1' or fullname[i] == '2' or fullname[i] == '3' or fullname[i] == '4' or fullname[i] == '5' or fullname[i] == '6' or fullname[i] == '7' or fullname[i] == '8' or fullname[i] == '9':
                    years += fullname[i]
              
                i += 1

            if len(years) >= 1:
                if years[0] == '-':
                    years =  years[1:]
                elif years[len(years)-1] == '-':
                    years = years[:len(years)-1] + years[len(years):]
            else:
                years = ""

            if not code or not years:
                messagebox.showinfo("Помилка", f'Немає шифру кафедри або року в комірці А3 у файлі: {file_path}.')
                continue

            cursor.execute("""
                SELECT 1
                FROM code_year
                WHERE "назва_кафедри" = ?
                AND "роки" = ?
                LIMIT 1
            """, (str(code),str(years)))

            if cursor.fetchone():

                result = messagebox.askyesno("Попередження",
                "Перезаписати дані для кафедри " + code + " " + years + " років?")
                
                if result:
                    cursor.execute("PRAGMA foreign_keys = ON;")

                    cursor.execute("""
                   
                    DELETE FROM job
                    WHERE "код_рік_id" IN (
                    SELECT id FROM code_year
                    WHERE "назва_кафедри" = ? AND "роки" = ?
                    );
                    """, (str(code), str(years)))
                    conn.commit()

                    cursor.execute("""
                    SELECT id FROM code_year
                    WHERE "назва_кафедри" = ? AND "роки" = ?
                    """, (str(code), str(years)))
                    code_years_id = int(cursor.fetchone()[0])
                    

                else:
                    continue

            else:
                cursor.execute("""
                INSERT INTO code_year (
                "назва_кафедри", "роки"
                )
                VALUES (?, ?)
                """, (str(code), str(years)))
                conn.commit()
                code_years_id = cursor.lastrowid


           

            for i in range(len(df)):

                try:
                    helper = int(get_cell_str(i,0).replace(' ',''))
                except Exception:
                    continue
                 
              
                helper = get_cell_str(i, 1)

                if not helper.replace(' ',''):
                    continue

                name = ""
                surname = ""
                patronymic = ""

                vacancy = ""
                vacancy_number = ""
                
                helper = helper.replace('  ', ' ')
                if helper[0] == ' ':
                    helper = helper[1:]
                if helper[len(helper)-1] == ' ':
                    helper = helper[:len(helper)-1]

                helper = helper.split()

                if len(helper) == 3:

                    surname = helper[0]
                    name = helper[1]
                    patronymic = helper[2]

                elif len(helper)==2:

                    if helper[0].lower().replace(' ','') == "вакансія":
                        vacancy = "Вакансія"
                        try:
                            vacancy_number = int(helper[1])
                        except Exception:
                            continue
                    else:
                        continue

                elif len(helper)==1:
                    
                    if helper[0].lower().replace(' ','')[:8] == "вакансія":
                        vacancy = "Вакансія"
                        
                        try:
                            vacancy_number = int(helper[0].lower().replace(' ','')[8:])
                        except Exception:
                            continue
                    else:
                        continue
                else:
                    continue

                helper = get_cell_str(i, 2)

                if not helper.replace(' ',''):
                    continue

                position = ""
                academic_title_academic_degree = ""

                if helper[0].lower() == 'з':
                    position = "заф. кафедри"
                elif helper[0].lower() == 'п':
                    position = "професор"
                elif helper[0].lower() == 'д':
                    position = "доцент"
                elif helper[0].lower() == 'с':
                    position = "ст. викладач"
                elif helper[0].lower() == 'а':
                    position = "асистент"
                elif helper[0].lower() == 'в':
                    if helper[1].lower()  == '.':
                        position = "в.о. заф. кафедри"
                    elif helper[1].lower() == 'и':
                        position = "викладач"
                    else:
                        continue
                else:
                    continue

                for j in range(helper.find(',')+1,len(helper)):
                    if helper[j] == '\n':
                        continue
                    academic_title_academic_degree += helper[j]

                academic_title_academic_degree = academic_title_academic_degree.strip()

                first_semester_bid, first_semester_sign_of_madness = bid_and_sign_of_madness(i)
                second_semester_bid, second_semester_sign_of_madness = bid_and_sign_of_madness(i + 1)
                academic_year_bid, academic_year_sign_of_madness = bid_and_sign_of_madness(i + 2)

                if first_semester_sign_of_madness or second_semester_sign_of_madness or academic_year_sign_of_madness:
                    sign_of_madness = "сум."
                else:
                    sign_of_madness = ""

                first_semester_float = get_cells_float(i)
                second_semester_float = get_cells_float(i+1)

                academic_year_float = []

                for j in enumerate(first_semester_float, 0):
                    academic_year_float.append(first_semester_float+second_semester_float)
               
               
                if name:
                    cursor.execute("""
                        SELECT 1

                        FROM code_year 
                         
                        JOIN job ON code_year.id = job."код_рік_id" 
                        JOIN person ON job.id = person."job_id" 
                         
                        WHERE
                        person."ім_я"=?
                        AND
                        person."прізвище"=?
                        AND
                        person."по-батькові"=?
                        AND
                        job."знак_сумісності"=?
                        AND
                        code_year."назва_кафедри"=?
                        AND
                        code_year."роки"=?

                        LIMIT 1
                    """, (str(name), str(surname), str(patronymic), str(sign_of_madness), str(code), str(years)))
                    
                    if cursor.fetchone():
                        if name:
                            if sign_of_madness:
                                messagebox.showinfo("Попередження", f"Спроба занести людину {name} {surname} {patronymic} {sign_of_madness} ({code} {years}) двічі у файлі ({file_path}) .")
                            else:
                                messagebox.showinfo("Попередження", f"Спроба занести людину {name} {surname} {patronymic} ({code} {years}) двічі у файлі ({file_path}) .")
                        else:
                            if sign_of_madness:
                                messagebox.showinfo("Попередження", f"Спроба занести Вакансію {vacancy_number} {sign_of_madness} ({code} {years}) двічі у файлі ({file_path}) .")
                            else:
                                messagebox.showinfo("Попередження", f"Спроба занести Вакансію {vacancy_number} ({code} {years}) двічі у файлі ({file_path}) .")
                
                        continue

                else:
                    cursor.execute("""
                        SELECT 1

                        FROM code_year 
                         
                        JOIN job ON code_year.id = job."код_рік_id" 
                        JOIN vacancy ON job.id = vacancy."job_id" 
                         
                        WHERE
                        vacancy."назва"=?
                        AND
                        vacancy."номер"=?
                        AND
                        job."знак_сумісності"=?
                        AND
                        code_year."назва_кафедри"=?
                        AND
                        code_year."роки"=?

                        LIMIT 1
                    """, (str(vacancy), str(vacancy_number), str(sign_of_madness), str(code), str(years)))

                

                    if cursor.fetchone():
                        if name:
                            if sign_of_madness:
                                messagebox.showinfo("Попередження", f"Спроба занести людину {name} {surname} {patronymic} {sign_of_madness} ({code} {years}) двічі у файлі ({file_path}) .")
                            else:
                                messagebox.showinfo("Попередження", f"Спроба занести людину {name} {surname} {patronymic} ({code} {years}) двічі у файлі ({file_path}) .")
                        else:
                            if sign_of_madness:
                                messagebox.showinfo("Попередження", f"Спроба занести Вакансію {vacancy_number} {sign_of_madness} ({code} {years}) двічі у файлі ({file_path}) .")
                            else:
                                messagebox.showinfo("Попередження", f"Спроба занести Вакансію {vacancy_number} ({code} {years}) двічі у файлі ({file_path}) .")
                
                        continue

                try:

                    NPP_PP = get_cell_str(i+2,29).lower().replace(' ','')[:1]
                
                    if NPP_PP == "n" or NPP_PP == "н" or NPP_PP == "н":
                        NPP_PP = "НПП"
                    else:
                        NPP_PP = "ПП"
                except Exception:
                    NPP_PP = "ПП"

                cursor.execute("""
                    INSERT INTO job (
                    "посада", "код_рік_id", "вчене_звання_вчена_ступінь", "знак_сумісності", "НПП_ПП"
                    )
                    VALUES (?, ?, ?, ?,?)
                """, (str(position), int(str(code_years_id)), str(academic_title_academic_degree), str(sign_of_madness), str(NPP_PP)))

                job_id = cursor.lastrowid

                conn.commit()

                if name:
                    cursor.execute("""
                        INSERT INTO person (
                        "ім_я", "прізвище", "по-батькові", "job_id"
                        )
                        VALUES (?, ?, ?, ?)
                    """, (str(name), str(surname), str(patronymic), int(str(job_id))))

                else:
                    cursor.execute("""
                        INSERT INTO vacancy(
                        "назва", "номер", "job_id"
                        )
                        VALUES (?, ?, ?)
                    """, (str(vacancy), str(vacancy_number), int(str(job_id))))

                conn.commit()

                try:
                    bids = get_cell_str(i+2,28)
                    if bids == "nan":
                        bids = ""
                except Exception:
                    bid = ""
           

                first_year = ""
                second_year = ""

                for k, value in enumerate(years):

                    if value == '-':
                        k+=1

                        while k < len(years):
                            second_year += years[k]
                            k += 1
                        break

                    first_year += value
               

                from datetime import datetime

                first_semester_start = datetime.strptime(str("01.09."+first_year+" 00:00:00"), "%d.%m.%Y %H:%M:%S")
                first_semester_end = datetime.strptime(str("31.01."+second_year+" 23:59:59"), "%d.%m.%Y %H:%M:%S")

                second_semester_start = datetime.strptime(str("01.02."+second_year+" 00:00:00"), "%d.%m.%Y %H:%M:%S")
                second_semester_end = datetime.strptime(str("30.06."+second_year+" 23:59:59"), "%d.%m.%Y %H:%M:%S")

                class BIDS:
                    def __init__(self, bid, start, end):
                        self.bid = float(str(bid).replace(' ', ''))
                        self.start = datetime.strptime(str(start).replace(' ', ''), "%d.%m.%y")
                        self.end = datetime.strptime(str(end).replace(' ', ''), "%d.%m.%y")
                        if self.start < first_semester_start:
                            self.start = first_semester_start
                        if self.end > second_semester_end:
                            self.end = second_semester_end

                       
                    def __repr__(self):
                        return f"{self.bid} ({self.start.strftime('%d.%m.%y')}-{self.end.strftime('%d.%m.%y')})"

                    def monthes(self):  
                        return round(float((self.end - self.start).days / ((31+28+31+30+31+30+31+31+30+31+30+31)/12)),1)

                    def monthes_with_start(self,start):  
                        return round(float((self.end - start).days / ((31+28+31+30+31+30+31+31+30+31+30+31)/12)),1)

                    def monthes_with_end(self,end):
                        return round(float((end - self.start).days / ((31+28+31+30+31+30+31+31+30+31+30+31)/12)),1)
                        
                        


                bids = bids.replace(' ','').replace(',','.')
                bids_array=[]
                if bids:
                    index = 0
                    while True:
                        try:
                            bid = ""
                            start = ""
                            end = ""
                        
                            if index == len(bids)-1:
                                break
                            while bids[index] != "(":
                                bid += str(bids[index])
                                index += 1
                            index += 1
                            while bids[index] != "-":
                                start += str(bids[index])
                                index += 1
                            index += 1
                            while bids[index] != ")":
                                end += str(bids[index])
                                index += 1

                        
                            bids_array.append(BIDS(bid, start, end))
                        except Exception:
                            bids = ""
                            if name:
                                if sign_of_madness:
                                    messagebox.showinfo("Помилка", f"Помилка у форматі ставок у файлі:\n\n{file_path}.\n\nЛюдина: {name} {surname} {patronymic} ({sign_of_madness}).")
                                else:
                                    messagebox.showinfo("Помилка", f"Помилка у форматі ставок у файлі:\n\n{file_path}.\n\nЛюдина: {name} {surname} {patronymic} (несумісник).")
                            else:
                                if sign_of_madness:
                                    messagebox.showinfo("Помилка", f"Помилка у форматі ставок у файлі:\n\n{file_path}.\n\nВакансія: {vacancy_number} ({sign_of_madness}).")
                                else:
                                    messagebox.showinfo("Помилка", f"Помилка у форматі ставок у файлі:\n\n{file_path}.\n\nВакансія: {vacancy_number} (несумісник).")
                            break
                            

                        if index == len(bids)-1:
                            break
                        index += 1
                        if index == len(bids)-1:
                            break


                if bids:

                    academic_year_bid = 0

                    monthes = 0.0
                    mini_bid= 00.0

                    for value in bids_array:
                       mini_bid += (value.bid * value.monthes())
                       monthes += value.monthes()
                   
                    if monthes!=0:
                        academic_year_bid = round(float(mini_bid/monthes),2)
                   
               
                if bids:

                    first_semester_bid = 0.00
                    second_semester_bid = 0.00
                    
                    first_semester_monthes = 0.00
                    first_semester_mini_bid= 0.00

                    second_semester_monthes = 0.00
                    second_semester_mini_bid= 0.00

                    for value in bids_array:    
                        if value.start >= first_semester_start and value.end <= first_semester_end:
                            first_semester_mini_bid += (value.bid * value.monthes())
                            first_semester_monthes += value.monthes()
                        else:
                            if value.start >= first_semester_start and value.end >= second_semester_start and value.start < second_semester_start:
                                first_semester_mini_bid += (value.bid * value.monthes_with_end(first_semester_end))
                                first_semester_monthes += value.monthes_with_end(first_semester_end)

                                second_semester_mini_bid += (value.bid * value.monthes_with_start(second_semester_start))
                                second_semester_monthes += value.monthes_with_start(second_semester_start)

                            else:
                                second_semester_mini_bid += (value.bid * value.monthes())
                                second_semester_monthes += value.monthes()

                    if first_semester_monthes != 0:
                        first_semester_bid = round(float(first_semester_mini_bid/first_semester_monthes),2)
                    if second_semester_monthes != 0:
                        second_semester_bid = round(float(second_semester_mini_bid/second_semester_monthes),2)

                first_semester_numbers = get_cells_float(i)
                second_semester_numbers= get_cells_float(i+1)

                academic_year_numbers = []

                for k in range(len(first_semester_numbers)):
                    academic_year_numbers.append(first_semester_numbers[k]+second_semester_numbers[k])


                cursor.execute("""
                INSERT INTO first_semester(
                    "ставка",
                    "лекції",
                    "практичні_(семінарські)_заняття",
                    "лабораторні_роботи",
                    "екзамени",
                    "консультації_перед_екзаменами",
                    "заліки",
                    "кваліфікаційна_робота",
                    "атестаційний_екзамен",
                    "виробнича_практика",
                    "навчальна_практика",
                    "поточні_консультації",
                    "індивідуальні",
                    "курсові_роботи",
                    "аспірантські_екзамени",
                    "керівництво_аспірантами",
                    "консультування_докторантів_здобувачів",
                    "керівництво_ФПК",
                    "робота_приймальної_комісії",
                    "інше",
                    "всього",
                    "job_id"
                 )
                 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                 """,(str(first_semester_bid),
                    first_semester_numbers[0],
                    first_semester_numbers[1],
                    first_semester_numbers[2],
                    first_semester_numbers[3],
                    first_semester_numbers[4],
                    first_semester_numbers[5],
                    first_semester_numbers[6],
                    first_semester_numbers[7],
                    first_semester_numbers[8],
                    first_semester_numbers[9],
                    first_semester_numbers[10],
                    first_semester_numbers[11],
                    first_semester_numbers[12],
                    first_semester_numbers[13],
                    first_semester_numbers[14],
                    first_semester_numbers[15],
                    first_semester_numbers[16],
                    first_semester_numbers[17],
                    first_semester_numbers[18],
                    first_semester_numbers[19],
                    int(str(job_id))
                ))

                conn.commit()

                cursor.execute("""
                INSERT INTO second_semester (
                    "ставка",
                    "лекції",
                    "практичні_(семінарські)_заняття",
                    "лабораторні_роботи",
                    "екзамени",
                    "консультації_перед_екзаменами",
                    "заліки",
                    "кваліфікаційна_робота",
                    "атестаційний_екзамен",
                    "виробнича_практика",
                    "навчальна_практика",
                    "поточні_консультації",
                    "індивідуальні",
                    "курсові_роботи",
                    "аспірантські_екзамени",
                    "керівництво_аспірантами",
                    "консультування_докторантів_здобувачів",
                    "керівництво_ФПК",
                    "робота_приймальної_комісії",
                    "інше",
                    "всього",
                    "job_id"
                )
                 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                 """, (str(second_semester_bid),
                       second_semester_numbers[0],
                       second_semester_numbers[1],
                       second_semester_numbers[2],
                       second_semester_numbers[3],
                       second_semester_numbers[4],
                       second_semester_numbers[5],
                       second_semester_numbers[6],
                       second_semester_numbers[7],
                       second_semester_numbers[8],
                       second_semester_numbers[9],
                       second_semester_numbers[10],
                       second_semester_numbers[11],
                       second_semester_numbers[12],
                       second_semester_numbers[13],
                       second_semester_numbers[14],
                       second_semester_numbers[15],
                       second_semester_numbers[16],
                       second_semester_numbers[17],
                       second_semester_numbers[18],
                       second_semester_numbers[19],
                    int(job_id)
                ))

                conn.commit()

                cursor.execute("""
                    INSERT INTO academic_year (
                        "ставка",
                        "лекції",
                        "практичні_(семінарські)_заняття",
                        "лабораторні_роботи",
                        "екзамени",
                        "консультації_перед_екзаменами",
                        "заліки",
                        "кваліфікаційна_робота",
                        "атестаційний_екзамен",
                        "виробнича_практика",
                        "навчальна_практика",
                        "поточні_консультації",
                        "індивідуальні",
                        "курсові_роботи",
                        "аспірантські_екзамени",
                        "керівництво_аспірантами",
                        "консультування_докторантів_здобувачів",
                        "керівництво_ФПК",
                        "робота_приймальної_комісії",
                        "інше",
                        "всього",
                        "розподіл_ставок_навчального_навантаження",
                        "job_id"
                     )
                     VALUES (?, ?, ?,?, ?, ?,?, ?, ?,?, ?, ?,?, ?, ?,?, ?, ?,?, ?, ?,?,?)
                    """, (str(academic_year_bid),
                       academic_year_numbers[0],
                       academic_year_numbers[1],
                       academic_year_numbers[2],
                       academic_year_numbers[3],
                       academic_year_numbers[4],
                       academic_year_numbers[5],
                       academic_year_numbers[6],
                       academic_year_numbers[7],
                       academic_year_numbers[8],
                       academic_year_numbers[9],
                       academic_year_numbers[10],
                       academic_year_numbers[11],
                       academic_year_numbers[12],
                       academic_year_numbers[13],
                       academic_year_numbers[14],
                       academic_year_numbers[15],
                       academic_year_numbers[16],
                       academic_year_numbers[17],
                       academic_year_numbers[18],
                       academic_year_numbers[19],
                       str(bids),
                       int(job_id)
                    ))
                conn.commit()


            
        conn.close()
        root.after(0, loading.destroy)
        

    from src.settings.settings import loading_window
    from src.menus.main import main_menu

    files_path = filedialog.askopenfilenames(
        title="Оберіть Excel файл",
        filetypes=[("Excel Files", "*.xlsx")]
    )
    
    if not files_path:
        messagebox.showinfo("Помилка", "Файл не обрано або має валідну помилку в назві!")
        return

        

    loading = loading_window(root)
    threading.Thread(target=read_files, args=(root, name_db, files_path, loading), daemon=True).start()
   
    return