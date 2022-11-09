from tkinter import *

TelaLogin = Tk()

PadSize = 3
FontSize = 15

TelaLogin.title('Painel de Controle')

rendimento = 0

LabelWelcome = Label(TelaLogin, text='Bem Vindo "User"', padx=PadSize, pady=PadSize, justify='left', font=FontSize)
LabelWelcome.grid(column=0, row=0, sticky=(W))

ButtonLogin = Button(TelaLogin, text='Alterar dados da conta', command=rendimento, padx=PadSize, pady=PadSize, font=FontSize)
ButtonLogin.grid(column=0, row=1, sticky=(E, W))

ButtonCadastro = Button(TelaLogin, text='Remover cadastro do sistema', command=rendimento, padx=PadSize, pady=PadSize, font=FontSize)
ButtonCadastro.grid(column=0, row=2, sticky=(E, W))

TelaLogin.mainloop()
