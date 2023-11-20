<<<<<<< HEAD
import tkinter as tk
import subprocess

# Fonction pour exécuter le script InscritsPasBoursiers.py
def comparer_fichiers():
    try:
        # Exécuter le script InscritsPasBoursiers.py en utilisant subprocess
        subprocess.run(["python", "InscritsPasBoursiers.py"])
        message_label.config(text="Le script a été exécuté avec succès.")
    except Exception as e:
        message_label.config(text="Erreur lors de l'exécution du script: " + str(e))

# Créer la fenêtre principale de l'interface graphique
root = tk.Tk()
root.title("Comparaison de fichiers")

# Créer un bouton "COMPARER" pour exécuter le script
compare_button = tk.Button(root, text="COMPARER", command=comparer_fichiers)
compare_button.pack(pady=20)

# Créer une étiquette pour afficher le message de fin
message_label = tk.Label(root, text="", fg="green")
message_label.pack()

# Lancer la boucle principale de l'interface graphique
root.mainloop()
=======
import tkinter as tk
import subprocess

# Fonction pour exécuter le script InscritsPasBoursiers.py
def comparer_fichiers():
    try:
        # Exécuter le script InscritsPasBoursiers.py en utilisant subprocess
        subprocess.run(["python", "InscritsPasBoursiers.py"])
        message_label.config(text="Le script a été exécuté avec succès.")
    except Exception as e:
        message_label.config(text="Erreur lors de l'exécution du script: " + str(e))

# Créer la fenêtre principale de l'interface graphique
root = tk.Tk()
root.title("Comparaison de fichiers")

# Créer un bouton "COMPARER" pour exécuter le script
compare_button = tk.Button(root, text="COMPARER", command=comparer_fichiers)
compare_button.pack(pady=20)

# Créer une étiquette pour afficher le message de fin
message_label = tk.Label(root, text="", fg="green")
message_label.pack()

# Lancer la boucle principale de l'interface graphique
root.mainloop()
>>>>>>> 123bf4729f62fae0ebb31f6472f83ab53deea68c
