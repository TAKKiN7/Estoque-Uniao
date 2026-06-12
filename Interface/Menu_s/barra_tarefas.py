from tkinter import Menu



def criar_menu(master):
    menu_tarefas : Menu = Menu(master, tearoff=0)

    menu_tarefas.add_command(
        label="Alterar usuário",
        command=lambda: alterar_usuario(master)
    )

    menu_tarefas.add_command(
        label="Fechar",
        command=lambda: master.destroy()
    )

    return menu_tarefas

def alterar_usuario(master):

    from Login import Login
    master.destroy()
    Login()

