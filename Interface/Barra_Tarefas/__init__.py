from customtkinter import CTkFrame, CTkEntry, CTkLabel
from Interface.Menu_s.barra_tarefas import criar_menu
from tkinter import Menu
import time
from threading import Thread


class Barra_Tarefas(CTkFrame):
    def __init__(self, master):
        self.master = master
        super().__init__(self.master, fg_color="#000", corner_radius=0, border_width=2, border_color="BLACK")
        self.config()


    def config(self):
        self.bind("<Button-3>", lambda e: self.abrir_menu(e))


        pesquisar_E : CTkEntry = CTkEntry(self, placeholder_text="Pesquisar...", corner_radius=0, fg_color="WHITE",
                                          border_color="BLACK", border_width=2)
        pesquisar_E.place(relx=0.04, rely=0, relwidth=.2, relheight=1)

        hora = time.strftime("%H:%M:%S")
        self.hora_L : CTkLabel = CTkLabel(self, text=hora,corner_radius=0, text_color="WHITE")
        self.hora_L.place(relx=.95, rely=.4, relheight=.25)

        self.after(1000, self.atualizar_hora)

        self.place(relx=0, rely=0.95, relwidth=1, relheight=.05)


    def abrir_menu(self, e):
        menu_tarefas : Menu = criar_menu(self.master)
        menu_tarefas.post(e.x_root, e.y_root) 


    def atualizar_hora(self):
        hora = time.strftime("%H:%M:%S")
        self.hora_L.configure(text=hora)

        self.after(1000, self.atualizar_hora)