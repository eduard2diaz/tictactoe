import sys
from src.game.Game import *
from src.player.HumanPlayer import HumanPlayer

class GameTerminal(Game):

    def printBoard(self):
        for i in range(3):
            for j in range(3):
                if j == 2:
                    print(self.board[i * 3 + j])
                else:
                    print(self.board[i * 3 + j], end='')

    def postFinish(self):
        self.turn = Util.changeTurn(self.turn)
        print(f'WINNER {self.currentPlayerName()}')
        sys.exit(0)

    def postTie(self):
        print('EMPATE!!')
        sys.exit(0)

    def requestNextMovement(self):
        print(f'TURNO DE PLAYER {self.currentPlayerName()}')
        if  isinstance(self.currentPlayer(), HumanPlayer) :
            row = int(input('Indique la fila donde escribir'))
            col = int(input('Indique la columna donde escribir'))
        else:
            row, col = self.currentPlayer().play(self.board)
        return row, col