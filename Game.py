from MinMaxPlayer import MinMaxPlayer
from Util import Util
import sys

class Game:

    def __init__(self):
        self.board = 'UUUUUUUUU'
        self.turn = 1

    def printBoard(self):
        for i in range(3):
            for j in range(3):
                if j == 2:
                    print(self.board[i * 3 + j])
                else:
                    print(self.board[i * 3 + j], end='')

    def currentPlayer(self):
        if self.mode == 2 and self.turn == 2:
            return 'PLAYER PC'
        else:
            return 'PLAYER ' + str(self.turn)

    def play(self):
        self.printBoard()
        if Util.isFinish(self.board):
            self.turn = Util.changeTurn(self.turn)
            if self.mode == 2 and self.turn == 2:
                print('WINNER PC')
            else:    
                print('WINNER PLAYER', )
            sys.exit(0)
        elif Util.isFull(self.board):
            print('EMPATE!!')
            sys.exit(0)
        elif self.mode == 1 or self.turn==1:
            print('TURNO DE PLAYER',self.currentPlayer())
            row = int(input('Indique la fila donde escribir'))
            col = int(input('Indique la columna donde escribir'))
        else:
            row, col = MinMaxPlayer.simulate(self.board, self.turn, 0)
        self.board = Util.setValue(self.board, row, col, Util.getValueToWrite(self.turn))

        self.turn = Util.changeTurn(self.turn)
        self.play()

    def start(self):
        print('MENU')
        print('Select game mode')
        print('1. Human VS Human')
        print('2. Human VS PC')
        mode = int(input('Mode:'))

        if mode != 1 and mode != 2:
            raise Exception('Wrong mode game')

        self.mode = mode
        self.play()


if __name__ == '__main__':
    from Game import Game
    game = Game()
    game.start()