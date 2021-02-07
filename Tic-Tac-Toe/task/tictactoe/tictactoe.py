# write your code here
row, col = 3, 3


class Board:
    def __init__(self):
        self.position = []
        self.player_x = Player('X')
        self.player_o = Player('O')

    def display_board(self):
        print('-' * 9)
        for i in range(1, row + 1):
            print('|')
            for j in range(1, col + 1):
                print(self.position[i][j])
            print('|')
        print('-' * 9)
        print()

    def status(self):
        if (abs(len(self.player_o.positions) - len(self.player_x.positions)) >= 2) or (
                self.player_x.status == self.player_o.status and self.player_x.status == 'win'):
            print("Impossible")
        elif self.player_x.status == 'win':
            print('X wins')
        elif self.player_o.status == 'win':
            print('O wins')
        elif self.player_x.status == self.player_o.status and (
                len(self.player_x.values) - len(self.player_o.values)) == 0:
            print("Draw")
        else:
            print("Game not finished")

    def take_input(self):
        # try:
        move = list(int(i) for i in input('Enter the coordinates: ').strip().split())
        if move[0] == 1:
            move[0] = 3
        if move[0] == 3:
            move[0] = 1
        # except ValueError:
        if type(move[0]) != type(0) or type(move[1]) != type(0):
            print("You should enter numbers!")
            move = -1
            return move
        if move[0] not in [1, 2, 3] or move[1] not in [1, 2, 3]:
            print("Coordinates should be from 1 to 3!")
            move = -1
            return move
        if move[1] * 3 + move[0] - 1 in self.player_o.positions or move[1] * 3 + move[
            0] - 1 in self.player_x.positions:
            print("This cell is occupied! Choose another one!")
            move = -1
            return move

        print(move)
        return move


class Player:
    def __init__(self, item):
        self.values = item
        self.positions = []
        self.status = None

    def place_occupied(self, positions):
        for i in range(1, row + 1):
            for count, symbol in enumerate(positions):
                if symbol == self.values:
                    self.positions.append(count)

    @staticmethod
    def is_win(position):
        if 0 in position:  # covers diagonal 1
            if 4 in position:
                if 8 in position:
                    return 'win'
        if 6 in position:  # covers diagonal 2
            if 4 in position:
                if 2 in position:
                    return 'win'
        for j in range(3):  # vertical row check
            for i in range(0, 9, 3):
                if i + j not in position:
                    break
                if i + j in [6, 7, 8]:
                    return 'win'

        for i in range(0, 9, 3):  # horizontal row check
            for j in range(3):
                if i + j not in position:
                    break
                if i + j in [2, 4, 5]:
                    return 'win'
            return 'no'


# driving code
game = Game()
counter = 0
first_input = [i for i in input().strip()]
game.board.position = first_input
game.board.display_board()
while counter < 9:
    player_move = game.take_input()
    if counter % 2 == 0:
        if player_move == -1:
            continue
        else:
            game.player_x.positions.append(player_move[0] * 3 + player_move[1])
            game.board.position[player_move[0] * 3 + player_move[1]] = 'X'
            counter += 1
            game.board.display_board()
    else:
        if player_move == -1:
            continue
        else:
            game.player_x.positions.append(player_move[0] * 3 + player_move[1])
            game.board.position[player_move[0] * 3 + player_move[1]] = 'X'
            counter += 1
            game.board.display_board()
