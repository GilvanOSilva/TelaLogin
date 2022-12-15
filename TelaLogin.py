from tkinter import *
from openpyxl import load_workbook
from time import sleep


class LoginSys(Tk):
    def __init__(self, *args, **kargs):
        Tk.__init__(self, *args, **kargs)
        screen = Frame(self)
        screen.pack()
        self.frames = {}
        for F in (Login, Registry, ResetPSW, ControlPanel, Update, Remove):
            page_name = F.__name__
            frame = F(parent=screen, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky='nsew')
        self.show_frame('Login')

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class Login(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        pad_size = 5
        font_size = 5
        username = StringVar()
        password = StringVar()
        username.set('user01')
        password.set('variant01')
        label_user = Label(self, text='Username', padx=pad_size, pady=pad_size, justify='left', font=font_size)
        label_user.grid(column=0, row=0, sticky='W')
        entry_user = Entry(self, textvariable=username, font=font_size)
        entry_user.grid(column=1, row=0)
        label_password = Label(self, text='Senha', padx=pad_size, pady=pad_size, justify='left', font=font_size)
        label_password.grid(column=0, row=1, sticky='W')
        entry_password = Entry(self, show='*', textvariable=password, font=font_size)
        entry_password.grid(column=1, row=1)
        button_login = Button(self, text='Acessar', command=lambda: self.access(entry_user.get(), entry_password.get()), padx=pad_size, pady=pad_size, font=font_size)
        button_login.grid(column=1, row=3, sticky='E , W')
        button_new_pass = Button(self, text='Esqueci a senha', command=lambda: controller.show_frame('ResetPSW'), padx=pad_size, pady=pad_size, font=font_size)
        button_new_pass.grid(column=1, row=4, sticky='E , W')
        button_registry = Button(self, text='Cadastrar Novo Username', command=lambda: controller.show_frame('Registry'), padx=pad_size, pady=pad_size, font=font_size)
        button_registry.grid(column=1, row=5, sticky='E , W')
        button_quit = Button(self, text='Sair', command=quit, padx=pad_size, pady=pad_size, font=font_size)
        button_quit.grid(column=1, row=6, sticky='E , W')
        Login.label_message = Label(self, text='', padx=pad_size, pady=pad_size, justify='left', font=font_size)
        Login.label_message.grid(column=1, row=7, sticky='W')

    def access(self, username, password):
        user_pos = globals()
        file_xl = load_workbook(filename='Logins.xlsx')
        logins = file_xl.active
        pos_tab = 1
        while logins['A' + str(pos_tab)].value is not None:
            if username == logins['A' + str(pos_tab)].value:
                if password == logins['B' + str(pos_tab)].value:
                    user_pos['USER'] = pos_tab
                    Update.password.set(logins['B' + str(USER)].value)
                    Update.name.set(logins['D' + str(USER)].value)
                    Update.age.set(logins['E' + str(USER)].value)

                    ControlPanel.label_welcome['text'] = 'Bem Vindo ' + logins['A' + str(pos_tab)].value
                    Remove.label_aviso['text'] = ControlPanel.label_welcome['text']
                    Login.label_message['text'] = 'Obtido acesso.'
                    sleep(1)
                    LoginSys.show_frame(self.controller, 'ControlPanel')
                    break
                else:
                    Login.label_message['text'] = 'Senha incorreta.'
                    break
            pos_tab += 1
        if logins['A' + str(pos_tab)].value is None:
            Login.label_message['text'] = 'User não está cadastrado.'


class Registry(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        pad_size = 5
        font_size = 5
        username = StringVar()
        password = StringVar()
        email = StringVar()
        name = StringVar()
        age = StringVar()
        label_user = Label(self, text='Username', padx=pad_size, pady=pad_size, justify='left', font=font_size)
        label_user.grid(column=0, row=0, sticky='W')
        entry_user = Entry(self, textvariable=username, font=font_size)
        entry_user.grid(column=1, row=0)
        label_password = Label(self, text='Senha', padx=pad_size, pady=pad_size, justify='left', font=font_size)
        label_password.grid(column=0, row=1, sticky='W')
        entry_password = Entry(self, textvariable=password, font=font_size)
        entry_password.grid(column=1, row=1)
        label_email = Label(self, text='E-Mail', padx=pad_size, pady=pad_size, justify='left', font=font_size)
        label_email.grid(column=0, row=2, sticky='W')
        entry_email = Entry(self, textvariable=email, font=font_size)
        entry_email.grid(column=1, row=2)
        label_name = Label(self, text='Nome', padx=pad_size, pady=pad_size, justify='left', font=font_size)
        label_name.grid(column=0, row=3, sticky='W')
        entry_name = Entry(self, textvariable=name, font=font_size)
        entry_name.grid(column=1, row=3)
        label_age = Label(self, text='Idade', padx=pad_size, pady=pad_size, justify='left', font=font_size)
        label_age.grid(column=0, row=4, sticky='W')
        entry_age = Entry(self, textvariable=age, font=font_size)
        entry_age.grid(column=1, row=4)
        button_registry = Button(self, text='Cadastar', command=lambda: self.registry_user(entry_user.get(), entry_password.get(), entry_email.get(), entry_name.get(), entry_age.get()), padx=pad_size, pady=pad_size, font=font_size)
        button_registry.grid(column=1, row=5, sticky='N , S, W, E')
        button_return = Button(self, text='Voltar', command=lambda: controller.show_frame('Login'), padx=pad_size, pady=pad_size, font=font_size)
        button_return.grid(column=1, row=6, sticky='N , S, W, E')
        Registry.label_message = Label(self, text='', padx=pad_size, pady=pad_size, justify='left', font=font_size)
        Registry.label_message.grid(column=1, row=7, rowspan=2, sticky='N , S')

    def registry_user(self, username, password, email, name, age):
        file_xl = load_workbook(filename='Logins.xlsx')
        logins = file_xl.active
        pos_tab = 1
        exist_user = False
        exist_email = False
        while logins['A' + str(pos_tab)].value is not None:
            if logins['A' + str(pos_tab)].value == username:
                exist_user = True
            if logins['C' + str(pos_tab)].value == email:
                exist_email = True
            pos_tab += 1
        if exist_user is True:
            Registry.label_message['text'] = 'Este usuário já está cadastrado.'
            print()
        elif len(username) < 6 or ' ' in username:
            Registry.label_message['text'] = 'Usuário não atende o crítério.'
            print()
        elif exist_email is True:
            Registry.label_message['text'] = 'Este E-mail já está cadastrado.'
            print()
        elif '@' not in email or '.' not in email or ' ' in email:
            Registry.label_message['text'] = 'E-mail não atende o crítério.'
            print()
        else:
            pos_tab = 1
            while logins['A' + str(pos_tab)].value is not None:
                pos_tab += 1
            logins['A' + str(pos_tab)] = username
            logins['B' + str(pos_tab)] = password
            logins['C' + str(pos_tab)] = email
            logins['D' + str(pos_tab)] = name
            logins['E' + str(pos_tab)] = age
            file_xl.save(filename='Logins.xlsx')
            Registry.label_message['text'] = 'Cadastro efetuado com sucesso.'


class ResetPSW(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        pad_size = 5
        font_size = 5
        username = StringVar()
        email = StringVar()
        label_message = Label(self, text='Digite os dados abaixo e confirme.', padx=pad_size, pady=pad_size, justify='left', font=font_size)
        label_message.grid(column=0, columnspan=2, row=1, sticky='N , S')
        label_user = Label(self, text='Username', padx=pad_size, pady=pad_size, justify='left', font=font_size)
        label_user.grid(column=0, row=2, sticky='W')
        entry_user = Entry(self, textvariable=username, font=font_size)
        entry_user.grid(column=1, row=2)
        label_email = Label(self, text='E-Mail', padx=pad_size, pady=pad_size, justify='left', font=font_size)
        label_email.grid(column=0, row=3, sticky='W')
        entry_email = Entry(self, textvariable=email, font=font_size)
        entry_email.grid(column=1, row=3)
        button_submit = Button(self, text='Confirmar', command=lambda: self.reset_user_psw(entry_user.get(), entry_email.get()), padx=pad_size, pady=pad_size, font=font_size)
        button_submit.grid(column=1, row=4, sticky='N , S, W, E')
        button_return = Button(self, text='Voltar', command=lambda: controller.show_frame('Login'), padx=pad_size, pady=pad_size, font=font_size)
        button_return.grid(column=1, row=5, sticky='N , S, W, E')
        ResetPSW.label_message = Label(self, text='', padx=pad_size, pady=pad_size, justify='left', font=font_size)
        ResetPSW.label_message.grid(column=0, columnspan=2, row=6, sticky='N , S')

    def reset_user_psw(self, username, email):
        file_xl = load_workbook(filename='Logins.xlsx')
        logins = file_xl.active
        pos_tab = 1
        while logins['A' + str(pos_tab)].value is not None:
            if logins['A' + str(pos_tab)].value == username:
                if logins['C' + str(pos_tab)].value == email:
                    logins['B' + str(pos_tab)] = 'Senha12345'
                    file_xl.save(filename='Logins.xlsx')
                    ResetPSW.label_message['text'] = 'Sua senha é, Senha12345, clique em voltar.'
                    break
                else:
                    ResetPSW.label_message['text'] = 'E-mail inválido.'
                    break
            pos_tab += 1
        if logins['A' + str(pos_tab)].value is None:
            ResetPSW.label_message['text'] = 'User não foi encontrado.'
            print('User não foi encontrado')


class ControlPanel(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        global USER
        pad_size = 5
        font_size = 5
        contagem_total = 4
        ControlPanel.label_welcome = Label(self, text='', padx=pad_size, pady=pad_size, justify='left', font=font_size)
        ControlPanel.label_welcome.grid(column=0, row=0, sticky='W')
        button_update = Button(self, text='Alterar dados da conta', command=lambda: controller.show_frame('Update'), padx=pad_size, pady=pad_size, font=font_size)
        button_update.grid(column=0, row=1, sticky='E , W')
        button_remove = Button(self, text='Remover cadastro do sistema', command=lambda: controller.show_frame('Remove'), padx=pad_size, pady=pad_size, font=font_size)
        button_remove.grid(column=0, row=2, sticky='E , W')
        button_return = Button(self, text='Encerrar Sessão', command=lambda: controller.show_frame('Login'), padx=pad_size, pady=pad_size, font=font_size)
        button_return.grid(column=0, row=4, sticky='N , S, W, E')
        label_total_user = Label(self, text='Total de users cadastrados: ' + str(contagem_total), padx=pad_size, pady=pad_size, justify='left', font=font_size)
        label_total_user.grid(column=0, row=5, sticky='W')


class Update(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        pad_size = 5
        font_size = 5
        Update.password = StringVar()
        Update.name = StringVar()
        Update.age = StringVar()
        label_password = Label(self, text='Senha', padx=pad_size, pady=pad_size, justify='left', font=font_size)
        label_password.grid(column=0, row=1, sticky='W')
        entry_password = Entry(self, textvariable=Update.password, font=font_size)
        entry_password.grid(column=1, row=1)
        label_name = Label(self, text='Nome', padx=pad_size, pady=pad_size, justify='left', font=font_size)
        label_name.grid(column=0, row=3, sticky='W')
        entry_name = Entry(self, textvariable=Update.name, font=font_size)
        entry_name.grid(column=1, row=3)
        label_age = Label(self, text='Idade', padx=pad_size, pady=pad_size, justify='left', font=font_size)
        label_age.grid(column=0, row=4, sticky='W')
        entry_age = Entry(self, textvariable=Update.age, font=font_size)
        entry_age.grid(column=1, row=4)
        button_update = Button(self, text='Alterar', command=lambda: self.update_user(entry_password.get(), entry_name.get(), entry_age.get()), padx=pad_size, pady=pad_size, font=font_size)
        button_update.grid(column=1, row=5, sticky='N , S, W, E')
        button_return = Button(self, text='Voltar', command=lambda: controller.show_frame('ControlPanel'), padx=pad_size, pady=pad_size, font=font_size)
        button_return.grid(column=1, row=6, sticky='N , S, W, E')
        Update.label_message = Label(self, text='', padx=pad_size, pady=pad_size, justify='left', font=font_size)
        Update.label_message.grid(column=1, row=7, rowspan=2, sticky='N , S')

    def update_user(self, password, name, age):
        global USER
        file_xl = load_workbook(filename='Logins.xlsx')
        logins = file_xl.active
        logins['B' + str(USER)] = password
        logins['D' + str(USER)] = name
        logins['E' + str(USER)] = age
        file_xl.save(filename='Logins.xlsx')
        Update.label_message['text'] = 'Dados alterados.'


class Remove(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        pad_size = 5
        font_size = 5
        Remove.label_aviso = Label(self, text='', padx=pad_size, pady=pad_size, justify='left', font=font_size)
        Remove.label_aviso.grid(column=0, row=0, sticky='W')
        label_message = Label(self, text='AVISO: Esta ação remove o seu user do sistema!', padx=pad_size, pady=pad_size, justify='left', font=font_size)
        label_message.grid(column=0, row=1, sticky='N , S')
        button_remove = Button(self, text='Remover', command=lambda: self.remove_user(), padx=pad_size, pady=pad_size, font=font_size)
        button_remove.grid(column=0, row=2, sticky='N , S, W, E')
        button_return = Button(self, text='Voltar', command=lambda: controller.show_frame('ControlPanel'), padx=pad_size, pady=pad_size, font=font_size)
        button_return.grid(column=0, row=3, sticky='N , S, W, E')

    def remove_user(self):
        global USER
        file_xl = load_workbook(filename='Logins.xlsx')
        logins = file_xl.active
        logins['A' + str(USER)] = None
        logins['B' + str(USER)] = None
        logins['C' + str(USER)] = None
        logins['D' + str(USER)] = None
        logins['E' + str(USER)] = None
        file_xl.save(filename='Logins.xlsx')
        LoginSys.show_frame(self.controller, 'Login')


USER = 9
prog = LoginSys()
prog.geometry('400x300')
prog.mainloop()
