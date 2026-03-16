class TicTacToe:
 
    def __init__(self, n: int):
        self.board = [['.']*n for i in range(n)]
        self.n = n
        self.num_moves_played = 0
        
        # Track counts for each row, column, and diagonal
        # Positive for player 1, negative for player 2
        self.row_counts = [0] * n
        self.col_counts = [0] * n
        self.diag_count = 0      # main diagonal (top-left to bottom-right)
        self.anti_diag_count = 0 # anti-diagonal (top-right to bottom-left)
        
 
    def move(self, row: int, col: int, player: int) -> int:
        """
        Place a mark on the board and check if the player wins.
        Returns:
            0 if no winner yet
            1 if player 1 wins
            2 if player 2 wins
        """
        # Determine the mark and the value to add to counts
        player_mark = 'X' if player == 1 else 'O'
        value = 1 if player == 1 else -1
        
        # Place the mark on the board
        self.board[row][col] = player_mark
        
        # Update row and column counts
        self.row_counts[row] += value
        self.col_counts[col] += value
        
        # Update diagonal count if on main diagonal
        if row == col:
            self.diag_count += value
        
        # Update anti-diagonal count if on anti-diagonal
        if row + col == self.n - 1:
            self.anti_diag_count += value
        
        # Increment move counter
        self.num_moves_played += 1
        
        # Check for winner
        # Player 1 wins if any count equals n
        # Player 2 wins if any count equals -n
        win_value = self.n if player == 1 else -self.n
        
        if (self.row_counts[row] == win_value or 
            self.col_counts[col] == win_value or 
            self.diag_count == win_value or 
            self.anti_diag_count == win_value):
            return player
        
        # No winner yet
        return 0
    
    def print_board(self):
        """Helper method to visualize the board"""
        for row in self.board:
            print(' '.join(row))
        print()