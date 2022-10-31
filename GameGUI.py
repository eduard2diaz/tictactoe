from tkinter import *
from functools import partial
from Game import *

class GameGUI(Game):

    def __init__(self):
        super().__init__()
        self.mode = 1
        self.status_label, buttons = None, None

    def createWindowTemplate(self):
        # Creamos la ventana
        ventana = Tk()
        # Cambiamos el titulo de la ventana
        ventana.title('Tic_Tac_Toe')
        # Cambiamos el tamanno de la ventana
        ventana.geometry('650x350')
        # Cambiarle el icono de la ventana
        ventana.iconbitmap('tic-tac-toe_39453.ico')
        # Creamos un frame y lo empaquetamos
        marco = Frame(ventana, background='white')
        marco.pack()
        # Cambiamos el tamanno del frame
        marco.config(width=650, height=350)
        # Impedimos que la ventana sea redimensionada en alguna direccion (ancho, alto) seria
        ventana.resizable(False, False)

        return ventana, marco

    def modelSelectionWindow(self, ventana, marco):
        label_game_mode = Label(marco, text='Seleccione el modo de juego', width=25)
        label_game_mode.place(relx=0.5, rely=30, anchor='center')
        label_game_mode.pack()

        img_mode1 = PhotoImage(file='./mode1.png')
        label_game_mode_player_vs_player = Label(marco, image=img_mode1)
        label_game_mode_player_vs_player.place(relx=0.5, rely=30, anchor='center')
        label_game_mode_player_vs_player.pack()

        img_mode2 = PhotoImage(file='./mode1.png')
        label_game_mode_player_vs_pc = Label(marco, image=img_mode2)
        label_game_mode_player_vs_pc.place(relx=0.5, rely=30, anchor='center')
        label_game_mode_player_vs_pc.pack()

        def setMode1(event):
            ventana.destroy()
            self.play()

        def setMode2(event):
            ventana.destroy()
            self.mode = 2
            self.play()

        label_game_mode_player_vs_player.bind('<Button-1>', setMode1)
        label_game_mode_player_vs_pc.bind('<Button-1>', setMode2)

        # Levantamos la ventana
        ventana.mainloop()

    def start(self):
        # Funcion que inicia el juego
        ventana, marco = self.createWindowTemplate()
        self.modelSelectionWindow(ventana, marco)

    def Action(self, i):
        # i = row * 3 + col
        row = 1

        if i < 3:
            row = 0
        elif i > 5:
            row = 2

        col = (i - row * 3)

        if not (Util.isFinish(self.board) or Util.isFull(self.board)):
            self.board = Util.setValue(self.board, row, col, Util.getValueToWrite(self.turn))
            self.buttons[i]['text'] = Util.getValueToWrite(self.turn)

            if Util.isFinish(self.board):
                self.status_label.config(text='WINNER ' + str(self.currentPlayer()))
            elif Util.isFull(self.board):
                self.status_label.config(text='EMPATE')
            else:
                self.turn = Util.changeTurn(self.turn)
                self.status_label.config(text='TURNO DE ' + self.currentPlayer())

                if self.turn == 2 and self.mode == 2:
                    row, col = MinMaxPlayer.simulate(self.board, self.turn, 0)
                    self.Action(row * 3 + col)

    def play(self):
        ventana, marco = self.createWindowTemplate()

        self.status_label = Label(ventana, text='Status:')
        self.status_label.place(relx=.65, rely=.1)

        self.buttons = [Button(marco, width=5, height=5, command=partial(self.Action, i)) for i in range(9)]
        for i in range(3):
            for j in range(3):
                self.buttons[i * 3 + j].grid(row=i, column=j)

        text = 'Modo de Juego: Player VS Player'
        if self.mode == 2:
            text = 'Modo de Juego: Player VS PC'

        game_mode = Label(ventana, text=text)
        game_mode.place(relx=.65)

        ventana.mainloop()


if __name__ == '__main__':
    from GameGUI import GameGUI
    game = GameGUI()
    game.start()        
