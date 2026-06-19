from customtkinter import CTkToplevel, CTkButton, CTkEntry
from tkinter.ttk import Treeview, Style
from Database.estoque import database
from Interface.Estoque.Adicionar import Adicionar
from Interface.Estoque.Editar import Editar
from Interface.Estoque.Saida import Saida
from Interface.Estoque.Entrada import Entrada
from tkinter import messagebox as msg
from Login.usuario import user_autoridade



class TI(CTkToplevel):
    def __init__(self, master):
        self.permissao = user_autoridade.autoridade
        print(self.permissao)
        super().__init__(master, fg_color="#1E293B")
        self.config()
        self.layout()



    def config(self):
        self.title("TI")
        self.grab_set()
        self.after(200,lambda: self.iconbitmap("Imagens/01.ico"))
        largura_janela = 900
        altura_janela = 600 
        
        #self.minsize(largura_janela,altura_janela)
        #self.maxsize(largura_janela,altura_janela)
        
        pos_x = int((self.winfo_screenwidth() / 2) - (largura_janela / 2))
        pos_y = int((self.winfo_screenheight() / 2) - (altura_janela / 2)) - int(altura_janela * 0.05)


        self.bind("<Escape>", lambda e: self.fechar(e))


        self.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")
        self.after(200, lambda: self.attributes("-fullscreen", True))


    def layout(self):
        self.tabela : Tabela = Tabela(self)
        #tabela.pack(fill="both", expand=True)
        self.tabela.place(relx=0, rely=0.05, relwidth=1, relheight=.9)
        if self.permissao in ("Admin"):
            #self.menu_admin()
            self.tabela.bind("<Double-Button-1>", lambda e: self.entrada(e))
        else:
            self.tabela.bind("<Double-Button-1>", lambda e: self.saida(e))
        #self.menu()

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

        entrada_B = CTkButton(
            self,
            text="📥 Entrada",
            command=self.entrada,
            width=120, height=35,
            corner_radius=8,
            fg_color="#0891B2", hover_color="#0E7490",
            text_color="white",
            font=("Segoe UI", 14, "bold"),
            border_width=2, border_color="#155E75"
        )

        editar_B.place(relx=.34, relwidth=.12, rely=.955, relheight=.04)
        remover_B.place(relx=.18, relwidth=.12, rely=.955, relheight=.04)
        adicionar_B.place(relx=.04, relwidth=.12, rely=.955, relheight=.04)
        entrada_B.place(relx=.7, relwidth=.1, rely=.955, relheight=.04)


    def menu(self):

        
        pesquisa_E = CTkEntry(
            self,
            font=("Itim", 14),
            height=35,
            placeholder_text="Pesquisar produto",
            corner_radius=8,
            border_width=2,
            border_color="#94A3B8",
            fg_color="#FFFFFF",
            text_color="#1E293B"
        )  

        pesquisa_E.bind("<Return>", lambda e: self.pesquisar(pesquisa_E.get(), e))
        pesquisa_E.place(relx=.3, rely=0, relwidth=.4)

        fechar_B = CTkButton(
            self,
            text="❌",
            command=self.fechar,
            width=120, height=35,
            corner_radius=8,
            fg_color="#F11313", hover_color="#F11313",
            text_color="white",
            font=("Segoe UI", 14, "bold"),
            border_width=2, border_color="#A81515"
        )
        fechar_B.place(relx=.95, rely=0, relwidth=.05)

        saida_B = CTkButton(
            self,
            text="📤 Saída",
            command=self.saida,
            width=120, height=35,
            corner_radius=8,
            fg_color="#EA580C", hover_color="#C2410C",
            text_color="white",
            font=("Segoe UI", 14, "bold"),
            border_width=2, border_color="#9A3412"
        )
        saida_B.place(relx=.85, relwidth=.1, rely=.955, relheight=.04)

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
        if self.permissao == "Admin":
            atualizar_B.place(relx=.63, relwidth=.05, rely=.955, relheight=.04)
        else:
            atualizar_B.place(relx=.78, relwidth=.05, rely=.955, relheight=.04)

        
    def pesquisar(self, nome_produto : str, e=None):
        if not nome_produto.strip():
            self.atualizar_tabela()
            return None
        produtos = database.pesquisar_produtos(nome_produto, master=self.master)

        self.atualizar_tabela(produtos)
    
    def saida(self, e=None):
        item = self.tabela.selection()
        if not item:
            msg.showerror("Falha", "Nenhum produto selecionado!", parent=self)
            return
        produto = self.tabela.item(item)["values"][1]
        
        values = self.tabela.item(item)["values"]
        Saida(self, values)

        #print(f"Registro realizado: {produto} alterado no estoque")

    
    def entrada(self, e=None):
        item = self.tabela.selection()
        if not item:
            msg.showerror("Falha", "Nenhum produto selecionado!", parent=self)
            return
        produto = self.tabela.item(item)["values"][1]
        
        values = self.tabela.item(item)["values"]
        Entrada(self, values)

        print(f"Registro realizado: {produto} alterado no estoque")

    def adicionar(self):
        Adicionar(self)
    

    def editar(self):
        produto = self.tabela.selection()
        if not produto:
            msg.showerror("Falha", "Nenhum produto selecionado!", parent=self)
            return
        values = self.tabela.item(produto)["values"]
        Editar(self, values)


    
    def atualizar_tabela(self, pesquisa=None):
        self.tabela.destroy()
        self.tabela : Tabela = Tabela(self, pesquisa)
        if self.permissao in ("Admin"):
            self.menu_admin()
            self.tabela.bind("<Double-Button-1>", lambda e: self.entrada(e))
        else:
            self.tabela.bind("<Double-Button-1>", lambda e: self.saida(e))
        self.tabela.place(relx=0, rely=0.05, relwidth=1, relheight=.9)


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
    def __init__(self, master, pesquisa=None):
        super().__init__(master, show="headings")
        self.style = Style()
        self.style.theme_use("clam")
        self.config()
        #self.layout(pesquisa)
        
    def config(self):
        self["columns"] = ("codigo", "produto", "modelo", "estoque")

        self.column("codigo", width=70, stretch=False)
        self.column("estoque", width=90,stretch=False, anchor="center")

        self.heading("codigo", text="Código")
        self.heading("produto", text="Produto")
        self.heading("modelo", text="Modelo")
        self.heading("estoque", text="Estoque")


        self.tag_configure(
            "linha_1",
            background="#aaaaaa"
        )

        self.tag_configure(
            "linha_2",
            background="#999999"
        )
    
        self.tag_configure(
            "estoque_baixo",
            foreground="RED"
        )


        self.style.configure(
            "Treeview",
            font=("Segoe UI", 11),
            rowheight=32,
            background="#FFFFFF",
            fieldbackground="#1E293B",
            foreground="#1E293B",
            borderwidth=0
        )
        # self.style.configure(
        #     "Treeview",
        #     font=("Segoe UI", 10),
        #     rowheight=36,
        #     background="#FFFFFF",
        #     fieldbackground="#FFFFFF",
        #     foreground="#334155",
        #     borderwidth=0
        # )

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

    def layout(self, pesquisa=None):
        if not pesquisa:
            self.inserir_registros()
            return
        self.inserir_registros_manual(pesquisa)



    def inserir_registros_manual(self, itens):
        
        for index, (cod, item, estoque) in enumerate(itens):

            valores = (cod, item.upper(), estoque)

            if index % 2 != 0:
                if estoque < 10:
                    self.insert("", "end", values=valores, tags=("linha_1", "estoque_baixo"))
                else:
                    self.insert("", "end", values=valores, tags=("linha_1",))
            else:
                if estoque < 10:
                    self.insert("", "end", values=valores, tags=("linha_2", "estoque_baixo"))
                else:
                    self.insert("", "end", values=valores, tags=("linha_2",))


    def inserir_registros(self):
        registros : list = database.listar_produtos()

        if not registros:
            return "Nenhum produto cadastrado."
        
        for index, registro in enumerate(registros):
            valores : tuple = (registro[0], registro[1].upper(), registro[2])
            
            estoque = int(registro[-1])

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