################# CODE CESAR ###################
##### FONCTIONS
# LETTRE CODEUSE
def lettre_codeuse () :
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
    return (lettre_codeuse, code)

# CODAGE
# DECODAGE
def decodage(lettre):#decalage = de la lettre codeuse
    """
    Permet le décodage d'un message codé à l'aide d'un code César.
    Utilisation : rentrer le message à décoder entre "", puis le numéro de la lettre codeuse.
    """
    message=input("Quel message souhaitez-vous décoder ?")
    message_decode=[]
    alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ' "
    message_erreur="Vous devez entrer des lettres en majuscule !  Message à décoder :"
    c=0
    while c==0:
        try:
            for i in message:
                if i in alphabet:
                    c=1
                else:
                    message=input(message_erreur)
        except:
            message=input(message_erreur)
            c=0
    taille_message=len(message)
    for i in range (0,taille_message,1):
        if (ord(message[0+i])==32) :
            nouvelle_lettre=' '
        elif (ord(message[0+i])==39):
            nouvelle_lettre="'"
        elif ord(message[0+i]) <(65+lettre) and ord(message[0+i])>64:
            nouvelle_lettre=ord(message[0+i])-lettre + 26
            nouvelle_lettre=chr(nouvelle_lettre)
        else :
            ord(message[0+i])
            nouvelle_lettre=ord(message[0+i])-lettre
            nouvelle_lettre=chr(nouvelle_lettre)
        message_decode.append(nouvelle_lettre)
    message_decode="".join(message_decode)
    return message_decode

#FIN DES FONCTIONS

############# PROGRAMME PRINCIPAL
#Entrer la phrase codeuse
lettre_fonction=lettre_codeuse()
lettre=lettre_fonction[1]
print("La lettre codeuse est donc", lettre_fonction[0], "donc le codage est ",lettre_fonction[1],".")
#Demander si l'utilisateur souahite coder ou décode + demander le message.
message_erreur= "Vous devez répondre par 'oui' ou 'non'"
coder = input("Voulez-vous coder un message ?")
c=0
while c==0:
    try:
        if coder =='oui'or coder=='non' :
            c=1
        else :
            coder=input(message_erreur)
    except:
        c=0

if coder =='oui':
    print(codage())
decoder =input("Voulez-vous décoder un message ?")
c=0
while c==0:
    try:
        if decoder=='oui'or decoder=='non' :
            c=1
        else:
            decoder=input(message_erreur)
    except:
        c=0
if decoder=='oui':
    print(decodage (lettre))
#### 
#Il fat juste créer la fonction qui code et après normalement c'est fini
