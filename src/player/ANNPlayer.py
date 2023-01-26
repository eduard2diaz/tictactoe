import keras
from src.player.Player import Player
from src.player.ANNPlayer import ANNPlayer
from src.game.GameTerminal import GameTerminal

class ANNPlayer(Player):
    def __init__(self, name, turn=None) -> None:
        super().__init__(name, turn)

        model = keras.Sequential()
        model.add(keras.layers.Dense(11, input_shape=(9,), activation = 'softmax'))
        model.compile(optimizer=keras.optimizers.Adam(1e-3),
                        loss="binary_crossentropy",
                        metrics=["accuracy"])
        self.model = model

    

    def fit(self):
        auxPlayer = ANNPlayer()
        for _ in range(200):
            game = GameTerminal(self, auxPlayer)
            game.play()


    def play(self, board):
        prediction = self.model.predict(board)   
