from src.player.Player import Player
from src.Util import Util

class Game:

    def __init__(self, playerA:Player, playerB:Player):
        self.board = 'UUUUUUUUU'
        self.turn = 1
        self.players = [playerA, playerB]
        for i in range(len(self.players)):
            self.players[i].turn = i+1

    def printBoard(self):
        pass

    def currentPlayerName(self):
        return self.currentPlayer().name
    
    def currentPlayer(self):
        return self.players[self.turn-1]

    def play(self):
        self.printBoard()
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
        pass

    def postTie(self):
        pass

    def requestNextMovement(self):
        pass