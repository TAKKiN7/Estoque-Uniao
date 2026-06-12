from customtkinter import CTkToplevel, CTkButton
from tkinter.ttk import Treeview
from Database.estoque import database
from Interface.Estoque.Adicionar import Adicionar
from Interface.Estoque.Editar import Editar
from tkinter import messagebox as msg
from Login.usuario import user_autoridade



class Impressora(CTkToplevel):
    def __init__(self, master):
        self.permissao = user_autoridade.autoridade
        print(self.permissao)
        super().__init__(master, fg_color="WHITE")
        self.config()
        self.layout()



    def config(self):
        self.title("Impressoras")
        self.grab_set()
        self.after(200,lambda: self.iconbitmap("Imagens/01.ico"))
        largura_janela = 900
        altura_janela = 600 
        
        self.minsize(largura_janela,altura_janela)
        self.maxsize(largura_janela,altura_janela)
        
        pos_x = int((self.winfo_screenwidth() / 2) - (largura_janela / 2))
        pos_y = int((self.winfo_screenheight() / 2) - (altura_janela / 2)) - int(altura_janela * 0.05)

        self.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")


    def layout(self):
        self.tabela : Tabela = Tabela(self)
        #tabela.pack(fill="both", expand=True)
        self.tabela.place(relx=0, rely=0, relwidth=1, relheight=.95)
        if self.permissao in ("Admin"):
            self.menu_admin()
        self.menu()

    def menu_admin(self): 

        editar_B : CTkButton = CTkButton(self, text="Editar", corner_radius=0, command=self.editar)
        remover_B : CTkButton = CTkButton(self, text="Remover", corner_radius=0, command=self.remover)
        adicionar_B : CTkButton = CTkButton(self, text="Adicionar", corner_radius=0, command=self.adicionar)

        editar_B.place(relx=.35, relwidth=.1, rely=.955, relheight=.04)
        remover_B.place(relx=.2, relwidth=.1, rely=.955, relheight=.04)
        adicionar_B.place(relx=.05, relwidth=.1, rely=.955, relheight=.04)


 
    def adicionar(self):
        Adicionar(self)
    

    def editar(self):
        produto = self.tabela.selection()
        if not produto:
            msg.showerror("Falha", "Nenhum produto selecionado!", parent=self)
            return
        values = self.tabela.item(produto)["values"]
        Editar(self, values)


    
    def atualizar_tabela(self):
        self.tabela.destroy()
        self.tabela : Tabela = Tabela(self)
        self.tabela.place(relx=0, rely=0, relwidth=1, relheight=.95)


    def remover(self):
        produto = self.tabela.selection()
        if not produto:
            msg.showerror("Falha", "Nenhum produto selecionado!", parent=self)
            return
        elif len(produto) > 1:
            msg.showerror("Falha", "Não é permitido excluir mais de um item por vez", parent=self)
            self.remover_selection()
            return

        values = self.tabela.item(produto)["values"]

        codigo = values[0]
        produto = values[1]

        confirmar = msg.askokcancel("Remover" , f"Tem certeza que deseja remover *{produto} cod-{codigo}*", parent=self)
        
        if not confirmar:
            self.remover_selection()
            return

        

        res = database.remover_produto(codigo)
        print(res)

        if "não" in res:
            msg.showerror("Falha", res, parent=self)
            return
        msg.showinfo("Concluído", res, parent=self)
        self.atualizar_tabela()

    def remover_selection(self):
        for item in self.tabela.selection():
                self.tabela.selection_remove(item)


class Tabela(Treeview):
    def __init__(self, master):
        super().__init__(master, show="headings")
        self.config()
        self.layout()
        
    def config(self):
        self["columns"] = ("codigo", "produto", "modelo", "quantidade")

        self.column("codigo", width=10)

        self.heading("codigo", text="Código")
        self.heading("produto", text="Produto")
        self.heading("modelo", text="Modelo")
        self.heading("quantidade", text="Quantidade")


        self.tag_configure(
            "linha_1",
            background="#aaaaaa"
        )

        self.tag_configure(
            "linha_2",
            background="#888888"
        )
    
        self.tag_configure(
            "estoque_baixo",
            foreground="RED"
        )

    def layout(self):
        self.inserir_registros()


    def inserir_registros(self):
        registros : list = database.listar_produtos()
        for index, resgistro in enumerate(registros):
            valores : tuple = (resgistro.get("codigo"), resgistro.get("produto").title(), resgistro.get("modelo"), resgistro.get("quantidade"))
            
            estoque = int(resgistro.get("quantidade"))

            if index % 2 != 0:
                if estoque < 10:
                    self.insert("", "end", values=valores, tags=("linha_1","estoque_baixo", ))
                else:
                    self.insert("", "end", values=valores, tags=("linha_1", ))
            else:
                if estoque < 10:
                    self.insert("", "end", values=valores, tags=("linha_2", "estoque_baixo",))
                else:
                    self.insert("", "end", values=valores, tags=("linha_2",))