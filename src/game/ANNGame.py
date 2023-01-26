""""
PENDIENTE POR ARREFGLAR
"""
from src.game.Game import *
from src.Util import Util

class ANNGame(Game):
    def __init__(self, playerA: Player, playerB: Player):
        super().__init__(playerA, playerB)
        self.X = []
        self.y = []

    def play(self):
        if Util.isFinish(self.board):
            self.postFinish()
        elif Util.isFull(self.board):
            self.postTie()
        else:
            row, col = self.requestNextMovement()
            self.board = Util.setValue(self.board, row, col, Util.getValueToWrite(self.turn))
            self.turn = Util.changeTurn(self.turn)
            self.play()

    def postFinish(self):
        turn = Util.changeTurn(self.turn)
        winner = self.currentPlayer()
        #Partimos del supuesto de que el primer jugador es al que entrenaremos
        reward = -1
        if winner.turn == self.players[0].turn:
            reward = 1
        #Saving trace
        self.saveTrace(reward)

    def postTie(self):
        self.turn = Util.changeTurn(self.turn)
        self.saveTrace(0)
    
    def saveTrace(self, reward, turn):
        self.y.append(reward)
        self.X.append(self.stringToVector(self.board, turn))

    def requestNextMovement(self):
        return self.currentPlayer().play(self.board)
    

    def stringToVector(string):
        vec = [string.index(char) for char in string]
        vec.append()
        return vec
