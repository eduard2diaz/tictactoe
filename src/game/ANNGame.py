from src.game.GameTerminal import *
from src.Util import Util
import random

class ANNGame(GameTerminal):
    REWARD_WIN = 3
    REWARD_LOST = 2
    REWARD_TIE = 1
    REWARD_WRONG_POSITION = 0

    def __init__(self, playerA: Player, playerB: Player):
        super().__init__(playerA, playerB)
        self.reward = [self.REWARD_TIE for _ in range(9)]
        print(self.reward)

    def play(self):
        while not Util.isFinish(self.board) and not Util.isFull(self.board):
            for i in range(len(self.board)):
                row, col = i//3, i%3
                if self.board[i] != Util.getPossibleValues()[0]:
                    self.reward[i] = self.REWARD_WRONG_POSITION
                elif Util.isFinish(Util.setValue(self.board, row, col, Util.getValueToWrite(self.turn))):
                    self.reward[i] = self.REWARD_WIN
                elif Util.isFinish(Util.setValue(self.board, row, col, Util.getValueToWrite(Util.changeTurn(self.turn)))):
                    self.reward[i] = self.REWARD_LOST
                else:
                    self.reward[i] = self.REWARD_TIE    

            print(self.board, self.reward)
            aux = [Util.getPossibleValues().index(character) for character in self.board]
            aux.append(self.turn)
            self.currentPlayer().model.fit([aux], [self.reward])
            row, col = self.currentPlayer().play(self.board)
            self.board = Util.setValue(self.board, row, col, Util.getValueToWrite(self.turn))
            self.turn = Util.changeTurn(self.turn)
            self.printBoard()

        if Util.isFinish(self.board):
            self.postFinish()
        elif Util.isFull(self.board):
            self.postTie()


    def postFinish(self):
        self.turn = Util.changeTurn(self.turn)
        print(f'WINNER {self.currentPlayerName()}')

    def postTie(self):
        print('EMPATE!!')