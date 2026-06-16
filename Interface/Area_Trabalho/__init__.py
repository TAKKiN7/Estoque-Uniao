from customtkinter import CTkFrame, CTkImage, CTkLabel, CTkButton, CTk
from Interface.Menu_s.area_trabalho import criar_menu
from tkinter import Menu
from PIL import Image
from pathlib import Path
from Interface.Estoque import Estoque
from Interface.Impressora import Impressora
from tkinter import messagebox as msg
from Login.usuario import user_autoridade

class Area_Trabalho(CTkFrame):
    #lista_icones : list = ["Estoque", "Impressora"]

    lista_icones : dict = {
        "Estoque": {
            "pos_x": .15,
            "pos_y": .8,
            "relwidth" : .1,
            "relheight" : .1,
            "cor" : "#000000"
        },
        "Sair" : {
            "pos_x": .005,
            "pos_y": .8,
            "relwidth" : .1,
            "relheight" : .1,
            "cor" : "#000000"
        },
        "Impressora" : {
            "pos_x": .25,
            "pos_y": .8,
            "relwidth" : .1,
            "relheight" : .1,
            "cor" : "#000000"
        },
        "TI" : {
            "pos_x": .35,
            "pos_y": .8,
            "relwidth" : .1,
            "relheight" : .1,
            "cor" : "#000000"
        }
    }

    def __init__(self, master: CTk):
        self.master = master
        super().__init__(self.master, fg_color="#27558F", corner_radius=0)
        self.papel_parede()
        self.icones()
        self.config()
        
    


    def papel_parede(self):
        largura_T = self.master.winfo_screenwidth()
        altura_T = (self.master.winfo_screenheight() - (self.master.winfo_screenheight() * 0.05))

        largura_T = self.master.winfo_screenwidth()
        altura_T = self.master.winfo_screenheight()


        print(self.winfo_screenwidth())
        
        image_path : Path  = Path.cwd() / "Imagens/01.png"

        image = Image.open(image_path)
        papel_parede_I : CTkImage = CTkImage(light_image=image, dark_image=image, size=(largura_T, altura_T))

        image_L : CTkLabel = CTkLabel(self, text="", image=papel_parede_I, bg_color="BLACK")
        #image_L.bind("<Button-3>", lambda e: self.abrir_menu(e))
        image_L.place(relx=0, rely=0, relwidth=1, relheight=1)


    def config(self):
        
        self.place(relx=0, rely=0, relwidth=1, relheight=.95)

    
    def abrir_menu(self, e):
        menu_area_trabalho : Menu = criar_menu(self, self.master)
        menu_area_trabalho.post(e.x_root, e.y_root)




    def icones(self):
        for icone in self.lista_icones:
            if user_autoridade.autoridade.lower() == "default":
                if icone not in ("Sair", "Estoque"):
                    continue

            pos_x = self.lista_icones.get(icone).get("pos_x")
            pos_y = self.lista_icones.get(icone).get("pos_y")
            relwidth= self.lista_icones.get(icone).get("relwidth")
            relheight= self.lista_icones.get(icone).get("relheight")

            texto_L : CTkLabel = CTkLabel(self, text=icone , text_color="BLACK", font=("Itim", 14), fg_color="#F4F4F6",
                                          corner_radius=0)
            rely = (pos_y + 0.065)

            #texto_L.place(relx=pos_x, rely=rely)
            
            image_path : Path = Path.cwd() / f"Imagens/Icones/{icone}.png"
            image : Image = Image.open(image_path)

            cor = self.lista_icones.get(icone).get("cor")

            imagem : CTkImage = CTkImage(light_image=image, dark_image=image, size=(60, 60))
            imagem_B : CTkButton = CTkButton(self, image=imagem, text="", fg_color=cor,
                                           corner_radius=0, bg_color=cor, hover_color=cor,
                                           command=lambda: print())


            imagem_B.bind("<Enter>", lambda e, botao=imagem_B: self.enter_mouse(e, botao))
            imagem_B.bind("<Leave>", lambda e, botao=imagem_B: self.leave_mouse(e, botao))
            imagem_B.bind("<Button-1>", lambda e, programa=icone: self.double_click(e, programa))
            

            

            
            imagem_B.place(relx=pos_x, rely=pos_y, relwidth=relwidth, relheight=relheight)
    


    def double_click(self, e, nome_programa : str):
        print(f"abrindo {nome_programa}...")

        match nome_programa:
            case "Estoque":
                janela_Estoque : Estoque = Estoque(self.master)
            case "Impressora":
                janela_Impressora : Impressora = Impressora(self.master)
            case "TI":
                msg.showinfo("Não encontrado", "disponível em breve!", parent=self.master)
            case "Sair":
                self.fechar()

    
    def enter_mouse(self, e, widget : CTkButton):
        widget.configure(border_width=1, border_color="#A7A7A7")
        widget.place(rely=.79)

    def leave_mouse(self, e, widget : CTkButton):
        widget.configure(border_width=0)
        widget.place(rely=.8)



    def fechar(self):
        res = msg.askokcancel("Fechar", "Tem certeza que deseja fechar?", parent=self.master)
        if not res:
            return
        self.master.destroy()