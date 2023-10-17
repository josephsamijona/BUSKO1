 
import customtkinter
import os
import PIL

import tkinter as tk
import customtkinter
import os
from PIL import ImageTk, Image
import sqlite3

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

class LoginWindow(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        self.geometry('1166x718')
        self.title("another")
        self.resizable(0, 0)
        self.state('zoomed')

        img1 = ImageTk.PhotoImage(Image.open("./assets/6881.jpg"))
        self.l1 = customtkinter.CTkLabel(master=self, image=img1)
        self.l1.pack()

        self.frame = customtkinter.CTkFrame(master=self.l1, width=520, height=560, corner_radius=0)
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "assets")

        self.labo = customtkinter.CTkImage(Image.open(os.path.join(image_path, "0.png")), size=(125, 100))

        self.home_labo = customtkinter.CTkLabel(master=self.frame, text="", image=self.labo)
        self.home_labo.place(x=185, y=120)

        self.l2 = customtkinter.CTkLabel(master=self.frame, text="BIENVENUE", font=('Century Gothic', 15))
        self.l2.place(x=205, y=45)
        self.l3 = customtkinter.CTkLabel(master=self.frame, text="CONNECTEZ-VOUS", font=('Century Gothic', 10))
        self.l3.place(x=210, y=220)
        self.entry1 = customtkinter.CTkEntry(master=self.frame, width=220, placeholder_text='Identifiant')
        self.entry1.place(x=150, y=260)
        self.entry2 = customtkinter.CTkEntry(master=self.frame, width=220, placeholder_text='mot de passe', show="*")
        self.entry2.place(x=150, y=325)

        self.button1 = customtkinter.CTkButton(master=self.frame, width=95, text="connexion", command=self.login)
        self.button1.place(x=205, y=400)

    def login(self):
        # Get the username and password from the entries
        username = self.entry1.get()
        password = self.entry2.get()

        # Connexion à la base de données SQLite
        conn = sqlite3.connect("base_de_donnees.db")
        cursor = conn.cursor()

        # Vérification des informations de connexion dans la base de données
        cursor.execute("SELECT * FROM user WHERE username=? AND password=?", (username, password))
        user = cursor.fetchone()

        if user:
            # L'utilisateur est authentifié avec succès
            if user[-1] == 'admin':
                # Si c'est un administrateur, faire quelque chose (par exemple, ouvrir une fenêtre d'administration)
                pass
            elif user[-1] == 'doctor':
                # Si c'est un médecin, faire quelque chose (par exemple, ouvrir une fenêtre de médecin)
                pass
            elif user[-1] == 'nurse':
                # Si c'est une infirmière, faire quelque chose (par exemple, ouvrir une fenêtre d'infirmière)
                pass
            else:
                # Si c'est un patient, faire quelque chose (par exemple, ouvrir une fenêtre de patient)
                pass
        else:
            # Afficher un message d'erreur pour une connexion invalide
            error_label = customtkinter.CTkLabel(master=self.frame, text="Nom d'utilisateur ou mot de passe invalide", font=('Century Gothic', 12), fg_color='red')
            error_label.place(x=200, y=430)

        # Fermer la connexion à la base de données
        conn.close()

if __name__ == "__main__":
    login_window = LoginWindow()
    login_window.mainloop()
