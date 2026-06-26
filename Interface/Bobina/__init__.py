from tkinter import *
from tkinter import messagebox as msg
from Interface.Bobina.Functions.nota_entrada_gerdau import gerdau_start
from Interface.Bobina.Functions.nota_entrada_aperam import aperam_start
from pyautogui import press


class Bobina(Tk):
    def __init__(self):
        super().__init__()

        self.title("Selecionar Empresa")
        self.geometry("500x350+-1156+194")
        self.after(200,lambda: self.iconbitmap("Imagens/01.ico"))
        self.configure(bg="#0F172A")

        self.layout()

        self.mainloop()

    def layout(self):

        Label(
            self,
            text="SELECIONE A EMPRESA",
            font=("Segoe UI", 18, "bold"),
            bg="#0F172A",
            fg="white"
        ).pack(pady=20)

        Button(
            self,
            text="GERDAU",
            bg="#DC2626",
            fg="white",
            font=("Segoe UI", 14, "bold"),
            relief="flat",
            cursor="hand2",
            command=self.janela_gerdau
        ).pack(fill="x", padx=30, pady=10, ipady=12)

        Button(
            self,
            text="APERAM",
            bg="#2563EB",
            fg="white",
            font=("Segoe UI", 14, "bold"),
            relief="flat",
            cursor="hand2",
            command=self.janela_aperam
        ).pack(fill="x", padx=30, pady=10, ipady=12)

        Button(
            self,
            text="USIMINAS",
            bg="#16A34A",
            fg="white",
            font=("Segoe UI", 14, "bold"),
            relief="flat",
            cursor="hand2",
            command=self.em_breve
        ).pack(fill="x", padx=30, pady=10, ipady=12)

    def em_breve(self):
        msg.showinfo("Não encontrado","Disponível em breve", parent=self)

    def tab(self, e=None):
        press("tab")

    def janela_gerdau(self):

        top = Toplevel(self)
        top.title("GERDAU")
        largura = 350
        altura = 220

        self.update_idletasks()

        x = self.winfo_x() + (self.winfo_width() - largura) // 2
        y = self.winfo_y() + (self.winfo_height() - altura) // 2

        top.geometry(f"{largura}x{altura}+{x}+{y}")
        top.configure(bg="#1E293B")
        top.grab_set()


        Label(
            top,
            text="Dados da Nota",
            font=("Segoe UI", 14, "bold"),
            bg="#1E293B",
            fg="white"
        ).pack(pady=10)

        Label(top, text="Número", bg="#1E293B",
              fg="white").pack(anchor="w", padx=20)

        numero = Entry(top, font=("Segoe UI", 11))
        numero.bind("<Return>", self.tab)
        numero.pack(fill="x", padx=20)


        Label(top, text="Lote", bg="#1E293B",
              fg="white").pack(anchor="w", padx=20)

        lote = Entry(top, font=("Segoe UI", 11))
        lote.bind("<Return>", self.tab)
        lote.pack(fill="x", padx=20)

        Label(top, text="Peso", bg="#1E293B",
              fg="white").pack(anchor="w", padx=20, pady=(10, 0))

        peso = Entry(top, font=("Segoe UI", 11))
        self.after(200, numero.focus_set)
        peso.pack(fill="x", padx=20)

        def confirmar(e=None):
            numero_valor = numero.get()
            lote_valor = lote.get()
            peso_valor = peso.get()

            #top.destroy()

            gerdau_start(numero_valor, lote_valor, peso_valor)

        btn = Button(
            top,
            text="CONFIRMAR",
            bg="#DC2626",
            fg="white",
            font=("Segoe UI", 11, "bold"),
            command=confirmar
        ).pack(pady=20)

        peso.bind("<Return>", lambda e: confirmar(e))
        

    def janela_aperam(self):

        top = Toplevel(self)
        top.title("APERAM")
        largura = 350
        altura = 320

        self.update_idletasks()

        x = self.winfo_x() + (self.winfo_width() - largura) // 2
        y = self.winfo_y() + (self.winfo_height() - altura) // 2

        top.geometry(f"{largura}x{altura}+{x}+{y}")
        top.configure(bg="#1E293B")
        top.grab_set()

        Label(
            top,
            text="Dados da Nota",
            font=("Segoe UI", 14, "bold"),
            bg="#1E293B",
            fg="white"
        ).pack(pady=10)

        Label(
            top,
            text="Número",
            font=("Segoe UI", 14, "bold"),
            bg="#1E293B",
            fg="white"
        ).pack(pady=15)

        nota = Entry(top, font=("Segoe UI", 11))
        self.after(200, nota.focus_set)
        nota.pack(fill="x", padx=20)
        nota.bind("<Return>", self.tab)


        Label(
            top,
            text="Quantidade de Lotes",
            font=("Segoe UI", 14, "bold"),
            bg="#1E293B",
            fg="white"
        ).pack(pady=15)

        qtd = Entry(top, font=("Segoe UI", 11))
        qtd.pack(fill="x", padx=20)

        def confirmar(e=None):
            nota_num = nota.get()
            qtd_lotes = int(qtd.get())
        

            top.destroy()

            aperam_start(nota_num, qtd_lotes)

        qtd.bind("<Return>", lambda event: confirmar())

        Button(
            top,
            text="CONFIRMAR",
            bg="#2563EB",
            fg="white",
            font=("Segoe UI", 11, "bold"),
            command=confirmar
        ).pack(pady=20)

