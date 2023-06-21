import tkinter as tk
from tkinter import messagebox

class TicTacToeGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe")
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.buttons = []

        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.window, text="", width=10, height=4,
                                   command=lambda r=i, c=j: self.make_move(r, c))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

    def make_move(self, row, col):
        if self.board[row][col] == "":
            self.buttons[row][col].config(text=self.current_player)
            self.board[row][col] = self.current_player

            if self.check_winner(self.current_player):
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_game()
            elif self.is_board_full():
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self, player):
        for i in range(3):
            if (self.board[i][0] == self.board[i][1] == self.board[i][2] == player or
                    self.board[0][i] == self.board[1][i] == self.board[2][i] == player):
                return True
        if (self.board[0][0] == self.board[1][1] == self.board[2][2] == player or
                self.board[0][2] == self.board[1][1] == self.board[2][0] == player):
            return True
        return False

    def is_board_full(self):
        for row in self.board:
            if "" in row:
                return False
        return True

    def reset_game(self):
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="")

    def run(self):
        self.window.mainloop()

game = TicTacToeGUI()
game.run()
