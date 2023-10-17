from tkinter import ttk, Tk, Label, Button, Frame, HORIZONTAL
import time
from PIL import Image, ImageTk
import os
from blogin import LoginWindow


class SplashScreen:
    def __init__(self, root):
        self.root = root
        self.root.title('Splash Screen')
        self.width_of_window = 427
        self.height_of_window = 250
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.x_coordinate = (self.screen_width / 2) - (self.width_of_window / 2)
        self.y_coordinate = (self.screen_height / 2) - (self.height_of_window / 2)
        self.root.geometry("%dx%d+%d+%d" % (self.width_of_window, self.height_of_window, self.x_coordinate, self.y_coordinate))
        self.root.overrideredirect(1)
        
        self.create_widgets()
        
    def create_widgets(self):
        # Couleur de fond pour le cadre
        self.a = '#249794'
        
        # Création d'un cadre pour afficher une couleur de fond spécifiée
        Frame(self.root, width=self.width_of_window, height=self.height_of_window, bg=self.a).place(x=0, y=0)
        
        
        
        # Création de la barre de progression
        self.progress = ttk.Progressbar(self.root, style="red.Horizontal.TProgressbar", orient=HORIZONTAL, length=500, mode='determinate')
        self.progress.place(x=-10, y=235)
        
        # Chargement de l'image et affichage centré
        self.image_path = os.path.join(os.path.dirname(__file__), 'busko-removebg-preview.png')
        self.assets_dir = os.path.join(os.path.dirname(__file__), "..", "..", "assets")
        self.image_path = os.path.join(self.assets_dir, "busko-removebg-preview.png")
        self.load_and_display_image()
        
        # Création du bouton "Lancer" avec appel à la fonction "bar()" lorsqu'il est cliqué
        self.b1 = Button(self.root, width=10, height=1, text='Lancer', command=self.bar, border=0, fg=self.a, bg='white')
        self.b1.place(x=320, y=190)
    
    def load_and_display_image(self):
        # Chargement de l'image
        self.img = Image.open(self.image_path)
        self.image_width, self.image_height = self.img.size
        self.aspect_ratio = min(self.width_of_window * 0.8 / self.image_width, self.height_of_window * 0.8 / self.image_height)
        self.new_image_width = int(self.image_width * self.aspect_ratio)
        self.new_image_height = int(self.image_height * self.aspect_ratio)
        
        # Conversion de l'image en un format Tkinter compatible
        self.tk_image = ImageTk.PhotoImage(self.img.resize((self.new_image_width, self.new_image_height), Image.ANTIALIAS))
        
        # Calcul des coordonnées pour centrer l'image après le redimensionnement
        self.image_x = (self.width_of_window - self.new_image_width) // 2
        self.image_y = (self.height_of_window - self.new_image_height) // 2
        
        # Création de l'étiquette pour afficher l'image centrée
        self.image_label = Label(self.root, image=self.tk_image, bg=self.a)
        self.image_label.place(x=self.image_x, y=self.image_y)
    
    def bar(self):
        # Affichage du texte "Chargement..."
        self.l4 = Label(self.root, text='Chargement...', fg='white', bg=self.a)
        lst4 = ('Calibri (Body)', 10)
        self.l4.config(font=lst4)
        self.l4.place(x=18, y=210)
        
        # Barre de progression
        r = 0
        for i in range(100):
            self.progress['value'] = r
            self.root.update_idletasks()
            time.sleep(0.03)
            r = r + 1
        
        # Fermeture de la fenêtre principale après la fin de la barre de progression et affichage d'une nouvelle fenêtre
        self.root.destroy()
        new_win()

def new_win():
    # Créez une instance de la classe LoginWindow pour afficher la page de connexion
    login_window = LoginWindow()
    login_window.mainloop()


if __name__ == "__main__":
    # Création de la fenêtre principale et affichage de l'écran de démarrage
    root = Tk()
    splash = SplashScreen(root)
    root.mainloop()