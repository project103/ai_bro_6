class TicTacToe4x4x4:
    def __init__(self):
        self.visited =  0 
        self.board = [[[0 for _ in range(4)] for _ in range(4)] for _ in range(4)]
        self.current_player = 1  # Player 1 starts

    def make_move(self, i, j, k):
        """Make a move on the board."""
        if self.board[i][j][k] == 0:
            self.board[i][j][k] = self.current_player
            self.current_player = -self.current_player  # Switch player
            return True
        else:
            return False  # Invalid move

    def is_terminal(self):
    # Check for a win in any dimension for both 'O' and 'X'
     for symbol in [1, -1]:
        # Check rows, columns, and diagonals
        for i in range(4):
            for j in range(4):
                if all(self.board[i][j][k] == symbol for k in range(4)):
                    return True

                if all(self.board[i][k][j] == symbol for k in range(4)):
                    return True

                if all(self.board[i][k][k] == symbol for k in range(4)):
                    return True

                if all(self.board[i][k][3 - k] == symbol for k in range(4)):
                    return True

            # Check depth
            if all(self.board[k][i][j] == symbol for k in range(4)):
                return True
            

     return False


    def evaluate_state(self, player):
        """Evaluate the desirability of a terminal game state for the given player."""
        score = 0
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    # Check rows
                    if all(self.board[i][j][l] == player for l in range(4)):
                        score += 90

                    # Check columns
                    if all(self.board[i][l][k] == player for l in range(4)):
                        score += 90

                    # Check diagonals
                    if all(self.board[i][l][l] == player for l in range(4)):
                        score += 90
                    if all(self.board[i][l][3 - l] == player for l in range(4)):
                        score += 90
                row = [self.board[i][j][k] for k in range(4)]
                score += self.evaluate_line(row, player)

                # Check columns
                col = [self.board[i][k][j] for k in range(4)]
                score += self.evaluate_line(col, player)

            # Check diagonals
                diag1 = [self.board[i][k][k] for k in range(4)]
                diag2 = [self.board[i][k][3-k] for k in range(4)]
                score += self.evaluate_line(diag1, player)
                score += self.evaluate_line(diag2, player)    

                for col in range(4):
                    for row in range(4):
                        if all(self.board[l][row][col] == player for l in range(4)):
                            score += 90
                if all(self.board[i][i][i] == player for i in range(4)) or all(self.board[i][i][3 - i] == player for i in range(4)):
                  score += 90


        return score
    def evaluate_line(self, line, player):
     opponent = -1  # Assuming players are represented by 1 and 2

    # Defensive evaluation 
     if line.count(player) == 3 and line.count(0) == 1:
        return 50
    # Offensive evaluation
     elif line.count(opponent) == 2 and line.count(0) == 2:
        return 25
     else:
        return 0




    def minimax(self, depth, maximizing_player):
        self.visited += 1
        if depth == 0 or self.is_terminal():
            return self.evaluate_state(1), None

        if maximizing_player:
            max_eval = float('-inf')
            best_move = None

            for i in range(4):
                for j in range(4):
                    for k in range(4):
                        if self.board[i][j][k] == 0:
                            self.board[i][j][k] = 1
                            eval, _ = self.minimax(depth - 1, False)
                            self.board[i][j][k] = 0

                            if eval > max_eval:
                                max_eval = eval
                                best_move = (i, j, k)

            return max_eval, best_move
        else:
            min_eval = float('inf')
            best_move = None

            for i in range(4):
                for j in range(4):
                    for k in range(4):
                        if self.board[i][j][k] == 0:
                            self.board[i][j][k] = -1
                            eval, _ = self.minimax(depth - 1, True)
                            self.board[i][j][k] = 0
                            

                            if eval < min_eval:
                                min_eval = eval
                                best_move = (i, j, k)

            return min_eval, best_move

