from Board import Board
import tkinter as tk
from tkinter import messagebox
from main import main
import subprocess


class TicTacToeGUI:
    
    def __init__(self, master):
        self.master = master
        self.master.title("4x4x4 Tic Tac Toe")

        self.board = Board()
        self.create_widgets()
        self.main = main
        
        
        self.set_players("x")
        self.update_status()
        
    def set_players(self, player):
        self.player = self.board.set_player(player)
        self.Ai_player = self.board.set_AI_player()

    def create_widgets(self):
        self.buttons = [[[tk.Button(self.master, text='', width=4, height=2, command=lambda layer=l, row=r, col=c: self.make_move(layer, row, col))
                         for c in range(4)] for r in range(4)] for l in range(4)]

        for layer in range(4):
            for row in range(4):
                for col in range(4):
                    self.buttons[layer][row][col].grid(row=row + layer * 4, column=col + layer * 4, padx=5, pady=0)

        self.status_label = tk.Label(self.master, text=f"Current Player: {self.board.current_player}")
        self.status_label.grid(row=16, columnspan=4)
        self.reset_button = tk.Button(self.master, text="Reset Game", command=self.reset_game)
        self.reset_button.grid(row=17, columnspan=4)
        self.back_button = tk.Button(self.master, text="back to menu", command=self.back_game)
        self.back_button.grid(row=17, columnspan=8)
    
    def back_game(self):
         self.master.destroy() # Hide the current window
         subprocess.run(["python", "main.py"])
    
    def reset_game(self):
        self.vis_label.config(text=" time: ")
        self.board.reset_board()
        for layer in range(4):
            for row in range(4):
                for col in range(4):
                    self.buttons[layer][row][col].config(text='')
        self.update_status()

    def make_move(self, layer, row, col):
        if self.board.get_value(layer, row, col) == '':
            self.board.set_value(layer, row, col)
            self.buttons[layer][row][col].config(text=self.board.current_player)
            self.board.turn()
            self.update_status()

            if self.board.current_player == self.Ai_player:
                # ****************************************************************
                # add here your best_move return and pass it to self.board.set_value(layer, row, col)
                # ****************************************************************
                #self.board.turn()  (note remove "#" from this line)
                self.update_status()

            if self.board.is_win('x') or self.board.is_win('O'):  # Corrected 'O' to 'o
                winner = 'Player X' if self.board.is_win('x') else 'Player O'
                messagebox.showinfo("Game Over", f"{winner} wins!")
                self.board.reset_board()

            if self.board.is_full():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.board.reset_board()

    def update_status(self):
        self.status_label.config(text=f"Current Player: {self.board.current_player}")


if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeGUI(root)
    root.mainloop()
