import tkinter as tk
from tkinter import messagebox
from alphaBita import ATicTacToe4x4x4
import subprocess
import time


class TicTacToeGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("4x4x4 Tic Tac Toe")
        
        self.Atic_tac_toe_game = ATicTacToe4x4x4() 
        
        self.create_widgets()
        
        self.set_players("x")
        self.update_status()
    
    def set_players(self, player):
        # Set players in the TicTacToe4x4x4 instance
        self.Atic_tac_toe_game.current_player = 1 if player == 'x' else -1

    def create_widgets(self):
        self.buttons = [[[tk.Button(self.master, text='', width=4, height=2, command=lambda layer=l, row=r, col=c: self.make_move(layer, row, col))
                         for c in range(4)] for r in range(4)] for l in range(4)]

        for layer in range(4):
            for row in range(4):
                for col in range(4):
                    self.buttons[layer][row][col].grid(row=row + layer * 4, column=col + layer * 4, padx=5, pady=0)

        self.status_label = tk.Label(self.master, text=f"Current Player: {self.Atic_tac_toe_game.current_player}")
        self.status_label.grid(row=16, columnspan=4)
        self.rec_label = tk.Label(self.master, text=f" time: ")
        self.rec_label.grid(row=18, columnspan=4)
        self.vis_label = tk.Label(self.master, text=f"visited nodes: ")
        self.vis_label.grid(row=19, columnspan=4)
        self.reset_button = tk.Button(self.master, text="Reset Game", command=self.reset_game)
        self.reset_button.grid(row=17, columnspan=4)
        self.back_button = tk.Button(self.master, text="back to menu", command=self.back_game)
        self.back_button.grid(row=17, columnspan=8)
    
    def back_game(self):
         self.master.destroy() # Hide the current window
         subprocess.run(["python", "main.py"])
    
    def reset_game(self):
        self.vis_label.config(text=" time: ")
        self.rec_label.config(text="Current performance: ")
        self.Atic_tac_toe_game = ATicTacToe4x4x4()  # Reset the game state
        for layer in range(4):
            for row in range(4):
                for col in range(4):
                    self.buttons[layer][row][col].config(text='')
        self.set_players("x")
        self.update_status()
        

    def make_move(self, layer, row, col):
        if self.Atic_tac_toe_game.board[layer][row][col] == 0:
            # Human move
            self.Atic_tac_toe_game.board[layer][row][col] = self.Atic_tac_toe_game.current_player
            self.buttons[layer][row][col].config(text='X' if self.Atic_tac_toe_game.current_player == 1 else 'O')

            if self.check_game_over():
                return
            else:
                self.Atic_tac_toe_game.current_player = -self.Atic_tac_toe_game.current_player  # Switch player
                self.update_status()
                # AI move
                #_, best_move,per = self.Atic_tac_toe_game.minimax(2, True)
                
                start_time = time.time()
                score, best_move = self.Atic_tac_toe_game.alpha_beta_wrapper(2,True)
                end_time = time.time()
               # _, best_move,per = self.Atic_tac_toe_game.minimax(2, True)
                if best_move:
                    self.rec_label.config(text=f"time: {end_time - start_time}")
                    self.vis_label.config(text=f"visited nodes:  {self.Atic_tac_toe_game.visited}")
                    self.Atic_tac_toe_game.visited = 0
                    layer_ai, row_ai, col_ai = best_move
                    self.Atic_tac_toe_game.board[layer_ai][row_ai][col_ai] = self.Atic_tac_toe_game.current_player
                    self.buttons[layer_ai][row_ai][col_ai].config(text='X' if self.Atic_tac_toe_game.current_player == 1 else 'O')
                    self.check_game_over()
                    self.Atic_tac_toe_game.current_player = -self.Atic_tac_toe_game.current_player  # Switch player
                    self.update_status()
                   

    def check_game_over(self):
        if self.Atic_tac_toe_game.is_terminal():
            winner = 'Player X' if self.Atic_tac_toe_game.current_player == 1 else 'Player O'
            messagebox.showinfo("Game Over", f"{winner} wins!")
            self.reset_game()
            return True
        elif all(self.Atic_tac_toe_game.board[i][j][k] != 0 for i in range(4) for j in range(4) for k in range(4)):
            messagebox.showinfo("Game Over", "It's a draw!")
            self.reset_game()
            return True
        return False

    def update_status(self):
        self.status_label.config(text=f"Current Player: {'X' if self.Atic_tac_toe_game.current_player == 1 else 'O'}")


if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeGUI(root)
    root.mainloop()
