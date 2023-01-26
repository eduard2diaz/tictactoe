from src.game.GameTerminal import GameTerminal
from src.player.HumanPlayer import HumanPlayer
from src.player.MinMaxPlayer import MinMaxPlayer

player1 = MinMaxPlayer('edua')
player2 = MinMaxPlayer('ney')

game = GameTerminal(player1, player2)
game.play()