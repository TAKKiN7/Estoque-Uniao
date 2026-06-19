from customtkinter import *
from PIL import Image
from pathlib import Path
from tkinter import messagebox as msg
from Interface import App
from pyautogui import press
from Login.usuario import user_autoridade



class Login(CTk):
    def __init__(self):
        super().__init__(fg_color="#06090E")
        self.config()
        self.layout()
        self.mainloop()


    
    
    def config(self):
        self.title("Aços União")
        self.iconbitmap("Imagens/01.ico")
        largura_janela = 600
        altura_janela = 350
        
        self.minsize(largura_janela,altura_janela)
        self.maxsize(largura_janela,altura_janela)

        tela_A = (self.winfo_screenheight() // 2) - (altura_janela // 2)
        tele_L = (self.winfo_screenwidth() // 2) - (largura_janela // 2)
        self.geometry(f"{largura_janela}x{altura_janela}+{tele_L}+{tela_A}")


        image_path : Path  = Path.cwd() / "Imagens/Login.png"

        image = Image.open(image_path)
        papel_parede_I : CTkImage = CTkImage(light_image=image, dark_image=image, size=(largura_janela, altura_janela))

        image_L : CTkLabel = CTkLabel(self, text="", image=papel_parede_I, bg_color="BLACK")
        image_L.place(relx=0, rely=0, relwidth=1, relheight=1)

        
        pos_x = int((self.winfo_screenwidth() / 2) - (largura_janela / 2))
        pos_y = int((self.winfo_screenheight() / 2) - (altura_janela / 2))

        self.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")


    


    def layout(self):
        self.user_E = CTkEntry(
            self,
            placeholder_text="👤  Usuário",
            font=("Itim", 12),
            height=40,
            corner_radius=8,
            border_width=3,
            border_color="#000000",
            fg_color="#06090E",
            bg_color="#06090E",
            text_color="WHITE"
        )
        self.user_E.bind("<Return>", lambda e: self.tab(e))
        #self.after(200, lambda: self.user_E.focus_set())

        self.pass_E = CTkEntry(
            self,
            placeholder_text="🔒  Senha",
            show="*",
            font=("Itim", 12),
            height=40,
            corner_radius=8,
            border_width=3,
            border_color="#000000",
            fg_color="#06090E",
            bg_color="#06090E",
            text_color="#ffffff"
        )

        self.login_B = CTkButton(
            self,
            text="Entrar",
            command=self.entrar,
            width=140,
            height=40,
            corner_radius=8,
            fg_color="#00115E",
            hover_color="#11005E",
            text_color="white",
            font=("Itim", 14, "bold"),
            border_width=2,
            border_color="#000000"
        )

        self.pass_E.bind("<Return>", lambda e: self.entrar(e))


        self.user_E.place(relx=.32, rely=.51, relwidth=.36, relheight=.09)
        self.pass_E.place(relx=.32, rely=.605  , relwidth=.36, relheight=.09)
        self.login_B.place(relx=.32, rely=.7, relwidth=.36, relheight=.09)
    

    def tab(self, e):
        press("tab")

    def entrar(self, e=None):
        user = self.user_E.get()
        passwd = self.pass_E.get()

        if user == "admin_juliana" and passwd == "159753" or user == "tk" and passwd == "347":
            user_autoridade.autoridade = "Admin"
            if user == "admin_juliana":
                user_autoridade.user = "JULIANA-RH"
            elif user == "tk":
                user_autoridade.user = "TK-TI"
            self.acesso_autorizado()
        elif user == "user" and passwd == "user" or user == "producao" and passwd == "producao" or user == "almo" and passwd == "almo":
            user_autoridade.autoridade = "Default"
            user_autoridade.user = "ALMAXARIFADO"
            self.acesso_autorizado()
            
        else:
            msg.showerror("Falha","Usuário ou senha incorreto(s)", parent=self)


    def acesso_autorizado(self):
        self.destroy()
        App()
    

if __name__ == "__main__":
    login : Login = Login()