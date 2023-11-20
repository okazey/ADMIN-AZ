# import pandas as pd

# # Charger les fichiers Excel dans des dataframes
# bourses = pd.read_excel("Bourses.xlsx")
# inscrits = pd.read_excel("Inscrits.xlsx")

# # Comparer les colonnes CNI pour trouver les CNI manquants
# cni_manquants = inscrits[~inscrits['CNI'].isin(bourses['CNI'])]

# # Créer un fichier Excel nommé "Traitement" avec les CNI manquants
# cni_manquants.to_excel("Traitement.xlsx", index=False)

# print("Opération terminée. Les CNI manquants ont été enregistrés dans le fichier 'Traitement.xlsx'.")

import tkinter as tk
from tkinter import messagebox
import pandas as pd
import os

# Fonction pour exécuter la comparaison et sauvegarder dans "Traitement.xlsx"
def comparer_et_sauvegarder():
    if os.path.exists("Traitement.xlsx"):
        # Si le fichier "Traitement.xlsx" existe, demander confirmation à l'utilisateur
        confirmation = messagebox.askokcancel("Confirmation", "Le fichier 'Traitement.xlsx' existe déjà. Voulez-vous l'écraser?")
        if not confirmation:
            return  # Abandonner si l'utilisateur choisit d'annuler

    # Charger les fichiers Excel dans des dataframes
    bourses = pd.read_excel("Bourses.xlsx")
    inscrits = pd.read_excel("Inscrits.xlsx")

    # Comparer les colonnes CNI pour trouver les CNI manquants
    cni_manquants = inscrits[~inscrits['CNI'].isin(bourses['CNI'])]

    # Sauvegarder dans "Traitement.xlsx"
    cni_manquants.to_excel("Traitement.xlsx", index=False)
    print("Opération terminée. Les étudiants inscrits et non bourisers ont été enregistrés dans le fichier 'Traitement.xlsx'.")

# Créer la fenêtre principale de l'interface graphique
root = tk.Tk()
root.title("Comparaison de fichiers")

# Créer un bouton "COMPARER" pour exécuter la comparaison et sauvegarder
compare_button = tk.Button(root, text="COMPARER", command=comparer_et_sauvegarder)
compare_button.pack(pady=20)

# Lancer la boucle principale de l'interface graphique
root.mainloop()
