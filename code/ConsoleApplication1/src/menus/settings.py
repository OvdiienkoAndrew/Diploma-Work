import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import math



def settings_menu(root, name_db):

    from src.settings.settings import clear_window, on_enter, on_leave
    from src.data_base.error.check.main import check_db
    from src.menus.exit import on_escape
    from src.menus.main import main_menu
    from src.menus.error import errors_menu
    from src.menus.request import requests_menu

    class load:
        def __init__(self, name, npp_pp, value):
            self.__name = str(name)
            self.__npp_pp = str(npp_pp)
            self.__value = float(value)

        def get_name(self):
            return self.__name

        def get_npp_pp(self):
            return self.__npp_pp

        def get_value(self):
            return self.__value

        def __str__(self):
            return f"{self.__name} | {self.__npp_pp} | {self.__value}"


    class Paginator:
        def __init__(self, root, name_db,counter=10):

            self.__root = root

            self.__name_db = name_db

            self.__counter = counter
    
            self.__this_page=0


            self.__pages = 0

            self.__array = ["Середнє навантаження", "Максимум перевищення у %", "Максимум","Мінімум","Рівномірність розподілу","Керівники аспірантів"]

            self.update_page()

        def update_page(self):
            

            clear_window( self.__root)

            self.__root.bind("<Escape>", lambda event: on_escape(event,  self.__root, name_db))

    
            menubar = tk.Menu(self.__root)

            filemenu = tk.Menu(menubar, tearoff=0)
            filemenu.add_command(label="Головне меню", command=lambda: main_menu( self.__root, name_db))
            filemenu.add_command(label="Запити", command=lambda: requests_menu(self.__root, name_db))
            filemenu.add_separator()
            filemenu.add_command(label="Вихід", command=lambda: on_escape(None, self.__root, name_db))
   
            menubar.add_cascade(label="Файл", menu=filemenu)

            if check_db(self.__root, name_db):
                errormenu = tk.Menu(menubar, tearoff=0)
                errormenu.add_command(label="Помилки", command=lambda: errors_menu(self.__root, name_db))
                menubar.add_cascade(label="Помилки", menu=errormenu)

            self.__root.config(menu=menubar)


            button_add = tk.Button(self.__root, text="➕", bg="white", fg="black",bd=2, command=self.add)
            button_remove = tk.Button(self.__root, text="➖", bg="white", fg="black",bd=2, command=self.remove)
            button_edit = tk.Button(self.__root, text="✎", bg="white", fg="black",bd=2,  command=self.edit)


            button_next = tk.Button(self.__root, text=">", bg="white", fg="black",bd=2,  command=self.next_page)
            button_last = tk.Button(self.__root, text="<", bg="white", fg="black",bd=2, command=self.prev_page)

            button_save = tk.Button(self.__root, text=f"💾", bg="white",fg="black",bd=2,  command=lambda: self.save(array_load,[value.get() for value in entries]))

            self.__root.update()

            button_next.bind("<Enter>", on_enter)
            button_last.bind("<Enter>", on_enter)
            button_save.bind("<Enter>", on_enter)
            button_add.bind("<Enter>", on_enter)
            button_remove.bind("<Enter>", on_enter)
            button_edit.bind("<Enter>", on_enter)


            button_next.bind("<Leave>", on_leave)
            button_last.bind("<Leave>", on_leave)
            button_save.bind("<Leave>", on_leave)
            button_add.bind("<Leave>", on_leave)
            button_remove.bind("<Leave>", on_leave)
            button_edit.bind("<Leave>", on_leave)


            self.__root.update()

            array_load = []

            conn = sqlite3.connect(self.__name_db)
            cursor = conn.cursor()

            cursor.execute("""
                SELECT name, npp_pp, value
                FROM load
                ORDER BY npp_pp, name
            """, ())

            results = [[str(value[0]), str(value[1]), float(value[2])] for value in cursor.fetchall()]

            conn.close()

            
            for value  in results:
                array_load.append(load(value[0], value[1], value[2]))

            self.__pages = math.ceil(len(array_load)/self.__counter)

            while self.__this_page>=self.__pages:
                self.__this_page -= 1

            labels = []
            entries = []

            for i,value  in enumerate(array_load):
                labels.append(tk.Label(self.__root, text=f"{value.get_name()} ({value.get_npp_pp()})", font=("Times New Roman", 32), bg="white", fg="black", bd=4, relief="solid"))
                entries.append(tk.Entry(root,  font=("Times New Roman", 32), bg="white", fg="black", bd=4))
                labels[i].place(x=0,y=-100)
                entries[i].place(x=0,y=-100,width=int(self.__root.winfo_width()/4))
                entries[i].insert(0, value.get_value())
                
            self.__root.update()

            start = self.__this_page * self.__counter

            empty_height = self.__root.winfo_height()

            j=0
            for i,value in enumerate(labels,start = start):
                empty_height -= labels[i].winfo_height()
                j+=1
                if j==9 or i+1 == len(labels):
                    break

            empty_height /= (j+1)


            j = 1
            for i,value in enumerate(labels,start = start):
                labels[i].place(x=10,y=empty_height*j + (j-1)*labels[0].winfo_height())
                entries[i].place(x=self.__root.winfo_width()/2 + self.__root.winfo_width()/4 - entries[i].winfo_width()/2,y=empty_height*j + (j-1)*labels[0].winfo_height())
                j += 1
                if i == start + 8 or i+1 == len(labels):
                    break

            self.__root.update()

            button_add.place(x=10,y=empty_height/4, width=empty_height/2, height=empty_height/2)
            button_remove.place(x=20 + empty_height/2 ,y=empty_height/4, width=empty_height/2, height=empty_height/2)
            button_edit.place(x=30 + empty_height,y=empty_height/4, width=empty_height/2, height=empty_height/2)

            button_last.place(x=10, y=self.__root.winfo_height() - empty_height*3/4, width=empty_height/2, height=empty_height/2)
            button_next.place(x=self.__root.winfo_width() - empty_height/2 - 10, y=self.__root.winfo_height() - empty_height*3/4, width=empty_height/2, height=empty_height/2)
            button_save.place(x=self.__root.winfo_width() - empty_height/2 - 10, y = 10, width=empty_height/2, height=empty_height/2)
            
            self.__root.update()

       

        def next_page(self):
            self.__this_page += 1
            if self.__this_page >= self.__pages:
                self.__this_page -= 1
            self.update_page()

        def prev_page(self):
            self.__this_page -= 1
            if self.__this_page < 0:
                self.__this_page = 0
            self.update_page()

        def save(self,load,entries):
            conn = sqlite3.connect(self.__name_db)
            cursor = conn.cursor()

            for i,value in enumerate(entries):
                try:
                    value = float(str(value).lower().replace(' ','').replace(',','.'))
                    if value <0:
                        messagebox.showerror("Помилка", f"Кіькість годин повинна бути невід'ємна ({load[i].get_name()} ({load[i].get_npp_pp()}))!")
                        conn.close()
                        return
                except Exception:
                    messagebox.showerror("Помилка", f"Кіькість годин повинно бути числом ({load[i].get_name()} ({load[i].get_npp_pp()}))!")
                    conn.close()
                    return

                cursor.execute("UPDATE load SET value = ? WHERE name = ? AND npp_pp = ?", (value,str(load[i].get_name()),str(load[i].get_npp_pp())))

                conn.commit()

            conn.close()
            messagebox.showinfo("Успіх", "Зміни збережено!")
           


        def add(self):
            clear_window( self.__root)

            self.__root.bind("<Escape>", lambda event: on_escape(event,  self.__root, name_db))

    
            menubar = tk.Menu(self.__root)

            filemenu = tk.Menu(menubar, tearoff=0)
            filemenu.add_command(label="Головне меню", command=lambda: main_menu( self.__root, name_db))
            filemenu.add_command(label="Налаштування", command=lambda: settings_menu(root, name_db))
            filemenu.add_command(label="Запити", command=lambda: requests_menu(self.__root, name_db))
            filemenu.add_separator()
            filemenu.add_command(label="Вихід", command=lambda: on_escape(None, self.__root, name_db))
   
            menubar.add_cascade(label="Файл", menu=filemenu)

            if check_db(self.__root, name_db):
                errormenu = tk.Menu(menubar, tearoff=0)
                errormenu.add_command(label="Помилки", command=lambda: errors_menu(self.__root, name_db))
                menubar.add_cascade(label="Помилки", menu=errormenu)

            self.__root.config(menu=menubar)

            label_name = tk.Label(self.__root, text="Назва:", font=("Times New Roman", 32), bg="white", fg="black", bd=4, relief="solid")
            entry_name = tk.Entry(self.__root,  font=("Times New Roman", 32), bg="white", fg="black", bd=4)
            label_npp_pp = tk.Label(self.__root, text="НПП ПП:", font=("Times New Roman", 32), bg="white", fg="black", bd=4, relief="solid")
            entry_npp_pp = ttk.Combobox(
                self.__root,
                font=("Times New Roman", 32),
                values=["ПП", "НПП"],
                state="readonly"
            )
            entry_npp_pp.current(0) 
            label_value = tk.Label(self.__root, text="Кількість годин:", font=("Times New Roman", 32), bg="white", fg="black", bd=4, relief="solid")
            entry_value = tk.Entry(self.__root,  font=("Times New Roman", 32), bg="white", fg="black", bd=4)
            button_save = tk.Button(self.__root, text="💾", bg="white",fg="black",bd=2, command=lambda: self.add_new(entry_name.get(), entry_npp_pp.get(), entry_value.get()))
            
            self.__root.update()

            label_name.place(x=0,y=0)
            entry_name.place(x=0,y=0)

            label_npp_pp.place(x=0,y=0)
            entry_npp_pp.place(x=0,y=0)

            label_value.place(x=0,y=0)
            entry_value.place(x=0,y=0)

            button_save.place(x=0,y=0)
            
            self.__root.update()
           

            button_save.bind("<Enter>", on_enter)
            button_save.bind("<Leave>", on_leave)

            self.__root.update()

            empty_height = self.__root.winfo_height()

            empty_height -= (max(label_name.winfo_height(),entry_name.winfo_height()) + button_save.winfo_height() + max(label_value.winfo_height(),entry_value.winfo_height()) + max(label_npp_pp.winfo_height(),entry_npp_pp.winfo_height())) 

            empty_height/=5


            empty_width = (self.__root.winfo_width() - (max(label_name.winfo_width(),label_npp_pp.winfo_width(),label_value.winfo_width())+max(entry_name.winfo_width(),entry_npp_pp.winfo_width(),entry_value.winfo_width()) ))/3



            label_name.place(x=empty_width ,y=empty_height)
            entry_name.place(x=empty_width*2 + max(label_name.winfo_width(),label_npp_pp.winfo_width(),label_value.winfo_width()),y=empty_height, width=int(self.__root.winfo_width()/4))

            label_npp_pp.place(x=empty_width ,y=2*empty_height + max(label_name.winfo_height(),entry_name.winfo_height()))
            entry_npp_pp.place(x=empty_width*2 + max(label_name.winfo_width(),label_npp_pp.winfo_width(),label_value.winfo_width()),y=2*empty_height + max(label_name.winfo_height(),entry_name.winfo_height()), width=int(self.__root.winfo_width()/4))

            label_value.place(x=empty_width ,y=3*empty_height + max(label_name.winfo_height(),entry_name.winfo_height()) + max(label_npp_pp.winfo_height(),entry_npp_pp.winfo_height()))
            entry_value.place(x=empty_width*2 + max(label_name.winfo_width(),label_npp_pp.winfo_width(),label_value.winfo_width()),y=3*empty_height + max(label_name.winfo_height(),entry_name.winfo_height()) + max(label_npp_pp.winfo_height(),entry_npp_pp.winfo_height()), width=int(self.__root.winfo_width()/4))


            button_save.place(x= (self.__root.winfo_width()-button_save.winfo_width())/2 ,y=4*empty_height + max(label_value.winfo_height(),entry_value.winfo_height()) + max(label_name.winfo_height(),entry_name.winfo_height()) + max(label_npp_pp.winfo_height(),entry_npp_pp.winfo_height()))

            self.__root.update()

        def add_new(self, entry_name, entry_npp_pp, entry_value):
            entry_name = str(entry_name).strip()

            if entry_name == "" or entry_value == "":
                messagebox.showerror("Помилка", "Всі поля повинні бути заповнені!")
                return

            if len(entry_name) >= 31:
                messagebox.showerror("Помилка", "Назва має бути менша ніж 31 символ!")
                return

            if '{' in entry_name and '}' in entry_name:
                messagebox.showerror("Помилка", "Назва не повинна містити символи: \'{\', \'}\'!")
                return

            if '{' in entry_name:
                messagebox.showerror("Помилка", "Назва не повинна містити символ: \'{\'!")
                return

            if '}' in entry_name:
                messagebox.showerror("Помилка", "Назва не повинна містити символ: \'}\'!")
                return

            entry_value = entry_value.replace(',','.').lower().replace(' ','')

            try:
                entry_value = float(entry_value)
            except:
                messagebox.showerror("Помилка", "Кіькість годин повинно бути числом!")
                return

            if entry_value <0:
                messagebox.showerror("Помилка", "Кіькість годин повинна бути невід'ємна!")
                return

            conn = sqlite3.connect(self.__name_db)
            cursor = conn.cursor()

            cursor.execute("""
                SELECT 1
                FROM load
                WHERE name = ? AND npp_pp = ?
                LIMIT 1
                
            """, (entry_name,entry_npp_pp))

            if cursor.fetchall():
                conn.close()
                messagebox.showerror("Помилка", f"{entry_name} ({entry_npp_pp}) вже існує!")
                return

            if entry_name in self.__array:
                text = f"{entry_name} ({entry_npp_pp}) - це одне з особливих імен, яке вже існує!\n\nВи не можете: додати, змінити, видалити - наступні назви:"
                for value in self.__array:
                    text += f"\n\t{value}"
                messagebox.showerror("Помилка", text)
                return



            cursor.execute("INSERT INTO load (name, npp_pp, value) VALUES (?, ?, ?)", (str(entry_name), str(entry_npp_pp), float(entry_value)))
            self.__this_page = 0
            conn.commit()

            conn.close()

            self.update_page()
           
        def remove(self):
            clear_window( self.__root)

            self.__root.bind("<Escape>", lambda event: on_escape(event,  self.__root, name_db))

    
            menubar = tk.Menu(self.__root)

            filemenu = tk.Menu(menubar, tearoff=0)
            filemenu.add_command(label="Головне меню", command=lambda: main_menu( self.__root, name_db))
            filemenu.add_command(label="Налаштування", command=lambda: settings_menu(root, name_db))
            filemenu.add_command(label="Запити", command=lambda: requests_menu(self.__root, name_db))
            filemenu.add_separator()
            filemenu.add_command(label="Вихід", command=lambda: on_escape(None, self.__root, name_db))
   
            menubar.add_cascade(label="Файл", menu=filemenu)

            if check_db(self.__root, name_db):
                errormenu = tk.Menu(menubar, tearoff=0)
                errormenu.add_command(label="Помилки", command=lambda: errors_menu(self.__root, name_db))
                menubar.add_cascade(label="Помилки", menu=errormenu)

            self.__root.config(menu=menubar)

            conn = sqlite3.connect(self.__name_db)
            cursor = conn.cursor()

            placeholders = ','.join('?' for _ in self.__array)
            sql = f"SELECT name, npp_pp, value FROM load WHERE name NOT IN ({placeholders}) ORDER BY npp_pp, name"
            cursor.execute(sql, self.__array)

            results =  cursor.fetchall()
            conn.close()
            

            label= tk.Label(self.__root, text="Оберіть елемент, який бажаєте видалити:", font=("Times New Roman", 32), bg="white", fg="black", bd=4, relief="solid")
            

            entries = ttk.Combobox(
                self.__root,
                font=("Times New Roman", 32),
                values=[ f"{value[0]} {{{value[1]}}} - {value[2]} годин." for value in results],
                state="readonly"
            )

            button_save = tk.Button(self.__root, text="💾", bg="white",fg="black",bd=2, command=lambda: self.remove_old(entries.get()))
            
            self.__root.update()
            button_save.bind("<Enter>", on_enter)
            button_save.bind("<Leave>", on_leave)

            entries.current(0)

            self.__root.update()

            entries.place(x=0,y=0,width=int(self.__root.winfo_width()*3/4))
            label.place(x=0,y=0)
            button_save.place(x=0,y=0)

            self.__root.update()

            empty_height = (self.__root.winfo_height() - (entries.winfo_height() + label.winfo_height() + button_save.winfo_height()))/4

            label.place(x=(self.__root.winfo_width() - label.winfo_width())/2,y=empty_height)
            entries.place(x=(self.__root.winfo_width() - entries.winfo_width())/2,y=empty_height*2+label.winfo_height())
            button_save.place(x=(self.__root.winfo_width() - button_save.winfo_width())/2,y=empty_height*3+label.winfo_height() + entries.winfo_height())

            self.__root.update()

        def remove_old(self, entries):
            name = entries.split(" {")[0]
            npp_pp = entries.split("{")[1].split("}")[0]
            
            conn = sqlite3.connect(self.__name_db)
            cursor = conn.cursor()

            cursor.execute("""
                DELETE
                FROM load
                WHERE name = ? AND npp_pp = ?
            """, (str(name),str(npp_pp)))

            conn.commit()
         
            conn.close()
            self.__this_page = 0
            self.update_page()

        def edit(self):
            clear_window( self.__root)

            self.__root.bind("<Escape>", lambda event: on_escape(event,  self.__root, name_db))

    
            menubar = tk.Menu(self.__root)

            filemenu = tk.Menu(menubar, tearoff=0)
            filemenu.add_command(label="Головне меню", command=lambda: main_menu( self.__root, name_db))
            filemenu.add_command(label="Налаштування", command=lambda: settings_menu(root, name_db))
            filemenu.add_command(label="Запити", command=lambda: requests_menu(self.__root, name_db))
            filemenu.add_separator()
            filemenu.add_command(label="Вихід", command=lambda: on_escape(None, self.__root, name_db))
   
            menubar.add_cascade(label="Файл", menu=filemenu)

            if check_db(self.__root, name_db):
                errormenu = tk.Menu(menubar, tearoff=0)
                errormenu.add_command(label="Помилки", command=lambda: errors_menu(self.__root, name_db))
                menubar.add_cascade(label="Помилки", menu=errormenu)

            self.__root.config(menu=menubar)

            conn = sqlite3.connect(self.__name_db)
            cursor = conn.cursor()

            placeholders = ','.join(['?'] * len(self.__array)) 
            sql = f"SELECT name, npp_pp, value FROM load  WHERE name NOT IN ({placeholders}) ORDER BY npp_pp, name"
            cursor.execute(sql, (self.__array))

            results =  cursor.fetchall()
            conn.close()
            

            label= tk.Label(self.__root, text="Оберіть елемент, який бажаєте редагувати:", font=("Times New Roman", 32), bg="white", fg="black", bd=4, relief="solid")
            

            entries = ttk.Combobox(
                self.__root,
                font=("Times New Roman", 32),
                values=[ f"{value[0]} {{{value[1]}}} - {value[2]} годин." for value in results],
                state="readonly"
            )

            button_save = tk.Button(self.__root, text="💾", bg="white",fg="black",bd=2, command=lambda: self.edit_old(entries.get()))
            
            self.__root.update()
            button_save.bind("<Enter>", on_enter)
            button_save.bind("<Leave>", on_leave)

            entries.current(0)

            self.__root.update()

            entries.place(x=0,y=0,width=int(self.__root.winfo_width()*3/4))
            label.place(x=0,y=0)
            button_save.place(x=0,y=0)

            self.__root.update()

            empty_height = (self.__root.winfo_height() - (entries.winfo_height() + label.winfo_height() + button_save.winfo_height()))/4

            label.place(x=(self.__root.winfo_width() - label.winfo_width())/2,y=empty_height)
            entries.place(x=(self.__root.winfo_width() - entries.winfo_width())/2,y=empty_height*2+label.winfo_height())
            button_save.place(x=(self.__root.winfo_width() - button_save.winfo_width())/2,y=empty_height*3+label.winfo_height() + entries.winfo_height())

            self.__root.update()
    
        def edit_old(self, entries):
            name = entries.split(" {")[0]
            npp_pp = entries.split("{")[1].split("}")[0]

            conn = sqlite3.connect(self.__name_db)
            cursor = conn.cursor()

            cursor.execute("""
                SELECT id, value
                FROM load
                WHERE name = ? AND npp_pp = ?
                LIMIT 1
            """, (str(name),str(npp_pp)))

            rsults = cursor.fetchall()
            conn.close()

            this_id = int(rsults[0][0])
            value = float(rsults[0][1])

            clear_window( self.__root)

            self.__root.bind("<Escape>", lambda event: on_escape(event,  self.__root, name_db))

    
            menubar = tk.Menu(self.__root)

            filemenu = tk.Menu(menubar, tearoff=0)
            filemenu.add_command(label="Головне меню", command=lambda: main_menu( self.__root, name_db))
            filemenu.add_command(label="Налаштування", command=lambda: settings_menu(root, name_db))
            filemenu.add_command(label="Запити", command=lambda: requests_menu(self.__root, name_db))
            filemenu.add_separator()
            filemenu.add_command(label="Вихід", command=lambda: on_escape(None, self.__root, name_db))
   
            menubar.add_cascade(label="Файл", menu=filemenu)

            if check_db(self.__root, name_db):
                errormenu = tk.Menu(menubar, tearoff=0)
                errormenu.add_command(label="Помилки", command=lambda: errors_menu(self.__root, name_db))
                menubar.add_cascade(label="Помилки", menu=errormenu)

            self.__root.config(menu=menubar)

            text_name = tk.StringVar()
            text_value = tk.StringVar()

            text_name.set(name)
            text_value.set(value)
            
            label_name = tk.Label(self.__root, text="Назва:", font=("Times New Roman", 32), bg="white", fg="black", bd=4, relief="solid")
            entry_name = tk.Entry(self.__root,  font=("Times New Roman", 32), bg="white", fg="black", bd=4, textvariable=text_name)
            if name in self.__array:
                entry_name = tk.Label(self.__root, text=name, font=("Times New Roman", 32), bg="white", fg="black", bd=4, relief="solid")
            
            label_npp_pp = tk.Label(self.__root, text="НПП ПП:", font=("Times New Roman", 32), bg="white", fg="black", bd=4, relief="solid")
           
            entry_npp_pp = ttk.Combobox(
                self.__root,
                font=("Times New Roman", 32),
                values=["ПП", "НПП"],
                state="readonly"
            )

            if npp_pp == "ПП":
                entry_npp_pp.current(0)
            else:
                entry_npp_pp.current(1)

            label_value = tk.Label(self.__root, text="Кількість годин:", font=("Times New Roman", 32), bg="white", fg="black", bd=4, relief="solid")
            entry_value = tk.Entry(self.__root,  font=("Times New Roman", 32), bg="white", fg="black", bd=4, textvariable=text_value)
            if name in self.__array:
                button_save = tk.Button(self.__root, text="💾", bg="white",fg="black",bd=2, command=lambda: self.update_old(this_id, entry_name.cget("text"), entry_npp_pp.get(), entry_value.get()))
            else:
                button_save = tk.Button(self.__root, text="💾", bg="white",fg="black",bd=2, command=lambda: self.update_old(this_id, entry_name.get(), entry_npp_pp.get(), entry_value.get()))
            
            self.__root.update()

            label_name.place(x=0,y=0)
            entry_name.place(x=0,y=0)

            label_npp_pp.place(x=0,y=0)
            entry_npp_pp.place(x=0,y=0)

            label_value.place(x=0,y=0)
            entry_value.place(x=0,y=0)

            button_save.place(x=0,y=0)
            
            self.__root.update()

            empty_height = self.__root.winfo_height()

            empty_height -= (max(label_name.winfo_height(),entry_name.winfo_height()) + button_save.winfo_height() + max(label_value.winfo_height(),entry_value.winfo_height()) + max(label_npp_pp.winfo_height(),entry_npp_pp.winfo_height())) 

            empty_height/=5


            empty_width = (self.__root.winfo_width() - (max(label_name.winfo_width(),label_npp_pp.winfo_width(),label_value.winfo_width())+max(entry_name.winfo_width(),entry_npp_pp.winfo_width(),entry_value.winfo_width()) ))/3



            label_name.place(x=empty_width ,y=empty_height)
            entry_name.place(x=empty_width*2 + max(label_name.winfo_width(),label_npp_pp.winfo_width(),label_value.winfo_width()),y=empty_height, width=int(self.__root.winfo_width()/3))

            label_npp_pp.place(x=empty_width ,y=2*empty_height + max(label_name.winfo_height(),entry_name.winfo_height()))
            entry_npp_pp.place(x=empty_width*2 + max(label_name.winfo_width(),label_npp_pp.winfo_width(),label_value.winfo_width()),y=2*empty_height + max(label_name.winfo_height(),entry_name.winfo_height()), width=int(self.__root.winfo_width()/3))

            label_value.place(x=empty_width ,y=3*empty_height + max(label_name.winfo_height(),entry_name.winfo_height()) + max(label_npp_pp.winfo_height(),entry_npp_pp.winfo_height()))
            entry_value.place(x=empty_width*2 + max(label_name.winfo_width(),label_npp_pp.winfo_width(),label_value.winfo_width()),y=3*empty_height + max(label_name.winfo_height(),entry_name.winfo_height()) + max(label_npp_pp.winfo_height(),entry_npp_pp.winfo_height()), width=int(self.__root.winfo_width()/3))


            button_save.place(x= (self.__root.winfo_width()-button_save.winfo_width())/2 ,y=4*empty_height + max(label_value.winfo_height(),entry_value.winfo_height()) + max(label_name.winfo_height(),entry_name.winfo_height()) + max(label_npp_pp.winfo_height(),entry_npp_pp.winfo_height()))

            self.__root.update()

            
        def update_old(self, this_id, entry_name, entry_npp_pp, entry_value):

            entry_name = str(entry_name).strip()

            if entry_name == "" or entry_value == "":
                messagebox.showerror("Помилка", "Всі поля повинні бути заповнені!")
                return

            if len(entry_name) >= 31:
                messagebox.showerror("Помилка", "Назва має бути менша ніж 31 символ!")
                return


            if '{' in entry_name and '}' in entry_name:
                messagebox.showerror("Помилка", "Назва не повинна містити символи: \'{\', \'}\'!")
                return

            if '{' in entry_name:
                messagebox.showerror("Помилка", "Назва не повинна містити символ: \'{\'!")
                return

            if '}' in entry_name:
                messagebox.showerror("Помилка", "Назва не повинна містити символ: \'}\'!")
                return

            entry_value = entry_value.replace(',','.').lower().replace(' ','')

            try:
                entry_value = float(entry_value)
            except:
                messagebox.showerror("Помилка", "Кіькість годин повинно бути числом!")
                return

             
            if entry_value <0:
                messagebox.showerror("Помилка", "Кіькість годин повинна бути невід'ємна!")
                return

           



            conn = sqlite3.connect(self.__name_db)
            cursor = conn.cursor()

       
            cursor.execute("""
                SELECT 1
                FROM load
                WHERE name = ? AND npp_pp = ?
                LIMIT 1
                
            """, (entry_name,entry_npp_pp))

            if cursor.fetchall():
                conn.close()
                messagebox.showerror("Помилка", f"{entry_name} ({entry_npp_pp}) вже існує!")
                return
            

           

            cursor.execute("UPDATE load SET name = ?, npp_pp = ?, value = ? WHERE id = ?", (str(entry_name), str(entry_npp_pp), float(entry_value), int(this_id)))
            self.__this_page = 0
            conn.commit()

            conn.close()

            self.update_page()
            


    Paginator(root, name_db)

   

