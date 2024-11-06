def decodage(message, lettre):
    """
    Permet le décodage d'un message codé à l'aide d'un code César.
    Utilisation : rentrer le message à décoder entre "", puis le numéro de la lettre codeuse.
    """
    message_decode=[]
    alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ' "
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
        if ord(message[0+i])==32 :
            nouvelle_lettre=message.replace(message[0+i]," ")
        elif ord(message[0+i])==39:
            nouvelle_lettre=message.replace(message[0+i],"'")
        elif ord(message[0+i]) <(65+lettre) and ord(message[0+i])>64:
            nouvelle_lettre=ord(message[0+i])-lettre + 26
            nouvelle_lettre=message.replace(message[0+i],chr(nouvelle_lettre))
        else :
            ord(message[0+i])
            nouvelle_lettre=ord(message[0+i])-lettre
            nouvelle_lettre=message.replace(message[0+i],chr(nouvelle_lettre))
    return nouvelle_lettre
#BOUCLE TEST
for i in range (27):
    print (i, decodage("ABCDEFGHIJK LMN'OPQRSTUVWXYZ",i))
#J'ai essayé de le faire avec la méthode .replace masi ça ne fonctionne pas.
