import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.board = ['' for _ in range(9)]  # Initialize empty board
        self.current_player = 'X'

        # Initialize buttons
        self.buttons = [tk.Button(self.window, text="", command=lambda i=i: self.on_click(i), height=3, width=6) for i in range(9)]
        for i, button in enumerate(self.buttons):
            button.grid(row=i//3, column=i%3)

    def on_click(self, cell):
        if self.board[cell] == '' and not self.is_game_over():
            self.buttons[cell]['text'] = self.current_player
            self.board[cell] = self.current_player
            if not self.is_game_over():
                self.current_player = 'O' if self.current_player == 'X' else 'X'
                if self.current_player == 'O':
                    self.computer_move()
                self.check_game_over()

    def computer_move(self):
        best_score = float('-inf')
        best_move = None
        for i in range(9):
            if self.board[i] == '':
                self.board[i] = 'O'
                score = self.minimax(self.board, 0, False)
                self.board[i] = ''
                if score > best_score:
                    best_score = score
                    best_move = i
        self.board[best_move] = 'O'
        self.buttons[best_move]['text'] = 'O'
        self.current_player = 'X'

    def minimax(self, board, depth, is_maximizing):
        if self.is_game_over():
            if self.board.count('X') == self.board.count('O'):
                return 0
            elif is_maximizing:
                return -1
            else:
                return 1

        if is_maximizing:
            best_score = float('-inf')
            for i in range(9):
                if board[i] == '':
                    board[i] = 'O'
                    score = self.minimax(board, depth + 1, False)
                    board[i] = ''
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(9):
                if board[i] == '':
                    board[i] = 'X'
                    score = self.minimax(board, depth + 1, True)
                    board[i] = ''
                    best_score = min(score, best_score)
            return best_score

    def is_game_over(self):
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for combination in winning_combinations:
            if self.board[combination[0]] == self.board[combination[1]] == self.board[combination[2]] != '':
                return True
        if '' not in self.board:
            return True
        return False

    def check_game_over(self):
        if self.is_game_over():
            winner = 'O' if self.board.count('X') != self.board.count('O') else 'X'
            message = f"Player {winner} won!" if self.board.count('X') != self.board.count('O') else "It's a draw!"
            messagebox.showinfo("Game Over", message)
            self.window.quit()

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()
