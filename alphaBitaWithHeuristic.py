class ATicTacToe4x4x4:
    def __init__(self):
        self.visited =  0 
        self.board = [[[0 for _ in range(4)] for _ in range(4)] for _ in range(4)]
        self.current_player = 1  # Player 1 starts
        self.board

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
        # Check rows
            for layer in self.board:
             for row in layer:
                if all(cell == symbol for cell in row):
                    return True

        # Check columns
            for col in range(4):
             for layer in self.board:
                if all(row[col] == symbol for row in layer):
                    return True

        # Check diagonals within layers
            for layer in self.board:
              if all(layer[i][i] == symbol for i in range(4)) or all(layer[i][3 - i] == symbol for i in range(4)):
                return True

        # Check across layers
            for col in range(4):
              for row in range(4):
                if all(self.board[l][row][col] == symbol for l in range(4)):
                    return True

        # Check diagonals between layers
            if all(self.board[i][i][i] == symbol for i in range(4)) or all(self.board[i][i][3 - i] == symbol for i in range(4)):
              return True

            if all(self.board[i][3 - i][i] == symbol for i in range(4)) or all(self.board[i][3 - i][3 - i] == symbol for i in range(4)):
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

    def alpha_beta(self, depth, alpha, beta, maximizing_player):
        self.visited += 1
        if depth == 0:
            return self.evaluate_state(1), None

        if maximizing_player:
            max_eval = float('-inf')
            best_move = None

            for i in range(4):
                for j in range(4):
                    for k in range(4):
                        if self.board[i][j][k] == 0:
                            self.board[i][j][k] = 1
                            eval, _ = self.alpha_beta(depth - 1, alpha, beta, False)
                            self.board[i][j][k] = 0

                            if eval > max_eval:
                                max_eval = eval
                                best_move = (i, j, k)

                            alpha = max(alpha, eval)
                            if beta <= alpha:
                                break

            return max_eval, best_move
        else:
            min_eval = float('inf')
            best_move = None

            for i in range(4):
                for j in range(4):
                    for k in range(4):
                        if self.board[i][j][k] == 0:
                            self.board[i][j][k] = -1
                            eval, _ = self.alpha_beta(depth - 1, alpha, beta, True)
                            self.board[i][j][k] = 0
                            

                            if eval < min_eval:
                                min_eval = eval
                                best_move = (i, j, k)

                            beta = min(beta, eval)
                            if beta <= alpha:
                                break

            return min_eval, best_move

    # Rename the minimax function to alpha_beta
    def alpha_beta_wrapper(self, depth, maximizing_player):
        return self.alpha_beta(depth, float('-inf'), float('inf'), maximizing_player)
