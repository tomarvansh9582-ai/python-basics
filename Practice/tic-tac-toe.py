import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("Tic Tac Toe")
turn = 'X'
buttons = []
def click(index):
    global turn
    btn = buttons[index]
    
    if btn['text'] == "":
        btn['text'] = turn
        check_winner()
        
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

def check_winner():
    combos = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    
    for a, b, c in combos:
        if buttons[a]['text'] == buttons[b]['text'] == buttons[c]['text'] and buttons[a]['text'] != "":
            messagebox.showinfo("Winner", f"Player {buttons[a]['text']} Wins!")
            root.quit()

for i in range(9):
    btn = tk.Button(root, text="", font=("Arial", 20), width=5, height=2, command=lambda i=i: click(i))
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

root.mainloop()
