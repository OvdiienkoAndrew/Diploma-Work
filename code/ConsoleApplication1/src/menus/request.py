# -*- coding: utf-8 -*-

import sqlite3
import tkinter as tk
from tkinter import font
import threading
from tkinter import messagebox
import pyperclip

from tkinter import font 
def requests_menu(root, name_db):
   
    from src.settings.settings import clear_window, on_enter, on_leave

    from src.data_base.error.check.main import check_db

    from src.menus.exit import on_escape

    from src.menus.main import main_menu

    from src.menus.main import main_menu

    from src.menus.error import errors_menu
    from src.menus.settings import settings_menu

    from src.settings.settings import loading_window

    def on_main_npp_button_click(root, name_db):
        def work(root, name_db, loading):

            conn = sqlite3.connect(name_db)
            cursor = conn.cursor()

            cursor.execute("""
                SELECT

                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN first_semester."всього" != 0 AND first_semester."ставка" != 0
                                    THEN first_semester."всього"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN first_semester."всього" != 0 AND first_semester."ставка" != 0
                                        THEN first_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2),

                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN second_semester."всього" != 0 AND second_semester."ставка" != 0
                                    THEN second_semester."всього"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN second_semester."всього" != 0 AND second_semester."ставка" != 0
                                        THEN second_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2),
 
                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN academic_year."всього" != 0 AND academic_year."ставка" != 0
                                    THEN academic_year."всього"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN academic_year."всього" != 0 AND academic_year."ставка" != 0
                                        THEN academic_year."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2)
                
                FROM job

                JOIN code_year ON job."код_рік_id" = code_year.id
                JOIN first_semester ON job.id = first_semester."job_id"
                JOIN second_semester ON job.id = second_semester."job_id"
                JOIN academic_year ON job.id = academic_year."job_id"

                WHERE job.НПП_ПП = 'НПП'

                UNION ALL

                SELECT

                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN first_semester."всього" != 0 AND first_semester."ставка" != 0
                                    THEN first_semester."всього"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN first_semester."всього" != 0 AND first_semester."ставка" != 0
                                        THEN first_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2),

                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN second_semester."всього" != 0 AND second_semester."ставка" != 0
                                    THEN second_semester."всього"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN second_semester."всього" != 0 AND second_semester."ставка" != 0
                                        THEN second_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2),
 
                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN academic_year."всього" != 0 AND academic_year."ставка" != 0
                                    THEN academic_year."всього"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN academic_year."всього" != 0 AND academic_year."ставка" != 0
                                        THEN academic_year."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2)
                
                FROM job

                JOIN code_year ON job."код_рік_id" = code_year.id
                JOIN first_semester ON job.id = first_semester."job_id"
                JOIN second_semester ON job.id = second_semester."job_id"
                JOIN academic_year ON job.id = academic_year."job_id"

                WHERE job.НПП_ПП = 'НПП' AND job.'посада' = 'заф. кафедри'
                
                UNION ALL

                SELECT

                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN first_semester."всього" != 0 AND first_semester."ставка" != 0
                                    THEN first_semester."всього"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN first_semester."всього" != 0 AND first_semester."ставка" != 0
                                        THEN first_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2),

                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN second_semester."всього" != 0 AND second_semester."ставка" != 0
                                    THEN second_semester."всього"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN second_semester."всього" != 0 AND second_semester."ставка" != 0
                                        THEN second_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2),
 
                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN academic_year."всього" != 0 AND academic_year."ставка" != 0
                                    THEN academic_year."всього"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN academic_year."всього" != 0 AND academic_year."ставка" != 0
                                        THEN academic_year."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2)
                
                FROM job

                JOIN code_year ON job."код_рік_id" = code_year.id
                JOIN first_semester ON job.id = first_semester."job_id"
                JOIN second_semester ON job.id = second_semester."job_id"
                JOIN academic_year ON job.id = academic_year."job_id"

                WHERE job.НПП_ПП = 'НПП' AND job.'посада' = 'професор'

                UNION ALL

                SELECT

                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN first_semester."всього" != 0 AND first_semester."ставка" != 0
                                    THEN first_semester."всього"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN first_semester."всього" != 0 AND first_semester."ставка" != 0
                                        THEN first_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2),

                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN second_semester."всього" != 0 AND second_semester."ставка" != 0
                                    THEN second_semester."всього"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN second_semester."всього" != 0 AND second_semester."ставка" != 0
                                        THEN second_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2),
 
                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN academic_year."всього" != 0 AND academic_year."ставка" != 0
                                    THEN academic_year."всього"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN academic_year."всього" != 0 AND academic_year."ставка" != 0
                                        THEN academic_year."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2)
                
                FROM job

                JOIN code_year ON job."код_рік_id" = code_year.id
                JOIN first_semester ON job.id = first_semester."job_id"
                JOIN second_semester ON job.id = second_semester."job_id"
                JOIN academic_year ON job.id = academic_year."job_id"

                WHERE job.НПП_ПП = 'НПП' AND job.'посада' = 'доцент'

                UNION ALL

                SELECT

                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN first_semester."всього" != 0 AND first_semester."ставка" != 0
                                    THEN first_semester."всього"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN first_semester."всього" != 0 AND first_semester."ставка" != 0
                                        THEN first_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2),

                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN second_semester."всього" != 0 AND second_semester."ставка" != 0
                                    THEN second_semester."всього"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN second_semester."всього" != 0 AND second_semester."ставка" != 0
                                        THEN second_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2),
 
                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN academic_year."всього" != 0 AND academic_year."ставка" != 0
                                    THEN academic_year."всього"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN academic_year."всього" != 0 AND academic_year."ставка" != 0
                                        THEN academic_year."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2)
                
                FROM job

                JOIN code_year ON job."код_рік_id" = code_year.id
                JOIN first_semester ON job.id = first_semester."job_id"
                JOIN second_semester ON job.id = second_semester."job_id"
                JOIN academic_year ON job.id = academic_year."job_id"

                WHERE job.НПП_ПП = 'НПП' AND job.'посада' = 'ст. викладач'

                UNION ALL

                SELECT

                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN first_semester."всього" != 0 AND first_semester."ставка" != 0
                                    THEN first_semester."всього"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN first_semester."всього" != 0 AND first_semester."ставка" != 0
                                        THEN first_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2),

                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN second_semester."всього" != 0 AND second_semester."ставка" != 0
                                    THEN second_semester."всього"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN second_semester."всього" != 0 AND second_semester."ставка" != 0
                                        THEN second_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2),
 
                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN academic_year."всього" != 0 AND academic_year."ставка" != 0
                                    THEN academic_year."всього"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN academic_year."всього" != 0 AND academic_year."ставка" != 0
                                        THEN academic_year."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2)
                
                FROM job

                JOIN code_year ON job."код_рік_id" = code_year.id
                JOIN first_semester ON job.id = first_semester."job_id"
                JOIN second_semester ON job.id = second_semester."job_id"
                JOIN academic_year ON job.id = academic_year."job_id"

                WHERE job.НПП_ПП = 'НПП' AND job.'посада' = 'асистент'

                UNION ALL

                SELECT

                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN first_semester."всього" != 0 AND first_semester."ставка" != 0
                                    THEN first_semester."всього"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN first_semester."всього" != 0 AND first_semester."ставка" != 0
                                        THEN first_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2),

                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN second_semester."всього" != 0 AND second_semester."ставка" != 0
                                    THEN second_semester."всього"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN second_semester."всього" != 0 AND second_semester."ставка" != 0
                                        THEN second_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2),
 
                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN academic_year."всього" != 0 AND academic_year."ставка" != 0
                                    THEN academic_year."всього"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN academic_year."всього" != 0 AND academic_year."ставка" != 0
                                        THEN academic_year."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2)
                
                FROM job

                JOIN code_year ON job."код_рік_id" = code_year.id
                JOIN first_semester ON job.id = first_semester."job_id"
                JOIN second_semester ON job.id = second_semester."job_id"
                JOIN academic_year ON job.id = academic_year."job_id"

                WHERE job.НПП_ПП = 'НПП' AND job.'посада' = 'в.о. заф. кафедри'

                UNION ALL

                SELECT

                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN first_semester."всього" != 0 AND first_semester."ставка" != 0
                                    THEN first_semester."всього"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN first_semester."всього" != 0 AND first_semester."ставка" != 0
                                        THEN first_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2),

                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN second_semester."всього" != 0 AND second_semester."ставка" != 0
                                    THEN second_semester."всього"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN second_semester."всього" != 0 AND second_semester."ставка" != 0
                                        THEN second_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2),
 
                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN academic_year."всього" != 0 AND academic_year."ставка" != 0
                                    THEN academic_year."всього"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN academic_year."всього" != 0 AND academic_year."ставка" != 0
                                        THEN academic_year."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2)
                
                FROM job

                JOIN code_year ON job."код_рік_id" = code_year.id
                JOIN first_semester ON job.id = first_semester."job_id"
                JOIN second_semester ON job.id = second_semester."job_id"
                JOIN academic_year ON job.id = academic_year."job_id"

                WHERE job.'НПП_ПП' = 'НПП' AND job.'посада' = 'викладач'
                
            """)
            

            result = []
            for value in cursor.fetchall():
                result.append((value[0],value[1],value[2]))
            
            msg = ""
            msg += f"Середнє навантаження НПП (заф. кафедри)\n\t перший семестр: {result[1][0]}\n\t другий семестр: {result[1][1]}\n\t рік: {result[1][2]}\n\n"
            msg += f"Середнє навантаження НПП (професор)\n\t перший семестр: {result[2][0]}\n\t другий семестр: {result[2][1]}\n\t рік: {result[2][2]}\n\n"
            msg += f"Середнє навантаження НПП (доцент)\n\t перший семестр: {result[3][0]}\n\t другий семестр: {result[3][1]}\n\t рік: {result[3][2]}\n\n"
            msg += f"Середнє навантаження НПП (ст. викладач)\n\t перший семестр: {result[4][0]}\n\t другий семестр: {result[4][1]}\n\t рік: {result[4][2]}\n\n"
            msg += f"Середнє навантаження НПП (асистент)\n\t перший семестр: {result[5][0]}\n\t другий семестр: {result[5][1]}\n\t рік: {result[5][2]}\n\n"
            msg += f"Середнє навантаження НПП (в.о. заф. кафедри)\n\t перший семестр: {result[6][0]}\n\t другий семестр: {result[6][1]}\n\t рік: {result[6][2]}\n\n"
            msg += f"Середнє навантаження НПП (викладач)\n\t перший семестр: {result[7][0]}\n\t другий семестр: {result[7][1]}\n\t рік: {result[7][2]}\n\n"
            msg += f"Середнє навантаження НПП (усі)\n\t перший семестр: {result[0][0]}\n\t другий семестр: {result[0][1]}\n\t рік: {result[0][2]}\n\n"

            with open("resources\\Середнэ навантаження\\НПП\\Загальне\\file.txt", "w", encoding="utf-8") as f:
                f.write(msg)

            msg = "Дані збереженно у файлі: \"resources\\Середнэ навантаження\\НПП\\Загальне\\file.txt\".\n\n\n" + msg
            msg += "\n\n\nКлацніть по екрану і натисніть Enter - щоб вийти з данної інформації.\n\n\n"
            second_window = tk.Toplevel(root)
            second_window.title("Результат")
            second_window.attributes('-fullscreen', True)

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
            text.insert("1.0", msg)

            copy_button = tk.Button(second_window, text="Копіювати текст", font=my_font,
            command=lambda: copy_text_to_clipboard(root, text))
            copy_button.pack(pady=20)

            text.bind('<Control-v>', lambda e: paste_from_clipboard(text))

            text.bind('<Control-c>', lambda e: copy_text_to_clipboard(root, text))

            second_window.bind("<Return>", lambda e: second_window.destroy())

            def copy_text_to_clipboard(root, text_widget):
                text = text_widget.get("1.0", "end-1c") 
                pyperclip.copy(text) 


            def paste_from_clipboard(text_widget):
                try:
                    clipboard_text = pyperclip.paste()
                    text_widget.insert(tk.INSERT, clipboard_text)
                except Exception as e:
                    messagebox.showwarning("Помилка", f"Помилка при вставці: {e}")

            conn.close()
            root.after(0, loading.destroy)

        loading = loading_window(root)
        threading.Thread(target=work, args=(root, name_db, loading), daemon=True).start()

    def on_main_pp_button_click(root, name_db):
        def work(root, name_db, loading):

            conn = sqlite3.connect(name_db)
            cursor = conn.cursor()

            cursor.execute("""
                SELECT

                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN first_semester."всього" != 0 AND first_semester."ставка" != 0
                                    THEN first_semester."всього"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN first_semester."всього" != 0 AND first_semester."ставка" != 0
                                        THEN first_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2),

                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN second_semester."всього" != 0 AND second_semester."ставка" != 0
                                    THEN second_semester."всього"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN second_semester."всього" != 0 AND second_semester."ставка" != 0
                                        THEN second_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2),
 
                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN academic_year."всього" != 0 AND academic_year."ставка" != 0
                                    THEN academic_year."всього"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN academic_year."всього" != 0 AND academic_year."ставка" != 0
                                        THEN academic_year."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2)
                
                FROM job

                JOIN code_year ON job."код_рік_id" = code_year.id
                JOIN first_semester ON job.id = first_semester."job_id"
                JOIN second_semester ON job.id = second_semester."job_id"
                JOIN academic_year ON job.id = academic_year."job_id"

                WHERE job.НПП_ПП = 'ПП'

                UNION ALL

                SELECT

                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN first_semester."всього" != 0 AND first_semester."ставка" != 0
                                    THEN first_semester."всього"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN first_semester."всього" != 0 AND first_semester."ставка" != 0
                                        THEN first_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2),

                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN second_semester."всього" != 0 AND second_semester."ставка" != 0
                                    THEN second_semester."всього"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN second_semester."всього" != 0 AND second_semester."ставка" != 0
                                        THEN second_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2),
 
                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN academic_year."всього" != 0 AND academic_year."ставка" != 0
                                    THEN academic_year."всього"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN academic_year."всього" != 0 AND academic_year."ставка" != 0
                                        THEN academic_year."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2)
                
                FROM job

                JOIN code_year ON job."код_рік_id" = code_year.id
                JOIN first_semester ON job.id = first_semester."job_id"
                JOIN second_semester ON job.id = second_semester."job_id"
                JOIN academic_year ON job.id = academic_year."job_id"

                WHERE job.НПП_ПП = 'ПП' AND job.'посада' = 'заф. кафедри'
                
                UNION ALL

                SELECT

                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN first_semester."всього" != 0 AND first_semester."ставка" != 0
                                    THEN first_semester."всього"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN first_semester."всього" != 0 AND first_semester."ставка" != 0
                                        THEN first_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2),

                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN second_semester."всього" != 0 AND second_semester."ставка" != 0
                                    THEN second_semester."всього"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN second_semester."всього" != 0 AND second_semester."ставка" != 0
                                        THEN second_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2),
 
                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN academic_year."всього" != 0 AND academic_year."ставка" != 0
                                    THEN academic_year."всього"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN academic_year."всього" != 0 AND academic_year."ставка" != 0
                                        THEN academic_year."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2)
                
                FROM job

                JOIN code_year ON job."код_рік_id" = code_year.id
                JOIN first_semester ON job.id = first_semester."job_id"
                JOIN second_semester ON job.id = second_semester."job_id"
                JOIN academic_year ON job.id = academic_year."job_id"

                WHERE job.НПП_ПП = 'ПП' AND job.'посада' = 'професор'

                UNION ALL

                SELECT

                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN first_semester."всього" != 0 AND first_semester."ставка" != 0
                                    THEN first_semester."всього"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN first_semester."всього" != 0 AND first_semester."ставка" != 0
                                        THEN first_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2),

                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN second_semester."всього" != 0 AND second_semester."ставка" != 0
                                    THEN second_semester."всього"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN second_semester."всього" != 0 AND second_semester."ставка" != 0
                                        THEN second_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2),
 
                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN academic_year."всього" != 0 AND academic_year."ставка" != 0
                                    THEN academic_year."всього"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN academic_year."всього" != 0 AND academic_year."ставка" != 0
                                        THEN academic_year."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2)
                
                FROM job

                JOIN code_year ON job."код_рік_id" = code_year.id
                JOIN first_semester ON job.id = first_semester."job_id"
                JOIN second_semester ON job.id = second_semester."job_id"
                JOIN academic_year ON job.id = academic_year."job_id"

                WHERE job.НПП_ПП = 'ПП' AND job.'посада' = 'доцент'

                UNION ALL

                SELECT

                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN first_semester."всього" != 0 AND first_semester."ставка" != 0
                                    THEN first_semester."всього"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN first_semester."всього" != 0 AND first_semester."ставка" != 0
                                        THEN first_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2),

                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN second_semester."всього" != 0 AND second_semester."ставка" != 0
                                    THEN second_semester."всього"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN second_semester."всього" != 0 AND second_semester."ставка" != 0
                                        THEN second_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2),
 
                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN academic_year."всього" != 0 AND academic_year."ставка" != 0
                                    THEN academic_year."всього"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN academic_year."всього" != 0 AND academic_year."ставка" != 0
                                        THEN academic_year."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2)
                
                FROM job

                JOIN code_year ON job."код_рік_id" = code_year.id
                JOIN first_semester ON job.id = first_semester."job_id"
                JOIN second_semester ON job.id = second_semester."job_id"
                JOIN academic_year ON job.id = academic_year."job_id"

                WHERE job.НПП_ПП = 'ПП' AND job.'посада' = 'ст. викладач'

                UNION ALL

                SELECT

                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN first_semester."всього" != 0 AND first_semester."ставка" != 0
                                    THEN first_semester."всього"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN first_semester."всього" != 0 AND first_semester."ставка" != 0
                                        THEN first_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2),

                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN second_semester."всього" != 0 AND second_semester."ставка" != 0
                                    THEN second_semester."всього"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN second_semester."всього" != 0 AND second_semester."ставка" != 0
                                        THEN second_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2),
 
                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN academic_year."всього" != 0 AND academic_year."ставка" != 0
                                    THEN academic_year."всього"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN academic_year."всього" != 0 AND academic_year."ставка" != 0
                                        THEN academic_year."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2)
                
                FROM job

                JOIN code_year ON job."код_рік_id" = code_year.id
                JOIN first_semester ON job.id = first_semester."job_id"
                JOIN second_semester ON job.id = second_semester."job_id"
                JOIN academic_year ON job.id = academic_year."job_id"

                WHERE job.НПП_ПП = 'ПП' AND job.'посада' = 'асистент'

                UNION ALL

                SELECT

                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN first_semester."всього" != 0 AND first_semester."ставка" != 0
                                    THEN first_semester."всього"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN first_semester."всього" != 0 AND first_semester."ставка" != 0
                                        THEN first_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2),

                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN second_semester."всього" != 0 AND second_semester."ставка" != 0
                                    THEN second_semester."всього"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN second_semester."всього" != 0 AND second_semester."ставка" != 0
                                        THEN second_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2),
 
                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN academic_year."всього" != 0 AND academic_year."ставка" != 0
                                    THEN academic_year."всього"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN academic_year."всього" != 0 AND academic_year."ставка" != 0
                                        THEN academic_year."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2)
                
                FROM job

                JOIN code_year ON job."код_рік_id" = code_year.id
                JOIN first_semester ON job.id = first_semester."job_id"
                JOIN second_semester ON job.id = second_semester."job_id"
                JOIN academic_year ON job.id = academic_year."job_id"

                WHERE job.НПП_ПП = 'ПП' AND job.'посада' = 'в.о. заф. кафедри'

                UNION ALL

                SELECT

                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN first_semester."всього" != 0 AND first_semester."ставка" != 0
                                    THEN first_semester."всього"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN first_semester."всього" != 0 AND first_semester."ставка" != 0
                                        THEN first_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2),

                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN second_semester."всього" != 0 AND second_semester."ставка" != 0
                                    THEN second_semester."всього"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN second_semester."всього" != 0 AND second_semester."ставка" != 0
                                        THEN second_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2),
 
                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN academic_year."всього" != 0 AND academic_year."ставка" != 0
                                    THEN academic_year."всього"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN academic_year."всього" != 0 AND academic_year."ставка" != 0
                                        THEN academic_year."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2)
                
                FROM job

                JOIN code_year ON job."код_рік_id" = code_year.id
                JOIN first_semester ON job.id = first_semester."job_id"
                JOIN second_semester ON job.id = second_semester."job_id"
                JOIN academic_year ON job.id = academic_year."job_id"

                WHERE job.'НПП_ПП' = 'ПП' AND job.'посада' = 'викладач'
                
            """)
            

            result = []
            for value in cursor.fetchall():
                result.append((value[0],value[1],value[2]))
            
            msg = ""
            msg += f"Середнє навантаження ПП (заф. кафедри)\n\t перший семестр: {result[1][0]}\n\t другий семестр: {result[1][1]}\n\t рік: {result[1][2]}\n\n"
            msg += f"Середнє навантаження ПП (професор)\n\t перший семестр: {result[2][0]}\n\t другий семестр: {result[2][1]}\n\t рік: {result[2][2]}\n\n"
            msg += f"Середнє навантаження ПП (доцент)\n\t перший семестр: {result[3][0]}\n\t другий семестр: {result[3][1]}\n\t рік: {result[3][2]}\n\n"
            msg += f"Середнє навантаження ПП (ст. викладач)\n\t перший семестр: {result[4][0]}\n\t другий семестр: {result[4][1]}\n\t рік: {result[4][2]}\n\n"
            msg += f"Середнє навантаження ПП (асистент)\n\t перший семестр: {result[5][0]}\n\t другий семестр: {result[5][1]}\n\t рік: {result[5][2]}\n\n"
            msg += f"Середнє навантаження ПП (в.о. заф. кафедри)\n\t перший семестр: {result[6][0]}\n\t другий семестр: {result[6][1]}\n\t рік: {result[6][2]}\n\n"
            msg += f"Середнє навантаження ПП (викладач)\n\t перший семестр: {result[7][0]}\n\t другий семестр: {result[7][1]}\n\t рік: {result[7][2]}\n\n"
            msg += f"Середнє навантаження ПП (усі)\n\t перший семестр: {result[0][0]}\n\t другий семестр: {result[0][1]}\n\t рік: {result[0][2]}\n\n"

            with open("resources\\Середнэ навантаження\\ПП\\Загальне\\file.txt", "w", encoding="utf-8") as f:
                f.write(msg)

            msg = "Дані збереженно у файлі: \"resources\\Середнэ навантаження\\ПП\\Загальне\\file.txt\".\n\n\n" + msg
            msg += "\n\n\nКлацніть по екрану і натисніть Enter - щоб вийти з данної інформації.\n\n\n"
            second_window = tk.Toplevel(root)
            second_window.title("Результат")
            second_window.attributes('-fullscreen', True)

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
            text.insert("1.0", msg)

            copy_button = tk.Button(second_window, text="Копіювати текст", font=my_font,
            command=lambda: copy_text_to_clipboard(root, text))
            copy_button.pack(pady=20)

            text.bind('<Control-v>', lambda e: paste_from_clipboard(text))

            text.bind('<Control-c>', lambda e: copy_text_to_clipboard(root, text))

            second_window.bind("<Return>", lambda e: second_window.destroy())

            def copy_text_to_clipboard(root, text_widget):
                text = text_widget.get("1.0", "end-1c") 
                pyperclip.copy(text) 


            def paste_from_clipboard(text_widget):
                try:
                    clipboard_text = pyperclip.paste()
                    text_widget.insert(tk.INSERT, clipboard_text)
                except Exception as e:
                    messagebox.showwarning("Помилка", f"Помилка при вставці: {e}")

            conn.close()
            root.after(0, loading.destroy)

        loading = loading_window(root)
        threading.Thread(target=work, args=(root, name_db, loading), daemon=True).start()

    def on_lecture_npp_button_click(root, name_db):
        def work(root, name_db, loading):

            conn = sqlite3.connect(name_db)
            cursor = conn.cursor()

            cursor.execute("""
                SELECT

                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN first_semester."лекції" != 0 AND first_semester."ставка" != 0
                                    THEN first_semester."лекції"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN first_semester."лекції" != 0 AND first_semester."ставка" != 0
                                        THEN first_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2),

                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN second_semester."лекції" != 0 AND second_semester."ставка" != 0
                                    THEN second_semester."лекції"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN second_semester."лекції" != 0 AND second_semester."ставка" != 0
                                        THEN second_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2),
 
                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN academic_year."лекції" != 0 AND academic_year."ставка" != 0
                                    THEN academic_year."лекції"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN academic_year."лекції" != 0 AND academic_year."ставка" != 0
                                        THEN academic_year."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2)
                
                FROM job

                JOIN code_year ON job."код_рік_id" = code_year.id
                JOIN first_semester ON job.id = first_semester."job_id"
                JOIN second_semester ON job.id = second_semester."job_id"
                JOIN academic_year ON job.id = academic_year."job_id"

                WHERE job.'посада' != 'асистент' AND job.'НПП_ПП' = 'НПП' AND academic_year.'лекції' != 0 AND academic_year.'ставка' != 0


                UNION ALL
            
                SELECT

                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN first_semester."лекції" != 0 AND first_semester."ставка" != 0
                                    THEN first_semester."лекції"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN first_semester."лекції" != 0 AND first_semester."ставка" != 0
                                        THEN first_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2),

                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN second_semester."лекції" != 0 AND second_semester."ставка" != 0
                                    THEN second_semester."лекції"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN second_semester."лекції" != 0 AND second_semester."ставка" != 0
                                        THEN second_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2),
 
                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN academic_year."лекції" != 0 AND academic_year."ставка" != 0
                                    THEN academic_year."лекції"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN academic_year."лекції" != 0 AND academic_year."ставка" != 0
                                        THEN academic_year."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2)
                
                FROM job

                JOIN code_year ON job."код_рік_id" = code_year.id
                JOIN first_semester ON job.id = first_semester."job_id"
                JOIN second_semester ON job.id = second_semester."job_id"
                JOIN academic_year ON job.id = academic_year."job_id"

                WHERE job.'посада' = 'заф. кафедри' AND job.'НПП_ПП' = 'НПП' AND academic_year.'лекції' != 0 AND academic_year.'ставка' != 0


                UNION ALL
            
                SELECT

                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN first_semester."лекції" != 0 AND first_semester."ставка" != 0
                                    THEN first_semester."лекції"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN first_semester."лекції" != 0 AND first_semester."ставка" != 0
                                        THEN first_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2),

                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN second_semester."лекції" != 0 AND second_semester."ставка" != 0
                                    THEN second_semester."лекції"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN second_semester."лекції" != 0 AND second_semester."ставка" != 0
                                        THEN second_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2),
 
                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN academic_year."лекції" != 0 AND academic_year."ставка" != 0
                                    THEN academic_year."лекції"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN academic_year."лекції" != 0 AND academic_year."ставка" != 0
                                        THEN academic_year."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2)
                
                FROM job

                JOIN code_year ON job."код_рік_id" = code_year.id
                JOIN first_semester ON job.id = first_semester."job_id"
                JOIN second_semester ON job.id = second_semester."job_id"
                JOIN academic_year ON job.id = academic_year."job_id"

                WHERE job.'посада' = 'професор' AND job.'НПП_ПП' = 'НПП' AND academic_year.'лекції' != 0 AND academic_year.'ставка' != 0

                UNION ALL
            
                SELECT

                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN first_semester."лекції" != 0 AND first_semester."ставка" != 0
                                    THEN first_semester."лекції"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN first_semester."лекції" != 0 AND first_semester."ставка" != 0
                                        THEN first_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2),

                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN second_semester."лекції" != 0 AND second_semester."ставка" != 0
                                    THEN second_semester."лекції"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN second_semester."лекції" != 0 AND second_semester."ставка" != 0
                                        THEN second_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2),
 
                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN academic_year."лекції" != 0 AND academic_year."ставка" != 0
                                    THEN academic_year."лекції"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN academic_year."лекції" != 0 AND academic_year."ставка" != 0
                                        THEN academic_year."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2)
                
                FROM job

                JOIN code_year ON job."код_рік_id" = code_year.id
                JOIN first_semester ON job.id = first_semester."job_id"
                JOIN second_semester ON job.id = second_semester."job_id"
                JOIN academic_year ON job.id = academic_year."job_id"

                WHERE job.'посада' = 'доцент' AND job.'НПП_ПП' = 'НПП' AND academic_year.'лекції' != 0 AND academic_year.'ставка' != 0


                UNION ALL

                SELECT

                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN first_semester."лекції" != 0 AND first_semester."ставка" != 0
                                    THEN first_semester."лекції"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN first_semester."лекції" != 0 AND first_semester."ставка" != 0
                                        THEN first_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2),

                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN second_semester."лекції" != 0 AND second_semester."ставка" != 0
                                    THEN second_semester."лекції"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN second_semester."лекції" != 0 AND second_semester."ставка" != 0
                                        THEN second_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2),
 
                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN academic_year."лекції" != 0 AND academic_year."ставка" != 0
                                    THEN academic_year."лекції"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN academic_year."лекції" != 0 AND academic_year."ставка" != 0
                                        THEN academic_year."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2)
                
                FROM job

                JOIN code_year ON job."код_рік_id" = code_year.id
                JOIN first_semester ON job.id = first_semester."job_id"
                JOIN second_semester ON job.id = second_semester."job_id"
                JOIN academic_year ON job.id = academic_year."job_id"

                WHERE job.'посада' = 'ст. викладач' AND job.'НПП_ПП' = 'НПП' AND academic_year.'лекції' != 0 AND academic_year.'ставка' != 0

                UNION ALL
            
                SELECT

                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN first_semester."лекції" != 0 AND first_semester."ставка" != 0
                                    THEN first_semester."лекції"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN first_semester."лекції" != 0 AND first_semester."ставка" != 0
                                        THEN first_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2),

                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN second_semester."лекції" != 0 AND second_semester."ставка" != 0
                                    THEN second_semester."лекції"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN second_semester."лекції" != 0 AND second_semester."ставка" != 0
                                        THEN second_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2),
 
                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN academic_year."лекції" != 0 AND academic_year."ставка" != 0
                                    THEN academic_year."лекції"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN academic_year."лекції" != 0 AND academic_year."ставка" != 0
                                        THEN academic_year."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2)
                
                FROM job

                JOIN code_year ON job."код_рік_id" = code_year.id
                JOIN first_semester ON job.id = first_semester."job_id"
                JOIN second_semester ON job.id = second_semester."job_id"
                JOIN academic_year ON job.id = academic_year."job_id"

                WHERE job.'посада' = 'в.о. заф. кафедри' AND job.'НПП_ПП' = 'НПП' AND academic_year.'лекції' != 0 AND academic_year.'ставка' != 0

                UNION ALL
            
                SELECT

                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN first_semester."лекції" != 0 AND first_semester."ставка" != 0
                                    THEN first_semester."лекції"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN first_semester."лекції" != 0 AND first_semester."ставка" != 0
                                        THEN first_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2),

                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN second_semester."лекції" != 0 AND second_semester."ставка" != 0
                                    THEN second_semester."лекції"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN second_semester."лекції" != 0 AND second_semester."ставка" != 0
                                        THEN second_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2),
 
                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN academic_year."лекції" != 0 AND academic_year."ставка" != 0
                                    THEN academic_year."лекції"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN academic_year."лекції" != 0 AND academic_year."ставка" != 0
                                        THEN academic_year."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2)
                
                FROM job

                JOIN code_year ON job."код_рік_id" = code_year.id
                JOIN first_semester ON job.id = first_semester."job_id"
                JOIN second_semester ON job.id = second_semester."job_id"
                JOIN academic_year ON job.id = academic_year."job_id"

                WHERE job.'посада' = 'викладач' AND job.'НПП_ПП' = 'НПП' AND academic_year.'лекції' != 0 AND academic_year.'ставка' != 0
            """)
            

            result = []
            for value in cursor.fetchall():
                result.append((value[0],value[1],value[2]))
            
            msg = ""
            msg += f"Середнє лекційне навантаження НПП (заф. кафедри)\n\t перший семестр: {result[1][0]}\n\t другий семестр: {result[1][1]}\n\t рік: {result[1][2]}\n\n"
            msg += f"Середнє лекційне навантаження НПП (професор)\n\t перший семестр: {result[2][0]}\n\t другий семестр: {result[2][1]}\n\t рік: {result[2][2]}\n\n"
            msg += f"Середнє лекційне навантаження НПП (доцент)\n\t перший семестр: {result[3][0]}\n\t другий семестр: {result[3][1]}\n\t рік: {result[3][2]}\n\n"
            msg += f"Середнє лекційне навантаження НПП (ст. викладач)\n\t перший семестр: {result[4][0]}\n\t другий семестр: {result[4][1]}\n\t рік: {result[4][2]}\n\n"
            msg += f"Середнє лекційне навантаження НПП (в.о. заф. кафедри)\n\t перший семестр: {result[5][0]}\n\t другий семестр: {result[5][1]}\n\t рік: {result[5][2]}\n\n"
            msg += f"Середнє лекційне навантаження НПП (викладач)\n\t перший семестр: {result[6][0]}\n\t другий семестр: {result[6][1]}\n\t рік: {result[6][2]}\n\n"
            msg += f"Середнє лекційне навантаження НПП (усі)\n\t перший семестр: {result[0][0]}\n\t другий семестр: {result[0][1]}\n\t рік: {result[0][2]}\n\n"

            with open("resources\\Середнэ навантаження\\НПП\\Лекційне\\file.txt", "w", encoding="utf-8") as f:
                f.write(msg)

            msg = "Дані збереженно у файлі: \"resources\\Середнэ навантаження\\НПП\\Лекційне\\file.txt\".\n\n\n" + msg
            msg += "\n\n\nКлацніть по екрану і натисніть Enter - щоб вийти з данної інформації.\n\n\n"
            second_window = tk.Toplevel(root)
            second_window.title("Результат")
            second_window.attributes('-fullscreen', True)

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
            text.insert("1.0", msg)

            copy_button = tk.Button(second_window, text="Копіювати текст", font=my_font,
            command=lambda: copy_text_to_clipboard(root, text))
            copy_button.pack(pady=20)

            text.bind('<Control-v>', lambda e: paste_from_clipboard(text))

            text.bind('<Control-c>', lambda e: copy_text_to_clipboard(root, text))

            second_window.bind("<Return>", lambda e: second_window.destroy())

            def copy_text_to_clipboard(root, text_widget):
                text = text_widget.get("1.0", "end-1c") 
                pyperclip.copy(text) 


            def paste_from_clipboard(text_widget):
                try:
                    clipboard_text = pyperclip.paste()
                    text_widget.insert(tk.INSERT, clipboard_text)
                except Exception as e:
                    messagebox.showwarning("Помилка", f"Помилка при вставці: {e}")

            conn.close()
            root.after(0, loading.destroy)

        loading = loading_window(root)
        threading.Thread(target=work, args=(root, name_db, loading), daemon=True).start()

    def on_lecture_pp_button_click(root, name_db):
        def work(root, name_db, loading):

            conn = sqlite3.connect(name_db)
            cursor = conn.cursor()

            cursor.execute("""
                SELECT

                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN first_semester."лекції" != 0 AND first_semester."ставка" != 0
                                    THEN first_semester."лекції"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN first_semester."лекції" != 0 AND first_semester."ставка" != 0
                                        THEN first_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2),

                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN second_semester."лекції" != 0 AND second_semester."ставка" != 0
                                    THEN second_semester."лекції"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN second_semester."лекції" != 0 AND second_semester."ставка" != 0
                                        THEN second_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2),
 
                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN academic_year."лекції" != 0 AND academic_year."ставка" != 0
                                    THEN academic_year."лекції"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN academic_year."лекції" != 0 AND academic_year."ставка" != 0
                                        THEN academic_year."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2)
                
                FROM job

                JOIN code_year ON job."код_рік_id" = code_year.id
                JOIN first_semester ON job.id = first_semester."job_id"
                JOIN second_semester ON job.id = second_semester."job_id"
                JOIN academic_year ON job.id = academic_year."job_id"

                WHERE job.'посада' != 'асистент' AND job.'НПП_ПП' = 'ПП' AND academic_year.'лекції' != 0 AND academic_year.'ставка' != 0


                UNION ALL
            
                SELECT

                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN first_semester."лекції" != 0 AND first_semester."ставка" != 0
                                    THEN first_semester."лекції"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN first_semester."лекції" != 0 AND first_semester."ставка" != 0
                                        THEN first_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2),

                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN second_semester."лекції" != 0 AND second_semester."ставка" != 0
                                    THEN second_semester."лекції"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN second_semester."лекції" != 0 AND second_semester."ставка" != 0
                                        THEN second_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2),
 
                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN academic_year."лекції" != 0 AND academic_year."ставка" != 0
                                    THEN academic_year."лекції"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN academic_year."лекції" != 0 AND academic_year."ставка" != 0
                                        THEN academic_year."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2)
                
                FROM job

                JOIN code_year ON job."код_рік_id" = code_year.id
                JOIN first_semester ON job.id = first_semester."job_id"
                JOIN second_semester ON job.id = second_semester."job_id"
                JOIN academic_year ON job.id = academic_year."job_id"

                WHERE job.'посада' = 'заф. кафедри' AND job.'НПП_ПП' = 'ПП' AND academic_year.'лекції' != 0 AND academic_year.'ставка' != 0


                UNION ALL
            
                SELECT

                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN first_semester."лекції" != 0 AND first_semester."ставка" != 0
                                    THEN first_semester."лекції"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN first_semester."лекції" != 0 AND first_semester."ставка" != 0
                                        THEN first_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2),

                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN second_semester."лекції" != 0 AND second_semester."ставка" != 0
                                    THEN second_semester."лекції"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN second_semester."лекції" != 0 AND second_semester."ставка" != 0
                                        THEN second_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2),
 
                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN academic_year."лекції" != 0 AND academic_year."ставка" != 0
                                    THEN academic_year."лекції"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN academic_year."лекції" != 0 AND academic_year."ставка" != 0
                                        THEN academic_year."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2)
                
                FROM job

                JOIN code_year ON job."код_рік_id" = code_year.id
                JOIN first_semester ON job.id = first_semester."job_id"
                JOIN second_semester ON job.id = second_semester."job_id"
                JOIN academic_year ON job.id = academic_year."job_id"

                WHERE job.'посада' = 'професор' AND job.'НПП_ПП' = 'ПП' AND academic_year.'лекції' != 0 AND academic_year.'ставка' != 0

                UNION ALL
            
                SELECT

                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN first_semester."лекції" != 0 AND first_semester."ставка" != 0
                                    THEN first_semester."лекції"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN first_semester."лекції" != 0 AND first_semester."ставка" != 0
                                        THEN first_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2),

                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN second_semester."лекції" != 0 AND second_semester."ставка" != 0
                                    THEN second_semester."лекції"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN second_semester."лекції" != 0 AND second_semester."ставка" != 0
                                        THEN second_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2),
 
                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN academic_year."лекції" != 0 AND academic_year."ставка" != 0
                                    THEN academic_year."лекції"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN academic_year."лекції" != 0 AND academic_year."ставка" != 0
                                        THEN academic_year."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2)
                
                FROM job

                JOIN code_year ON job."код_рік_id" = code_year.id
                JOIN first_semester ON job.id = first_semester."job_id"
                JOIN second_semester ON job.id = second_semester."job_id"
                JOIN academic_year ON job.id = academic_year."job_id"

                WHERE job.'посада' = 'доцент' AND job.'НПП_ПП' = 'ПП' AND academic_year.'лекції' != 0 AND academic_year.'ставка' != 0


                UNION ALL

                SELECT

                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN first_semester."лекції" != 0 AND first_semester."ставка" != 0
                                    THEN first_semester."лекції"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN first_semester."лекції" != 0 AND first_semester."ставка" != 0
                                        THEN first_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2),

                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN second_semester."лекції" != 0 AND second_semester."ставка" != 0
                                    THEN second_semester."лекції"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN second_semester."лекції" != 0 AND second_semester."ставка" != 0
                                        THEN second_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2),
 
                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN academic_year."лекції" != 0 AND academic_year."ставка" != 0
                                    THEN academic_year."лекції"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN academic_year."лекції" != 0 AND academic_year."ставка" != 0
                                        THEN academic_year."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2)
                
                FROM job

                JOIN code_year ON job."код_рік_id" = code_year.id
                JOIN first_semester ON job.id = first_semester."job_id"
                JOIN second_semester ON job.id = second_semester."job_id"
                JOIN academic_year ON job.id = academic_year."job_id"

                WHERE job.'посада' = 'ст. викладач' AND job.'НПП_ПП' = 'ПП' AND academic_year.'лекції' != 0 AND academic_year.'ставка' != 0

                UNION ALL
            
                SELECT

                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN first_semester."лекції" != 0 AND first_semester."ставка" != 0
                                    THEN first_semester."лекції"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN first_semester."лекції" != 0 AND first_semester."ставка" != 0
                                        THEN first_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2),

                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN second_semester."лекції" != 0 AND second_semester."ставка" != 0
                                    THEN second_semester."лекції"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN second_semester."лекції" != 0 AND second_semester."ставка" != 0
                                        THEN second_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2),
 
                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN academic_year."лекції" != 0 AND academic_year."ставка" != 0
                                    THEN academic_year."лекції"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN academic_year."лекції" != 0 AND academic_year."ставка" != 0
                                        THEN academic_year."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2)
                
                FROM job

                JOIN code_year ON job."код_рік_id" = code_year.id
                JOIN first_semester ON job.id = first_semester."job_id"
                JOIN second_semester ON job.id = second_semester."job_id"
                JOIN academic_year ON job.id = academic_year."job_id"

                WHERE job.'посада' = 'в.о. заф. кафедри' AND job.'НПП_ПП' = 'ПП' AND academic_year.'лекції' != 0 AND academic_year.'ставка' != 0

                UNION ALL
            
                SELECT

                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN first_semester."лекції" != 0 AND first_semester."ставка" != 0
                                    THEN first_semester."лекції"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN first_semester."лекції" != 0 AND first_semester."ставка" != 0
                                        THEN first_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2),

                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN second_semester."лекції" != 0 AND second_semester."ставка" != 0
                                    THEN second_semester."лекції"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN second_semester."лекції" != 0 AND second_semester."ставка" != 0
                                        THEN second_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2),
 
                    ROUND(
                        COALESCE(
                            SUM(
                                CASE
                                    WHEN academic_year."лекції" != 0 AND academic_year."ставка" != 0
                                    THEN academic_year."лекції"
                                    ELSE 0
                                END
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN academic_year."лекції" != 0 AND academic_year."ставка" != 0
                                        THEN academic_year."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2)
                
                FROM job

                JOIN code_year ON job."код_рік_id" = code_year.id
                JOIN first_semester ON job.id = first_semester."job_id"
                JOIN second_semester ON job.id = second_semester."job_id"
                JOIN academic_year ON job.id = academic_year."job_id"

                WHERE job.'посада' = 'викладач' AND job.'НПП_ПП' = 'ПП' AND academic_year.'лекції' != 0 AND academic_year.'ставка' != 0
            """)
            

            result = []
            for value in cursor.fetchall():
                result.append((value[0],value[1],value[2]))
            
            msg = ""
            msg += f"Середнє лекційне навантаження ПП (заф. кафедри)\n\t перший семестр: {result[1][0]}\n\t другий семестр: {result[1][1]}\n\t рік: {result[1][2]}\n\n"
            msg += f"Середнє лекційне навантаження ПП (професор)\n\t перший семестр: {result[2][0]}\n\t другий семестр: {result[2][1]}\n\t рік: {result[2][2]}\n\n"
            msg += f"Середнє лекційне навантаження ПП (доцент)\n\t перший семестр: {result[3][0]}\n\t другий семестр: {result[3][1]}\n\t рік: {result[3][2]}\n\n"
            msg += f"Середнє лекційне навантаження ПП (ст. викладач)\n\t перший семестр: {result[4][0]}\n\t другий семестр: {result[4][1]}\n\t рік: {result[4][2]}\n\n"
            msg += f"Середнє лекційне навантаження ПП (в.о. заф. кафедри)\n\t перший семестр: {result[5][0]}\n\t другий семестр: {result[5][1]}\n\t рік: {result[5][2]}\n\n"
            msg += f"Середнє лекційне навантаження ПП (викладач)\n\t перший семестр: {result[6][0]}\n\t другий семестр: {result[6][1]}\n\t рік: {result[6][2]}\n\n"
            msg += f"Середнє лекційне навантаження ПП (усі)\n\t перший семестр: {result[0][0]}\n\t другий семестр: {result[0][1]}\n\t рік: {result[0][2]}\n\n"

            with open("resources\\Середнэ навантаження\\ПП\\Лекційне\\file.txt", "w", encoding="utf-8") as f:
                f.write(msg)

            msg = "Дані збереженно у файлі: \"resources\\Середнэ навантаження\\ПП\\Лекційне\\file.txt\".\n\n\n" + msg
            msg += "\n\n\nКлацніть по екрану і натисніть Enter - щоб вийти з данної інформації.\n\n\n"
            second_window = tk.Toplevel(root)
            second_window.title("Результат")
            second_window.attributes('-fullscreen', True)

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
            text.insert("1.0", msg)

            copy_button = tk.Button(second_window, text="Копіювати текст", font=my_font,
            command=lambda: copy_text_to_clipboard(root, text))
            copy_button.pack(pady=20)

            text.bind('<Control-v>', lambda e: paste_from_clipboard(text))

            text.bind('<Control-c>', lambda e: copy_text_to_clipboard(root, text))

            second_window.bind("<Return>", lambda e: second_window.destroy())

            def copy_text_to_clipboard(root, text_widget):
                text = text_widget.get("1.0", "end-1c") 
                pyperclip.copy(text) 


            def paste_from_clipboard(text_widget):
                try:
                    clipboard_text = pyperclip.paste()
                    text_widget.insert(tk.INSERT, clipboard_text)
                except Exception as e:
                    messagebox.showwarning("Помилка", f"Помилка при вставці: {e}")

            conn.close()
            root.after(0, loading.destroy)

        loading = loading_window(root)
        threading.Thread(target=work, args=(root, name_db, loading), daemon=True).start()

    def on_audience_npp_button_click(root, name_db):
        def work(root, name_db, loading):

            conn = sqlite3.connect(name_db)
            cursor = conn.cursor()

            cursor.execute("""
                SELECT
                    ROUND(
                    ROUND(
                        COALESCE(
                            (
                                SUM(
                                    CASE
                                        WHEN first_semester."практичні_(семінарські)_заняття" != 0 AND first_semester."ставка" != 0
                                        THEN first_semester."практичні_(семінарські)_заняття"
                                        ELSE 0
                                    END
                                )
                                +
                                SUM(
                                    CASE
                                        WHEN first_semester."лабораторні_роботи" != 0 AND first_semester."ставка" != 0
                                        THEN first_semester."лабораторні_роботи"
                                        ELSE 0
                                    END
                                )
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN first_semester."ставка" != 0 AND (first_semester."практичні_(семінарські)_заняття" != 0 OR first_semester."лабораторні_роботи" != 0)
                                        THEN first_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2)
                    +
                    (
                        SELECT

                        ROUND(
                            COALESCE(
                                SUM(
                                    CASE
                                        WHEN first_semester."лекції" != 0 AND first_semester."ставка" != 0
                                        THEN first_semester."лекції"
                                        ELSE 0
                                    END
                                )
                                /
                                NULLIF(
                                    SUM(
                                        CASE
                                            WHEN first_semester."лекції" != 0 AND first_semester."ставка" != 0
                                            THEN first_semester."ставка"
                                            ELSE 0
                                        END
                                    )
                                ,0)
                            ,0)
                        ,2)

                
                        FROM job

                        JOIN code_year ON job."код_рік_id" = code_year.id
                        JOIN first_semester ON job.id = first_semester."job_id"
                        JOIN second_semester ON job.id = second_semester."job_id"
                        JOIN academic_year ON job.id = academic_year."job_id"

                        WHERE job.'посада' != 'асистент' AND job.'НПП_ПП' = 'НПП'

                    ),2),

                    ROUND(
                    ROUND(
                        COALESCE(
                            (
                                SUM(
                                    CASE
                                        WHEN second_semester."практичні_(семінарські)_заняття" != 0 AND second_semester."ставка" != 0
                                        THEN second_semester."практичні_(семінарські)_заняття"
                                        ELSE 0
                                    END
                                )
                                +
                                SUM(
                                    CASE
                                        WHEN second_semester."лабораторні_роботи" != 0 AND second_semester."ставка" != 0
                                        THEN second_semester."лабораторні_роботи"
                                        ELSE 0
                                    END
                                )
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN second_semester."ставка" != 0 AND (second_semester."практичні_(семінарські)_заняття" != 0 OR second_semester."лабораторні_роботи" != 0)
                                        THEN second_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2)
                    +
                    (
                        SELECT

                        ROUND(
                            COALESCE(
                                SUM(
                                    CASE
                                        WHEN second_semester."лекції" != 0 AND second_semester."ставка" != 0
                                        THEN second_semester."лекції"
                                        ELSE 0
                                    END
                                )
                                /
                                NULLIF(
                                    SUM(
                                        CASE
                                            WHEN second_semester."лекції" != 0 AND second_semester."ставка" != 0
                                            THEN second_semester."ставка"
                                            ELSE 0
                                        END
                                    )
                                ,0)
                            ,0)
                        ,2)

                
                        FROM job

                        JOIN code_year ON job."код_рік_id" = code_year.id
                        JOIN first_semester ON job.id = first_semester."job_id"
                        JOIN second_semester ON job.id = second_semester."job_id"
                        JOIN academic_year ON job.id = academic_year."job_id"

                        WHERE job.'посада' != 'асистент' AND job.'НПП_ПП' = 'НПП'

                    ),2),

                    ROUND(
                    ROUND(
                        COALESCE(
                            (
                                SUM(
                                    CASE
                                        WHEN academic_year."практичні_(семінарські)_заняття" != 0 AND academic_year."ставка" != 0
                                        THEN academic_year."практичні_(семінарські)_заняття"
                                        ELSE 0
                                    END
                                )
                                +
                                SUM(
                                    CASE
                                        WHEN academic_year."лабораторні_роботи" != 0 AND academic_year."ставка" != 0
                                        THEN academic_year."лабораторні_роботи"
                                        ELSE 0
                                    END
                                )
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN academic_year."ставка" != 0 AND (academic_year."практичні_(семінарські)_заняття" != 0 OR academic_year."лабораторні_роботи" != 0)
                                        THEN academic_year."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2)
                    +
                    (
                        SELECT

                        ROUND(
                            COALESCE(
                                SUM(
                                    CASE
                                        WHEN academic_year."лекції" != 0 AND academic_year."ставка" != 0
                                        THEN academic_year."лекції"
                                        ELSE 0
                                    END
                                )
                                /
                                NULLIF(
                                    SUM(
                                        CASE
                                            WHEN academic_year."лекції" != 0 AND academic_year."ставка" != 0
                                            THEN academic_year."ставка"
                                            ELSE 0
                                        END
                                    )
                                ,0)
                            ,0)
                        ,2)

                
                        FROM job

                        JOIN code_year ON job."код_рік_id" = code_year.id
                        JOIN first_semester ON job.id = first_semester."job_id"
                        JOIN second_semester ON job.id = second_semester."job_id"
                        JOIN academic_year ON job.id = academic_year."job_id"

                        WHERE job.'посада' != 'асистент' AND job.'НПП_ПП' = 'НПП'

                    )
                    ,2)

                
                FROM job

                JOIN code_year ON job."код_рік_id" = code_year.id
                JOIN first_semester ON job.id = first_semester."job_id"
                JOIN second_semester ON job.id = second_semester."job_id"
                JOIN academic_year ON job.id = academic_year."job_id"

                WHERE job.'НПП_ПП' = 'НПП'

                UNION ALL

                SELECT
                    ROUND(
                    ROUND(
                        COALESCE(
                            (
                                SUM(
                                    CASE
                                        WHEN first_semester."практичні_(семінарські)_заняття" != 0 AND first_semester."ставка" != 0
                                        THEN first_semester."практичні_(семінарські)_заняття"
                                        ELSE 0
                                    END
                                )
                                +
                                SUM(
                                    CASE
                                        WHEN first_semester."лабораторні_роботи" != 0 AND first_semester."ставка" != 0
                                        THEN first_semester."лабораторні_роботи"
                                        ELSE 0
                                    END
                                )
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN first_semester."ставка" != 0 AND (first_semester."практичні_(семінарські)_заняття" != 0 OR first_semester."лабораторні_роботи" != 0)
                                        THEN first_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2)
                    +
                    (
                        SELECT

                        ROUND(
                            COALESCE(
                                SUM(
                                    CASE
                                        WHEN first_semester."лекції" != 0 AND first_semester."ставка" != 0
                                        THEN first_semester."лекції"
                                        ELSE 0
                                    END
                                )
                                /
                                NULLIF(
                                    SUM(
                                        CASE
                                            WHEN first_semester."лекції" != 0 AND first_semester."ставка" != 0
                                            THEN first_semester."ставка"
                                            ELSE 0
                                        END
                                    )
                                ,0)
                            ,0)
                        ,2)

                
                        FROM job

                        JOIN code_year ON job."код_рік_id" = code_year.id
                        JOIN first_semester ON job.id = first_semester."job_id"
                        JOIN second_semester ON job.id = second_semester."job_id"
                        JOIN academic_year ON job.id = academic_year."job_id"

                        WHERE job.'посада' = 'заф. кафедри' AND job.'НПП_ПП' = 'НПП'

                    ),2),

                    ROUND(
                    ROUND(
                        COALESCE(
                            (
                                SUM(
                                    CASE
                                        WHEN second_semester."практичні_(семінарські)_заняття" != 0 AND second_semester."ставка" != 0
                                        THEN second_semester."практичні_(семінарські)_заняття"
                                        ELSE 0
                                    END
                                )
                                +
                                SUM(
                                    CASE
                                        WHEN second_semester."лабораторні_роботи" != 0 AND second_semester."ставка" != 0
                                        THEN second_semester."лабораторні_роботи"
                                        ELSE 0
                                    END
                                )
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN second_semester."ставка" != 0 AND (second_semester."практичні_(семінарські)_заняття" != 0 OR second_semester."лабораторні_роботи" != 0)
                                        THEN second_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2)
                    +
                    (
                        SELECT

                        ROUND(
                            COALESCE(
                                SUM(
                                    CASE
                                        WHEN second_semester."лекції" != 0 AND second_semester."ставка" != 0
                                        THEN second_semester."лекції"
                                        ELSE 0
                                    END
                                )
                                /
                                NULLIF(
                                    SUM(
                                        CASE
                                            WHEN second_semester."лекції" != 0 AND second_semester."ставка" != 0
                                            THEN second_semester."ставка"
                                            ELSE 0
                                        END
                                    )
                                ,0)
                            ,0)
                        ,2)

                
                        FROM job

                        JOIN code_year ON job."код_рік_id" = code_year.id
                        JOIN first_semester ON job.id = first_semester."job_id"
                        JOIN second_semester ON job.id = second_semester."job_id"
                        JOIN academic_year ON job.id = academic_year."job_id"

                        WHERE job.'посада' = 'заф. кафедри' AND job.'НПП_ПП' = 'НПП'

                    ),2),

                    ROUND(
                    ROUND(
                        COALESCE(
                            (
                                SUM(
                                    CASE
                                        WHEN academic_year."практичні_(семінарські)_заняття" != 0 AND academic_year."ставка" != 0
                                        THEN academic_year."практичні_(семінарські)_заняття"
                                        ELSE 0
                                    END
                                )
                                +
                                SUM(
                                    CASE
                                        WHEN academic_year."лабораторні_роботи" != 0 AND academic_year."ставка" != 0
                                        THEN academic_year."лабораторні_роботи"
                                        ELSE 0
                                    END
                                )
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN academic_year."ставка" != 0 AND (academic_year."практичні_(семінарські)_заняття" != 0 OR academic_year."лабораторні_роботи" != 0)
                                        THEN academic_year."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2)
                    +
                    (
                        SELECT

                        ROUND(
                            COALESCE(
                                SUM(
                                    CASE
                                        WHEN academic_year."лекції" != 0 AND academic_year."ставка" != 0
                                        THEN academic_year."лекції"
                                        ELSE 0
                                    END
                                )
                                /
                                NULLIF(
                                    SUM(
                                        CASE
                                            WHEN academic_year."лекції" != 0 AND academic_year."ставка" != 0
                                            THEN academic_year."ставка"
                                            ELSE 0
                                        END
                                    )
                                ,0)
                            ,0)
                        ,2)

                
                        FROM job

                        JOIN code_year ON job."код_рік_id" = code_year.id
                        JOIN first_semester ON job.id = first_semester."job_id"
                        JOIN second_semester ON job.id = second_semester."job_id"
                        JOIN academic_year ON job.id = academic_year."job_id"

                        WHERE job.'посада' = 'заф. кафедри' AND job.'НПП_ПП' = 'НПП'

                    )
                    ,2)

                
                FROM job

                JOIN code_year ON job."код_рік_id" = code_year.id
                JOIN first_semester ON job.id = first_semester."job_id"
                JOIN second_semester ON job.id = second_semester."job_id"
                JOIN academic_year ON job.id = academic_year."job_id"

                WHERE job.'НПП_ПП' = 'НПП' AND job.'посада' = 'заф. кафедри'

                UNION ALL

                SELECT
                    ROUND(
                    ROUND(
                        COALESCE(
                            (
                                SUM(
                                    CASE
                                        WHEN first_semester."практичні_(семінарські)_заняття" != 0 AND first_semester."ставка" != 0
                                        THEN first_semester."практичні_(семінарські)_заняття"
                                        ELSE 0
                                    END
                                )
                                +
                                SUM(
                                    CASE
                                        WHEN first_semester."лабораторні_роботи" != 0 AND first_semester."ставка" != 0
                                        THEN first_semester."лабораторні_роботи"
                                        ELSE 0
                                    END
                                )
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN first_semester."ставка" != 0 AND (first_semester."практичні_(семінарські)_заняття" != 0 OR first_semester."лабораторні_роботи" != 0)
                                        THEN first_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2)
                    +
                    (
                        SELECT

                        ROUND(
                            COALESCE(
                                SUM(
                                    CASE
                                        WHEN first_semester."лекції" != 0 AND first_semester."ставка" != 0
                                        THEN first_semester."лекції"
                                        ELSE 0
                                    END
                                )
                                /
                                NULLIF(
                                    SUM(
                                        CASE
                                            WHEN first_semester."лекції" != 0 AND first_semester."ставка" != 0
                                            THEN first_semester."ставка"
                                            ELSE 0
                                        END
                                    )
                                ,0)
                            ,0)
                        ,2)

                
                        FROM job

                        JOIN code_year ON job."код_рік_id" = code_year.id
                        JOIN first_semester ON job.id = first_semester."job_id"
                        JOIN second_semester ON job.id = second_semester."job_id"
                        JOIN academic_year ON job.id = academic_year."job_id"

                        WHERE job.'посада' = 'професор' AND job.'НПП_ПП' = 'НПП'

                    ),2),

                    ROUND(
                    ROUND(
                        COALESCE(
                            (
                                SUM(
                                    CASE
                                        WHEN second_semester."практичні_(семінарські)_заняття" != 0 AND second_semester."ставка" != 0
                                        THEN second_semester."практичні_(семінарські)_заняття"
                                        ELSE 0
                                    END
                                )
                                +
                                SUM(
                                    CASE
                                        WHEN second_semester."лабораторні_роботи" != 0 AND second_semester."ставка" != 0
                                        THEN second_semester."лабораторні_роботи"
                                        ELSE 0
                                    END
                                )
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN second_semester."ставка" != 0 AND (second_semester."практичні_(семінарські)_заняття" != 0 OR second_semester."лабораторні_роботи" != 0)
                                        THEN second_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2)
                    +
                    (
                        SELECT

                        ROUND(
                            COALESCE(
                                SUM(
                                    CASE
                                        WHEN second_semester."лекції" != 0 AND second_semester."ставка" != 0
                                        THEN second_semester."лекції"
                                        ELSE 0
                                    END
                                )
                                /
                                NULLIF(
                                    SUM(
                                        CASE
                                            WHEN second_semester."лекції" != 0 AND second_semester."ставка" != 0
                                            THEN second_semester."ставка"
                                            ELSE 0
                                        END
                                    )
                                ,0)
                            ,0)
                        ,2)

                
                        FROM job

                        JOIN code_year ON job."код_рік_id" = code_year.id
                        JOIN first_semester ON job.id = first_semester."job_id"
                        JOIN second_semester ON job.id = second_semester."job_id"
                        JOIN academic_year ON job.id = academic_year."job_id"

                        WHERE job.'посада' = 'професор' AND job.'НПП_ПП' = 'НПП'

                    ),2),

                    ROUND(
                    ROUND(
                        COALESCE(
                            (
                                SUM(
                                    CASE
                                        WHEN academic_year."практичні_(семінарські)_заняття" != 0 AND academic_year."ставка" != 0
                                        THEN academic_year."практичні_(семінарські)_заняття"
                                        ELSE 0
                                    END
                                )
                                +
                                SUM(
                                    CASE
                                        WHEN academic_year."лабораторні_роботи" != 0 AND academic_year."ставка" != 0
                                        THEN academic_year."лабораторні_роботи"
                                        ELSE 0
                                    END
                                )
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN academic_year."ставка" != 0 AND (academic_year."практичні_(семінарські)_заняття" != 0 OR academic_year."лабораторні_роботи" != 0)
                                        THEN academic_year."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2)
                    +
                    (
                        SELECT

                        ROUND(
                            COALESCE(
                                SUM(
                                    CASE
                                        WHEN academic_year."лекції" != 0 AND academic_year."ставка" != 0
                                        THEN academic_year."лекції"
                                        ELSE 0
                                    END
                                )
                                /
                                NULLIF(
                                    SUM(
                                        CASE
                                            WHEN academic_year."лекції" != 0 AND academic_year."ставка" != 0
                                            THEN academic_year."ставка"
                                            ELSE 0
                                        END
                                    )
                                ,0)
                            ,0)
                        ,2)

                
                        FROM job

                        JOIN code_year ON job."код_рік_id" = code_year.id
                        JOIN first_semester ON job.id = first_semester."job_id"
                        JOIN second_semester ON job.id = second_semester."job_id"
                        JOIN academic_year ON job.id = academic_year."job_id"

                        WHERE job.'посада' = 'професор' AND job.'НПП_ПП' = 'НПП'

                    )
                    ,2)

                
                FROM job

                JOIN code_year ON job."код_рік_id" = code_year.id
                JOIN first_semester ON job.id = first_semester."job_id"
                JOIN second_semester ON job.id = second_semester."job_id"
                JOIN academic_year ON job.id = academic_year."job_id"

                WHERE job.'НПП_ПП' = 'НПП' AND job.'посада' = 'професор'

                UNION ALL

                SELECT
                    ROUND(
                    ROUND(
                        COALESCE(
                            (
                                SUM(
                                    CASE
                                        WHEN first_semester."практичні_(семінарські)_заняття" != 0 AND first_semester."ставка" != 0
                                        THEN first_semester."практичні_(семінарські)_заняття"
                                        ELSE 0
                                    END
                                )
                                +
                                SUM(
                                    CASE
                                        WHEN first_semester."лабораторні_роботи" != 0 AND first_semester."ставка" != 0
                                        THEN first_semester."лабораторні_роботи"
                                        ELSE 0
                                    END
                                )
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN first_semester."ставка" != 0 AND (first_semester."практичні_(семінарські)_заняття" != 0 OR first_semester."лабораторні_роботи" != 0)
                                        THEN first_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2)
                    +
                    (
                        SELECT

                        ROUND(
                            COALESCE(
                                SUM(
                                    CASE
                                        WHEN first_semester."лекції" != 0 AND first_semester."ставка" != 0
                                        THEN first_semester."лекції"
                                        ELSE 0
                                    END
                                )
                                /
                                NULLIF(
                                    SUM(
                                        CASE
                                            WHEN first_semester."лекції" != 0 AND first_semester."ставка" != 0
                                            THEN first_semester."ставка"
                                            ELSE 0
                                        END
                                    )
                                ,0)
                            ,0)
                        ,2)

                
                        FROM job

                        JOIN code_year ON job."код_рік_id" = code_year.id
                        JOIN first_semester ON job.id = first_semester."job_id"
                        JOIN second_semester ON job.id = second_semester."job_id"
                        JOIN academic_year ON job.id = academic_year."job_id"

                        WHERE job.'посада' = 'доцент' AND job.'НПП_ПП' = 'НПП'

                    ),2),

                    ROUND(
                    ROUND(
                        COALESCE(
                            (
                                SUM(
                                    CASE
                                        WHEN second_semester."практичні_(семінарські)_заняття" != 0 AND second_semester."ставка" != 0
                                        THEN second_semester."практичні_(семінарські)_заняття"
                                        ELSE 0
                                    END
                                )
                                +
                                SUM(
                                    CASE
                                        WHEN second_semester."лабораторні_роботи" != 0 AND second_semester."ставка" != 0
                                        THEN second_semester."лабораторні_роботи"
                                        ELSE 0
                                    END
                                )
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN second_semester."ставка" != 0 AND (second_semester."практичні_(семінарські)_заняття" != 0 OR second_semester."лабораторні_роботи" != 0)
                                        THEN second_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2)
                    +
                    (
                        SELECT

                        ROUND(
                            COALESCE(
                                SUM(
                                    CASE
                                        WHEN second_semester."лекції" != 0 AND second_semester."ставка" != 0
                                        THEN second_semester."лекції"
                                        ELSE 0
                                    END
                                )
                                /
                                NULLIF(
                                    SUM(
                                        CASE
                                            WHEN second_semester."лекції" != 0 AND second_semester."ставка" != 0
                                            THEN second_semester."ставка"
                                            ELSE 0
                                        END
                                    )
                                ,0)
                            ,0)
                        ,2)

                
                        FROM job

                        JOIN code_year ON job."код_рік_id" = code_year.id
                        JOIN first_semester ON job.id = first_semester."job_id"
                        JOIN second_semester ON job.id = second_semester."job_id"
                        JOIN academic_year ON job.id = academic_year."job_id"

                        WHERE job.'посада' = 'доцент' AND job.'НПП_ПП' = 'НПП'

                    ),2),

                    ROUND(
                    ROUND(
                        COALESCE(
                            (
                                SUM(
                                    CASE
                                        WHEN academic_year."практичні_(семінарські)_заняття" != 0 AND academic_year."ставка" != 0
                                        THEN academic_year."практичні_(семінарські)_заняття"
                                        ELSE 0
                                    END
                                )
                                +
                                SUM(
                                    CASE
                                        WHEN academic_year."лабораторні_роботи" != 0 AND academic_year."ставка" != 0
                                        THEN academic_year."лабораторні_роботи"
                                        ELSE 0
                                    END
                                )
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN academic_year."ставка" != 0 AND (academic_year."практичні_(семінарські)_заняття" != 0 OR academic_year."лабораторні_роботи" != 0)
                                        THEN academic_year."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2)
                    +
                    (
                        SELECT

                        ROUND(
                            COALESCE(
                                SUM(
                                    CASE
                                        WHEN academic_year."лекції" != 0 AND academic_year."ставка" != 0
                                        THEN academic_year."лекції"
                                        ELSE 0
                                    END
                                )
                                /
                                NULLIF(
                                    SUM(
                                        CASE
                                            WHEN academic_year."лекції" != 0 AND academic_year."ставка" != 0
                                            THEN academic_year."ставка"
                                            ELSE 0
                                        END
                                    )
                                ,0)
                            ,0)
                        ,2)

                
                        FROM job

                        JOIN code_year ON job."код_рік_id" = code_year.id
                        JOIN first_semester ON job.id = first_semester."job_id"
                        JOIN second_semester ON job.id = second_semester."job_id"
                        JOIN academic_year ON job.id = academic_year."job_id"

                        WHERE job.'посада' = 'доцент' AND job.'НПП_ПП' = 'НПП'

                    )
                    ,2)

                
                FROM job

                JOIN code_year ON job."код_рік_id" = code_year.id
                JOIN first_semester ON job.id = first_semester."job_id"
                JOIN second_semester ON job.id = second_semester."job_id"
                JOIN academic_year ON job.id = academic_year."job_id"

                WHERE job.'НПП_ПП' = 'НПП' AND job.'посада' = 'доцент'


                UNION ALL

                SELECT
                    ROUND(
                    ROUND(
                        COALESCE(
                            (
                                SUM(
                                    CASE
                                        WHEN first_semester."практичні_(семінарські)_заняття" != 0 AND first_semester."ставка" != 0
                                        THEN first_semester."практичні_(семінарські)_заняття"
                                        ELSE 0
                                    END
                                )
                                +
                                SUM(
                                    CASE
                                        WHEN first_semester."лабораторні_роботи" != 0 AND first_semester."ставка" != 0
                                        THEN first_semester."лабораторні_роботи"
                                        ELSE 0
                                    END
                                )
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN first_semester."ставка" != 0 AND (first_semester."практичні_(семінарські)_заняття" != 0 OR first_semester."лабораторні_роботи" != 0)
                                        THEN first_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2)
                    +
                    (
                        SELECT

                        ROUND(
                            COALESCE(
                                SUM(
                                    CASE
                                        WHEN first_semester."лекції" != 0 AND first_semester."ставка" != 0
                                        THEN first_semester."лекції"
                                        ELSE 0
                                    END
                                )
                                /
                                NULLIF(
                                    SUM(
                                        CASE
                                            WHEN first_semester."лекції" != 0 AND first_semester."ставка" != 0
                                            THEN first_semester."ставка"
                                            ELSE 0
                                        END
                                    )
                                ,0)
                            ,0)
                        ,2)

                
                        FROM job

                        JOIN code_year ON job."код_рік_id" = code_year.id
                        JOIN first_semester ON job.id = first_semester."job_id"
                        JOIN second_semester ON job.id = second_semester."job_id"
                        JOIN academic_year ON job.id = academic_year."job_id"

                        WHERE job.'посада' = 'ст. викладач' AND job.'НПП_ПП' = 'НПП'

                    ),2),

                    ROUND(
                    ROUND(
                        COALESCE(
                            (
                                SUM(
                                    CASE
                                        WHEN second_semester."практичні_(семінарські)_заняття" != 0 AND second_semester."ставка" != 0
                                        THEN second_semester."практичні_(семінарські)_заняття"
                                        ELSE 0
                                    END
                                )
                                +
                                SUM(
                                    CASE
                                        WHEN second_semester."лабораторні_роботи" != 0 AND second_semester."ставка" != 0
                                        THEN second_semester."лабораторні_роботи"
                                        ELSE 0
                                    END
                                )
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN second_semester."ставка" != 0 AND (second_semester."практичні_(семінарські)_заняття" != 0 OR second_semester."лабораторні_роботи" != 0)
                                        THEN second_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2)
                    +
                    (
                        SELECT

                        ROUND(
                            COALESCE(
                                SUM(
                                    CASE
                                        WHEN second_semester."лекції" != 0 AND second_semester."ставка" != 0
                                        THEN second_semester."лекції"
                                        ELSE 0
                                    END
                                )
                                /
                                NULLIF(
                                    SUM(
                                        CASE
                                            WHEN second_semester."лекції" != 0 AND second_semester."ставка" != 0
                                            THEN second_semester."ставка"
                                            ELSE 0
                                        END
                                    )
                                ,0)
                            ,0)
                        ,2)

                
                        FROM job

                        JOIN code_year ON job."код_рік_id" = code_year.id
                        JOIN first_semester ON job.id = first_semester."job_id"
                        JOIN second_semester ON job.id = second_semester."job_id"
                        JOIN academic_year ON job.id = academic_year."job_id"

                        WHERE job.'посада' = 'ст. викладач' AND job.'НПП_ПП' = 'НПП'

                    ),2),

                    ROUND(
                    ROUND(
                        COALESCE(
                            (
                                SUM(
                                    CASE
                                        WHEN academic_year."практичні_(семінарські)_заняття" != 0 AND academic_year."ставка" != 0
                                        THEN academic_year."практичні_(семінарські)_заняття"
                                        ELSE 0
                                    END
                                )
                                +
                                SUM(
                                    CASE
                                        WHEN academic_year."лабораторні_роботи" != 0 AND academic_year."ставка" != 0
                                        THEN academic_year."лабораторні_роботи"
                                        ELSE 0
                                    END
                                )
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN academic_year."ставка" != 0 AND (academic_year."практичні_(семінарські)_заняття" != 0 OR academic_year."лабораторні_роботи" != 0)
                                        THEN academic_year."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2)
                    +
                    (
                        SELECT

                        ROUND(
                            COALESCE(
                                SUM(
                                    CASE
                                        WHEN academic_year."лекції" != 0 AND academic_year."ставка" != 0
                                        THEN academic_year."лекції"
                                        ELSE 0
                                    END
                                )
                                /
                                NULLIF(
                                    SUM(
                                        CASE
                                            WHEN academic_year."лекції" != 0 AND academic_year."ставка" != 0
                                            THEN academic_year."ставка"
                                            ELSE 0
                                        END
                                    )
                                ,0)
                            ,0)
                        ,2)

                
                        FROM job

                        JOIN code_year ON job."код_рік_id" = code_year.id
                        JOIN first_semester ON job.id = first_semester."job_id"
                        JOIN second_semester ON job.id = second_semester."job_id"
                        JOIN academic_year ON job.id = academic_year."job_id"

                        WHERE job.'посада' = 'ст. викладач' AND job.'НПП_ПП' = 'НПП'

                    )
                    ,2)

                
                FROM job

                JOIN code_year ON job."код_рік_id" = code_year.id
                JOIN first_semester ON job.id = first_semester."job_id"
                JOIN second_semester ON job.id = second_semester."job_id"
                JOIN academic_year ON job.id = academic_year."job_id"

                WHERE job.'НПП_ПП' = 'НПП' AND job.'посада' = 'ст. викладач'

                UNION ALL

                SELECT
                    ROUND(
                    ROUND(
                        COALESCE(
                            (
                                SUM(
                                    CASE
                                        WHEN first_semester."практичні_(семінарські)_заняття" != 0 AND first_semester."ставка" != 0
                                        THEN first_semester."практичні_(семінарські)_заняття"
                                        ELSE 0
                                    END
                                )
                                +
                                SUM(
                                    CASE
                                        WHEN first_semester."лабораторні_роботи" != 0 AND first_semester."ставка" != 0
                                        THEN first_semester."лабораторні_роботи"
                                        ELSE 0
                                    END
                                )
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN first_semester."ставка" != 0 AND (first_semester."практичні_(семінарські)_заняття" != 0 OR first_semester."лабораторні_роботи" != 0)
                                        THEN first_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2),2),

                    ROUND(
                    ROUND(
                        COALESCE(
                            (
                                SUM(
                                    CASE
                                        WHEN second_semester."практичні_(семінарські)_заняття" != 0 AND second_semester."ставка" != 0
                                        THEN second_semester."практичні_(семінарські)_заняття"
                                        ELSE 0
                                    END
                                )
                                +
                                SUM(
                                    CASE
                                        WHEN second_semester."лабораторні_роботи" != 0 AND second_semester."ставка" != 0
                                        THEN second_semester."лабораторні_роботи"
                                        ELSE 0
                                    END
                                )
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN second_semester."ставка" != 0 AND (second_semester."практичні_(семінарські)_заняття" != 0 OR second_semester."лабораторні_роботи" != 0)
                                        THEN second_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2),2),

                    ROUND(
                    ROUND(
                        COALESCE(
                            (
                                SUM(
                                    CASE
                                        WHEN academic_year."практичні_(семінарські)_заняття" != 0 AND academic_year."ставка" != 0
                                        THEN academic_year."практичні_(семінарські)_заняття"
                                        ELSE 0
                                    END
                                )
                                +
                                SUM(
                                    CASE
                                        WHEN academic_year."лабораторні_роботи" != 0 AND academic_year."ставка" != 0
                                        THEN academic_year."лабораторні_роботи"
                                        ELSE 0
                                    END
                                )
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN academic_year."ставка" != 0 AND (academic_year."практичні_(семінарські)_заняття" != 0 OR academic_year."лабораторні_роботи" != 0)
                                        THEN academic_year."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2)
                    ,2)

                
                FROM job

                JOIN code_year ON job."код_рік_id" = code_year.id
                JOIN first_semester ON job.id = first_semester."job_id"
                JOIN second_semester ON job.id = second_semester."job_id"
                JOIN academic_year ON job.id = academic_year."job_id"

                WHERE job.'НПП_ПП' = 'НПП' AND job.'посада' = 'асистент'

                UNION ALL

                SELECT
                    ROUND(
                    ROUND(
                        COALESCE(
                            (
                                SUM(
                                    CASE
                                        WHEN first_semester."практичні_(семінарські)_заняття" != 0 AND first_semester."ставка" != 0
                                        THEN first_semester."практичні_(семінарські)_заняття"
                                        ELSE 0
                                    END
                                )
                                +
                                SUM(
                                    CASE
                                        WHEN first_semester."лабораторні_роботи" != 0 AND first_semester."ставка" != 0
                                        THEN first_semester."лабораторні_роботи"
                                        ELSE 0
                                    END
                                )
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN first_semester."ставка" != 0 AND (first_semester."практичні_(семінарські)_заняття" != 0 OR first_semester."лабораторні_роботи" != 0)
                                        THEN first_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2)
                    +
                    (
                        SELECT

                        ROUND(
                            COALESCE(
                                SUM(
                                    CASE
                                        WHEN first_semester."лекції" != 0 AND first_semester."ставка" != 0
                                        THEN first_semester."лекції"
                                        ELSE 0
                                    END
                                )
                                /
                                NULLIF(
                                    SUM(
                                        CASE
                                            WHEN first_semester."лекції" != 0 AND first_semester."ставка" != 0
                                            THEN first_semester."ставка"
                                            ELSE 0
                                        END
                                    )
                                ,0)
                            ,0)
                        ,2)

                
                        FROM job

                        JOIN code_year ON job."код_рік_id" = code_year.id
                        JOIN first_semester ON job.id = first_semester."job_id"
                        JOIN second_semester ON job.id = second_semester."job_id"
                        JOIN academic_year ON job.id = academic_year."job_id"

                        WHERE job.'посада' = 'в.о. заф. кафедри' AND job.'НПП_ПП' = 'НПП'

                    ),2),

                    ROUND(
                    ROUND(
                        COALESCE(
                            (
                                SUM(
                                    CASE
                                        WHEN second_semester."практичні_(семінарські)_заняття" != 0 AND second_semester."ставка" != 0
                                        THEN second_semester."практичні_(семінарські)_заняття"
                                        ELSE 0
                                    END
                                )
                                +
                                SUM(
                                    CASE
                                        WHEN second_semester."лабораторні_роботи" != 0 AND second_semester."ставка" != 0
                                        THEN second_semester."лабораторні_роботи"
                                        ELSE 0
                                    END
                                )
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN second_semester."ставка" != 0 AND (second_semester."практичні_(семінарські)_заняття" != 0 OR second_semester."лабораторні_роботи" != 0)
                                        THEN second_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2)
                    +
                    (
                        SELECT

                        ROUND(
                            COALESCE(
                                SUM(
                                    CASE
                                        WHEN second_semester."лекції" != 0 AND second_semester."ставка" != 0
                                        THEN second_semester."лекції"
                                        ELSE 0
                                    END
                                )
                                /
                                NULLIF(
                                    SUM(
                                        CASE
                                            WHEN second_semester."лекції" != 0 AND second_semester."ставка" != 0
                                            THEN second_semester."ставка"
                                            ELSE 0
                                        END
                                    )
                                ,0)
                            ,0)
                        ,2)

                
                        FROM job

                        JOIN code_year ON job."код_рік_id" = code_year.id
                        JOIN first_semester ON job.id = first_semester."job_id"
                        JOIN second_semester ON job.id = second_semester."job_id"
                        JOIN academic_year ON job.id = academic_year."job_id"

                        WHERE job.'посада' = 'в.о. заф. кафедри' AND job.'НПП_ПП' = 'НПП'

                    ),2),

                    ROUND(
                    ROUND(
                        COALESCE(
                            (
                                SUM(
                                    CASE
                                        WHEN academic_year."практичні_(семінарські)_заняття" != 0 AND academic_year."ставка" != 0
                                        THEN academic_year."практичні_(семінарські)_заняття"
                                        ELSE 0
                                    END
                                )
                                +
                                SUM(
                                    CASE
                                        WHEN academic_year."лабораторні_роботи" != 0 AND academic_year."ставка" != 0
                                        THEN academic_year."лабораторні_роботи"
                                        ELSE 0
                                    END
                                )
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN academic_year."ставка" != 0 AND (academic_year."практичні_(семінарські)_заняття" != 0 OR academic_year."лабораторні_роботи" != 0)
                                        THEN academic_year."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2)
                    +
                    (
                        SELECT

                        ROUND(
                            COALESCE(
                                SUM(
                                    CASE
                                        WHEN academic_year."лекції" != 0 AND academic_year."ставка" != 0
                                        THEN academic_year."лекції"
                                        ELSE 0
                                    END
                                )
                                /
                                NULLIF(
                                    SUM(
                                        CASE
                                            WHEN academic_year."лекції" != 0 AND academic_year."ставка" != 0
                                            THEN academic_year."ставка"
                                            ELSE 0
                                        END
                                    )
                                ,0)
                            ,0)
                        ,2)

                
                        FROM job

                        JOIN code_year ON job."код_рік_id" = code_year.id
                        JOIN first_semester ON job.id = first_semester."job_id"
                        JOIN second_semester ON job.id = second_semester."job_id"
                        JOIN academic_year ON job.id = academic_year."job_id"

                        WHERE job.'посада' = 'в.о. заф. кафедри' AND job.'НПП_ПП' = 'НПП'

                    )
                    ,2)

                
                FROM job

                JOIN code_year ON job."код_рік_id" = code_year.id
                JOIN first_semester ON job.id = first_semester."job_id"
                JOIN second_semester ON job.id = second_semester."job_id"
                JOIN academic_year ON job.id = academic_year."job_id"

                WHERE job.'НПП_ПП' = 'НПП' AND job.'посада' = 'в.о. заф. кафедри'

                UNION ALL

                SELECT
                    ROUND(
                    ROUND(
                        COALESCE(
                            (
                                SUM(
                                    CASE
                                        WHEN first_semester."практичні_(семінарські)_заняття" != 0 AND first_semester."ставка" != 0
                                        THEN first_semester."практичні_(семінарські)_заняття"
                                        ELSE 0
                                    END
                                )
                                +
                                SUM(
                                    CASE
                                        WHEN first_semester."лабораторні_роботи" != 0 AND first_semester."ставка" != 0
                                        THEN first_semester."лабораторні_роботи"
                                        ELSE 0
                                    END
                                )
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN first_semester."ставка" != 0 AND (first_semester."практичні_(семінарські)_заняття" != 0 OR first_semester."лабораторні_роботи" != 0)
                                        THEN first_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2)
                    +
                    (
                        SELECT

                        ROUND(
                            COALESCE(
                                SUM(
                                    CASE
                                        WHEN first_semester."лекції" != 0 AND first_semester."ставка" != 0
                                        THEN first_semester."лекції"
                                        ELSE 0
                                    END
                                )
                                /
                                NULLIF(
                                    SUM(
                                        CASE
                                            WHEN first_semester."лекції" != 0 AND first_semester."ставка" != 0
                                            THEN first_semester."ставка"
                                            ELSE 0
                                        END
                                    )
                                ,0)
                            ,0)
                        ,2)

                
                        FROM job

                        JOIN code_year ON job."код_рік_id" = code_year.id
                        JOIN first_semester ON job.id = first_semester."job_id"
                        JOIN second_semester ON job.id = second_semester."job_id"
                        JOIN academic_year ON job.id = academic_year."job_id"

                        WHERE job.'посада' = 'викладач' AND job.'НПП_ПП' = 'НПП'

                    ),2),

                    ROUND(
                    ROUND(
                        COALESCE(
                            (
                                SUM(
                                    CASE
                                        WHEN second_semester."практичні_(семінарські)_заняття" != 0 AND second_semester."ставка" != 0
                                        THEN second_semester."практичні_(семінарські)_заняття"
                                        ELSE 0
                                    END
                                )
                                +
                                SUM(
                                    CASE
                                        WHEN second_semester."лабораторні_роботи" != 0 AND second_semester."ставка" != 0
                                        THEN second_semester."лабораторні_роботи"
                                        ELSE 0
                                    END
                                )
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN second_semester."ставка" != 0 AND (second_semester."практичні_(семінарські)_заняття" != 0 OR second_semester."лабораторні_роботи" != 0)
                                        THEN second_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2)
                    +
                    (
                        SELECT

                        ROUND(
                            COALESCE(
                                SUM(
                                    CASE
                                        WHEN second_semester."лекції" != 0 AND second_semester."ставка" != 0
                                        THEN second_semester."лекції"
                                        ELSE 0
                                    END
                                )
                                /
                                NULLIF(
                                    SUM(
                                        CASE
                                            WHEN second_semester."лекції" != 0 AND second_semester."ставка" != 0
                                            THEN second_semester."ставка"
                                            ELSE 0
                                        END
                                    )
                                ,0)
                            ,0)
                        ,2)

                
                        FROM job

                        JOIN code_year ON job."код_рік_id" = code_year.id
                        JOIN first_semester ON job.id = first_semester."job_id"
                        JOIN second_semester ON job.id = second_semester."job_id"
                        JOIN academic_year ON job.id = academic_year."job_id"

                        WHERE job.'посада' = 'викладач' AND job.'НПП_ПП' = 'НПП'

                    ),2),

                    ROUND(
                    ROUND(
                        COALESCE(
                            (
                                SUM(
                                    CASE
                                        WHEN academic_year."практичні_(семінарські)_заняття" != 0 AND academic_year."ставка" != 0
                                        THEN academic_year."практичні_(семінарські)_заняття"
                                        ELSE 0
                                    END
                                )
                                +
                                SUM(
                                    CASE
                                        WHEN academic_year."лабораторні_роботи" != 0 AND academic_year."ставка" != 0
                                        THEN academic_year."лабораторні_роботи"
                                        ELSE 0
                                    END
                                )
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN academic_year."ставка" != 0 AND (academic_year."практичні_(семінарські)_заняття" != 0 OR academic_year."лабораторні_роботи" != 0)
                                        THEN academic_year."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2)
                    +
                    (
                        SELECT

                        ROUND(
                            COALESCE(
                                SUM(
                                    CASE
                                        WHEN academic_year."лекції" != 0 AND academic_year."ставка" != 0
                                        THEN academic_year."лекції"
                                        ELSE 0
                                    END
                                )
                                /
                                NULLIF(
                                    SUM(
                                        CASE
                                            WHEN academic_year."лекції" != 0 AND academic_year."ставка" != 0
                                            THEN academic_year."ставка"
                                            ELSE 0
                                        END
                                    )
                                ,0)
                            ,0)
                        ,2)

                
                        FROM job

                        JOIN code_year ON job."код_рік_id" = code_year.id
                        JOIN first_semester ON job.id = first_semester."job_id"
                        JOIN second_semester ON job.id = second_semester."job_id"
                        JOIN academic_year ON job.id = academic_year."job_id"

                        WHERE job.'посада' = 'викладач' AND job.'НПП_ПП' = 'НПП'

                    )
                    ,2)

                
                FROM job

                JOIN code_year ON job."код_рік_id" = code_year.id
                JOIN first_semester ON job.id = first_semester."job_id"
                JOIN second_semester ON job.id = second_semester."job_id"
                JOIN academic_year ON job.id = academic_year."job_id"

                WHERE job.'НПП_ПП' = 'НПП' AND job.'посада' = 'викладач'

     
            """)
            # 

            result = []
            for value in cursor.fetchall():
                result.append((value[0],value[1],value[2]))
            
            msg = ""
            msg += f"Середнє аудиторне навантаження НПП (заф. кафедри)\n\t перший семестр: {result[1][0]}\n\t другий семестр: {result[1][1]}\n\t рік: {result[1][2]}\n\n"
            msg += f"Середнє аудиторне навантаження НПП (професор)\n\t перший семестр: {result[2][0]}\n\t другий семестр: {result[2][1]}\n\t рік: {result[2][2]}\n\n"
            msg += f"Середнє аудиторне навантаження НПП (доцент)\n\t перший семестр: {result[3][0]}\n\t другий семестр: {result[3][1]}\n\t рік: {result[3][2]}\n\n"
            msg += f"Середнє аудиторне навантаження НПП (ст. викладач)\n\t перший семестр: {result[4][0]}\n\t другий семестр: {result[4][1]}\n\t рік: {result[4][2]}\n\n"
            msg += f"Середнє аудиторне навантаження НПП (асистент)\n\t перший семестр: {result[5][0]}\n\t другий семестр: {result[5][1]}\n\t рік: {result[5][2]}\n\n"
            msg += f"Середнє аудиторне навантаження НПП (в.о. заф. кафедри)\n\t перший семестр: {result[6][0]}\n\t другий семестр: {result[6][1]}\n\t рік: {result[6][2]}\n\n"
            msg += f"Середнє аудиторне навантаження НПП (викладач)\n\t перший семестр: {result[7][0]}\n\t другий семестр: {result[7][1]}\n\t рік: {result[7][2]}\n\n"
            msg += f"Середнє аудиторне навантаження НПП (усі)\n\t перший семестр: {result[0][0]}\n\t другий семестр: {result[0][1]}\n\t рік: {result[0][2]}\n\n"

            with open("resources\\Середнэ навантаження\\НПП\\Аудиторне\\file.txt", "w", encoding="utf-8") as f:
                f.write(msg)

            msg = "Дані збереженно у файлі: \"resources\\Середнэ навантаження\\НПП\\Аудиторне\\file.txt\".\n\n\n" + msg
            msg += "\n\n\nКлацніть по екрану і натисніть Enter - щоб вийти з данної інформації.\n\n\n"
            second_window = tk.Toplevel(root)
            second_window.title("Результат")
            second_window.attributes('-fullscreen', True)

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
            text.insert("1.0", msg)

            copy_button = tk.Button(second_window, text="Копіювати текст", font=my_font,
            command=lambda: copy_text_to_clipboard(root, text))
            copy_button.pack(pady=20)

            text.bind('<Control-v>', lambda e: paste_from_clipboard(text))

            text.bind('<Control-c>', lambda e: copy_text_to_clipboard(root, text))

            second_window.bind("<Return>", lambda e: second_window.destroy())

            def copy_text_to_clipboard(root, text_widget):
                text = text_widget.get("1.0", "end-1c") 
                pyperclip.copy(text) 


            def paste_from_clipboard(text_widget):
                try:
                    clipboard_text = pyperclip.paste()
                    text_widget.insert(tk.INSERT, clipboard_text)
                except Exception as e:
                    messagebox.showwarning("Помилка", f"Помилка при вставці: {e}")

            conn.close()
            root.after(0, loading.destroy)

        loading = loading_window(root)
        threading.Thread(target=work, args=(root, name_db, loading), daemon=True).start()

    def on_audience_pp_button_click(root, name_db):
        def work(root, name_db, loading):

            conn = sqlite3.connect(name_db)
            cursor = conn.cursor()

            cursor.execute("""
                SELECT
                    ROUND(
                    ROUND(
                        COALESCE(
                            (
                                SUM(
                                    CASE
                                        WHEN first_semester."практичні_(семінарські)_заняття" != 0 AND first_semester."ставка" != 0
                                        THEN first_semester."практичні_(семінарські)_заняття"
                                        ELSE 0
                                    END
                                )
                                +
                                SUM(
                                    CASE
                                        WHEN first_semester."лабораторні_роботи" != 0 AND first_semester."ставка" != 0
                                        THEN first_semester."лабораторні_роботи"
                                        ELSE 0
                                    END
                                )
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN first_semester."ставка" != 0 AND (first_semester."практичні_(семінарські)_заняття" != 0 OR first_semester."лабораторні_роботи" != 0)
                                        THEN first_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2)
                    +
                    (
                        SELECT

                        ROUND(
                            COALESCE(
                                SUM(
                                    CASE
                                        WHEN first_semester."лекції" != 0 AND first_semester."ставка" != 0
                                        THEN first_semester."лекції"
                                        ELSE 0
                                    END
                                )
                                /
                                NULLIF(
                                    SUM(
                                        CASE
                                            WHEN first_semester."лекції" != 0 AND first_semester."ставка" != 0
                                            THEN first_semester."ставка"
                                            ELSE 0
                                        END
                                    )
                                ,0)
                            ,0)
                        ,2)

 
                        FROM job

                        JOIN code_year ON job."код_рік_id" = code_year.id
                        JOIN first_semester ON job.id = first_semester."job_id"
                        JOIN second_semester ON job.id = second_semester."job_id"
                        JOIN academic_year ON job.id = academic_year."job_id"

                        WHERE job.'посада' != 'асистент' AND job.'НПП_ПП' = 'ПП'

                    ),2),

                    ROUND(
                    ROUND(
                        COALESCE(
                            (
                                SUM(
                                    CASE
                                        WHEN second_semester."практичні_(семінарські)_заняття" != 0 AND second_semester."ставка" != 0
                                        THEN second_semester."практичні_(семінарські)_заняття"
                                        ELSE 0
                                    END
                                )
                                +
                                SUM(
                                    CASE
                                        WHEN second_semester."лабораторні_роботи" != 0 AND second_semester."ставка" != 0
                                        THEN second_semester."лабораторні_роботи"
                                        ELSE 0
                                    END
                                )
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN second_semester."ставка" != 0 AND (second_semester."практичні_(семінарські)_заняття" != 0 OR second_semester."лабораторні_роботи" != 0)
                                        THEN second_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2)
                    +
                    (
                        SELECT

                        ROUND(
                            COALESCE(
                                SUM(
                                    CASE
                                        WHEN second_semester."лекції" != 0 AND second_semester."ставка" != 0
                                        THEN second_semester."лекції"
                                        ELSE 0
                                    END
                                )
                                /
                                NULLIF(
                                    SUM(
                                        CASE
                                            WHEN second_semester."лекції" != 0 AND second_semester."ставка" != 0
                                            THEN second_semester."ставка"
                                            ELSE 0
                                        END
                                    )
                                ,0)
                            ,0)
                        ,2)

 
                        FROM job

                        JOIN code_year ON job."код_рік_id" = code_year.id
                        JOIN first_semester ON job.id = first_semester."job_id"
                        JOIN second_semester ON job.id = second_semester."job_id"
                        JOIN academic_year ON job.id = academic_year."job_id"

                        WHERE job.'посада' != 'асистент' AND job.'НПП_ПП' = 'ПП'

                    ),2),

                    ROUND(
                    ROUND(
                        COALESCE(
                            (
                                SUM(
                                    CASE
                                        WHEN academic_year."практичні_(семінарські)_заняття" != 0 AND academic_year."ставка" != 0
                                        THEN academic_year."практичні_(семінарські)_заняття"
                                        ELSE 0
                                    END
                                )
                                +
                                SUM(
                                    CASE
                                        WHEN academic_year."лабораторні_роботи" != 0 AND academic_year."ставка" != 0
                                        THEN academic_year."лабораторні_роботи"
                                        ELSE 0
                                    END
                                )
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN academic_year."ставка" != 0 AND (academic_year."практичні_(семінарські)_заняття" != 0 OR academic_year."лабораторні_роботи" != 0)
                                        THEN academic_year."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2)
                    +
                    (
                        SELECT

                        ROUND(
                            COALESCE(
                                SUM(
                                    CASE
                                        WHEN academic_year."лекції" != 0 AND academic_year."ставка" != 0
                                        THEN academic_year."лекції"
                                        ELSE 0
                                    END
                                )
                                /
                                NULLIF(
                                    SUM(
                                        CASE
                                            WHEN academic_year."лекції" != 0 AND academic_year."ставка" != 0
                                            THEN academic_year."ставка"
                                            ELSE 0
                                        END
                                    )
                                ,0)
                            ,0)
                        ,2)

 
                        FROM job

                        JOIN code_year ON job."код_рік_id" = code_year.id
                        JOIN first_semester ON job.id = first_semester."job_id"
                        JOIN second_semester ON job.id = second_semester."job_id"
                        JOIN academic_year ON job.id = academic_year."job_id"

                        WHERE job.'посада' != 'асистент' AND job.'НПП_ПП' = 'ПП'

                    )
                    ,2)

 
                FROM job

                JOIN code_year ON job."код_рік_id" = code_year.id
                JOIN first_semester ON job.id = first_semester."job_id"
                JOIN second_semester ON job.id = second_semester."job_id"
                JOIN academic_year ON job.id = academic_year."job_id"

                WHERE job.'НПП_ПП' = 'ПП'

                UNION ALL

                SELECT
                    ROUND(
                    ROUND(
                        COALESCE(
                            (
                                SUM(
                                    CASE
                                        WHEN first_semester."практичні_(семінарські)_заняття" != 0 AND first_semester."ставка" != 0
                                        THEN first_semester."практичні_(семінарські)_заняття"
                                        ELSE 0
                                    END
                                )
                                +
                                SUM(
                                    CASE
                                        WHEN first_semester."лабораторні_роботи" != 0 AND first_semester."ставка" != 0
                                        THEN first_semester."лабораторні_роботи"
                                        ELSE 0
                                    END
                                )
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN first_semester."ставка" != 0 AND (first_semester."практичні_(семінарські)_заняття" != 0 OR first_semester."лабораторні_роботи" != 0)
                                        THEN first_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2)
                    +
                    (
                        SELECT

                        ROUND(
                            COALESCE(
                                SUM(
                                    CASE
                                        WHEN first_semester."лекції" != 0 AND first_semester."ставка" != 0
                                        THEN first_semester."лекції"
                                        ELSE 0
                                    END
                                )
                                /
                                NULLIF(
                                    SUM(
                                        CASE
                                            WHEN first_semester."лекції" != 0 AND first_semester."ставка" != 0
                                            THEN first_semester."ставка"
                                            ELSE 0
                                        END
                                    )
                                ,0)
                            ,0)
                        ,2)

 
                        FROM job

                        JOIN code_year ON job."код_рік_id" = code_year.id
                        JOIN first_semester ON job.id = first_semester."job_id"
                        JOIN second_semester ON job.id = second_semester."job_id"
                        JOIN academic_year ON job.id = academic_year."job_id"

                        WHERE job.'посада' = 'заф. кафедри' AND job.'НПП_ПП' = 'ПП'

                    ),2),

                    ROUND(
                    ROUND(
                        COALESCE(
                            (
                                SUM(
                                    CASE
                                        WHEN second_semester."практичні_(семінарські)_заняття" != 0 AND second_semester."ставка" != 0
                                        THEN second_semester."практичні_(семінарські)_заняття"
                                        ELSE 0
                                    END
                                )
                                +
                                SUM(
                                    CASE
                                        WHEN second_semester."лабораторні_роботи" != 0 AND second_semester."ставка" != 0
                                        THEN second_semester."лабораторні_роботи"
                                        ELSE 0
                                    END
                                )
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN second_semester."ставка" != 0 AND (second_semester."практичні_(семінарські)_заняття" != 0 OR second_semester."лабораторні_роботи" != 0)
                                        THEN second_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2)
                    +
                    (
                        SELECT

                        ROUND(
                            COALESCE(
                                SUM(
                                    CASE
                                        WHEN second_semester."лекції" != 0 AND second_semester."ставка" != 0
                                        THEN second_semester."лекції"
                                        ELSE 0
                                    END
                                )
                                /
                                NULLIF(
                                    SUM(
                                        CASE
                                            WHEN second_semester."лекції" != 0 AND second_semester."ставка" != 0
                                            THEN second_semester."ставка"
                                            ELSE 0
                                        END
                                    )
                                ,0)
                            ,0)
                        ,2)

 
                        FROM job

                        JOIN code_year ON job."код_рік_id" = code_year.id
                        JOIN first_semester ON job.id = first_semester."job_id"
                        JOIN second_semester ON job.id = second_semester."job_id"
                        JOIN academic_year ON job.id = academic_year."job_id"

                        WHERE job.'посада' = 'заф. кафедри' AND job.'НПП_ПП' = 'ПП'

                    ),2),

                    ROUND(
                    ROUND(
                        COALESCE(
                            (
                                SUM(
                                    CASE
                                        WHEN academic_year."практичні_(семінарські)_заняття" != 0 AND academic_year."ставка" != 0
                                        THEN academic_year."практичні_(семінарські)_заняття"
                                        ELSE 0
                                    END
                                )
                                +
                                SUM(
                                    CASE
                                        WHEN academic_year."лабораторні_роботи" != 0 AND academic_year."ставка" != 0
                                        THEN academic_year."лабораторні_роботи"
                                        ELSE 0
                                    END
                                )
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN academic_year."ставка" != 0 AND (academic_year."практичні_(семінарські)_заняття" != 0 OR academic_year."лабораторні_роботи" != 0)
                                        THEN academic_year."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2)
                    +
                    (
                        SELECT

                        ROUND(
                            COALESCE(
                                SUM(
                                    CASE
                                        WHEN academic_year."лекції" != 0 AND academic_year."ставка" != 0
                                        THEN academic_year."лекції"
                                        ELSE 0
                                    END
                                )
                                /
                                NULLIF(
                                    SUM(
                                        CASE
                                            WHEN academic_year."лекції" != 0 AND academic_year."ставка" != 0
                                            THEN academic_year."ставка"
                                            ELSE 0
                                        END
                                    )
                                ,0)
                            ,0)
                        ,2)

 
                        FROM job

                        JOIN code_year ON job."код_рік_id" = code_year.id
                        JOIN first_semester ON job.id = first_semester."job_id"
                        JOIN second_semester ON job.id = second_semester."job_id"
                        JOIN academic_year ON job.id = academic_year."job_id"

                        WHERE job.'посада' = 'заф. кафедри' AND job.'НПП_ПП' = 'ПП'

                    )
                    ,2)

 
                FROM job

                JOIN code_year ON job."код_рік_id" = code_year.id
                JOIN first_semester ON job.id = first_semester."job_id"
                JOIN second_semester ON job.id = second_semester."job_id"
                JOIN academic_year ON job.id = academic_year."job_id"

                WHERE job.'НПП_ПП' = 'ПП' AND job.'посада' = 'заф. кафедри'

                UNION ALL

                SELECT
                    ROUND(
                    ROUND(
                        COALESCE(
                            (
                                SUM(
                                    CASE
                                        WHEN first_semester."практичні_(семінарські)_заняття" != 0 AND first_semester."ставка" != 0
                                        THEN first_semester."практичні_(семінарські)_заняття"
                                        ELSE 0
                                    END
                                )
                                +
                                SUM(
                                    CASE
                                        WHEN first_semester."лабораторні_роботи" != 0 AND first_semester."ставка" != 0
                                        THEN first_semester."лабораторні_роботи"
                                        ELSE 0
                                    END
                                )
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN first_semester."ставка" != 0 AND (first_semester."практичні_(семінарські)_заняття" != 0 OR first_semester."лабораторні_роботи" != 0)
                                        THEN first_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2)
                    +
                    (
                        SELECT

                        ROUND(
                            COALESCE(
                                SUM(
                                    CASE
                                        WHEN first_semester."лекції" != 0 AND first_semester."ставка" != 0
                                        THEN first_semester."лекції"
                                        ELSE 0
                                    END
                                )
                                /
                                NULLIF(
                                    SUM(
                                        CASE
                                            WHEN first_semester."лекції" != 0 AND first_semester."ставка" != 0
                                            THEN first_semester."ставка"
                                            ELSE 0
                                        END
                                    )
                                ,0)
                            ,0)
                        ,2)

 
                        FROM job

                        JOIN code_year ON job."код_рік_id" = code_year.id
                        JOIN first_semester ON job.id = first_semester."job_id"
                        JOIN second_semester ON job.id = second_semester."job_id"
                        JOIN academic_year ON job.id = academic_year."job_id"

                        WHERE job.'посада' = 'професор' AND job.'НПП_ПП' = 'ПП'

                    ),2),

                    ROUND(
                    ROUND(
                        COALESCE(
                            (
                                SUM(
                                    CASE
                                        WHEN second_semester."практичні_(семінарські)_заняття" != 0 AND second_semester."ставка" != 0
                                        THEN second_semester."практичні_(семінарські)_заняття"
                                        ELSE 0
                                    END
                                )
                                +
                                SUM(
                                    CASE
                                        WHEN second_semester."лабораторні_роботи" != 0 AND second_semester."ставка" != 0
                                        THEN second_semester."лабораторні_роботи"
                                        ELSE 0
                                    END
                                )
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN second_semester."ставка" != 0 AND (second_semester."практичні_(семінарські)_заняття" != 0 OR second_semester."лабораторні_роботи" != 0)
                                        THEN second_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2)
                    +
                    (
                        SELECT

                        ROUND(
                            COALESCE(
                                SUM(
                                    CASE
                                        WHEN second_semester."лекції" != 0 AND second_semester."ставка" != 0
                                        THEN second_semester."лекції"
                                        ELSE 0
                                    END
                                )
                                /
                                NULLIF(
                                    SUM(
                                        CASE
                                            WHEN second_semester."лекції" != 0 AND second_semester."ставка" != 0
                                            THEN second_semester."ставка"
                                            ELSE 0
                                        END
                                    )
                                ,0)
                            ,0)
                        ,2)

 
                        FROM job

                        JOIN code_year ON job."код_рік_id" = code_year.id
                        JOIN first_semester ON job.id = first_semester."job_id"
                        JOIN second_semester ON job.id = second_semester."job_id"
                        JOIN academic_year ON job.id = academic_year."job_id"

                        WHERE job.'посада' = 'професор' AND job.'НПП_ПП' = 'ПП'

                    ),2),

                    ROUND(
                    ROUND(
                        COALESCE(
                            (
                                SUM(
                                    CASE
                                        WHEN academic_year."практичні_(семінарські)_заняття" != 0 AND academic_year."ставка" != 0
                                        THEN academic_year."практичні_(семінарські)_заняття"
                                        ELSE 0
                                    END
                                )
                                +
                                SUM(
                                    CASE
                                        WHEN academic_year."лабораторні_роботи" != 0 AND academic_year."ставка" != 0
                                        THEN academic_year."лабораторні_роботи"
                                        ELSE 0
                                    END
                                )
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN academic_year."ставка" != 0 AND (academic_year."практичні_(семінарські)_заняття" != 0 OR academic_year."лабораторні_роботи" != 0)
                                        THEN academic_year."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2)
                    +
                    (
                        SELECT

                        ROUND(
                            COALESCE(
                                SUM(
                                    CASE
                                        WHEN academic_year."лекції" != 0 AND academic_year."ставка" != 0
                                        THEN academic_year."лекції"
                                        ELSE 0
                                    END
                                )
                                /
                                NULLIF(
                                    SUM(
                                        CASE
                                            WHEN academic_year."лекції" != 0 AND academic_year."ставка" != 0
                                            THEN academic_year."ставка"
                                            ELSE 0
                                        END
                                    )
                                ,0)
                            ,0)
                        ,2)

 
                        FROM job

                        JOIN code_year ON job."код_рік_id" = code_year.id
                        JOIN first_semester ON job.id = first_semester."job_id"
                        JOIN second_semester ON job.id = second_semester."job_id"
                        JOIN academic_year ON job.id = academic_year."job_id"

                        WHERE job.'посада' = 'професор' AND job.'НПП_ПП' = 'ПП'

                    )
                    ,2)

 
                FROM job

                JOIN code_year ON job."код_рік_id" = code_year.id
                JOIN first_semester ON job.id = first_semester."job_id"
                JOIN second_semester ON job.id = second_semester."job_id"
                JOIN academic_year ON job.id = academic_year."job_id"

                WHERE job.'НПП_ПП' = 'ПП' AND job.'посада' = 'професор'

                UNION ALL

                SELECT
                    ROUND(
                    ROUND(
                        COALESCE(
                            (
                                SUM(
                                    CASE
                                        WHEN first_semester."практичні_(семінарські)_заняття" != 0 AND first_semester."ставка" != 0
                                        THEN first_semester."практичні_(семінарські)_заняття"
                                        ELSE 0
                                    END
                                )
                                +
                                SUM(
                                    CASE
                                        WHEN first_semester."лабораторні_роботи" != 0 AND first_semester."ставка" != 0
                                        THEN first_semester."лабораторні_роботи"
                                        ELSE 0
                                    END
                                )
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN first_semester."ставка" != 0 AND (first_semester."практичні_(семінарські)_заняття" != 0 OR first_semester."лабораторні_роботи" != 0)
                                        THEN first_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2)
                    +
                    (
                        SELECT

                        ROUND(
                            COALESCE(
                                SUM(
                                    CASE
                                        WHEN first_semester."лекції" != 0 AND first_semester."ставка" != 0
                                        THEN first_semester."лекції"
                                        ELSE 0
                                    END
                                )
                                /
                                NULLIF(
                                    SUM(
                                        CASE
                                            WHEN first_semester."лекції" != 0 AND first_semester."ставка" != 0
                                            THEN first_semester."ставка"
                                            ELSE 0
                                        END
                                    )
                                ,0)
                            ,0)
                        ,2)

 
                        FROM job

                        JOIN code_year ON job."код_рік_id" = code_year.id
                        JOIN first_semester ON job.id = first_semester."job_id"
                        JOIN second_semester ON job.id = second_semester."job_id"
                        JOIN academic_year ON job.id = academic_year."job_id"

                        WHERE job.'посада' = 'доцент' AND job.'НПП_ПП' = 'ПП'

                    ),2),

                    ROUND(
                    ROUND(
                        COALESCE(
                            (
                                SUM(
                                    CASE
                                        WHEN second_semester."практичні_(семінарські)_заняття" != 0 AND second_semester."ставка" != 0
                                        THEN second_semester."практичні_(семінарські)_заняття"
                                        ELSE 0
                                    END
                                )
                                +
                                SUM(
                                    CASE
                                        WHEN second_semester."лабораторні_роботи" != 0 AND second_semester."ставка" != 0
                                        THEN second_semester."лабораторні_роботи"
                                        ELSE 0
                                    END
                                )
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN second_semester."ставка" != 0 AND (second_semester."практичні_(семінарські)_заняття" != 0 OR second_semester."лабораторні_роботи" != 0)
                                        THEN second_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2)
                    +
                    (
                        SELECT

                        ROUND(
                            COALESCE(
                                SUM(
                                    CASE
                                        WHEN second_semester."лекції" != 0 AND second_semester."ставка" != 0
                                        THEN second_semester."лекції"
                                        ELSE 0
                                    END
                                )
                                /
                                NULLIF(
                                    SUM(
                                        CASE
                                            WHEN second_semester."лекції" != 0 AND second_semester."ставка" != 0
                                            THEN second_semester."ставка"
                                            ELSE 0
                                        END
                                    )
                                ,0)
                            ,0)
                        ,2)

 
                        FROM job

                        JOIN code_year ON job."код_рік_id" = code_year.id
                        JOIN first_semester ON job.id = first_semester."job_id"
                        JOIN second_semester ON job.id = second_semester."job_id"
                        JOIN academic_year ON job.id = academic_year."job_id"

                        WHERE job.'посада' = 'доцент' AND job.'НПП_ПП' = 'ПП'

                    ),2),

                    ROUND(
                    ROUND(
                        COALESCE(
                            (
                                SUM(
                                    CASE
                                        WHEN academic_year."практичні_(семінарські)_заняття" != 0 AND academic_year."ставка" != 0
                                        THEN academic_year."практичні_(семінарські)_заняття"
                                        ELSE 0
                                    END
                                )
                                +
                                SUM(
                                    CASE
                                        WHEN academic_year."лабораторні_роботи" != 0 AND academic_year."ставка" != 0
                                        THEN academic_year."лабораторні_роботи"
                                        ELSE 0
                                    END
                                )
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN academic_year."ставка" != 0 AND (academic_year."практичні_(семінарські)_заняття" != 0 OR academic_year."лабораторні_роботи" != 0)
                                        THEN academic_year."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2)
                    +
                    (
                        SELECT

                        ROUND(
                            COALESCE(
                                SUM(
                                    CASE
                                        WHEN academic_year."лекції" != 0 AND academic_year."ставка" != 0
                                        THEN academic_year."лекції"
                                        ELSE 0
                                    END
                                )
                                /
                                NULLIF(
                                    SUM(
                                        CASE
                                            WHEN academic_year."лекції" != 0 AND academic_year."ставка" != 0
                                            THEN academic_year."ставка"
                                            ELSE 0
                                        END
                                    )
                                ,0)
                            ,0)
                        ,2)

 
                        FROM job

                        JOIN code_year ON job."код_рік_id" = code_year.id
                        JOIN first_semester ON job.id = first_semester."job_id"
                        JOIN second_semester ON job.id = second_semester."job_id"
                        JOIN academic_year ON job.id = academic_year."job_id"

                        WHERE job.'посада' = 'доцент' AND job.'НПП_ПП' = 'ПП'

                    )
                    ,2)

 
                FROM job

                JOIN code_year ON job."код_рік_id" = code_year.id
                JOIN first_semester ON job.id = first_semester."job_id"
                JOIN second_semester ON job.id = second_semester."job_id"
                JOIN academic_year ON job.id = academic_year."job_id"

                WHERE job.'НПП_ПП' = 'ПП' AND job.'посада' = 'доцент'


                UNION ALL

                SELECT
                    ROUND(
                    ROUND(
                        COALESCE(
                            (
                                SUM(
                                    CASE
                                        WHEN first_semester."практичні_(семінарські)_заняття" != 0 AND first_semester."ставка" != 0
                                        THEN first_semester."практичні_(семінарські)_заняття"
                                        ELSE 0
                                    END
                                )
                                +
                                SUM(
                                    CASE
                                        WHEN first_semester."лабораторні_роботи" != 0 AND first_semester."ставка" != 0
                                        THEN first_semester."лабораторні_роботи"
                                        ELSE 0
                                    END
                                )
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN first_semester."ставка" != 0 AND (first_semester."практичні_(семінарські)_заняття" != 0 OR first_semester."лабораторні_роботи" != 0)
                                        THEN first_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2)
                    +
                    (
                        SELECT

                        ROUND(
                            COALESCE(
                                SUM(
                                    CASE
                                        WHEN first_semester."лекції" != 0 AND first_semester."ставка" != 0
                                        THEN first_semester."лекції"
                                        ELSE 0
                                    END
                                )
                                /
                                NULLIF(
                                    SUM(
                                        CASE
                                            WHEN first_semester."лекції" != 0 AND first_semester."ставка" != 0
                                            THEN first_semester."ставка"
                                            ELSE 0
                                        END
                                    )
                                ,0)
                            ,0)
                        ,2)

 
                        FROM job

                        JOIN code_year ON job."код_рік_id" = code_year.id
                        JOIN first_semester ON job.id = first_semester."job_id"
                        JOIN second_semester ON job.id = second_semester."job_id"
                        JOIN academic_year ON job.id = academic_year."job_id"

                        WHERE job.'посада' = 'ст. викладач' AND job.'НПП_ПП' = 'ПП'

                    ),2),

                    ROUND(
                    ROUND(
                        COALESCE(
                            (
                                SUM(
                                    CASE
                                        WHEN second_semester."практичні_(семінарські)_заняття" != 0 AND second_semester."ставка" != 0
                                        THEN second_semester."практичні_(семінарські)_заняття"
                                        ELSE 0
                                    END
                                )
                                +
                                SUM(
                                    CASE
                                        WHEN second_semester."лабораторні_роботи" != 0 AND second_semester."ставка" != 0
                                        THEN second_semester."лабораторні_роботи"
                                        ELSE 0
                                    END
                                )
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN second_semester."ставка" != 0 AND (second_semester."практичні_(семінарські)_заняття" != 0 OR second_semester."лабораторні_роботи" != 0)
                                        THEN second_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2)
                    +
                    (
                        SELECT

                        ROUND(
                            COALESCE(
                                SUM(
                                    CASE
                                        WHEN second_semester."лекції" != 0 AND second_semester."ставка" != 0
                                        THEN second_semester."лекції"
                                        ELSE 0
                                    END
                                )
                                /
                                NULLIF(
                                    SUM(
                                        CASE
                                            WHEN second_semester."лекції" != 0 AND second_semester."ставка" != 0
                                            THEN second_semester."ставка"
                                            ELSE 0
                                        END
                                    )
                                ,0)
                            ,0)
                        ,2)

 
                        FROM job

                        JOIN code_year ON job."код_рік_id" = code_year.id
                        JOIN first_semester ON job.id = first_semester."job_id"
                        JOIN second_semester ON job.id = second_semester."job_id"
                        JOIN academic_year ON job.id = academic_year."job_id"

                        WHERE job.'посада' = 'ст. викладач' AND job.'НПП_ПП' = 'ПП'

                    ),2),

                    ROUND(
                    ROUND(
                        COALESCE(
                            (
                                SUM(
                                    CASE
                                        WHEN academic_year."практичні_(семінарські)_заняття" != 0 AND academic_year."ставка" != 0
                                        THEN academic_year."практичні_(семінарські)_заняття"
                                        ELSE 0
                                    END
                                )
                                +
                                SUM(
                                    CASE
                                        WHEN academic_year."лабораторні_роботи" != 0 AND academic_year."ставка" != 0
                                        THEN academic_year."лабораторні_роботи"
                                        ELSE 0
                                    END
                                )
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN academic_year."ставка" != 0 AND (academic_year."практичні_(семінарські)_заняття" != 0 OR academic_year."лабораторні_роботи" != 0)
                                        THEN academic_year."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2)
                    +
                    (
                        SELECT

                        ROUND(
                            COALESCE(
                                SUM(
                                    CASE
                                        WHEN academic_year."лекції" != 0 AND academic_year."ставка" != 0
                                        THEN academic_year."лекції"
                                        ELSE 0
                                    END
                                )
                                /
                                NULLIF(
                                    SUM(
                                        CASE
                                            WHEN academic_year."лекції" != 0 AND academic_year."ставка" != 0
                                            THEN academic_year."ставка"
                                            ELSE 0
                                        END
                                    )
                                ,0)
                            ,0)
                        ,2)

 
                        FROM job

                        JOIN code_year ON job."код_рік_id" = code_year.id
                        JOIN first_semester ON job.id = first_semester."job_id"
                        JOIN second_semester ON job.id = second_semester."job_id"
                        JOIN academic_year ON job.id = academic_year."job_id"

                        WHERE job.'посада' = 'ст. викладач' AND job.'НПП_ПП' = 'ПП'

                    )
                    ,2)

 
                FROM job

                JOIN code_year ON job."код_рік_id" = code_year.id
                JOIN first_semester ON job.id = first_semester."job_id"
                JOIN second_semester ON job.id = second_semester."job_id"
                JOIN academic_year ON job.id = academic_year."job_id"

                WHERE job.'НПП_ПП' = 'ПП' AND job.'посада' = 'ст. викладач'

                UNION ALL

                SELECT
                    ROUND(
                    ROUND(
                        COALESCE(
                            (
                                SUM(
                                    CASE
                                        WHEN first_semester."практичні_(семінарські)_заняття" != 0 AND first_semester."ставка" != 0
                                        THEN first_semester."практичні_(семінарські)_заняття"
                                        ELSE 0
                                    END
                                )
                                +
                                SUM(
                                    CASE
                                        WHEN first_semester."лабораторні_роботи" != 0 AND first_semester."ставка" != 0
                                        THEN first_semester."лабораторні_роботи"
                                        ELSE 0
                                    END
                                )
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN first_semester."ставка" != 0 AND (first_semester."практичні_(семінарські)_заняття" != 0 OR first_semester."лабораторні_роботи" != 0)
                                        THEN first_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2),2),

                    ROUND(
                    ROUND(
                        COALESCE(
                            (
                                SUM(
                                    CASE
                                        WHEN second_semester."практичні_(семінарські)_заняття" != 0 AND second_semester."ставка" != 0
                                        THEN second_semester."практичні_(семінарські)_заняття"
                                        ELSE 0
                                    END
                                )
                                +
                                SUM(
                                    CASE
                                        WHEN second_semester."лабораторні_роботи" != 0 AND second_semester."ставка" != 0
                                        THEN second_semester."лабораторні_роботи"
                                        ELSE 0
                                    END
                                )
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN second_semester."ставка" != 0 AND (second_semester."практичні_(семінарські)_заняття" != 0 OR second_semester."лабораторні_роботи" != 0)
                                        THEN second_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2),2),

                    ROUND(
                    ROUND(
                        COALESCE(
                            (
                                SUM(
                                    CASE
                                        WHEN academic_year."практичні_(семінарські)_заняття" != 0 AND academic_year."ставка" != 0
                                        THEN academic_year."практичні_(семінарські)_заняття"
                                        ELSE 0
                                    END
                                )
                                +
                                SUM(
                                    CASE
                                        WHEN academic_year."лабораторні_роботи" != 0 AND academic_year."ставка" != 0
                                        THEN academic_year."лабораторні_роботи"
                                        ELSE 0
                                    END
                                )
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN academic_year."ставка" != 0 AND (academic_year."практичні_(семінарські)_заняття" != 0 OR academic_year."лабораторні_роботи" != 0)
                                        THEN academic_year."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2)
                    ,2)

 
                FROM job

                JOIN code_year ON job."код_рік_id" = code_year.id
                JOIN first_semester ON job.id = first_semester."job_id"
                JOIN second_semester ON job.id = second_semester."job_id"
                JOIN academic_year ON job.id = academic_year."job_id"

                WHERE job.'НПП_ПП' = 'ПП' AND job.'посада' = 'асистент'

                UNION ALL

                SELECT
                    ROUND(
                    ROUND(
                        COALESCE(
                            (
                                SUM(
                                    CASE
                                        WHEN first_semester."практичні_(семінарські)_заняття" != 0 AND first_semester."ставка" != 0
                                        THEN first_semester."практичні_(семінарські)_заняття"
                                        ELSE 0
                                    END
                                )
                                +
                                SUM(
                                    CASE
                                        WHEN first_semester."лабораторні_роботи" != 0 AND first_semester."ставка" != 0
                                        THEN first_semester."лабораторні_роботи"
                                        ELSE 0
                                    END
                                )
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN first_semester."ставка" != 0 AND (first_semester."практичні_(семінарські)_заняття" != 0 OR first_semester."лабораторні_роботи" != 0)
                                        THEN first_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2)
                    +
                    (
                        SELECT

                        ROUND(
                            COALESCE(
                                SUM(
                                    CASE
                                        WHEN first_semester."лекції" != 0 AND first_semester."ставка" != 0
                                        THEN first_semester."лекції"
                                        ELSE 0
                                    END
                                )
                                /
                                NULLIF(
                                    SUM(
                                        CASE
                                            WHEN first_semester."лекції" != 0 AND first_semester."ставка" != 0
                                            THEN first_semester."ставка"
                                            ELSE 0
                                        END
                                    )
                                ,0)
                            ,0)
                        ,2)

 
                        FROM job

                        JOIN code_year ON job."код_рік_id" = code_year.id
                        JOIN first_semester ON job.id = first_semester."job_id"
                        JOIN second_semester ON job.id = second_semester."job_id"
                        JOIN academic_year ON job.id = academic_year."job_id"

                        WHERE job.'посада' = 'в.о. заф. кафедри' AND job.'НПП_ПП' = 'ПП'

                    ),2),

                    ROUND(
                    ROUND(
                        COALESCE(
                            (
                                SUM(
                                    CASE
                                        WHEN second_semester."практичні_(семінарські)_заняття" != 0 AND second_semester."ставка" != 0
                                        THEN second_semester."практичні_(семінарські)_заняття"
                                        ELSE 0
                                    END
                                )
                                +
                                SUM(
                                    CASE
                                        WHEN second_semester."лабораторні_роботи" != 0 AND second_semester."ставка" != 0
                                        THEN second_semester."лабораторні_роботи"
                                        ELSE 0
                                    END
                                )
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN second_semester."ставка" != 0 AND (second_semester."практичні_(семінарські)_заняття" != 0 OR second_semester."лабораторні_роботи" != 0)
                                        THEN second_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2)
                    +
                    (
                        SELECT

                        ROUND(
                            COALESCE(
                                SUM(
                                    CASE
                                        WHEN second_semester."лекції" != 0 AND second_semester."ставка" != 0
                                        THEN second_semester."лекції"
                                        ELSE 0
                                    END
                                )
                                /
                                NULLIF(
                                    SUM(
                                        CASE
                                            WHEN second_semester."лекції" != 0 AND second_semester."ставка" != 0
                                            THEN second_semester."ставка"
                                            ELSE 0
                                        END
                                    )
                                ,0)
                            ,0)
                        ,2)

 
                        FROM job

                        JOIN code_year ON job."код_рік_id" = code_year.id
                        JOIN first_semester ON job.id = first_semester."job_id"
                        JOIN second_semester ON job.id = second_semester."job_id"
                        JOIN academic_year ON job.id = academic_year."job_id"

                        WHERE job.'посада' = 'в.о. заф. кафедри' AND job.'НПП_ПП' = 'ПП'

                    ),2),

                    ROUND(
                    ROUND(
                        COALESCE(
                            (
                                SUM(
                                    CASE
                                        WHEN academic_year."практичні_(семінарські)_заняття" != 0 AND academic_year."ставка" != 0
                                        THEN academic_year."практичні_(семінарські)_заняття"
                                        ELSE 0
                                    END
                                )
                                +
                                SUM(
                                    CASE
                                        WHEN academic_year."лабораторні_роботи" != 0 AND academic_year."ставка" != 0
                                        THEN academic_year."лабораторні_роботи"
                                        ELSE 0
                                    END
                                )
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN academic_year."ставка" != 0 AND (academic_year."практичні_(семінарські)_заняття" != 0 OR academic_year."лабораторні_роботи" != 0)
                                        THEN academic_year."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2)
                    +
                    (
                        SELECT

                        ROUND(
                            COALESCE(
                                SUM(
                                    CASE
                                        WHEN academic_year."лекції" != 0 AND academic_year."ставка" != 0
                                        THEN academic_year."лекції"
                                        ELSE 0
                                    END
                                )
                                /
                                NULLIF(
                                    SUM(
                                        CASE
                                            WHEN academic_year."лекції" != 0 AND academic_year."ставка" != 0
                                            THEN academic_year."ставка"
                                            ELSE 0
                                        END
                                    )
                                ,0)
                            ,0)
                        ,2)

 
                        FROM job

                        JOIN code_year ON job."код_рік_id" = code_year.id
                        JOIN first_semester ON job.id = first_semester."job_id"
                        JOIN second_semester ON job.id = second_semester."job_id"
                        JOIN academic_year ON job.id = academic_year."job_id"

                        WHERE job.'посада' = 'в.о. заф. кафедри' AND job.'НПП_ПП' = 'ПП'

                    )
                    ,2)

 
                FROM job

                JOIN code_year ON job."код_рік_id" = code_year.id
                JOIN first_semester ON job.id = first_semester."job_id"
                JOIN second_semester ON job.id = second_semester."job_id"
                JOIN academic_year ON job.id = academic_year."job_id"

                WHERE job.'НПП_ПП' = 'ПП' AND job.'посада' = 'в.о. заф. кафедри'

                UNION ALL

                SELECT
                    ROUND(
                    ROUND(
                        COALESCE(
                            (
                                SUM(
                                    CASE
                                        WHEN first_semester."практичні_(семінарські)_заняття" != 0 AND first_semester."ставка" != 0
                                        THEN first_semester."практичні_(семінарські)_заняття"
                                        ELSE 0
                                    END
                                )
                                +
                                SUM(
                                    CASE
                                        WHEN first_semester."лабораторні_роботи" != 0 AND first_semester."ставка" != 0
                                        THEN first_semester."лабораторні_роботи"
                                        ELSE 0
                                    END
                                )
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN first_semester."ставка" != 0 AND (first_semester."практичні_(семінарські)_заняття" != 0 OR first_semester."лабораторні_роботи" != 0)
                                        THEN first_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2)
                    +
                    (
                        SELECT

                        ROUND(
                            COALESCE(
                                SUM(
                                    CASE
                                        WHEN first_semester."лекції" != 0 AND first_semester."ставка" != 0
                                        THEN first_semester."лекції"
                                        ELSE 0
                                    END
                                )
                                /
                                NULLIF(
                                    SUM(
                                        CASE
                                            WHEN first_semester."лекції" != 0 AND first_semester."ставка" != 0
                                            THEN first_semester."ставка"
                                            ELSE 0
                                        END
                                    )
                                ,0)
                            ,0)
                        ,2)

 
                        FROM job

                        JOIN code_year ON job."код_рік_id" = code_year.id
                        JOIN first_semester ON job.id = first_semester."job_id"
                        JOIN second_semester ON job.id = second_semester."job_id"
                        JOIN academic_year ON job.id = academic_year."job_id"

                        WHERE job.'посада' = 'викладач' AND job.'НПП_ПП' = 'ПП'

                    ),2),

                    ROUND(
                    ROUND(
                        COALESCE(
                            (
                                SUM(
                                    CASE
                                        WHEN second_semester."практичні_(семінарські)_заняття" != 0 AND second_semester."ставка" != 0
                                        THEN second_semester."практичні_(семінарські)_заняття"
                                        ELSE 0
                                    END
                                )
                                +
                                SUM(
                                    CASE
                                        WHEN second_semester."лабораторні_роботи" != 0 AND second_semester."ставка" != 0
                                        THEN second_semester."лабораторні_роботи"
                                        ELSE 0
                                    END
                                )
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN second_semester."ставка" != 0 AND (second_semester."практичні_(семінарські)_заняття" != 0 OR second_semester."лабораторні_роботи" != 0)
                                        THEN second_semester."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2)
                    +
                    (
                        SELECT

                        ROUND(
                            COALESCE(
                                SUM(
                                    CASE
                                        WHEN second_semester."лекції" != 0 AND second_semester."ставка" != 0
                                        THEN second_semester."лекції"
                                        ELSE 0
                                    END
                                )
                                /
                                NULLIF(
                                    SUM(
                                        CASE
                                            WHEN second_semester."лекції" != 0 AND second_semester."ставка" != 0
                                            THEN second_semester."ставка"
                                            ELSE 0
                                        END
                                    )
                                ,0)
                            ,0)
                        ,2)

 
                        FROM job

                        JOIN code_year ON job."код_рік_id" = code_year.id
                        JOIN first_semester ON job.id = first_semester."job_id"
                        JOIN second_semester ON job.id = second_semester."job_id"
                        JOIN academic_year ON job.id = academic_year."job_id"

                        WHERE job.'посада' = 'викладач' AND job.'НПП_ПП' = 'ПП'

                    ),2),

                    ROUND(
                    ROUND(
                        COALESCE(
                            (
                                SUM(
                                    CASE
                                        WHEN academic_year."практичні_(семінарські)_заняття" != 0 AND academic_year."ставка" != 0
                                        THEN academic_year."практичні_(семінарські)_заняття"
                                        ELSE 0
                                    END
                                )
                                +
                                SUM(
                                    CASE
                                        WHEN academic_year."лабораторні_роботи" != 0 AND academic_year."ставка" != 0
                                        THEN academic_year."лабораторні_роботи"
                                        ELSE 0
                                    END
                                )
                            )
                            /
                            NULLIF(
                                SUM(
                                    CASE
                                        WHEN academic_year."ставка" != 0 AND (academic_year."практичні_(семінарські)_заняття" != 0 OR academic_year."лабораторні_роботи" != 0)
                                        THEN academic_year."ставка"
                                        ELSE 0
                                    END
                                )
                            ,0)
                        ,0)
                    ,2)
                    +
                    (
                        SELECT

                        ROUND(
                            COALESCE(
                                SUM(
                                    CASE
                                        WHEN academic_year."лекції" != 0 AND academic_year."ставка" != 0
                                        THEN academic_year."лекції"
                                        ELSE 0
                                    END
                                )
                                /
                                NULLIF(
                                    SUM(
                                        CASE
                                            WHEN academic_year."лекції" != 0 AND academic_year."ставка" != 0
                                            THEN academic_year."ставка"
                                            ELSE 0
                                        END
                                    )
                                ,0)
                            ,0)
                        ,2)

 
                        FROM job

                        JOIN code_year ON job."код_рік_id" = code_year.id
                        JOIN first_semester ON job.id = first_semester."job_id"
                        JOIN second_semester ON job.id = second_semester."job_id"
                        JOIN academic_year ON job.id = academic_year."job_id"

                        WHERE job.'посада' = 'викладач' AND job.'НПП_ПП' = 'ПП'

                    )
                    ,2)

 
                FROM job

                JOIN code_year ON job."код_рік_id" = code_year.id
                JOIN first_semester ON job.id = first_semester."job_id"
                JOIN second_semester ON job.id = second_semester."job_id"
                JOIN academic_year ON job.id = academic_year."job_id"

                WHERE job.'НПП_ПП' = 'ПП' AND job.'посада' = 'викладач'

     
            """)
            # 

            result = []
            for value in cursor.fetchall():
                result.append((value[0],value[1],value[2]))
            
            msg = ""
            msg += f"Середнє аудиторне навантаження ПП (заф. кафедри)\n\t перший семестр: {result[1][0]}\n\t другий семестр: {result[1][1]}\n\t рік: {result[1][2]}\n\n"
            msg += f"Середнє аудиторне навантаження ПП (професор)\n\t перший семестр: {result[2][0]}\n\t другий семестр: {result[2][1]}\n\t рік: {result[2][2]}\n\n"
            msg += f"Середнє аудиторне навантаження ПП (доцент)\n\t перший семестр: {result[3][0]}\n\t другий семестр: {result[3][1]}\n\t рік: {result[3][2]}\n\n"
            msg += f"Середнє аудиторне навантаження ПП (ст. викладач)\n\t перший семестр: {result[4][0]}\n\t другий семестр: {result[4][1]}\n\t рік: {result[4][2]}\n\n"
            msg += f"Середнє аудиторне навантаження ПП (асистент)\n\t перший семестр: {result[5][0]}\n\t другий семестр: {result[5][1]}\n\t рік: {result[5][2]}\n\n"
            msg += f"Середнє аудиторне навантаження ПП (в.о. заф. кафедри)\n\t перший семестр: {result[6][0]}\n\t другий семестр: {result[6][1]}\n\t рік: {result[6][2]}\n\n"
            msg += f"Середнє аудиторне навантаження ПП (викладач)\n\t перший семестр: {result[7][0]}\n\t другий семестр: {result[7][1]}\n\t рік: {result[7][2]}\n\n"
            msg += f"Середнє аудиторне навантаження ПП (усі)\n\t перший семестр: {result[0][0]}\n\t другий семестр: {result[0][1]}\n\t рік: {result[0][2]}\n\n"

            with open("resources\\Середнэ навантаження\\ПП\\Аудиторне\\file.txt", "w", encoding="utf-8") as f:
                f.write(msg)

            msg = "Дані збереженно у файлі: \"resources\\Середнэ навантаження\\ПП\\Аудиторне\\file.txt\".\n\n\n" + msg
            msg += "\n\n\nКлацніть по екрану і натисніть Enter - щоб вийти з данної інформації.\n\n\n"
            second_window = tk.Toplevel(root)
            second_window.title("Результат")
            second_window.attributes('-fullscreen', True)

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
            text.insert("1.0", msg)

            copy_button = tk.Button(second_window, text="Копіювати текст", font=my_font,
            command=lambda: copy_text_to_clipboard(root, text))
            copy_button.pack(pady=20)

            text.bind('<Control-v>', lambda e: paste_from_clipboard(text))

            text.bind('<Control-c>', lambda e: copy_text_to_clipboard(root, text))

            second_window.bind("<Return>", lambda e: second_window.destroy())

            def copy_text_to_clipboard(root, text_widget):
                text = text_widget.get("1.0", "end-1c") 
                pyperclip.copy(text) 


            def paste_from_clipboard(text_widget):
                try:
                    clipboard_text = pyperclip.paste()
                    text_widget.insert(tk.INSERT, clipboard_text)
                except Exception as e:
                    messagebox.showwarning("Помилка", f"Помилка при вставці: {e}")

            conn.close()
            root.after(0, loading.destroy)

        loading = loading_window(root)
        threading.Thread(target=work, args=(root, name_db, loading), daemon=True).start()


    clear_window(root)

    root.bind("<Escape>", lambda event: on_escape(event, root, name_db))

    menubar = tk.Menu(root)

    filemenu = tk.Menu(menubar, tearoff=0)
    filemenu.add_command(label="Головне меню", command=lambda: main_menu(root, name_db))
    filemenu.add_command(label="Налаштування", command=lambda: settings_menu(root, name_db))
    filemenu.add_separator()
    filemenu.add_command(label="Вихід", command=lambda: on_escape(None, root, name_db))
   
    menubar.add_cascade(label="Файл", menu=filemenu)

    if check_db(root, name_db):
        errormenu = tk.Menu(menubar, tearoff=0)
        errormenu.add_command(label="Помилки", command=lambda: errors_menu(root, name_db))
        menubar.add_cascade(label="Помилки", menu=errormenu)

    root.config(menu=menubar)

    root.update()

    main_npp_button = tk.Button(root, text="Середнє навантаження НПП", 
        command=lambda: on_main_npp_button_click(root, name_db),
        bg="white", fg="black", activebackground="darkgreen", 
        activeforeground="black", bd=4, relief="solid",
        highlightbackground="black", highlightthickness=2)

    lecture_npp_button = tk.Button(root, text="Середнє лекційне навантаження НПП", 
        command=lambda: on_lecture_npp_button_click(root, name_db),
        bg="white", fg="black", activebackground="darkgreen", 
        activeforeground="black", bd=4, relief="solid",
        highlightbackground="black", highlightthickness=2)

    audience_npp_button = tk.Button(root, text="Середнє аудиторне навантаження НПП", 
        command=lambda: on_audience_npp_button_click(root, name_db),
        bg="white", fg="black", activebackground="darkgreen", 
        activeforeground="black", bd=4, relief="solid",
        highlightbackground="black", highlightthickness=2)

    main_pp_button = tk.Button(root, text="Середнє навантаження ПП", 
        command=lambda: on_main_pp_button_click(root, name_db),
        bg="white", fg="black", activebackground="darkgreen", 
        activeforeground="black", bd=4, relief="solid",
        highlightbackground="black", highlightthickness=2)

    lecture_pp_button = tk.Button(root, text="Середнє лекційне навантаження ПП", 
        command=lambda: on_lecture_pp_button_click(root, name_db),
        bg="white", fg="black", activebackground="darkgreen", 
        activeforeground="black", bd=4, relief="solid",
        highlightbackground="black", highlightthickness=2)

    audience_pp_button = tk.Button(root, text="Середнє аудиторне навантаження ПП", 
        command=lambda: on_audience_pp_button_click(root, name_db),
        bg="white", fg="black", activebackground="darkgreen", 
        activeforeground="black", bd=4, relief="solid",
        highlightbackground="black", highlightthickness=2)
    root.update()

    buttons = [main_npp_button, lecture_npp_button, audience_npp_button, main_pp_button, lecture_pp_button, audience_pp_button]

    for button in buttons:
        button.pack()

    root.update()

    for button in buttons:
        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)

    root.update()

    height_empty = (root.winfo_height() - max(button.winfo_height() for button in buttons)*(len(buttons)/2))/(len(buttons)/2 + 1)
    width_empty = (root.winfo_width() - max(button.winfo_width() for button in buttons)*2)/3

    root.update()
    
    for i, button in enumerate(buttons):
        if i >= len(buttons)/2:
            break

        button.place(x = width_empty, y = height_empty*(i+1) + max(button.winfo_height() for button in buttons)*i)

        buttons[int(len(buttons)/2)+i].place(x = 2*width_empty + max(button.winfo_width() for button in buttons), y = height_empty*(i+1) + max(button.winfo_height() for button in buttons)*i)

    root.update()

