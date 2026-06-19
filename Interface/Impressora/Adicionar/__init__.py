from customtkinter import CTkToplevel, CTkButton, CTkLabel, CTkEntry, StringVar
from tkinter import messagebox as msg
from Database.impressoras import impressora_db
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
            text="Modelo",
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


        
        ip_L = CTkLabel(
            self,
            text="IP",
            font=("Itim", 14, "bold"),
            text_color="#1E293B"
        )
        ip_E = CTkEntry(
            self,
            font=("Itim", 13, "bold"),
            height=35,
            corner_radius=8,
            border_width=2,
            border_color="#0891B2",
            fg_color="#FFFFFF",
            text_color="#1E293B"
        )
        ip_E.bind("<Escape>", lambda e: self.fechar(e))
        ip_E.bind("<Return>", lambda e: self.tab(e))


        local_L = CTkLabel(
            self,
            text="Local",
            font=("Itim", 14, "bold"),
            text_color="#1E293B"
        )
        local_E = CTkEntry(
            self,
            font=("Itim", 13, "bold"),
            height=35,
            corner_radius=8,
            border_width=2,
            border_color="#0891B2",
            fg_color="#FFFFFF",
            text_color="#1E293B"
        )

        local_E.bind("<Escape>", lambda e: self.fechar(e))
        local_E.bind("<Return>", lambda e: self.confirmar(nome_produto_E.get(), ip_E.get(), local_E.get(), e))

        confirmar_B = CTkButton(
            self,
            text="✓ Confirmar",
            command=lambda: self.confirmar(
                nome_produto_E.get(),
                ip_E.get(),
                local_E.get()
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
        nome_produto_E.place(relx=.1, rely=.17, relwidth=.5)
        self.after(100, lambda: nome_produto_E.focus_set())
        
        ip_L.place(relx=.1, rely=.41)
        ip_E.place(relx=.1, rely=.53, relwidth=.25)

        local_L.place(relx=.4, rely=.41)
        local_E.place(relx=.4, rely=.53, relwidth=.35)

        
        confirmar_B.place(relx=.2, rely=.8, relwidth=.2)
        cancelar_B.place(relx=.6, rely=.8, relwidth=.2)



    def tab(self, e):
        press("tab")

    def fechar(self, e=None):
        self.destroy()

    def confirmar(self, modelo : str, ip : str, local : str, e=None):
        if not modelo:
            msg.showerror("Erro", "Campo *Modelo* é obrigatório!", parent=self.master)
            return
        if not ip:
            msg.showerror("Erro", "Campo *IP* é obrigatório!", parent=self.master)
            return
        
        if local == "":
            local = "Sem informação"
        
        values : tuple = (modelo, ip, local)

        self.destroy()
        res = impressora_db.nova_impressora(values, master=self.master)
        if res:
            msg.showinfo("Concluído", "Produto cadastrado!", parent=self.master)
        self.master.grab_set()
        self.master.atualizar_tabela()
