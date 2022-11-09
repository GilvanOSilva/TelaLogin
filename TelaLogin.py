from tkinter import *

TelaLogin = Tk()

PadSize = 3
FontSize = 15

TelaLogin.title('Acesso Inicial')

rendimento = 0

LabelUser = Label(TelaLogin, text='Username', padx=PadSize, pady=PadSize, justify='left', font=FontSize)
LabelUser.grid(column=0, row=0, sticky=(W))
EntryUser = Entry(TelaLogin, textvariable=rendimento, font=FontSize)
EntryUser.grid(column=1, row=0)

LabelSenha = Label(TelaLogin, text='Senha', padx=PadSize, pady=PadSize, justify='left', font=FontSize)
LabelSenha.grid(column=0, row=1, sticky=(W))
EntrySenha = Entry(TelaLogin, textvariable=rendimento, font=FontSize)
EntrySenha.grid(column=1, row=1)

ButtonLogin = Button(TelaLogin, text='Acessar', command=rendimento, padx=PadSize, pady=PadSize, font=FontSize)
ButtonLogin.grid(column=1, row=3, sticky=(E, W))

ButtonCadastro = Button(TelaLogin, text='Cadastrar Novo Username', command=rendimento, padx=PadSize, pady=PadSize, font=FontSize)
ButtonCadastro.grid(column=1, row=4, sticky=(E, W))

TelaLogin.mainloop()
