import tkinter as tk

def on_escape(event, root, name_db):

    from src.settings.settings import clear_window, on_enter, on_leave
    from src.menus.main import main_menu

    def on_click_yes(root, name_db):
       root.destroy()

    def on_click_no(root, name_db):
       main_menu(root, name_db)

    clear_window(root)

    label_question = tk.Label(root, text="Ви точно хочете вийт з програми?", bg="white", fg="black")
    label_question.pack()

    button_yes_exit = tk.Button(root, text="Так", command=lambda: on_click_yes(root, name_db),  bg="white", fg="black", activebackground="darkgreen", activeforeground="black")
    button_no_exit = tk.Button(root, text="Ні", command=lambda: on_click_no(root, name_db),  bg="white", fg="black", activebackground="darkgreen", activeforeground="black")

    button_yes_exit.pack()
    button_no_exit.pack()

    root.update()

    button_yes_exit.bind("<Enter>", on_enter)
    button_no_exit.bind("<Enter>", on_enter)
    button_yes_exit.bind("<Leave>", on_leave)
    button_no_exit.bind("<Leave>", on_leave)

    label_question.place( x = ( root.winfo_width() - label_question.winfo_width() ) / 2, y = ( root.winfo_height() - label_question.winfo_height() - button_yes_exit.winfo_height() ) / 3)

    button_yes_exit.place( x = ( root.winfo_width() - button_no_exit.winfo_width() - button_yes_exit.winfo_width() ) / 3, y = 2 * ( ( root.winfo_height() - label_question.winfo_height() - button_yes_exit.winfo_height() ) / 3 ) + label_question.winfo_height() )

    button_no_exit.place( x = 2 * ( ( root.winfo_width() - button_no_exit.winfo_width() - button_yes_exit.winfo_width() ) / 3 ) + button_no_exit.winfo_width(), y = 2 * ( ( root.winfo_height() - label_question.winfo_height() - button_yes_exit.winfo_height() ) / 3 ) + label_question.winfo_height() )

    root.update()

