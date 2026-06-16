from customtkinter import CTkToplevel, CTkButton
from tkinter.ttk import Treeview, Style
from Database.impressoras import impressora_db
from Interface.Impressora.Adicionar import Adicionar
from Interface.Estoque.Editar import Editar
from tkinter import messagebox as msg
from Login.usuario import user_autoridade



class Impressora(CTkToplevel):
    def __init__(self, master):
        self.permissao = user_autoridade.autoridade
        print(self.permissao)
        super().__init__(master, fg_color="#1E293B")
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

        self.bind("<Escape>", lambda e: self.fechar(e))

        self.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")


    def layout(self):
        self.tabela : Tabela = Tabela(self)
        #tabela.pack(fill="both", expand=True)
        self.tabela.place(relx=0, rely=0, relwidth=1, relheight=.95)
        if self.permissao in ("Admin"):
            self.menu_admin()
            self.tabela.bind("<Double-Button-1>", lambda e: self.entrada(e))
        else:
            self.tabela.bind("<Double-Button-1>", lambda e: self.saida(e))
        self.menu()

    def menu_admin(self): 


        editar_B = CTkButton(
            self,
            text="✏️Editar",
            command=self.editar,
            width=120, height=35,
            corner_radius=8,
            fg_color="#2563EB", hover_color="#1D4ED8",
            text_color="white",
            font=("Segoe UI", 14, "bold"),
            border_width=2, border_color="#1E40AF"
)

        remover_B = CTkButton(
            self,
            text="🗑 Remover",
            command=self.remover,
            width=120, height=35,
            corner_radius=8,
            fg_color="#DC2626", hover_color="#B91C1C",
            text_color="white",
            font=("Segoe UI", 14, "bold"),
            border_width=2, border_color="#991B1B"
        )

        adicionar_B = CTkButton(
            self,
            text="➕ Adicionar",
            command=self.adicionar,
            width=120, height=35,
            corner_radius=8,
            fg_color="#16A34A", hover_color="#15803D",
            text_color="white",
            font=("Segoe UI", 14, "bold"),
            border_width=2, border_color="#166534"
        )

        #editar_B.place(relx=.34, relwidth=.12, rely=.955, relheight=.04)
        #remover_B.place(relx=.18, relwidth=.12, rely=.955, relheight=.04)
        adicionar_B.place(relx=.04, relwidth=.12, rely=.955, relheight=.04)


    def menu(self):
        atualizar_B = CTkButton(
            self,
            text="🔃",
            command=self.atualizar_tabela,
            width=120, height=35,
            corner_radius=8,
            fg_color="#F1DB13", hover_color="#F1DB13",
            text_color="white",
            font=("Segoe UI", 14, "bold"),
            border_width=2, border_color="#C0AF15"
        )
        atualizar_B.place(relx=.9, relwidth=.05, rely=.955, relheight=.04)


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
        if self.permissao in ("Admin"):
            self.menu_admin()
            self.tabela.bind("<Double-Button-1>", lambda e: self.entrada(e))
        else:
            self.tabela.bind("<Double-Button-1>", lambda e: self.saida(e))
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

        

        res = database.remover_produto(codigo, master=self)
        print(res)

        if "não" in res:
            msg.showerror("Falha", res, parent=self)
            return
        msg.showinfo("Concluído", res, parent=self)
        self.atualizar_tabela()

    def remover_selection(self):
        for item in self.tabela.selection():
                self.tabela.selection_remove(item)

    def fechar(self, e=None):
        self.destroy()

class Tabela(Treeview):
    def __init__(self, master):
        super().__init__(master, show="headings")
        self.style = Style()
        self.style.theme_use("clam")
        self.config()
        self.layout()
        
    def config(self):
        self["columns"] = ("id", "modelo", "ip", "local", "tonner")

        self.column("id", width=70, stretch=False)
        self.column("ip", anchor="center")
        self.column("local", anchor="center")
        self.column("tonner", width=90,stretch=False, anchor="center")

        self.heading("id", text="ID")
        self.heading("modelo", text="Modelo")
        self.heading("ip", text="IP")
        self.heading("local", text="Local")
        self.heading("tonner", text="Tonner")


        self.tag_configure(
            "linha_1",
            background="#aaaaaa"
        )

        self.tag_configure(
            "linha_2",
            background="#999999"
        )
    
        self.tag_configure(
            "tonner_baixo",
            foreground="RED"
        )
        
        self.tag_configure(
            "tonner_otimo",
            foreground="GREEN"
        )


        self.style.configure(
            "Treeview",
            font=("Segoe UI", 11),
            rowheight=32,
            background="#FFFFFF",
            fieldbackground="#FFFFFF",
            foreground="#1E293B",
            borderwidth=0
        )


        self.style.map(
            "Treeview",
            background=[("selected", "#2563EB")],
            foreground=[("selected", "white")]
        )

        self.style.configure(
            "Treeview.Heading",
            font=("Segoe UI", 12, "bold"),
            background="#081233",
            foreground="white",
            relief="flat"
        )

        self.style.map(
            "Treeview.Heading",
            background=[("active", "#2563EB")]
        )

    def layout(self):
        self.inserir_registros()
        


    def inserir_registros(self):
        registros : list = impressora_db.listar_registros()

        for index, registro in enumerate(registros):

            valores = (registro[0], registro[1], registro[2], registro[3], registro[4])

            quantidade_tonner = int(registro[-1])

            if index % 2 != 0:
                if quantidade_tonner < 10:
                    self.insert("", "end", values=valores, tags=("linha_1","tonner_baixo", ))
                else:
                    self.insert("", "end", values=valores, tags=("linha_1", ))
            else:
                if quantidade_tonner < 10:
                    self.insert("", "end", values=valores, tags=("linha_2", "tonner_otimo",))
                else:
                    self.insert("", "end", values=valores, tags=("linha_2",))

