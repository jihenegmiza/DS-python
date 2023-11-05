#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import colorama
from colorama import Fore
import cowsay
from art import text2art
import re
import hashlib
import getpass
import string
import matplotlib.pyplot as plt
import pandas as pd

# Display a welcome message with ASCII art
print(text2art('Bienvenue'))
cowsay.fox(Fore.MAGENTA + "Mini Projet".center(45, '-'))

#1- Enregistrement
# Function to input and validate an email address
def enter_email():
    regex = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    while True:
        email = input("Entrez votre Email: ")
        if re.match(regex, email):
            return email
        else:
            print("S'il vous plaît, mettez une adresse email valide")

# Function to input and validate a password
def enter_password():
    while True:
        pwd = getpass.getpass("Entrez votre mot de passe: ")
        if len(pwd) == 8:
            if any(char.isdigit() for char in pwd):
                if any(char.isupper() for char in pwd):
                    if any(char.islower() for char in pwd):
                        if any(char in string.punctuation for char in pwd):
                            pwd = hashlib.sha256(pwd.encode()).hexdigest()
                            return pwd
                        else:
                            print("Le mot de passe doit contenir un caractère spécial.")
                    else:
                        print("Le mot de passe doit contenir un caractère minuscule.")
                else:
                    print("Le mot de passe doit contenir un caractère majuscule.")
            else:
                print("Le mot de passe doit contenir un chiffre.")
        else:
            print("Le mot de passe doit avoir une longueur de 8 caractères.")

email = ''
pwd = ''

