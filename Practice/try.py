import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Tabs with Buttons")
root.geometry("400x250")

notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both")

tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
tab3 = ttk.Frame(notebook)

notebook.add(tab1, text="Tab 1")
notebook.add(tab2, text="Tab 2")
notebook.add(tab3, text="Tab 3")

def go_to_tab(target):
    notebook.select(target)

ttk.Label(tab1, text="This is Tab 1").pack(pady=10)
ttk.Button(tab1, text="Go to Tab 2", command=lambda: go_to_tab(tab2)).pack(pady=10)

ttk.Label(tab2, text="This is Tab 2").pack(pady=10)
ttk.Button(tab2, text="Go to Tab 3", command=lambda: go_to_tab(tab3)).pack(pady=10)

ttk.Label(tab3, text="This is Tab 3").pack(pady=10)
ttk.Button(tab3, text="Go to Tab 1", command=lambda: go_to_tab(tab1)).pack(pady=10)

root.mainloop()
