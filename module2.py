# Créé par elevessi, le 10/10/2024 en Python 3.7
def codage(caractere, decalage):
    if decalage > 26:
        quotient = decalage//26
        decalage = decalage - quotient*26
    caractere= ord(caractere)
    if caractere>64 and caractere<91:
        caractere_code = chr(caractere+decalage)
    elif caractere>96 and caractere<123:
        caractere_code = chr(caractere+decalage-32)
    elif caractere == 39:
        caractere_code = chr(caractere)
    else:
        caractere_code = chr(0)
    return caractere_code

def messagecodage(message,decalage):
    message_code = ""
    for i in message :
        message_code += codage(i,decalage)
    return message_code

print(messagecodage("Le message code est incroyablement bien code", 1))

#mon code marche nickel pour les sceptiques
##jsp si ton code finctiknne du coup mais j'ai fais ça.

def codage(message,lettre):
    """
    Permet le codage d'un message à l'aide d'un code César.
   """
    message_code=[]
    alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ' "
    message_erreur="Vous devez entrer des lettres en majuscule !  Message à coder :"
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
        if (ord(message[0+i])==32) :
            nouvelle_lettre=' '
        elif (ord(message[0+i])==39):
            nouvelle_lettre="'"
        else :
            ord(message[0+i])
            nouvelle_lettre=ord(message[0+i])+lettre
            if nouvelle_lettre>90:
                nouvelle_lettre=nouvelle_lettre-26
            nouvelle_lettre=chr(nouvelle_lettre)
        message_code.append(nouvelle_lettre)
    message_code="".join(message_code)
    return message_code
#BOUCLE TEST
for i in range (27):
    print (i, codage("ABCDEFGHIJK LMN'OPQRSTUVWXYZ",i))
    