# Authentication
def authentifier():
    email = input("Entrez votre e-mail : ")
    password = getpass.getpass("Entrez votre mot de passe : ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    with open("Enregistrement.txt", 'r') as file:
        for line in file:
            stored_email, stored_password = line.strip().split(":")
            if email == stored_email and hashed_password == stored_password:
                return True
    return False

# Main menu
def menu_principal():
    print(colorama.Fore.RED + "Menu principal")
    print("1- Enregistrement")
    print("2- Authentication")
    print("3- Quitter")
    
# Fonction pour hacher un mot par sha256
def hacher_sha256(word):
    sha256 = hashlib.sha256()
    sha256.update(word.encode('utf-8'))
    return sha256.hexdigest()

# Fonction pour Attaquer par dictionnaire le mot inséré.
def attaquer_par_dictionnaire(mot, dictionnaire):
    trouve = False
    for key, mots in dictionnaire.items():
        if mot in mots:
            print(f"Le mot '{mot}' a été trouvé dans la catégorie '{key}'.")
            trouve = True
    if not trouve:
        print(f"Le mot '{mot}' n'a pas été trouvé dans le dictionnaire.")

# Fonction Cesar avec code ASCII
def cesar_with_ascii_code(texte, decalage):
    texte_chiffre = ""
    
    for char in texte:
        if char.isalpha():
            min_maj = ord('a') if char.islower() else ord('A')
            texte_chiffre += chr((ord(char) - min_maj + decalage) % 26 + min_maj)
        else:
            texte_chiffre += char
    
    return texte_chiffre


# Fonction Cesar dans les 26 lettres
def cesar_with_26_letters(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shifted_alphabet_index = ord(char.lower()) + shift
            if char.isupper():
                result += chr(shifted_alphabet_index).upper()
            else:
                result += chr(shifted_alphabet_index)
        else:
            result += char
    return result

# Fonction Chiffrer le message (a) 
def chiffrement_cesar(message, decalage):
    resultat = ""
    for lettre in message:
        if lettre.isalpha():
            decalage_modifie = decalage % 26  # Assure que le décalage reste dans l'alphabet
            if lettre.islower():
                lettre_chiffree = chr(((ord(lettre) - ord('a') + decalage_modifie) % 26) + ord('a'))
            else:
                lettre_chiffree = chr(((ord(lettre) - ord('A') + decalage_modifie) % 26) + ord('A'))
            resultat += lettre_chiffree
        else:
            resultat += lettre  # Conserve les caractères non alphabétiques inchangés
    return resultat

# Fonction Déchiffrer le message (b)
def dechiffrement_cesar(message, decalage):
    return chiffrement_cesar(message, -decalage)

# dictionnaire
dictionnaire = {
    "country": ["France", "Germany", "Spain", "Italy", "United Kingdom"],
    "city": ["Paris", "Berlin", "Madrid", "Rome", "London"]
}

# Fonction pour Afficher le Dataset sous forme de dictionnaire.
def collecter_dataset():
    data = {
        "make": ["Toyota", "Honda", "Ford", "Nissan", "Chevrolet", "Volkswagen"],
        "year": [2020, 2018, 2019, 2021, 2017, 2018]
    }
    print(data)

# Fonction pour afficher des courbes 
def afficher_courbes():
    df = pd.DataFrame(data)
    plt.figure(figsize=(10, 7))
    plt.plot(df['make'], df['year'], marker='o')
    plt.title('Vehicle Makes vs Production Years')
    plt.xlabel('Make')
    plt.ylabel('Year')
    plt.grid(True)
    plt.show()

# Menu des options après authentification
def menu_options():
    while True:
        print(colorama.Fore.BLUE + "Menu des options")
        print("A- Donnez un mot à hacher (en mode invisible)")
        print("    a- Hacher le mot par SHA-256")
        print("    b- Attaquer par dictionnaire le mot inséré")
        print("    d- Revenir au menu principal")

        print("B- Décalage par CESAR")
        print("    a- Donnez un mot à chiffrer")
        print("        1- Cesar avec code ASCII")
        print("        2- Cesar dans les 26 lettres")
        print("    b- Chiffrer le message (a)")
        print("    c- Déchiffrer le message (b)")
        print("    d- Revenir au menu principal")

        print("C- Collecter une Dataset de votre choix")
        print("    a- Afficher le Dataset sous forme de dictionnaire")
        print("    b- Afficher des courbes de votre choix")
        print("    c- Revenir au menu principal")

        option = input("Choisissez une option : ( A ou B ou C ) ")

        if option == 'A':
            sous_menu = input("Choisissez une option : (a ou b ou d) ")

            if sous_menu == 'a':
                mot_a_hacher = input("Entrez un mot à hacher : ")
                mot_hache = hacher_sha256(mot_a_hacher)
                print(f"Mot haché : {mot_hache}")
            elif sous_menu == 'b':
                mot_a_rechercher = input("Entrez un mot à attaquer : ")
                attaquer_par_dictionnaire(mot_a_rechercher, dictionnaire)
            elif sous_menu == 'd':
                break

        elif option == 'B':
            sous_menu = input("Choisissez une option : (a ou b ou c) ")

            if sous_menu == 'a':
                type_cesar = input("Choisissez un type de Cesar (1 ou 2) : ")
                if type_cesar == '1':
                    text = input("Entrez le texte à chiffrer : ")
                    shift = int(input("Entrez le décalage : "))
                    result = cesar_with_ascii_code(text, shift)
                    print("Résultat : ", result)
                elif type_cesar == '2':
                    text = input("Entrez le texte à chiffrer : ")
                    shift = int(input("Entrez le décalage : "))
                    result = cesar_with_26_letters(text, shift)
                    print("Résultat : ", result)
                else:
                    print("Choix incorrect, veuillez réessayer.")

            elif sous_menu == 'b':
                message = input("Entrez le message à chiffrer : ")
                decalage = int(input("Entrez le décalage : "))
                message_chiffre = chiffrement_cesar(message, decalage)
                print("Message chiffré :", message_chiffre)

            elif sous_menu == 'c':
                message_chiffre = input("Entrez le message à déchiffrer : ")
                decalage = int(input("Entrez le décalage : "))
                message_dechiffre = dechiffrement_cesar(message_chiffre, decalage)
                print("Message déchiffré :", message_dechiffre)
            elif sous_menu == 'd':
                break

        elif option == 'C':
            sous_menu = input("Choisissez une option : (a ou b ou c) ")

            if sous_menu == 'a':
                collecter_dataset()
            elif sous_menu == 'b':
                afficher_courbes()
            elif sous_menu == 'c':
                break
        elif option == 'D':
            break
data = {
    "make": ["Toyota", "Honda", "Ford", "Nissan", "Chevrolet", "Volkswagen"],
    "year": [2020, 2018, 2019, 2021, 2017, 2018]
}
# Programme principal
while True:
    menu_principal()
    choix = input("Choisissez une option : ")
    if choix == '1':
            while email == '':
                email = enter_email()
            pwd = enter_password()
            with open("Enregistrement.txt", 'w') as file:
                file.write(f"{email}:{pwd}")
            print("Enregistrement réussi!")
    elif choix == '2':
        if authentifier():
            print("Authentification réussie !")
            menu_options()
        else:
            print("L'authentification a échoué. Veuillez vous enregistrer d'abord.")
    elif choix == '3':
        print("Au revoir !")
        break


# In[ ]:




