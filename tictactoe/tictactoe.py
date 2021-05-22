class TicTacToe:
    def __init__(self) -> None:
        self.players_turn = "X"
        self.set_board()

    def set_board(self):
        """Initialize empty 3x3 game board"""
        self.board = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""],
        ]

    def draw_board(self):
        """Print Gameboard to screen"""
        print(f"{'':6}{'A':^6}{'B':^6}{'C':^6}\n")
        for i, row in enumerate(self.board):
            print(f"{i:^7}{row[0]:^4}|{row[1]:^5}|{row[2]:^5}")

            # don't print row seperator at bottom
            if i != 2:
                print(f"{'':5}", "-" * 17)

        print()

    def is_winner(self):
        """Check for a Winner

        Returns:
            String: Winner: "X" or "O", draw: "DRAW" or empty string
        """

        # check rows
        for row in self.board:
            if row[0] == row[1] == row[2]:
                return row[0]

        # check columns
        for col in zip(*self.board):
            if col[0] == col[1] == col[2]:
                return col[0]

        # check diaganol
        if self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return self.board[0][0]
        elif self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return self.board[0][2]

        # check for draw
        for row in self.board:
            draw = True
            if "" in row:
                draw = False
        if draw:
            return "DRAW"

        # Return empty string if game there is no winner and game is not a draw
        return ""

    def player_selection(self):
        """Get user selection, validate input, plase selection on board
        and toggle player turn"""
        valid_cols = ["A", "B", "C"]
        valid_rows = ["0", "1", "2"]

        print(f"Player {self.players_turn}, it is your turn to pick")
        valid = False
        while not valid:
            selection = input("Selection: ").upper()
            selection = selection.replace(" ", "")
            if (
                len(selection) == 2
                and selection[0] in valid_cols
                and selection[1] in valid_rows
            ):
                valid = True
            else:
                print("Invalid Selection, try again")

        col = valid_cols.index(selection[0])
        row = int(selection[1])

        self.board[row][col] = self.players_turn
        if self.players_turn == "X":
            self.players_turn = "O"
        else:
            self.players_turn = "X"
