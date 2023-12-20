class Board:
    players = ['x', 'O','']

    def __init__(self):
         self.board =  [[['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', '']],
                         [['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', '']],
                         [['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', '']],
                         [['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', '']]]
         self.current_player = self.players[0]  # Set default player to 'x'

    def set_player(self, player):
        if player in self.players:
            self.current_player = player
        else:
            raise ValueError("Invalid player. Choose from:", self.players)

    def set_AI_player(self):
     if self.current_player == 'x':
        self.AI_player = 'O'
     elif self.current_player == 'O':
        self.AI_player = 'x'
     elif self.current_player == '':
        None
     else:
        raise ValueError("Invalid current player. Cannot determine AI player.")


    def set_value(self, layer, row, column):
        if self.board[layer][row][column] == '':
            self.board[layer][row][column] = self.current_player
        else:
            print("Cell already occupied.")

    def get_value(self, layer, row, column):
        return self.board[layer][row][column]

    def turn(self):
        # Switch the current player after each turn
        if self.current_player == self.players[0]:
            self.current_player = self.players[1]
        else:
            self.current_player = self.players[0]

    def print_board(self):
        for layer in range(4):
            print(f"Layer {layer + 1}:")
            for row in range(4):
                print(" | ".join(str(cell) if cell != '' else ' ' for cell in self.board[layer][row]))
                if row < 3:
                    print("-" * 23)  # Divider between rows
            print("\n" * 2)  # Space between layers

    def is_win(self, player):
        # Check rows
        for layer in self.board:
            for row in layer:
                if all(cell == player for cell in row):
                    return True

        # Check columns
        for col in range(4):
            for layer in self.board:
                if all(row[col] == player for row in layer):
                    return True

        # Check diagonals within layers
        for layer in self.board:
            if all(layer[i][i] == player for i in range(4)) or all(layer[i][3 - i] == player for i in range(4)):
                return True

        # Check across layers
        for col in range(4):
            for row in range(4):
                if all(self.board[l][row][col] == player for l in range(4)):
                    return True

        # Check diagonals between layers
        if all(self.board[i][i][i] == player for i in range(4)) or all(self.board[i][i][3 - i] == player for i in range(4)):
            return True

        if all(self.board[i][3 - i][i] == player for i in range(4)) or all(self.board[i][3 - i][3 - i] == player for i in range(4)):
            return True

        return False
    def is_empty(self):
        # Check if the entire board is empty
        return all(self.board[layer][row][column] == '' for layer in range(4) for row in range(4) for column in range(4))

    def is_full(self):
        # Check if the entire board is full
        return all(self.board[layer][row][column] != '' for layer in range(4) for row in range(4) for column in range(4))

    def get_invalid_spaces(self):
        invalid_spaces = []
        for layer in range(4):
            for row in range(4):
                for column in range(4):
                    if self.board[layer][row][column] not in self.players:
                        invalid_spaces.append((layer, row, column))
        return invalid_spaces

    def reset_board(self):
     for layer in range(4):
        for row in range(4):
            for column in range(4):
                self.board[layer][row][column] = ''


    def is_symmetric(self, player, layer, row, column):
        # Check symmetry across layers
        if [self.board[l][row][column] for l in range(4)] != [player] * 4:
            return False

        # Check symmetry across rows
        if [self.board[layer][r][column] for r in range(4)] != [player] * 4:
            return False

        # Check symmetry across columns
        if [self.board[layer][row][c] for c in range(4)] != [player] * 4:
            return False

        return True



