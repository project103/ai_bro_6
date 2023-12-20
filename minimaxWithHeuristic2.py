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
        # Heuristic function: Count the number of possible ways to win for the given player
        score = 0

        # Check rows
        for layer in range(4):
            for row in range(4):
                if all(self.board[layer][row][ col] == player for col in range(4)):
                    score += 1

        # Check columns
        for layer in range(4):
            for col in range(4):
                if all(self.board[layer][row][ col] == player for row in range(4)):
                    score += 1

        # Check diagonals
        for layer in range(4):
            # Main diagonals
            if all(self.board[layer][i][i] == player for i in range(4)):
                score += 1
            if all(self.board[layer][i][3 - i] == player for i in range(4)):
                score += 1

            # Upper diagonals
            if all(self.board[layer][0][i] == player for i in range(4)):
                score += 1
            if all(self.board[layer][1][i] == player for i in range(4)):
                score += 1

            # Lower diagonals
            if all(self.board[layer][i][0] == player for i in range(4)):
                score += 1
            if all(self.board[layer][i][1] == player for i in range(4)):
                score += 1

        return score

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

