import numpy as np
import keras
from src.Util import Util
from src.player.Player import Player

class ANNPlayer(Player):

    def __init__(self, name, turn=None) -> None:
        super().__init__(name, turn)

        #Input: first 9 positions are the cells and 10th position is the turn of the player
        #Output: 9 possible rewards in base of position
        
        self.model = keras.Sequential()
        self.model.add(keras.layers.Dense(9, input_shape=(10,), activation = 'softmax'))
        self.model.compile(optimizer='SGD',
                        loss="mae",
                        metrics=["accuracy"])
        
    def play(self, board):
        _X = [Util.getPossibleValues().index(char) for char in board]
        _X.append(self.turn)
        prediction = self.model.predict([_X]) 
        prediction_index = np.argmax(prediction, axis=1)[0]        
        row = prediction_index//3
        col = prediction_index%3
        print(f'{self.name}: prediction-> {prediction} \
              prediction_index->{prediction_index} \
              row-> {row} col-> {col}') 
        return row, col
