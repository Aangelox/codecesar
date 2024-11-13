####################################################
#################### FONCTIONS #####################
####################################################

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

def decodage():
    """
    Permet le décodage d'un message codé à l'aide d'un code César.
    Elle retourne le message décodé.
    """
    message = input("Quel message souhaitez-vous décoder ? ")
    message_decode = []
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ' "
    message_erreur = "Vous devez entrer des lettres en majuscule ! Message à décoder : "
    message_special = "Vous avez fait une erreur de saisie"

    # Validation du message
    while any(char not in alphabet for char in message):
        if any(not (char.isalpha() or char in ["'", " "]) for char in message):
            print(message_special)
            return
        message = input(message_erreur)
    # Définir la lettre codeuse
    decalage=lettre_codeuse()
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

def lettre_codeuse () :
    """
    Permet de demander la phrase qui contient la lettre codeuse, et de définir qu'elle est cette dernière.
    Elle retourne un tuple contenant la lettre codeuse et son nombre associé.
    """
    alphabet ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    phrase=input("Donner la phrase qui constitue la lettre codeuse.")
    phrase=phrase.split(" ")
    taille = len(phrase)
    for i in range (taille):
        for j in range (len(phrase[i])-1):
            iterations=phrase[i].count(phrase[i][j])
            if iterations ==2:
                lettre_codeuse=phrase[i][j]
                lettre_codeuse=lettre_codeuse.upper()
                code=alphabet.index(lettre_codeuse)+1
                break
            else:
                j+=1
        i=i+1
    return code

def encodagedecodage():
    """
    Permet de choisir entre coder ou décoder un message.
    """
    choix = input('Si vous souhaitez encoder un message, entrez "CODAGE" comme ceci, si vous souhaitez décoder un message, entrez "DECODAGE" comme ceci ')
    c=0
    while c==0:
        try :
            if choix=="CODAGE" or choix =="DECODAGE":
                c=1
            else:
                choix=input('Vous avez fait une erreur de saisie. Entrez soit "CODAGE" soit "DECODAGE" ')
        except :
            c=0
    if choix == "CODAGE":
        print("Le message codé est :", messagecodage())
    if choix=="DECODAGE":
        print ("Le message décodé est :", decodage())
###########################################################
################## PROGRAMME PRINCIPAL ####################
###########################################################

#pour choisir entre codage ou decodage ecrire encodagedecodage()

encodagedecodage()

