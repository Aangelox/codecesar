def codage(caractere, decalage):
    decalage = int(decalage)  # Convertit le décalage en entier
    decalage = decalage % 26  # Réduit le décalage à une valeur entre 0 et 25
    caractere_code = caractere  # Valeur par défaut pour le caractère codé

    # Convertir le caractère en majuscule
    caractere = caractere.upper()

    # Vérifier si le caractère est une lettre majuscule
    if 'A' <= caractere <= 'Z':
        # Calcule le caractère codé en utilisant la formule du code César
        caractere_code = chr((ord(caractere) - 65 + decalage) % 26 + 65)
    
    return caractere_code  # Retourne le caractère codé

def messagecodage():
    print("Entrez le message que vous souhaitez encoder")  # Demande à l'utilisateur d'entrer un message
    message = input()  # Lit le message entré par l'utilisateur
    
    # Vérifier les caractères spéciaux
    for char in message:
        if not (char.isalpha() or char in ["'", " "]):  # Vérifie si le caractère est une lettre ou un espace
            print("Vous avez fait une erreur de saisie")  # Affiche un message d'erreur
            return  # Quitte la fonction si un caractère invalide est trouvé

    while True:  # Boucle pour demander un décalage valide
        print("Entrez le décalage que vous souhaitez appliquer")  # Demande à l'utilisateur d'entrer un décalage
        decalage = input()  # Lit le décalage entré par l'utilisateur
        try:
            decalage = int(decalage)  # Tente de convertir le décalage en entier
            break  # Sort de la boucle si la conversion réussit
        except ValueError:
            print("Vous n'avez pas entré un nombre entier !")  # Affiche un message d'erreur si la conversion échoue

    message_code = ""  # Initialise une chaîne vide pour le message codé
    for i in message:  # Pour chaque caractère dans le message
        message_code += codage(i, decalage)  # Encode le caractère et l'ajoute au message codé
    print("Le message codé est :", message_code)  # Affiche le message codé

def decodage():
    """
    Permet le décodage d'un message codé à l'aide d'un code César.
    Elle retourne le message décodé.
    """
    message = input("Quel message souhaitez-vous décoder ? ")  # Demande à l'utilisateur le message à décoder
    decalage = input("Quel est le décalage que vous souhaitez appliquer ? ")  # Demande le décalage
    message_decode = []  # Initialise une liste pour stocker le message décodé
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ' "  # Définit l'alphabet autorisé
    message_erreur = "Vous devez entrer des lettres en majuscule ! Message à décoder : "  # Message d'erreur pour le format
    message_special = "Vous avez fait une erreur de saisie"  # Message d'erreur pour les caractères invalides

    # Validation du message
    while any(char not in alphabet for char in message):  # Tant qu'il y a des caractères non valides dans le message
        if any(not (char.isalpha() or char in ["'", " "]) for char in message):  # Vérifie les caractères spéciaux
            print(message_special)  # Affiche un message d'erreur
            return  # Quitte la fonction
        message = input(message_erreur)  # Redemande le message à l'utilisateur

    # Convertir le décalage en entier
    try:
        decalage = int(decalage)  # Tente de convertir le décalage en entier
    except ValueError:
        print("Vous devez entrer un nombre entier pour le décalage !")  # Affiche un message d'erreur si la conversion échoue
        return  # Quitte la fonction

    # Décodage du message
    for caractere in message:  # Pour chaque caractère dans le message
        if caractere == ' ':
            nouvelle_lettre = ' '  # Conserve les espaces
        elif caractere == "'":
            nouvelle_lettre = "'"  # Conserve les apostrophes
        elif ord(caractere) < (65 + decalage):  # Vérifie si le caractère est en dehors de la plage pour le décalage
