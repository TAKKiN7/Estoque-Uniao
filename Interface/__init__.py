from customtkinter import *
from time import sleep as pause
from Interface.Barra_Tarefas import Barra_Tarefas
from Interface.Area_Trabalho import Area_Trabalho
from PIL import Image
from pathlib import Path

class App(CTk):
    def __init__(self):
        super().__init__()
        self.protocol("WM_DELETE_WINDOW", lambda: print())
        self.logo()
        self.mainloop()


    def logo(self):
        self.overrideredirect(True)
        janela_A = 300
        janela_L = 500
        tela_A = (self.winfo_screenheight() // 2) - (janela_A // 2)
        tele_L = (self.winfo_screenwidth() // 2) - (janela_L // 2)
        self.geometry(f"{janela_L}x{janela_A}+{tele_L}+{tela_A}")

        image_path : Path  = Path.cwd() / "Imagens/01.png"

        image = Image.open(image_path)
        papel_parede_I : CTkImage = CTkImage(light_image=image, dark_image=image, size=(janela_L, janela_A))

        image_L : CTkLabel = CTkLabel(self, text="", image=papel_parede_I, bg_color="BLACK")
        image_L.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.after(3000, self.configuração)


    def configuração(self):
        self.overrideredirect(False)
        self.title("Aços União")
        janela_A = 1200
        janela_L = 1500
        tela_A = (self.winfo_screenheight() // 2) - (janela_A // 2)
        tele_L = (self.winfo_screenwidth() // 2) - (janela_L // 2)
        self.geometry(f"{janela_L}x{janela_A}+{tele_L}+{tela_A}")
        self.attributes("-fullscreen", True)
        self.layout()
    

    def layout(self):
        self.Area_Trabalho_F : CTkFrame = Area_Trabalho(self)
        self.Barra_Tarefas_F : CTkFrame = Barra_Tarefas(self)


    def fechar(self):
        self.destroy()

    

if __name__ == "__main__":
    app = App()