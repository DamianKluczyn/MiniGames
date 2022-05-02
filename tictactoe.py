import random
class tictactoegame:
    def __init__(self):
        self.board = []

    #Randomizing which player starts
    def WhoIsFirst(self):
        return random.randint(1,2)

    #Creating 3x3 board filled with '-'
    def CreateBoard(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.board.append(row)

    #Function to show board
    def ShowBoard(self):
        for i in self.board:
            for item in i:
                print(item, end=" ")
            print()
    #Inserting value on board
    def Insert(self, row, col, player):
        self.board[row][col] = player

    #Checking if player won
    def DidPlayerWon(self, player):
        a = len(self.board)
        win = None
        #checking if player won in rows
        for i in range(a):
            win = True
            for j in range(a):
                if self.board[i][j] != player:
                    win = False
                    break
            if win:
                return win
        #cheking if player won in columns
        for i in range(a):
            win = True
            for j in range(a):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win
        #checking if player won on diagonals
        for i in range(a):
            win = True
            if self.board[i][i] != player:
                win = False
                break
        if win:
            return win
        for i in range(a):
            win = True
            if self.board[i][(a-1)-i] != player:
                win = False
                break
        if win:
            return win
    #checking if board is filled
    def IsFilled(self):
        for i in self.board:
            for item in i:
                if item == '-':
                    return False
        return True
    #swapping player turn
    def player_swap(self,player):
        return 'X' if player == 'O' else 'O'

    def game(self):
        self.CreateBoard()
        player = 'X' if self.WhoIsFirst() == 1 else 'O'
        while True:
            print(f"Player {player} turn")

            self.ShowBoard()

            row, col = list(map(int, input("Enter row and column numbers to input your figure: ").split()))
            print()

            self.Insert(row-1, col-1, player)
            if self.DidPlayerWon(player):
                print(f"Player {player} wins the game!")
                break
            if self.IsFilled():
                print("Draw!")
                break
            player = self.player_swap(player)
        print()
        self.ShowBoard()