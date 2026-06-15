from customtkinter import CTkToplevel, CTkButton
from tkinter.ttk import Treeview, Style
from Database.estoque import database
from Interface.Estoque.Adicionar import Adicionar
from Interface.Estoque.Editar import Editar
from Interface.Estoque.Saida import Saida
from Interface.Estoque.Entrada import Entrada
from tkinter import messagebox as msg
from Login.usuario import user_autoridade



class Estoque(CTkToplevel):
    def __init__(self, master):
        self.permissao = user_autoridade.autoridade
        print(self.permissao)
        super().__init__(master, fg_color="#1E293B")
        self.config()
        self.layout()



    def config(self):
        self.title("Estoque")
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
        self.tabela.place(relx=0, rely=0.05, relwidth=1, relheight=.9)
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
        atualizar_B.place(relx=.47, relwidth=.05, rely=.955, relheight=.04)

        


    
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


    
    def atualizar_tabela(self):
        self.tabela.destroy()
        self.tabela : Tabela = Tabela(self)
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


class Tabela(Treeview):
    def __init__(self, master):
        super().__init__(master, show="headings")
        self.style = Style()
        self.style.theme_use("clam")
        self.config()
        self.layout()
        
    def config(self):
        self["columns"] = ("codigo", "item", "estoque")

        self.column("codigo", width=70, stretch=False)
        self.column("estoque", width=90,stretch=False, anchor="center")

        self.heading("codigo", text="Código")
        self.heading("item", text="Item")
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
            fieldbackground="#FFFFFF",
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

    def layout(self):
        self.inserir_registros()



    def inserir_registros_teste_manual(self):
        itens = [
    ("AVENTAL DE RASPA", 41),
    ("BOTINA DE ELASTICO TAMANHO 38", 14),
    ("BOTINA DE ELASTICO TAMANHO 39", 12),
    ("BOTINA DE ELASTICO TAMANHO 40", 123),
    ("BOTINA DE ELASTICO TAMANHO 41", 123),
    ("BOTINA DE ELASTICO TAMANHO 42", 123),
    ("BOTINA DE ELASTICO TAMANHO 43", 123),
    ("BOTINA DE ELASTICO TAMANHO 44", 123),
    ("BOTINA DE ELASTICO TAMANHO 45", 0),
    ("BOTINA DE ELASTICO TAMANHO 46", 0),
    ("BOTINA DE ELASTICO TAMANHO 47", 0),
    ("BOTINA NOBUCK TAMANHO 36", 0),
    ("BOTINA NOBUCK TAMANHO 37", 0),
    ("BOTINA NOBUCK TAMANHO 38", 0),
    ("BOTINA NOBUCK TAMANHO 39", 0),
    ("BOTINA NOBUCK TAMANHO 40", 0),
    ("BOTINA NOBUCK TAMANHO 41", 0),
    ("BOTINA NOBUCK TAMANHO 42", 0),
    ("CALÇA JEANS INDUSTRIAL TAMANHO 36", 0),
    ("CALÇA JEANS INDUSTRIAL TAMANHO 38", 0),
    ("CALÇA JEANS INDUSTRIAL TAMANHO 40", 0),
    ("CALÇA JEANS INDUSTRIAL TAMANHO 42", 0),
    ("CALÇA JEANS INDUSTRIAL TAMANHO 44", 0),
    ("CALÇA JEANS INDUSTRIAL TAMANHO 46", 0),
    ("CALÇA JEANS INDUSTRIAL TAMANHO 48", 0),
    ("CALÇA JEANS INDUSTRIAL TAMANHO 50", 0),
    ("CALÇA JEANS INDUSTRIAL TAMANHO 52", 0),
    ("CALÇA JEANS INDUSTRIAL TAMANHO 54", 0),
    ("CALÇA JEANS INDUSTRIAL TAMANHO 56", 0),
    ("CALÇA JEANS INDUSTRIAL TAMANHO 58", 0),
    ("CAMISA DE UNIFORME AZUL TAMANHO P", 0),
    ("CAMISA DE UNIFORME AZUL TAMANHO M", 0),
    ("CAMISA DE UNIFORME AZUL TAMANHO G", 0),
    ("CAMISA DE UNIFORME AZUL TAMANHO GG", 0),
    ("CAMISA DE UNIFORME AZUL TAMANHO XG", 0),
    ("CAMISA DE UNIFORME AZUL TAMANHO XGG", 0),
    ("CANTONEIRA PLASTICA PARA FITA 19MM (PACOTE 1000)", 0),
    ("CAPA DE CHUVA", 0),
    ("CAPACETE AMARELO COM CARNEIRA", 0),
    ("CAPACETE AZUL COM CARNEIRA", 0),
    ("CAPACETE BRANCO COM CARNEIRA", 0),
    ("CAPACETE VERDE COM CARNEIRA", 0),
    ("CARNEIRA", 0),
    ("CINTA - SLING CS60Q 5 TON. VERT. / 4 METROS F.S. 5:1 CINZA", 0),
    ("CINTA - SLING CS60Q 5 TON. VERT. / 4 METROS F.S. 5:1 VERDE", 0),
    ("CREME DE PROTECAO PARA MAOS", 0),
    ("DESENGRIPANTE", 0),
    ("DISCO DE CORTE 4\"1/2", 0),
    ("DISCO DE CORTE 7\"", 0),
    ("DISCO DE CORTE 9\"", 0),
    ("DISCO DE DESBASTE 7\"", 0),
    ("DISCO DE DESBASTE 9\"", 0),
    ("ELETRODO 2,50 / 6013 – 20KG", 0),
    ("GALOCHA 35", 0),
    ("GALOCHA 36", 0),
    ("GALOCHA 37", 0),
    ("GALOCHA 38", 0),
    ("GALOCHA 39", 0),
    ("GALOCHA 40", 0),
    ("JUGULAR", 0),
    ("LENTE DE SOLDA ESCURA NUMERO 10", 0),
    ("LENTE TRANSPARENTE", 0),
    ("LONA PARA CARREGAMENTO", 0),
    ("LUVA ALG/NITRILICA PARA SETUP (CA 42426)", 0),
    ("LUVA DE RASPA CANO LONGO (CA 6314)", 0),
    ("LUVA DE VAQUETA MISTA", 0),
    ("LUVA PANO PIGMENTADA (CA 31911)", 0),
    ("MANGOTE - REF: 4181.50", 0),
    ("MARCADOR INDUSTRIAL (AMARELO)", 0),
    ("MASCARA DE SOLDA", 0),
    ("MASCARA PFF2-S", 0),
    ("OCULOS DE PROTEÇÃO", 0),
    ("OLEO SS PROT 50", 0),
    ("PERNEIRA", 0),
    ("PROTETOR AURICULAR CONCHA", 0),
    ("PROTETOR AURICULAR SILICONE 3M (CA 5745)", 0),
    ("SABAO EM PO AMARELO GALO BARRICA 40 KG", 0),
    ("TRENA 5 METROS STARRET", 0),
    ("TRENA 8 METROS STARRET", 0),
]
        for index, (item, estoque) in enumerate(itens):

            valores = ("", item.upper(), estoque)

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