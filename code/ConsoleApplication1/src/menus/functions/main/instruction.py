import tkinter as tk
from tkinter import font, messagebox
import pyperclip

def on_click_instruction(root, name_db):
    msg = "Під час роботи з програмою слід дотримуватися певних вимог, щоб правильно заносити результати.\n\n"
    msg += "1. Назва файлу може бути довільною.\n2. Файл має бути правильно збережений у форматі “.xlsx”.\n3. Надана інформація повинна розміщатися на листі з назвою: “Загальна” – строго дотримуючись верхнього та\n\tнижнього регістрів, ніякий порожні символів.\n4. У комірці А3 має бути назва кафедри у круглих дужках, а також роки у вигляді цифр і тире між роками.\n\tНаприклад: “Розподіл навчального навантаження між викладачами кафедри педагогічної та\n\tвікової психології (ДПП) на 2024-2025 навчальний рік” - ніяких цифр (окрім дати) або\n\tдужок (окрім кафедри).\n5. Із стовпця I по стовпець AB мають бути прописані години виключно у такому порядку: \"лекції\",\n\t\"практичні (семінарські) заняття\", \"лабораторні роботи\", \"екзамени\", \"консультації перед екзаменами\",\n\t\"заліки\", \"кваліфікаційна робота\", \"атестаційний екзамен\", \"виробнича практика\", \"навчальна практика\",\n\t\"поточні консультації\", \"індивідуальні заняття\", \"курсові роботи\", \"аспірантські екзамени\",\n\t\"керівництво аспірантами\", \"консультування докторантів і здобувачів\", \"керівництво ФПК\",\n\t\"робота приймальної комісії\", \"інше\", \"всього\" - i в колонці АС: “розподіл ставок”.\n6. Починаючи з комірки А7 мають стояти цілі числа, обʼєднані на 3 клітинки вниз, включно з поточною.\n\tНаприклад, якщо цифра стоїть у комірці А3 – то комірки А3-А5 мають бути обʼєднані.\n7. Праворуч аналогічно обʼєднаним коміркам в стовбці А мають бути обʼєднані комірки у стовпці В.\n\tУ них має бути записані ФІО через пробіл, або слово “Вакансія” й обовʼязково номер.\n8. Аналогічно до стовпців А та В мають бути обʼєднані комірки у стовпці С.\n\tА в них спочатку йти посада, потім кома, вчене звання та ступінь.\n9. Аналогічно обʼєднанним коміркам у стовпцях А-С мають бути необʼєднанні комірки у стовпці D.\n\tЦе є ставка та ознака сумісності (якщо є), які стоять для першого семестру, другого семестру\n\tта року – відповідно зверху вниз.\n10. Відповідно до стовпця D організований стовпець AC. Але перший семестр та другий залишаються порожніми,\n\tа у рік записується розподіл ставок на рік.\n11. Відповідно обʼєднанним коміркам у стовпцях А-С мають бути необʼєднанні комірки у стовпцях від I до AB,\n\tде прописані години навчального навантаження на перший семестр, другий семестр та рік.\n\n"

    msg += "Клацніть по екрану і натисніть Enter - щоб вийти з данної інформації."

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