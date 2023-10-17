import tkinter as tk
import sqlite3
import customtkinter
import os
from PIL import ImageTk, Image

# Initialiser la configuration de customtkinter
customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

# Créer une classe personnalisée pour la fenêtre de connexion
class LoginWindow(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        self.geometry('1166x718')
        self.title("another")
        self.resizable(0, 0)
        self.state('zoomed')

        # Créer une étiquette avec une image de fond
         # Obtenez le chemin absolu du répertoire "assets" en utilisant os.path
        assets_dir = os.path.join(os.path.dirname(__file__), "..", "..", "assets")

        # Spécifiez le chemin relatif de l'image à partir du répertoire "assets"
        image_path = os.path.join(assets_dir, "6881.jpg")
        img1 = ImageTk.PhotoImage(Image.open(image_path))
        self.l1 = customtkinter.CTkLabel(master=self, image=img1)
        self.l1.pack()

        # Créer un cadre pour le formulaire de connexion
        self.frame = customtkinter.CTkFrame(master=self.l1, width=520, height=560, corner_radius=0)
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

       

        self.labo = customtkinter.CTkImage(Image.open(os.path.join(assets_dir, "0.png")), size=(125, 100))

        # Placer l'image sur le cadre
        self.home_labo = customtkinter.CTkLabel(master=self.frame, text="", image=self.labo)
        self.home_labo.place(x=185, y=120)

        # Créer des étiquettes et des champs pour le nom d'utilisateur et le mot de passe
        self.l2 = customtkinter.CTkLabel(master=self.frame, text="BIENVENUE", font=('Century Gothic', 15))
        self.l2.place(x=205, y=45)
        self.l3 = customtkinter.CTkLabel(master=self.frame, text="CONNECTEZ-VOUS", font=('Century Gothic', 10))
        self.l3.place(x=210, y=220)
        self.entry1 = customtkinter.CTkEntry(master=self.frame, width=220, placeholder_text='Identifiant')
        self.entry1.place(x=150, y=260)
        self.entry2 = customtkinter.CTkEntry(master=self.frame, width=220, placeholder_text='mot de passe', show="*")
        self.entry2.place(x=150, y=325)

        # Créer un bouton de connexion
        self.button1 = customtkinter.CTkButton(master=self.frame, width=95, text="connexion", command=self.login)
        self.button1.place(x=205, y=400)

    # Définir la fonction de connexion
    def login(self):
        # Récupérer le nom d'utilisateur et le mot de passe depuis les champs
        username = self.entry1.get()
        password = self.entry2.get()

        # Se connecter à la base de données SQLite
        # Obtenir le chemin absolu du répertoire "database" en utilisant os.path
        database_dir = os.path.join(os.path.dirname(__file__), "..", "database")

       # Spécifiez le chemin absolu de la base de données dans le dossier "database"
        db_path = os.path.join(database_dir, "clinique.db")

# Ouvrez la connexion vers la base de données
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Interroger la base de données pour vérifier si le nom d'utilisateur et le mot de passe sont valides
        cursor.execute("SELECT * FROM Utilisateurs WHERE Username=? AND Password=?", (username, password))
        user = cursor.fetchone()

        conn.close()

        if user:
            # Si le nom d'utilisateur et le mot de passe sont valides, créer une nouvelle fenêtre pour la page de bienvenue
            w = customtkinter.CTk()
            w.geometry("1280x720")
            w.title("Welcome")
            l1 = customtkinter.CTkLabel(master=w, text="Home Page", font=('Century Gothic', 60))
            l1.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        else:
            # Afficher un message d'erreur en cas de connexion invalide
            error_label = customtkinter.CTkLabel(master=self.frame, text="Nom d'utilisateur ou mot de passe invalide", font=('Century Gothic', 12), fg_color='red')
            error_label.place(x=200, y=430)

# Si vous souhaitez exécuter la fenêtre de connexion en tant qu'application autonome
if __name__ == "__main__":
    login_window = LoginWindow()
    login_window.mainloop()
