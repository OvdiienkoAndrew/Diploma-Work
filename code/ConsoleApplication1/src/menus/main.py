import tkinter as tk

def main_menu(root, name_db):

    from src.menus.functions.main.input import on_click_input
    from src.menus.functions.main.check import on_click_check
    from src.menus.functions.main.output import on_click_output
    from src.menus.functions.main.instruction import on_click_instruction

    from src.menus.error import errors_menu
    from src.menus.request import requests_menu

    from src.data_base.error.check.main import check_db

    from src.settings.settings import clear_window, on_enter, on_leave
    from src.menus.exit import on_escape

    from src.menus.settings import settings_menu
    
    clear_window(root)

    root.bind("<Escape>", lambda event: on_escape(event, root, name_db))

    menubar = tk.Menu(root)

    filemenu = tk.Menu(menubar, tearoff=0)
    filemenu.add_command(label="Налаштування", command=lambda: settings_menu(root, name_db))
    filemenu.add_command(label="Запити", command=lambda: requests_menu(root, name_db))
    filemenu.add_separator()
    filemenu.add_command(label="Вихід", command=lambda: on_escape(None, root, name_db))
   
    menubar.add_cascade(label="Файл", menu=filemenu)

    if check_db(root, name_db):
        errormenu = tk.Menu(menubar, tearoff=0)
        errormenu.add_command(label="Помилки", command=lambda: errors_menu(root, name_db))
        menubar.add_cascade(label="Помилки", menu=errormenu)

    root.config(menu=menubar)
    
    button_input = tk.Button(root, text="Занести дані до бази", command=lambda: on_click_input(root, name_db),  bg="white", fg="black", activebackground="darkgreen", activeforeground="black")
    button_check = tk.Button(root, text="Перевірити", command=lambda: on_click_check(root, name_db),  bg="white", fg="black", activebackground="darkgreen", activeforeground="black")
    button_output = tk.Button(root, text="Експортувати дані в Excel", command=lambda: on_click_output(root, name_db),  bg="white", fg="black", activebackground="darkgreen", activeforeground="black")
    button_instruction = tk.Button(root, text="Інструкція Excel файлів", command=lambda: on_click_instruction(root, name_db),  bg="white", fg="black", activebackground="darkgreen", activeforeground="black")
    
    button_input.pack()
    button_check.pack()
    button_output.pack()
    button_instruction.pack()

    root.update()

    button_input.bind("<Enter>", on_enter)
    button_check.bind("<Enter>", on_enter)
    button_output.bind("<Enter>", on_enter)
    button_instruction.bind("<Enter>", on_enter)

    button_input.bind("<Leave>", on_leave)
    button_check.bind("<Leave>", on_leave)
    button_output.bind("<Leave>", on_leave)
    button_instruction.bind("<Leave>", on_leave)

    buttons = [button_input,button_check, button_output, button_instruction]

    empty_height = root.winfo_height()

    for button in buttons:
        empty_height -= button.winfo_height()

    empty_height /= ( len(buttons) + 1 )


    for i, button in enumerate(buttons):
        button.place( x = ( root.winfo_width() - button.winfo_width() ) / 2, y = empty_height *(i+1) + button_input.winfo_height()*i)

    root.update()

    root.mainloop()

