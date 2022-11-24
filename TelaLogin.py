from tkinter import *
from openpyxl import load_workbook


def acessar():
    file_xl = load_workbook(filename='Logins.xlsx')
    logins = file_xl.active
    pos_tab = 1
    user = EntryUser.get()
    senha = EntrySenha.get()
    while logins['A' + str(pos_tab)].value is not None:
        if user == logins['A' + str(pos_tab)].value:
            if senha == logins['B' + str(pos_tab)].value:
                LabelMensagem['text'] = 'Obtido acesso.'
                User.set(logins['A' + str(pos_tab)].value)
                tela_painel(pos_tab)
                break
            else:
                LabelMensagem['text'] = 'Senha incorreta.'
                break
        pos_tab += 1
    if logins['A' + str(pos_tab)].value is None:
        LabelMensagem['text'] = 'User não está cadastrado.'


def cadastar():
    file_xl = load_workbook(filename='Logins.xlsx')
    logins = file_xl.active
    pos_tab = 1
    exist_user = False
    exist_email = False
    while logins['A' + str(pos_tab)].value is not None:
        if logins['A' + str(pos_tab)].value == Username.get():
            exist_user = True
        if logins['C' + str(pos_tab)].value == Email.get():
            exist_email = True
        pos_tab += 1
    if exist_user is True:
        LabelMensagem['text'] = 'Este usuário já está cadastrado.'
    elif len(Username.get()) < 6 or ' ' in Username.get():
        LabelMensagem['text'] = 'Usuário não atende o crítério.'
    elif exist_email is True:
        LabelMensagem['text'] = 'Este E-mail já está cadastrado.'
    elif '@' or '.' not in Email.get() and ' ' in Email.get():
        LabelMensagem['text'] = 'E-mail não atende o crítério.'
    else:
        pos_tab = 1
        while logins['A' + str(pos_tab)].value is not None:
            pos_tab += 1
        logins['A' + str(pos_tab)] = Username.get()
        logins['B' + str(pos_tab)] = Senha.get()
        logins['C' + str(pos_tab)] = Email.get()
        logins['D' + str(pos_tab)] = Nome.get()
        logins['E' + str(pos_tab)] = Idade.get()
        file_xl.save(filename='Logins.xlsx')
        LabelMensagem['text'] = 'Cadastro efetuado com sucesso.'


def alterar():
    file_xl = load_workbook(filename='Logins.xlsx')
    logins = file_xl.active
    logins['B' + str(navpos)] = Senha.get()
    logins['D' + str(navpos)] = Nome.get()
    logins['E' + str(navpos)] = Idade.get()
    file_xl.save(filename='Logins.xlsx')
    LabelMensagem['text'] = 'Dados alterados.'
    tela_painel(navpos)


def alterar():
    file_xl = load_workbook(filename='Logins.xlsx')
    logins = file_xl.active

    logins['B' + str(navpos)] = Senha.get()
    logins['D' + str(navpos)] = Nome.get()
    logins['E' + str(navpos)] = Idade.get()
    file_xl.save(filename='Logins.xlsx')
    LabelMensagem['text'] = 'Dados alterados.'
    tela_painel(navpos)


def remover():
    file_xl = load_workbook(filename='Logins.xlsx')
    logins = file_xl.active
    logins['A' + str(navpos)] = None
    logins['B' + str(navpos)] = None
    logins['C' + str(navpos)] = None
    logins['D' + str(navpos)] = None
    logins['E' + str(navpos)] = None
    file_xl.save(filename='Logins.xlsx')
    LabelMensagem['text'] = 'Dados alterados.'
    tela_login()


def tela_cadastro():
    Choose.set('2')
    TelaLogin.destroy()


def tela_login():
    Choose.set('1')
    TelaLogin.destroy()


def tela_painel(pos):
    Choose.set('3')
    UserId.set(pos)
    TelaLogin.destroy()


def voltar_painel():
    Choose.set('3')
    UserId.set(navpos)
    TelaLogin.destroy()


def tela_alterar():
    Choose.set('4')
    UserId.set(navpos)
    TelaLogin.destroy()


def tela_remover():
    Choose.set('5')
    UserId.set(navpos)
    TelaLogin.destroy()


