import os
from PIL import Image
import customtkinter


class lesobjets:
    def __init__(self):
        self.petit_object = self.PetitObject()
        self.moyen_object = self.MoyenObject()
        self.grand_object = self.GrandObject()

    class PetitObject:
        def __init__(self):
           self.image_path  = {}
            

        def ajouter_image(self,image_path ):
            self.image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "png")
            self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path,"0.png")),size=(125,100))
            self.add = customtkinter.CTkImage(Image.open(os.path.join(image_path, "addd.png")), size=(35, 35))
            self.database = customtkinter.CTkImage(Image.open(os.path.join(image_path, "databasee.png")),size=(35, 35))
            self.dueexpense = customtkinter.CTkImage( Image.open(os.path.join(image_path, "expenses-duepaymentt.png")), size=(35, 35))
            self.analyticss = customtkinter.CTkImage(Image.open(os.path.join(image_path,"analyticss.png")),size=(35,35))
            self.backdoorr = customtkinter.CTkImage(Image.open(os.path.join(image_path,"backdoorr.png")),size=(35,35))
            self.closee = customtkinter.CTkImage(Image.open(os.path.join(image_path,"closee.png")),size=(20,20))
            self.due_insertionn = customtkinter.CTkImage(Image.open(os.path.join(image_path,"due_insertionn.png")),size=(35,35))
            self.due_receivingg = customtkinter.CTkImage(Image.open(os.path.join(image_path,"due_receivingg.png")),size=(35,35))
            self.exitt = customtkinter.CTkImage(Image.open(os.path.join(image_path,"exitt.png")),size=(35,35))
            self.homee = customtkinter.CTkImage(Image.open(os.path.join(image_path,"homee.png")),size=(35,35))
            self.immagine1 = customtkinter.CTkImage(Image.open(os.path.join(image_path,"immagine1.png")),size=(35,35))
            self.insert_item_savee = customtkinter.CTkImage(Image.open(os.path.join(image_path,"insert_item_savee.png")),size=(35,35))
            self.inventoryy = customtkinter.CTkImage(Image.open(os.path.join(image_path,"inventoryy.png")),size=(35,35))
            self.linvoicee = customtkinter.CTkImage(Image.open(os.path.join(image_path,"invoicee.png")),size=(35,35))
            self.larbExchangess = customtkinter.CTkImage(Image.open(os.path.join(image_path,"labExchangess.png")),size=(35,35))
            self.searchh = customtkinter.CTkImage(Image.open(os.path.join(image_path,"searchh.png")),size=(35,35))
            self.send_itemm = customtkinter.CTkImage(Image.open(os.path.join(image_path,"send_itemm.png")),size=(35,35))
            self.substractt = customtkinter.CTkImage(Image.open(os.path.join(image_path,"substractt.png")),size=(35,35))
            self.schedulee = customtkinter.CTkImage(Image.open(os.path.join(image_path,"schedulee.png")),size=(35,35))
            self.schedule_22 = customtkinter.CTkImage(Image.open(os.path.join(image_path,"schedule_22.png")),size=(35,35))
            self.receive_itemm = customtkinter.CTkImage(Image.open(os.path.join(image_path,"receive_itemm.png")),size=(35,35))
            self.projectt = customtkinter.CTkImage(Image.open(os.path.join(image_path,"projectt.png")),size=(35,35))
            self.prescriptionn_22 = customtkinter.CTkImage(Image.open(os.path.join(image_path,"prescription_22.png")),size=(35,35))
            self.labExchangess = customtkinter.CTkImage(Image.open(os.path.join(image_path,"labExchangess.png")),size=(35,35))
            
              

    class MoyenObject:
        def __init__(self):
            self.boutons = []
            self.labels = []
            self.options_menu = []

        def ajouter_bouton(self,):
            self.navigation_frame_label = customtkinter.CTkLabel(self.f1, text="   ", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
            self.navigation_frame_label.place( x=10 ,y=20)
             
            self.home_button = customtkinter.CTkButton(self.f1, corner_radius=0, height=40, border_spacing=10, text="Home",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.homee, anchor="w",command=self.default_home   )
            self.home_button.place( x=10 ,y=200)
            self.home_button_button_state = True
            ######################################
            self.dbase = customtkinter.CTkButton(self.f1, corner_radius=0, height=40, border_spacing=10, text="Dossier",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.database, anchor="w",command=self.pagedossiermed)
            self.dbase.place( x=10 ,y=250)
            self.dbase_button_state = True
            ####################################
            self.facture = customtkinter.CTkButton(self.f1, corner_radius=0, height=40, border_spacing=10, text="facture",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.linvoicee , anchor="w",command=self.pagefacturation  )
            self.facture.place( x=10 ,y=300)
            self.facturee_button_state = True
            ####################################
            self.analyseee = customtkinter.CTkButton(self.f1, corner_radius=0, height=40, border_spacing=10, text="analytique",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.analyticss , anchor="w",command=self.pagedanalyse  )
            self.analyseee.place ( x=10 ,y=350)
            self.analyse_button_state = True
            ####################################
            self.dueexpen = customtkinter.CTkButton(self.f1, corner_radius=0, height=40, border_spacing=10, text="dépense",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.dueexpense , anchor="w", command=self.pagedepense  )
            self.dueexpen.place ( x=10 ,y=400)
            self.dueexpen_button_state = True
            ####################################
            self.labExchan = customtkinter.CTkButton(self.f1, corner_radius=0, height=40, border_spacing=10, text="laboratoires",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.labExchangess , anchor="w",command=self.pagelaboratoire  )
            self.labExchan.place( x=10 ,y=450)
            self.labExchan_button_state = True
            ########################################
            self.backdoorre = customtkinter.CTkButton(self.f1, corner_radius=0, height=40, border_spacing=10, text="paramètre",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.backdoorr , anchor="w",command=self.pagedeparametre  )
            self.backdoorre.place( x=10 ,y=500)
            self.parametre_button_state = True
            self.button1 = customtkinter.CTkButton(master= self.frame_right, width= 95, text="Chercher" )
            self.button1.place(x=900, y=12) 
         
            self.b2 = customtkinter.CTkButton(master= self.frame_right, corner_radius=0, height=20, border_spacing=10, text="MENU ",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.img1 , anchor="w",command=self.toggle_button_action  )
            self.b2.place(x=1100, y=1)

        def ajouter_label(self, nom_label):
            self.navigation_frame_label = customtkinter.CTkLabel(self.f1, text="   ", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
            self.navigation_frame_label.place( x=10 ,y=20)

        def ajouter_option_menu(self, nom_option_menu):
           self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.f1, values=["Light", "Dark", "System"],
                                                                command=self.change_appearance_mode_event)
           self.appearance_mode_menu.place( x=10 ,y=600)
    class GrandObject:
     def __init__(self):
        self.heureetdate = []
        self.meteo = []
        self.schedule = []
