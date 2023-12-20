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





    def minimax(self, depth, maximizing_player):
        self.visited += 1
        if depth == 0:
            if self.is_terminal():
                return 20, None
            else:
                return 0 , None

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

