import tkinter as tk
from tkinter import messagebox
import random

# ---------- FUNCTIONS ----------

def check_winner():
    global winner, x_score, o_score
    
    win_combinations = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    
    for combo in win_combinations:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "":
            
            for i in combo:
                buttons[i].config(bg="green")
            
            winner = True
            player = buttons[combo[0]]["text"]
            
            if player == "X":
                x_score += 1
            else:
                o_score += 1
            
            update_score()
            messagebox.showinfo("Tic-Tac-Toe", f"Player {player} Wins!")
            return
    
    # Draw condition
    if all(button["text"] != "" for button in buttons) and not winner:
        messagebox.showinfo("Tic-Tac-Toe", "It's a Draw!")


def button_click(index):
    global current_player
    
    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] = current_player
        
        if current_player == "X":
            buttons[index].config(fg="#2980b9")
        else:
            buttons[index].config(fg="#c0392b")
        
        check_winner()
        
        if not winner:
            toggle_player()
            
            if ai_mode and current_player == "O":
                root.after(500, ai_move)


def toggle_player():
    global current_player
    current_player = "O" if current_player == "X" else "X"
    label.config(text=f"Player {current_player}'s Turn")


def ai_move():
    empty = [i for i in range(9) if buttons[i]["text"] == ""]
    if empty and not winner:
        move = random.choice(empty)
        button_click(move)


def restart_game():
    global winner, current_player
    
    winner = False
    current_player = "X"
    label.config(text=f"Player {current_player}'s Turn")
    
    for button in buttons:
        button.config(text="", bg="#ecf0f1")


def update_score():
    score_label.config(text=f"Score  X: {x_score}   O: {o_score}")


# ---------- UI SETUP ----------

root = tk.Tk()
root.title("Tic-Tac-Toe")
root.configure(bg="#2c3e50")

buttons = []

for i in range(9):
    button = tk.Button(
        root,
        text="",
        font=("Arial", 25, "bold"),
        width=6,
        height=2,
        bg="#ecf0f1",
        activebackground="#bdc3c7",
        command=lambda i=i: button_click(i)
    )
    button.grid(row=i // 3, column=i % 3, padx=5, pady=5)
    buttons.append(button)

current_player = "X"
winner = False
x_score = 0
o_score = 0
ai_mode = True   # True = Play vs Computer | False = 2 Player Mode

label = tk.Label(
    root,
    text=f"Player {current_player}'s Turn",
    font=("Arial", 16, "bold"),
    bg="#2c3e50",
    fg="white"
)
label.grid(row=3, column=0, columnspan=3, pady=10)

restart_btn = tk.Button(
    root,
    text="Restart Game",
    font=("Arial", 14),
    bg="#e67e22",
    fg="white",
    command=restart_game
)
restart_btn.grid(row=4, column=0, columnspan=3, pady=5)

score_label = tk.Label(
    root,
    text="Score  X: 0   O: 0",
    font=("Arial", 14, "bold"),
    bg="#2c3e50",
    fg="white"
)
score_label.grid(row=5, column=0, columnspan=3, pady=10)

root.mainloop()
