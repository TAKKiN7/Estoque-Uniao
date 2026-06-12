from tkinter import Menu
from time import sleep as pause



def criar_menu(master, root):
    menu_tarefas : Menu = Menu(master, tearoff=0)

    menu_tarefas.add_command(
        label="Alterar usuário",
        command=lambda: alterar_usuario(root)
    )

    menu_tarefas.add_command(
        label="Fechar",
        command=lambda: root.destroy()
    )

    return menu_tarefas


def alterar_usuario(root):

    from Login import Login
    root.destroy()
    Login()
