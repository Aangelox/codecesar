def codage(caractere, decalage):
    decalage = int(decalage)
    decalage = decalage % 26  # Réduit le décalage à une valeur entre 0 et 25
    caractere_code = caractere  # Valeur par défaut

    # Convertir le caractère en majuscule
    caractere = caractere.upper()

    if 'A' <= caractere <= 'Z':
        caractere_code = chr((ord(caractere) - 65 + decalage) % 26 + 65)

    return caractere_code

def messagecodage():
    """
    Permet de coder un message entré par l'utilisateur.
    Elle retourne le message codé.
    """
    message = input("Entrez le message que vous souhaitez coder")

    # Vérifier les caractères spéciaux
    for char in message:
        if not (char.isalpha() or char in ["'", " "]):
            print("Vous avez fait une erreur de saisie")
            return
    #Définir la lettre codeuse
    decalage=lettre_codeuse()
    # Coder le message
    message_code = ""
    for i in message:
        message_code += codage(i, decalage)
    return message_code
