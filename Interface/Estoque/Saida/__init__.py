from customtkinter import CTkToplevel, CTkButton, CTkLabel, CTkEntry, IntVar, StringVar
from tkinter import messagebox as msg
from Database import database
from pyautogui import press



class Saida(CTkToplevel):
    def __init__(self, master, values):
        self.master = master
        self.values = values
        self.codigo = self.values[0]
        super().__init__(master, fg_color="#aaaaaa")
        self.config()
        self.layout()



    def config(self):
        self.title("Saída de Material")
        self.grab_set()
        largura_janela = 400
        altura_janela = 300
        
        #self.minsize(largura_janela,altura_janela)
        #self.maxsize(largura_janela,altura_janela)
        
        pos_x = int((self.winfo_screenwidth() / 2) - (largura_janela / 2))
        pos_y = int((self.winfo_screenheight() / 2) - (altura_janela / 2))

        self.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")


    def layout(self):
        nome_produto_L : CTkLabel = CTkLabel(self, text="Nome do produto")
        nome_prduto : StringVar = StringVar() 
        nome_prduto.set(self.values[1])
        nome_produto_E : CTkEntry = CTkEntry(self, font=("Itim", 13), textvariable=nome_prduto, state="disabled")

        nome_produto_E.bind("<Escape>", lambda e: self.fechar(e))
        nome_produto_E.bind("<Return>", lambda e: self.tab(e))

        modelo_produto_L : CTkLabel = CTkLabel(self, text="Modelo do produto")
        modelo_produto : StringVar = StringVar()
        modelo_produto.set(self.values[2])
        modelo_produto_E : CTkEntry = CTkEntry(self, font=("itim", 13), textvariable=modelo_produto, state="disabled")
        modelo_produto_E.bind("<Escape>", lambda e: self.fechar(e))

        
        quantidade = IntVar()
        quantidade.set(self.values[-1])
        quantidade_estoque_L : CTkLabel = CTkLabel(self, text="Quantidade de saída")
        quantidade_estoque_E : CTkEntry = CTkEntry(self, font=("itim", 13), textvariable=quantidade)
        quantidade_estoque_E.bind("<Escape>", lambda e: self.fechar(e))

        confirmar_B : CTkButton = CTkButton(self, text="OK", font=("Itim", 13, "bold"),
                                            command=lambda: self.confirmar(nome_produto_E.get(), modelo_produto_E.get(), quantidade_estoque_E.get()))
        cancelar_B : CTkButton = CTkButton(self, text="Cancelar", font=("itim", 13, "bold"), command=self.fechar)

        nome_produto_L.place(relx=.1, rely=.1)
        nome_produto_E.place(relx=.1, rely=.17, relwidth=.7)
        self.after(100, lambda: nome_produto_E.focus_set())
        
        modelo_produto_L.place(relx=.1, rely=.28)
        modelo_produto_E.place(relx=.1, rely=.35, relwidth=.7)

        quantidade_estoque_L.place(relx=.1, rely=.46)
        quantidade_estoque_E.place(relx=.1, rely=.53, relwidth=.2)
        
        confirmar_B.place(relx=.2, rely=.8, relwidth=.2)
        cancelar_B.place(relx=.6, rely=.8, relwidth=.2)



    def fechar(self, e=None):
        self.destroy()

    def confirmar(self, produto : str, modelo: str, quantidade : str):
    


        values : tuple = (produto, modelo, quantidade, self.codigo)

        database.atualizar_produto(self.codigo, values)
        self.destroy()
        msg.showinfo("Concluído", "Produto atualizado!", parent=self.master)
        self.master.grab_set()
        self.master.atualizar_tabela()