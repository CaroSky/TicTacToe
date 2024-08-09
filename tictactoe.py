import tkinter as tk
from tkinter import messagebox
import random


class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic-Tac-Toe")
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_winner = None
        self.human_score = 0
        self.ai_score = 0
        self.tie_score = 0
        self.human_starts = random.choice([True, False])

        self.create_board_buttons()
        self.create_scoreboard()
        self.create_new_game_button()
        self.reset_game()

    def create_board_buttons(self):
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.master, text=' ', font=('normal', 20, 'bold'), width=5, height=2,
                                               command=lambda row=i, col=j: self.make_move(row, col))
                self.buttons[i][j].grid(row=i, column=j)

    def create_scoreboard(self):
        self.score_frame = tk.Frame(self.master)
        self.score_frame.grid(row=3, column=0, columnspan=3, pady=10)

        tk.Label(self.score_frame, text="Human: ").grid(row=0, column=0)
        self.human_score_label = tk.Label(self.score_frame, text="0")
        self.human_score_label.grid(row=0, column=1)

        tk.Label(self.score_frame, text="AI: ").grid(row=0, column=2)
        self.ai_score_label = tk.Label(self.score_frame, text="0")
        self.ai_score_label.grid(row=0, column=3)

        tk.Label(self.score_frame, text="Ties: ").grid(row=0, column=4)
        self.tie_score_label = tk.Label(self.score_frame, text="0")
        self.tie_score_label.grid(row=0, column=5)

        self.turn_label = tk.Label(self.master, text="", font=('normal', 12))
        self.turn_label.grid(row=5, column=0, columnspan=3)

    def create_new_game_button(self):
        self.new_game_button = tk.Button(self.master, text="New Game", command=self.reset_game)
        self.new_game_button.grid(row=4, column=0, columnspan=3, pady=10)

    def make_move(self, row, col):
        if self.board[row][col] == ' ' and self.human_starts:
            self.board[row][col] = 'X'
            self.buttons[row][col].config(text='X', state='disabled')
            if self.check_winner('X'):
                self.end_game("You win!")
                self.human_score += 1
                self.update_scoreboard()
            elif self.is_board_full():
                self.end_game("It's a tie!")
                self.tie_score += 1
                self.update_scoreboard()
            else:
                self.human_starts = False
                self.update_turn_label()
                self.master.after(100, self.ai_move)

    def ai_move(self):
        if all(self.board[i][j] == ' ' for i in range(3) for j in range(3)):
            # If it's the first move, choose a random corner or the center
            possible_moves = [(0, 0), (0, 2), (2, 0), (2, 2), (1, 1)]
            move = random.choice(possible_moves)
        else:
            # Use minimax for subsequent moves
            _, move = self.minimax(True, float('-inf'), float('inf'))

        row, col = move
        self.board[row][col] = 'O'
        self.buttons[row][col].config(text='O', state='disabled')
        if self.check_winner('O'):
            self.end_game("AI wins!")
            self.ai_score += 1
            self.update_scoreboard()
        elif self.is_board_full():
            self.end_game("It's a tie!")
            self.tie_score += 1
            self.update_scoreboard()
        else:
            self.human_starts = True
            self.update_turn_label()

    def check_winner(self, player):
        for i in range(3):
            if all([self.board[i][j] == player for j in range(3)]) or \
                    all([self.board[j][i] == player for j in range(3)]):
                return True
        if all([self.board[i][i] == player for i in range(3)]) or \
                all([self.board[i][2 - i] == player for i in range(3)]):
            return True
        return False

    def is_board_full(self):
        return all([self.board[i][j] != ' ' for i in range(3) for j in range(3)])

    def minimax(self, maximizing_player, alpha, beta):
        if self.check_winner('O'):
            return 1, None
        if self.check_winner('X'):
            return -1, None
        if self.is_board_full():
            return 0, None

        if maximizing_player:
            max_eval = float('-inf')
            best_move = None
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == ' ':
                        self.board[i][j] = 'O'
                        eval, _ = self.minimax(False, alpha, beta)
                        self.board[i][j] = ' '
                        if eval > max_eval:
                            max_eval = eval
                            best_move = (i, j)
                        alpha = max(alpha, eval)
                        if beta <= alpha:
                            break
            return max_eval, best_move
        else:
            min_eval = float('inf')
            best_move = None
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == ' ':
                        self.board[i][j] = 'X'
                        eval, _ = self.minimax(True, alpha, beta)
                        self.board[i][j] = ' '
                        if eval < min_eval:
                            min_eval = eval
                            best_move = (i, j)
                        beta = min(beta, eval)
                        if beta <= alpha:
                            break
            return min_eval, best_move

    def end_game(self, message):
        for row in self.buttons:
            for button in row:
                button.config(state='disabled')
        messagebox.showinfo("Game Over", message)

    def reset_game(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text=' ', state='normal')
        self.current_winner = None
        self.human_starts = not self.human_starts  # Alternate who starts
        self.update_turn_label()
        if not self.human_starts:
            self.master.after(100, self.ai_move)

    def update_scoreboard(self):
        self.human_score_label.config(text=str(self.human_score))
        self.ai_score_label.config(text=str(self.ai_score))
        self.tie_score_label.config(text=str(self.tie_score))

    def update_turn_label(self):
        if self.human_starts:
            self.turn_label.config(text="Your turn (X)")
        else:
            self.turn_label.config(text="AI's turn (O)")


def main():
    root = tk.Tk()
    TicTacToe(root)
    root.mainloop()


if __name__ == "__main__":
    main()