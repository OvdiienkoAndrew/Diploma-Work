import tkinter as tk
from tkinter import filedialog, messagebox, Toplevel, Label

def clear_window(root):
    for widget in root.winfo_children():
        widget.destroy()

    root.configure(bg="white") 

def on_enter(e):
    e.widget['background'] = 'grey'

def on_leave(e):
    e.widget['background'] = 'white'

def loading_window(root):
    loading = tk.Toplevel(root)
    loading.title("Завантаження...")
    loading.geometry("300x100")
    loading.transient(root)
    loading.grab_set()
    loading.attributes("-topmost", True)
    loading.protocol("WM_DELETE_WINDOW", lambda: None)
    clear_window(loading)
    label = tk.Label(loading, text="Завантаження...", bg="white", fg="black")
    label.place(x=0,y=0)
    root.update()
    label.place(x=(loading.winfo_width()-label.winfo_width())/2, y=(loading.winfo_height()-label.winfo_height())/2)
    root.update()
    return loading