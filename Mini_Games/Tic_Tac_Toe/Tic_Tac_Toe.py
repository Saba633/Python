
#   STEPS:
# 1-- Create the Basic Tkinter Window
# 2-- Create the Game Board
# 3-- Handle Button Clicks
# 4--Update Button Clicks
# 5-- Check for a Winner
# 6-- Display the Winner
# 7-- Reset the Game

import tkinter as tk
from tkinter import messagebox
def main():
# Create the Basic Tkinter Window
    root = tk.Tk()
    root.title('Tic Tac Toe')
    root.geometry('400x480')
# Check for a Winner
    def check_winner():
        for i in range(3):
            if buttons[i][0]['text'] == buttons[i][1]['text'] == buttons[i][2]['text'] !="":
                return buttons[i][0]['text']
            if buttons[0][i]['text'] == buttons[1][i]['text'] == buttons[2][i]['text'] !="":
                return buttons[0][0]['text']
            
        if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
            return buttons[0][0]['text']
        if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
            return buttons[0][2]['text']
        
        return None
    
    global current_player 
    current_player = 'X'
# Reset the Game
    def reset_game():
        for i in range(3):
            for j in range(3):
                buttons[i][j]['text'] = ""
        global current_player 
        current_player = 'X'
# Handle Button Clicks
    def button_click(i,j):
        global current_player
        if buttons[i][j]['text'] == "":
            buttons[i][j]['text'] = current_player
            winner = check_winner()
# Display the Winner
            if winner:
                messagebox.showinfo('Game Over,', f'{winner} wins!')
                reset_game()
            current_player = "O" if current_player == "X" else "X"
# Create the Game Board
    buttons = [[None,None,None],[None,None,None],[None,None,None]]
    for i in range(3):
        for j in range(3):
            buttons[i][j] = tk.Button(root, font=('Arial', 40), width=4,text="", height=2,bg="lightblue", fg="darkblue",
                                    command=lambda i=i, j=j: button_click(i,j)) #Update Button Clicks
            buttons[i][j].grid(row=i, column = j)


    root.mainloop()

if __name__ == '__main__':
    main()
