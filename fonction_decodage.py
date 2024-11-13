# Créé par Utilisateur, le 13/11/2024 en Python 3.7
def decodage(message, decalage):
    """
    Permet le décodage d'un message codé à l'aide d'un code César.
    Elle retourne le message décodé.
    """
    message = input("Quel message souhaitez-vous décoder ? ")
    message_decode = []
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ' "
    message_erreur = "Vous devez entrer des lettres en majuscule ! Message à décoder : "

    # Validation du message
    while any(char not in alphabet for char in message):
        message = input(message_erreur)

    # Décodage du message
    for caractere in message:
        if caractere == ' ':
            nouvelle_lettre = ' '
        elif caractere == "'":
            nouvelle_lettre = "'"
        elif ord(caractere) < (65 + decalage):
            # Si décalage en dehors de la plage, boucle en ajoutant 26
            nouvelle_lettre = chr(ord(caractere) - decalage + 26)
        else:
            nouvelle_lettre = chr(ord(caractere) - decalage)
        message_decode.append(nouvelle_lettre)

    return ''.join(message_decode)
