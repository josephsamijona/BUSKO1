import sqlite3
import random
import string

# Connexion à la base de données SQLite
conn = sqlite3.connect("base_de_donnees.db")
cursor = conn.cursor()

# Création de la table "user" avec la colonne "user_id" de type TEXT
cursor.execute('''CREATE TABLE IF NOT EXISTS user
                  (user_id TEXT PRIMARY KEY,
                   first_name TEXT NOT NULL,
                   last_name TEXT NOT NULL,
                   username TEXT NOT NULL UNIQUE,
                   email TEXT NOT NULL UNIQUE,
                   phone TEXT,
                   password TEXT NOT NULL,
                   date_of_creation TEXT NOT NULL,
                   account_type TEXT NOT NULL)''')

# Fonction pour générer un identifiant utilisateur aléatoire
def generate_user_id(first_name, last_name, date_of_creation):
    # Générer un identifiant en utilisant les trois premières lettres du prénom,
    # les trois premières lettres du nom de famille et les deux derniers chiffres de l'année de création
    user_id = (first_name[:3] + last_name[:3] + date_of_creation[-2:]).lower()
    return user_id

# Insertion de l'administrateur
admin_data = ('Admin', 'Admin', 'admin', 'admin@example.com', '1234567890', 'admin_password', '2023-09-05', 'admin')
cursor.execute('''INSERT INTO user
                  (user_id, first_name, last_name, username, email, phone, password, date_of_creation, account_type)
                  VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', admin_data)

# Insertion du docteur
doctor_data = ('Docteur', 'Médecin', 'doctor', 'doctor@example.com', '9876543210', 'doctor_password', '2023-09-05', 'doctor')
cursor.execute('''INSERT INTO user
                  (user_id, first_name, last_name, username, email, phone, password, date_of_creation, account_type)
                  VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', doctor_data)

# Insertion de l'infirmière
nurse_data = ('Infirmière', 'Soins', 'nurse', 'nurse@example.com', '5555555555', 'nurse_password', '2023-09-05', 'nurse')
cursor.execute('''INSERT INTO user
                  (user_id, first_name, last_name, username, email, phone, password, date_of_creation, account_type)
                  VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', nurse_data)

# Insertion de 17 patients avec des identifiants générés aléatoirement
patients_data = [
    ('Patient1', 'Nom1', 'patient1', 'patient1@example.com', '1111111111', 'patient1_password', '2023-09-05', 'patient'),
    ('Patient2', 'Nom2', 'patient2', 'patient2@example.com', '2222222222', 'patient2_password', '2023-09-05', 'patient'),
    # Ajoutez les données des autres patients ici...
]

for patient in patients_data:
    first_name, last_name, username, email, phone, password, date_of_creation, account_type = patient
    user_id = generate_user_id(first_name, last_name, date_of_creation)
    cursor.execute('''INSERT INTO user
                      (user_id, first_name, last_name, username, email, phone, password, date_of_creation, account_type)
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', (user_id, first_name, last_name, username, email, phone, password, date_of_creation, account_type))

# Valider et enregistrer les modifications
conn.commit()

# Fermer la connexion à la base de données
conn.close()


