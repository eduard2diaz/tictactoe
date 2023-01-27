class Util:

    @staticmethod
    def changeTurn(turno):
        if turno == 1:
            return turno + 1
        return turno - 1

    @staticmethod
    def getPossibleValues():
        return ['U','X', 'O']
    
    @staticmethod
    def getValueToWrite(turn):
        return Util.getPossibleValues()[turn]

    @staticmethod
    def getValue(board, row, col):
        if row < 0 or row > 2 or col < 0 or col > 2:
            raise Exception('Invalid position')
        return board[row * 3 + col]

    @staticmethod
    def setValue(board, row, col, value):
        if row < 0 or row > 2 or col < 0 or col > 2:
            raise Exception('Invalid position', (row, col))
        return board[:row * 3 + col] + value + board[row * 3 + col + 1: len(board)]

    @staticmethod
    def isFull(board):
        return not 'U' in board

    @staticmethod
    def isFinish(board):
        # Funcion que retorna un booleano que indica si algun jugador gano
        for i in range(3):
            if (Util.getValue(board, 0, i) == Util.getValue(board, 1, i)
                and Util.getValue(board, 1, i) == Util.getValue(board, 2, i)
                and Util.getValue(board, 1, i) != 'U') or (Util.getValue(board, i, 0) == Util.getValue(board, i, 1)
                                                      and Util.getValue(board, i, 1) == Util.getValue(board, i, 2)
                                                      and Util.getValue(board, i, 1) != 'U'):
                return True

        if (Util.getValue(board, 0, 0) == Util.getValue(board, 1, 1)
            and Util.getValue(board, 1, 1) == Util.getValue(board, 2, 2)
            and Util.getValue(board, 1, 1) != 'U') or (Util.getValue(board, 0, 2) == Util.getValue(board, 1, 1)
                                                  and Util.getValue(board, 1, 1) == Util.getValue(board, 2, 0)
                                                  and Util.getValue(board, 1, 1) != 'U'):
            return True
        return False