from src.Util import Util
from src.player.Player import Player

class MinMaxPlayer(Player):
    
    @staticmethod
    def simulate(board, turn, depth):
        if Util.isFinish(board):
            if turn == 1: #PC won
                return (1, depth)
            else: #Player 1 won
                return (-1, depth)
        elif Util.isFull(board):
            return (0, depth)
        
        choices = []
        for i in range(3):
            for j in range(3):
                if Util.getValue(board,i,j) == 'U':
                    board_new = Util.setValue(board, i, j, Util.getValueToWrite(turn))
                    result_value, result_depth = MinMaxPlayer.simulate(board_new, Util.changeTurn(turn), depth+1)
                    choices.append({'row':i, 'col':j, 'result':result_value, 'depth': result_depth})

        def choiceNextStep(choices, turn, nivel):
            row, col, val, depth = choices[0]['row'],\
                                choices[0]['col'],\
                                choices[0]['result'],\
                                choices[0]['depth']

            for i in range(1, len(choices)):
                if turn == 1: #Player 1 (BUSCANDO EL VALOR MAS PEQUENO, LUEGO EN CASO DE EMPATE EL MAS CERCANO)
                    if choices[i]['result'] < val:
                        row, col, val, depth = choices[i]['row'], choices[i]['col'], choices[i]['result'], choices[i]['depth']
                    elif choices[i]['result'] == val and choices[i]['depth'] < depth:
                        row, col, val, depth = choices[i]['row'], choices[i]['col'], choices[i]['result'], choices[i]['depth']
                else: #PC (BUSCANDO EL VALOR MAS GRANDE, LUEGO EN CASO DE EMPATE EL MAS CERCANO)
                    if choices[i]['result'] > val:
                        row, col, val, depth = choices[i]['row'], choices[i]['col'], choices[i]['result'], choices[i]['depth']
                    elif choices[i]['result'] == val and choices[i]['depth'] < depth:
                        row, col, val, depth = choices[i]['row'], choices[i]['col'], choices[i]['result'], choices[i]['depth']

            #sI ESTOY EN EL NIVEL CERO, ES PORQUE ES LA PC BUSCANDO EL PRIMER PASO DE SU MEJOR SECUENCIA DE PASOS,
            #POR LO QUE RETORNO EL PASO A DAR
            if nivel==0:
                print('MEJOR FILA', row, 'MEJOR COLUMA', col)
                return (row, col)
            #SINO RETORNO EL PESO Y NIVEL DE PROFUNDIDAD DE LA MEJOR JUGADA
            print('VALOR', val, 'DEPTH', depth)
            return (val, depth)
            
        return choiceNextStep(choices, turn, depth)
    
    def play(self, board):
        return MinMaxPlayer.simulate(board, self.turn, 0)
