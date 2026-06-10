from tkinter import Menu
from time import sleep as pause



def criar_menu(master, root):
    menu_tarefas : Menu = Menu(master, tearoff=0)
        
    menu_tarefas.add_command(
        label="Encerrar programa",
        command=lambda: root.destroy() 
    )

    return menu_tarefas