Menu = 1
while True:
    if Menu == 1:
        TelaLogin = Tk()
        PadSize = 3
        FontSize = 15
        TelaLogin.title('Acesso Inicial')
        Choose = StringVar()
        User = StringVar()
        UserId = StringVar()
        Senha = StringVar()
        Choose.set('1')

        LabelUser = Label(TelaLogin, text='Username', padx=PadSize, pady=PadSize, justify='left', font=FontSize)
        LabelUser.grid(column=0, row=0, sticky='W')
        EntryUser = Entry(TelaLogin, textvariable=User, font=FontSize)
        EntryUser.grid(column=1, row=0)

        LabelSenha = Label(TelaLogin, text='Senha', padx=PadSize, pady=PadSize, justify='left', font=FontSize)
        LabelSenha.grid(column=0, row=1, sticky='W')
        EntrySenha = Entry(TelaLogin, show='*', textvariable=Senha, font=FontSize)
        EntrySenha.grid(column=1, row=1)

        ButtonLogin = Button(TelaLogin, text='Acessar', command=acessar, padx=PadSize, pady=PadSize, font=FontSize)
        ButtonLogin.grid(column=1, row=3, sticky='E , W')

        ButtonCadastro = Button(TelaLogin, text='Cadastrar Novo Username', command=tela_cadastro, padx=PadSize, pady=PadSize, font=FontSize)
        ButtonCadastro.grid(column=1, row=4, sticky='E , W')

        ButtonSair = Button(TelaLogin, text='Sair', command=quit, padx=PadSize, pady=PadSize, font=FontSize)
        ButtonSair.grid(column=1, row=5, sticky='E , W')

        LabelMensagem = Label(TelaLogin, text='', padx=PadSize, pady=PadSize, justify='left', font=FontSize)
        LabelMensagem.grid(column=1, row=6, sticky='W')

        TelaLogin.mainloop()
        Menu = int(Choose.get())
        navpos = str(UserId.get())

    if Menu == 2:
        TelaLogin = Tk()

        PadSize = 3
        FontSize = 15

        TelaLogin.title('Cadastro')

        Username = StringVar()
        Senha = StringVar()
        Email = StringVar()
        Nome = StringVar()
        Idade = StringVar()

        LabelUser = Label(TelaLogin, text='Username', padx=PadSize, pady=PadSize, justify='left', font=FontSize)
        LabelUser.grid(column=0, row=0, sticky='W')
        EntryUser = Entry(TelaLogin, textvariable=Username, font=FontSize)
        EntryUser.grid(column=1, row=0)

        LabelSenha = Label(TelaLogin, text='Senha', padx=PadSize, pady=PadSize, justify='left', font=FontSize)
        LabelSenha.grid(column=0, row=1, sticky='W')
        EntrySenha = Entry(TelaLogin, textvariable=Senha, font=FontSize)
        EntrySenha.grid(column=1, row=1)

        LabelEmail = Label(TelaLogin, text='E-Mail', padx=PadSize, pady=PadSize, justify='left', font=FontSize)
        LabelEmail.grid(column=0, row=2, sticky='W')
        EntryEmail = Entry(TelaLogin, textvariable=Email, font=FontSize)
        EntryEmail.grid(column=1, row=2)

        LabelNome = Label(TelaLogin, text='Nome', padx=PadSize, pady=PadSize, justify='left', font=FontSize)
        LabelNome.grid(column=0, row=3, sticky='W')
        EntryNome = Entry(TelaLogin, textvariable=Nome, font=FontSize)
        EntryNome.grid(column=1, row=3)

        LabelIdade = Label(TelaLogin, text='Idade', padx=PadSize, pady=PadSize, justify='left', font=FontSize)
        LabelIdade.grid(column=0, row=4, sticky='W')
        EntryIdade = Entry(TelaLogin, textvariable=Idade, font=FontSize)
        EntryIdade.grid(column=1, row=4)

        ButtonLogin = Button(TelaLogin, text='Cadastar', command=cadastar, padx=PadSize, pady=PadSize, font=FontSize)
        ButtonLogin.grid(column=1, row=5, sticky='N , S, W, E')

        ButtonVoltar = Button(TelaLogin, text='Voltar', command=tela_login, padx=PadSize, pady=PadSize, font=FontSize)
        ButtonVoltar.grid(column=1, row=6, sticky='N , S, W, E')

        LabelMensagem = Label(TelaLogin, text='', padx=PadSize, pady=PadSize, justify='left', font=FontSize)
        LabelMensagem.grid(column=1, row=7, rowspan=2, sticky='N , S')

        TelaLogin.mainloop()
        Menu = int(Choose.get())

    if Menu == 3:
        TelaLogin = Tk()

        pad_size = 3
        font_size = 15

        TelaLogin.title('Painel de Controle')
        UserId = StringVar()
        contagem_total = 4

        label_welcome = Label(TelaLogin, text='Bem Vindo ' + str(navpos), padx=pad_size, pady=pad_size, justify='left', font=font_size)
        label_welcome.grid(column=0, row=0, sticky='W')

        button_alterar = Button(TelaLogin, text='Alterar dados da conta', command=tela_alterar, padx=pad_size, pady=pad_size, font=font_size)
        button_alterar.grid(column=0, row=1, sticky='E , W')

        button_remover = Button(TelaLogin, text='Remover cadastro do sistema', command=tela_remover, padx=pad_size, pady=pad_size, font=font_size)
        button_remover.grid(column=0, row=2, sticky='E , W')

        ButtonVoltar = Button(TelaLogin, text='Encerrar Sessão', command=tela_login, padx=PadSize, pady=PadSize, font=FontSize)
        ButtonVoltar.grid(column=0, row=4, sticky='N , S, W, E')

        label_total_user = Label(TelaLogin, text='Total de users cadastrados: ' + str(contagem_total), padx=pad_size, pady=pad_size, justify='left', font=font_size)
        label_total_user.grid(column=0, row=5, sticky='W')

        TelaLogin.mainloop()
        Menu = int(Choose.get())
        navpos = str(UserId.get())

    if Menu == 4:
        TelaLogin = Tk()

        PadSize = 3
        FontSize = 15

        TelaLogin.title('Alterar Dados')
        file_xl = load_workbook(filename='Logins.xlsx')
        logins = file_xl.active

        Senha = StringVar()
        Nome = StringVar()
        Idade = StringVar()
        Senha.set(logins['B' + str(navpos)].value)
        Nome.set(logins['D' + str(navpos)].value)
        Idade.set(logins['E' + str(navpos)].value)

        LabelSenha = Label(TelaLogin, text='Senha', padx=PadSize, pady=PadSize, justify='left', font=FontSize)
        LabelSenha.grid(column=0, row=1, sticky='W')
        EntrySenha = Entry(TelaLogin, textvariable=Senha, font=FontSize)
        EntrySenha.grid(column=1, row=1)

        LabelNome = Label(TelaLogin, text='Nome', padx=PadSize, pady=PadSize, justify='left', font=FontSize)
        LabelNome.grid(column=0, row=3, sticky='W')
        EntryNome = Entry(TelaLogin, textvariable=Nome, font=FontSize)
        EntryNome.grid(column=1, row=3)

        LabelIdade = Label(TelaLogin, text='Idade', padx=PadSize, pady=PadSize, justify='left', font=FontSize)
        LabelIdade.grid(column=0, row=4, sticky='W')
        EntryIdade = Entry(TelaLogin, textvariable=Idade, font=FontSize)
        EntryIdade.grid(column=1, row=4)

        ButtonAlterar = Button(TelaLogin, text='Alterar', command=alterar, padx=PadSize, pady=PadSize, font=FontSize)
        ButtonAlterar.grid(column=1, row=5, sticky='N , S, W, E')

        ButtonVoltar = Button(TelaLogin, text='Voltar', command=voltar_painel, padx=PadSize, pady=PadSize, font=FontSize)
        ButtonVoltar.grid(column=1, row=6, sticky='N , S, W, E')

        LabelMensagem = Label(TelaLogin, text='', padx=PadSize, pady=PadSize, justify='left', font=FontSize)
        LabelMensagem.grid(column=1, row=7, rowspan=2, sticky='N , S')

        TelaLogin.mainloop()
        Menu = int(Choose.get())
        navpos = str(UserId.get())

    if Menu == 5:
        TelaLogin = Tk()

        PadSize = 3
        FontSize = 15

        TelaLogin.title('Remover User')

        label_aviso = Label(TelaLogin, text='Alerta ao user: ' + str(navpos), padx=pad_size, pady=pad_size, justify='left', font=font_size)
        label_aviso.grid(column=0, row=0, sticky='W')
        LabelMensagem = Label(TelaLogin, text='AVISO: Esta ação remove o seu user do sistema!', padx=PadSize, pady=PadSize, justify='left', font=FontSize)
        LabelMensagem.grid(column=0, row=1, sticky='N , S')

        ButtonRemover = Button(TelaLogin, text='Remover', command=remover, padx=PadSize, pady=PadSize, font=FontSize)
        ButtonRemover.grid(column=0, row=2, sticky='N , S, W, E')

        ButtonVoltar = Button(TelaLogin, text='Voltar', command=voltar_painel, padx=PadSize, pady=PadSize, font=FontSize)
        ButtonVoltar.grid(column=0, row=3, sticky='N , S, W, E')

        TelaLogin.mainloop()
        Menu = int(Choose.get())
        navpos = str(UserId.get())

print('fim do programa')
