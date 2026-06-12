from customtkinter import CTkFrame, CTkImage, CTkLabel, CTkButton
from Interface.Menu_s.area_trabalho import criar_menu
from tkinter import Menu
from PIL import Image
from pathlib import Path
from Interface.Estoque import Estoque

class Area_Trabalho(CTkFrame):
    lista_icones : list = ["Estoque"]

    def __init__(self, master):
        self.master = master
        super().__init__(self.master, fg_color="#27558F", corner_radius=0)
        self.papel_parede()
        self.icones()
        self.config()
        
    


    def papel_parede(self):
        largura_T = self.master.winfo_screenwidth()
        altura_T = (self.master.winfo_screenheight() - (self.master.winfo_screenheight() * 0.05))

        largura_T = 1366
        altura_T = 729

        
        image_path : Path  = Path.cwd() / "Imagens/02.png"

        image = Image.open(image_path)
        papel_parede_I : CTkImage = CTkImage(light_image=image, dark_image=image, size=(largura_T, altura_T))

        image_L : CTkLabel = CTkLabel(self, text="", image=papel_parede_I, bg_color="BLACK")
        image_L.bind("<Button-3>", lambda e: self.abrir_menu(e))
        image_L.place(relx=0, rely=0, relwidth=1, relheight=1)


    def config(self):
        
        self.place(relx=0, rely=0, relwidth=1, relheight=.95)

    
    def abrir_menu(self, e):
        menu_area_trabalho : Menu = criar_menu(self, self.master)
        menu_area_trabalho.post(e.x_root, e.y_root)




    def icones(self):
        for icon in self.lista_icones:

            texto_L : CTkLabel = CTkLabel(self, text=icon , text_color="BLACK", font=("Itim", 14), fg_color="#F4F4F6",
                                          corner_radius=0)
            texto_L.place(relx=.4, rely=.07)
            
            image_path : Path = Path.cwd() / f"Imagens/Icones/{icon}.png"
            image : Image = Image.open(image_path)

            imagem : CTkImage = CTkImage(light_image=image, dark_image=image, size=(45, 45))
            imagem_B : CTkButton = CTkButton(self, image=imagem, text="", fg_color="#F4F4F6",
                                           corner_radius=0, bg_color="#F4F4F6", hover_color="#F4F4F6")


            imagem_B.bind("<Enter>", lambda e: self.enter_mouse(e, imagem_B))
            imagem_B.bind("<Leave>", lambda e: self.leave_mouse(e, imagem_B))
            imagem_B.bind("<Double-Button-1>", lambda e: self.double_click(e, icon))
            

            

            
            imagem_B.place(relx=.4, rely=.005, relwidth=0.04)
            


    def double_click(self, e, nome_programa : str):
        print(f"abrindo {nome_programa}...")

        match nome_programa:
            case "Estoque":
                janela_Estoque : Estoque = Estoque(self.master)

    
    def enter_mouse(self, e, widget : CTkButton):
        widget.configure(border_width=1, border_color="BLACK")
    
    def leave_mouse(self, e, widget : CTkButton):
        widget.configure(border_width=0)
