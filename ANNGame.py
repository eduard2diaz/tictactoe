from Game import *
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers


class ANNGame(Game):

    def currentPlayer(self):
        if self.turn == 2:
            return 'PLAYER MinMAX'
        else:
            return 'PLAYER ANN'

    def play(self):
        self.printBoard()
        if Util.isFinish(self.board):
            self.turn = Util.changeTurn(self.turn)
            if self.turn == 2:
                print('WINNER MinMax')
            else:    
                print('WINNER ANN')
        elif Util.isFull(self.board):
            print('EMPATE!!')
            return 0
        elif self.turn==1:
            print('TURNO DE PLAYER',self.currentPlayer())
            row = int(input('Indique la fila donde escribir'))
            col = int(input('Indique la columna donde escribir'))
        else:
            row, col = MinMaxPlayer.simulate(self.board, self.turn, 0)
        self.board = Util.setValue(self.board, row, col, Util.getValueToWrite(self.turn))

        self.turn = Util.changeTurn(self.turn)
        self.play()

    def start(self):

        def getModel():
            model = tf.keras.Sequential()
            model.add(layers.Dense(12, input_shape=(9,)))
            model.add(layers.Dense(12))
            model.add(layers.Dense(12))
            model.add(layers.Dense(9, activation= "softmax"))

            model.compile(optimizer=keras.optimizers.Adam(1e-3),
                        loss="binary_crossentropy",
                        metrics=["accuracy"])

            model.summary()

            return model

        ann = getModel()
        
        n_games = 500

        while n_games > 0:
            self.play()
            n_games -=1

if __name__ == '__main__':
    from ANNGame import ANNGame
    game = ANNGame()
    game.start()