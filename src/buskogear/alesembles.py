import tkinter as tk
import os
from PIL import Image
import customtkinter

# Define a custom application class inheriting from customtkinter.CTk
class ToggleMenuApp(customtkinter.CTk):
    def __init__(self):
         
        # Set the initial window properties
        super().__init__()
        self.geometry('1166x718')
        self.title("another")
        self.resizable(0, 0)
        self.state('zoomed')
        self.create_toggle_button()
        self.default_home()
        self.current_frame = None 
      #--------------image---------------------------------------- 
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "png")
    
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
              
         
    #####################################################################################################
    def load_image(self, filename):
        try:
            # Try to open the image file and return the customtkinter.CTkImage object
            return customtkinter.CTkImage(Image.open(filename))
        except FileNotFoundError:
            # If the file is not found, print an error message and return None
            print(f"Error: File '{filename}' not found.")
            return None
        except Exception as e:
            # If there's any other exception while loading the image, print an error message and return None
            print(f"Error loading image '{filename}': {e}")
            return None
    #################################################BUTTONS######################################################
    def create_toggle_button(self):
       # Create the main toggle button with the initial image and bind it to the toggle_win method
       # Load images for toggle button
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "png")
        self.img1 = customtkinter.CTkImage(Image.open(os.path.join(image_path, "menue.png")), size=(35, 35))
        self.img2 = customtkinter.CTkImage(Image.open(os.path.join(image_path, "menue2.png")), size=(35, 35))
        
        self.toggle_button_state = True
         
    ################################################################################################################ 
    def toggle_button_action(self):
        
        if  self.toggle_button_state:
            self.close_current_frame() 
            self.f1 = customtkinter.CTkFrame(self, width=190, height=900,corner_radius=0 )
            self.f1.place(x=0, y=0)

            # Function for creating buttons
             # Function for creating buttons
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
            ##########################################
            self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.f1, values=["Light", "Dark", "System"],
                                                                command=self.change_appearance_mode_event)
            self.appearance_mode_menu.place( x=10 ,y=600)
            

            # Create the buttons with different options
           

            self.b2.configure(image=self.img2)
            self.toggle_button_state = False
        else:
            self.f1.destroy()
            self.close_current_frame() 
            self.b2.configure(image=self.img1)
            self.toggle_button_state = True 
        
    def default_home(self):
        # Create two CTkFrames
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)

        self.frame_right = customtkinter.CTkFrame(master=self, corner_radius=0)
        self.frame_right.grid(row=0, column=1, rowspan=1, pady=0, padx=0, sticky="nsew")
        #image 
        
        # Configure grid layout for the right frame
        self.frame_right.grid_rowconfigure(1, weight=1)
        self.frame_right.grid_rowconfigure(0, weight=0)
        self.frame_right.grid_columnconfigure(0, weight=1)
        self.frame_right.grid_columnconfigure(1, weight=0)
        self.frame_right.grid_columnconfigure(2, weight=1)

        # Create an entry widget within the right frame
         
        
        self.entry = customtkinter.CTkEntry(master=self.frame_right, width=5,
                                            placeholder_text="Nom du patient")
        self.entry.grid(row=0, column=0, sticky="we", padx=(470, 0), pady=12)
        self.entry.bind("<Return>", self.on_search)  # Bind the Return key press event to the entry widget
        #main frame
        self.frame = customtkinter.CTkFrame(master=self, width=800, height=550, corner_radius=10 )
        self.frame.place(relx=0.5, rely=0.5,anchor=tk.CENTER)

        # Create a button widget within the right frame
        self.button1 = customtkinter.CTkButton(master= self.frame_right, width= 95, text="Chercher" )
        self.button1.place(x=900, y=12) 
         
        self.b2 = customtkinter.CTkButton(master= self.frame_right, corner_radius=0, height=20, border_spacing=10, text="MENU ",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.img1 , anchor="w",command=self.toggle_button_action  )
        self.b2.place(x=1100, y=1)
    
    def pagedossiermed(self):
         
           self.close_current_frame()
           self.f2 = customtkinter.CTkFrame(self, width=900, height=455)
           self.f2.place(x=0, y=45)
           self.l2 = customtkinter.CTkLabel(self.f2, text='dossier medical')
           self.l2.configure(font=('Comic Sans MS', 90))
           self.l2.place(x=290, y=150 - 45)
           self.b2.configure(image=self.img1)
           self.home_button_button_state=False
         
    def close_current_frame(self):
        if self.current_frame:
            self.current_frame.destroy()
            self.current_frame = None    
    
            

    def pagefacturation(self):
        self.close_current_frame()
        self.f2 = customtkinter.CTkFrame(self, width=900, height=455)
        self.f2.place(x=0, y=45)
        self.l2 = customtkinter.CTkLabel(self.f2, text='facturation')
        self.l2.configure(font=('Comic Sans MS', 90))
        self.l2.place(x=320, y=150 - 45)
         
        

    def pagedanalyse(self):
        self.close_current_frame()
        self.f2 = customtkinter.CTkFrame(self, width=900, height=455)
        self.f2.place(x=0, y=45)
        self.l2 = customtkinter.CTkLabel(self.f2, text='analyse')
        self.l2.configure(font=('Comic Sans MS', 90))
        self.l2.place(x=290, y=150 - 45)
        self.b2.configure(image=self.img1)
       

    def pagedepense(self):
        self.close_current_frame()
        self.f2 = customtkinter.CTkFrame(self, width=900, height=455)
        self.f2.place(x=0, y=45)
        self.l2 = customtkinter.CTkLabel(self.f2, text='depense')
        self.l2.configure(font=('Comic Sans MS', 90))
        self.l2.place(x=320, y=150 - 45)
        self.b2.configure(image=self.img1)
         
     
    def pagelaboratoire(self):
        self.close_current_frame()
        self.f2 = customtkinter.CTkFrame(self, width=900, height=455)
        self.f2.place(x=0, y=45)
        self.l2 = customtkinter.CTkLabel(self.f2, text='laboratoire')
        self.l2.configure(font=('Comic Sans MS', 90))
        self.l2.place(x=290, y=150 - 45)
        self.b2.configure(image=self.img1)
        

    def pagedeparametre(self):
        self.close_current_frame()
        self.f2 = customtkinter.CTkFrame(self, width=900, height=455)
        self.f2.place(x=0, y=45)
        self.l2 = customtkinter.CTkLabel(self.f2, text='parametre')
        self.l2.configure(font=('Comic Sans MS', 90))
        self.l2.place(x=320, y=150 - 45)
        self.b2.configure(image=self.img1)
         

    def on_search(self, event=None):
         
        dossierdupatient = self.entry.get()  
        print(" Recherche pour:", dossierdupatient)  
    def run(self):
        # Start the main event loop
        self.mainloop()
    def change_appearance_mode_event(self, new_appearance_mode):
      
     customtkinter.set_appearance_mode(new_appearance_mode)





# Entry point of the application
if __name__ == "__main__":
    app = ToggleMenuApp()
    app.run()
    
