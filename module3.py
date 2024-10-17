# Décoder un message
def decodage (message, lettre):
    """
    Permet le décodage d'un message codé à l'aide d'un code César.
    Utilisation : rentrer le message à décoder entre guillemets, puis le numéro de la lettre codeuse.
    """
    message_decode=[]
    alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    c=0
    message_erreur="Vous devez entrer des lettres en majuscule ! Message à décoder :"
    try:
        while c==0:
            for i in message :
                if i in alphabet:
                    c=1
                else:
                    message=input(message_erreur)
                    c=0
    except:
        c=0
        message=input(message_erreur)
    taille_message=len(message)
    for i in range (0,taille_message,1):
        if ord(message [0+i])<(65+lettre)and ord(message [0+i])>64: 
            nouvelle_lettre=ord(message[0+i])-lettre + 26
            nouvelle_lettre=chr(nouvelle_lettre)
        else : 
            ord(mess[0+i])
            nouvelle_lettre=ord(message[0+i])-lettre
        message_decode.append(nouvelle_lettre)
    print("".join(mess_decode))
    return message_decode
print(decodage("",1))

#########################

#jsp si ton code fonctionne mais personnellement jsuis parti sur quelquqe chose comme ca
# Décoder un message
def decodage(caractere,clef):
  caractere = ord(caractere)
  if caractere>64 and caractere<91 :
    caractere_code = chr(caractere-clef)
  elif caractere>64 and caractere<91 and caractere>(64-clef):
    caractere_code = chr(caractere-clef+26)
  elif caractere == 39:
    caractere_code = chr(caractere)
  else:
    print("Erreur dans la saisie du message codé")
  return caractere_code

def messagedecodage(code,clef):
  message_decode = ""
  for i in code:
    message_decode += decodage(i,clef)
  return message_decode

print(messagedecodage("PENTALON",1))
