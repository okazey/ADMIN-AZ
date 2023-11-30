import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os
import subprocess
import time

# Fonction pour exécuter le code et gérer le bouton
def execute_code():
    global processing
    global button

    file_name = "Traitement.xlsx"
    if os.path.exists(file_name):
        message = "Le fichier existe. Voulez-vous écraser le fichier existant?"
        response = messagebox.askokcancel("Attention", message)
        if not response:  # Si l'utilisateur a choisi d'annuler
            return

    if processing:  # Si le processus est en cours, ne rien faire
        return

    processing = True
    style = ttk.Style()
    style.theme_use('default')

    style.configure("red.Horizontal.TProgressbar", foreground='red', background='red')
    style.configure("green.Horizontal.TProgressbar", foreground='green', background='green')

    progress['style'] = 'red.Horizontal.TProgressbar'
    progress['maximum'] = 100

    button['text'] = 'Veuillez patienter...'

    for i in range(101):
        time.sleep(0.1)  # Simule une opération longue
        progress['value'] = i
        root.update_idletasks()

    progress['style'] = 'green.Horizontal.TProgressbar'

    button['text'] = 'Terminé!'
    processing = False
    button['command'] = reset_button  # Modifier le comportement du bouton

    subprocess.Popen(['python', 'traitement.py'])  # Exécuter le script traitement.py

# Fonction pour réinitialiser le bouton
def reset_button():
    global button
    button['text'] = 'Comparer'
    button['command'] = execute_code  # Rétablir le comportement initial

# Création de la fenêtre
root = tk.Tk()
root.title("Exécution de code")

# Barre de progression
progress = ttk.Progressbar(root, orient='horizontal', length=200, mode='determinate')
progress.pack(pady=10)

# Déclaration de la variable pour suivre l'état du traitement
processing = False

# Bouton pour exécuter le code
button = tk.Button(root, text="Comparer", command=execute_code)
button.pack()

# Lancement de la boucle principale
root.mainloop()
