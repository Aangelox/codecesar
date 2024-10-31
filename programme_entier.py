#Code César
##### FONCTIONS
# Décodage
def decodage(message, lettre):#decalage = de la lettre codeuse
    """
    Permet le décodage d'un message codé à l'aide d'un code César.
    Utilisation : rentrer le message à décoder entre "", puis le numéro de la lettre codeuse.
    """

    message_decode=[]
    alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message_erreur="Vous devez entrer des lettres en majuscule !  Message à décoder :"
    c=0
    try:
        while c==0:
            for i in message:
                if i in alphabet:
                    c=1
                else:
                    message=input(message_erreur)
                    c=0
    except:
        message=input(message_erreur)
        c=0


    taille_message=len(message)
    for i in range (0,taille_message,1):
        if ord(message[0+i]) <(65+lettre) and ord(message[0+i])>64:
            nouvelle_lettre=ord(message[0+i])-lettre + 26
            nouvelle_lettre=chr(nouvelle_lettre)
        else :
            ord(message[0+i])
            nouvelle_lettre=ord(message[0+i])-lettre
            nouvelle_lettre=chr(nouvelle_lettre)
        message_decode.append(nouvelle_lettre)
    message_decode="".join(message_decode)
    return message_decode
############# PROGRAMME PRINCIPAL
