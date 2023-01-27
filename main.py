from src.player.ANNPlayer import ANNPlayer
from src.game.ANNGame import ANNGame

trainable = ANNPlayer('edua')
game_count = 0

for _ in range(200):
    auxPlayer = ANNPlayer('Auxiliar')
    game_count+=1
    print(f'Game {game_count}:', end='')
    
    game = ANNGame(trainable, auxPlayer)
    game.play()

    #Training the model
    print()
    
trainable.model.save('trainable_model.h5')