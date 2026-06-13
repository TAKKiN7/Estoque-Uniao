from customtkinter import CTkToplevel, CTkButton, CTkLabel, CTkEntry, StringVar
from tkinter import messagebox as msg
from Database.estoque import database
from pyautogui import press



class Adicionar(CTkToplevel):
    def __init__(self, master):
        self.master = master
        super().__init__(master, fg_color="#848688")
        self.config()
        self.layout()



    def config(self):
        self.title("Cadastro de Produto")
        self.grab_set()
        self.after(200,lambda: self.iconbitmap("Imagens/01.ico"))
        largura_janela = 500
        altura_janela = 200
        
        #self.minsize(largura_janela,altura_janela)
        #self.maxsize(largura_janela,altura_janela)
        
        pos_x = int((self.winfo_screenwidth() / 2) - (largura_janela / 2))
        pos_y = int((self.winfo_screenheight() / 2) - (altura_janela / 2))

        self.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")


    def layout(self):
        nome_produto_L = CTkLabel(
            self,
            text="Nome do produto",
            font=("Itim", 14, "bold"),
            text_color="#1E293B"
        )

        nome_produto_E = CTkEntry(
            self,
            font=("Itim", 13),
            height=35,
            corner_radius=8,
            border_width=2,
            border_color="#94A3B8",
            fg_color="#FFFFFF",
            text_color="#1E293B"
        )

        nome_produto_E.bind("<Escape>", lambda e: self.fechar(e))
        nome_produto_E.bind("<Return>", lambda e: self.tab(e))


        
        quantidade = StringVar()
        quantidade.set("0")
        quantidade_estoque_L = CTkLabel(
            self,
            text="Quantidade em estoque",
            font=("Itim", 14, "bold"),
            text_color="#1E293B"
        )
        quantidade_estoque_E = CTkEntry(
            self,
            font=("Itim", 13, "bold"),
            textvariable=quantidade,
            height=35,
            corner_radius=8,
            border_width=2,
            border_color="#0891B2",
            fg_color="#FFFFFF",
            text_color="#1E293B",
            justify="center"
        )
        quantidade_estoque_E.bind("<Escape>", lambda e: self.fechar(e))
        quantidade_estoque_E.bind("<Return>", lambda e: self.confirmar(nome_produto_E.get(), quantidade_estoque_E.get(), e))

        confirmar_B = CTkButton(
            self,
            text="✓ Confirmar",
            command=lambda: self.confirmar(
                nome_produto_E.get(),
                quantidade_estoque_E.get()
            ),
            width=120, height=35,
            corner_radius=8,
            fg_color="#16A34A",
            hover_color="#15803D",
            text_color="white",
            font=("Segoe UI", 13, "bold"),
            border_width=2,
            border_color="#166534"
        )

        cancelar_B = CTkButton(
            self,
            text="✕ Cancelar",
            command=self.fechar,
            width=120, height=35,
            corner_radius=8,
            fg_color="#6B7280",
            hover_color="#4B5563",
            text_color="white",
            font=("Segoe UI", 13, "bold"),
            border_width=2,
            border_color="#374151"
        )

        nome_produto_L.place(relx=.1, rely=.05)
        nome_produto_E.place(relx=.1, rely=.17, relwidth=.7)
        self.after(100, lambda: nome_produto_E.focus_set())
        
 

        quantidade_estoque_L.place(relx=.1, rely=.41)
        quantidade_estoque_E.place(relx=.1, rely=.53, relwidth=.2)
        
        confirmar_B.place(relx=.2, rely=.8, relwidth=.2)
        cancelar_B.place(relx=.6, rely=.8, relwidth=.2)



    def tab(self, e):
        press("tab")

    def fechar(self, e=None):
        self.destroy()

    def confirmar(self, produto : str, quantidade : str, e=None):
        if not produto:
            msg.showerror("Erro", "Campo *Nome do Produto* é obrigatório!", parent=self.master)
            return
        try:
            qtdd : int = int(quantidade)
            if qtdd < 0:
                raise ValueError("Quantidade não pode ser um numeral negativo")
        except:
            msg.showerror("Falha","Campo *Quantidade em estoque* inválido!", parent=self.master)
            return
        
        

        values : tuple = (produto, quantidade)

        self.destroy()
        database.inserir_porduto(values)
        msg.showinfo("Concluído", "Produto cadastrado!", parent=self.master)
        self.master.grab_set()
        self.master.atualizar_tabela()
