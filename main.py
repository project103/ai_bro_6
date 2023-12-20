# main.py
import tkinter as tk
import time

from PIL import Image, ImageTk
import subprocess

class main(tk.Tk):
    
    def __init__(self):
        super().__init__()

        self.geometry("350x350")
        self.title("Tic Tac Toe Game")

        self.background_image = Image.open("tic_tac_toe_back.jpg")
        self.background_image = ImageTk.PhotoImage(self.background_image)

        self.canvas = tk.Canvas(self, width=self.background_image.width(), height=self.background_image.height())
        self.canvas.pack(fill="both", expand=True)

        self.canvas.create_image(0, 0, anchor="nw", image=self.background_image)

        
        
        self.button1 = tk.Button(self.canvas, text="Ease", command=lambda: self.set_difficulty(1))
        self.button2 = tk.Button(self.canvas, text="Normal", command=lambda: self.set_difficulty(2))
        self.button3 = tk.Button(self.canvas, text="Hard", command=lambda: self.set_difficulty(3))
        self.button4 = tk.Button(self.canvas, text="Start", command=self.check_and_open_gui)
        self.button5 = tk.Button(self.canvas, text="2 players", command=lambda: self.set_difficulty(4))
        self.button6 = tk.Button(self.canvas, text="alphaBita", command=lambda: self.set_difficulty(5))
        self.button7 = tk.Button(self.canvas, text="minimax", command=lambda: self.set_difficulty(6))
        
        
        
        self.button1.place(relx=0.5, rely=0.3, anchor="center")
        self.button2.place(relx=0.5, rely=0.4, anchor="center")
        self.button3.place(relx=0.5, rely=0.5, anchor="center")
        self.button5.place(relx=0.5, rely=0.8, anchor="center")
        self.button6.place(relx=0.5, rely=0.7, anchor="center")
        self.button7.place(relx=0.5, rely=0.6, anchor="center")
        self.button4.place(relx=0.5, rely=0.9, anchor="center")



        self.label = tk.Label(self.canvas, text="Main Name")
        self.label.place(relx=0.5, rely=0.2, anchor="center")


        self.val = None


    def set_difficulty(self, difficulty):
        self.label.config(text="minimax with heuristic2" if difficulty == 1 else "minimax with heuristic1" if difficulty == 2 else "alpha bita with heuristic1"  if difficulty == 3 else "2 players" if difficulty == 4 else "alpha bita" if difficulty == 5 else "minimax")
        self.val = difficulty




    def check_and_open_gui(self):
        if self.val :
            self.withdraw()  # Hide the current window
            if self.val == 1:
             subprocess.run(["python", "MX2_gui.py"])
            elif self.val == 2:
             subprocess.run(["python", "MX1_gui.py"])
            elif self.val == 3:
             subprocess.run(["python", "APH_gui.py"])
            elif self.val == 4:
             subprocess.run(["python", "gui.py"])
            elif self.val == 5:
             subprocess.run(["python", "AP_gui.py"])
            elif self.val == 6:
             subprocess.run(["python", "MX_gui.py"])
        elif self.val == None:
            self.label.config(text="you must select difficulty level!")

if __name__ == "__main__":
    app = main()
    app.mainloop()