def decodage(message, lettre):#decalage = de la lettre codeuse
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
#BOUCLE TEST
for i in range (27):
    print (i, decodage("ABCDEFGHIJK LMN'OPQRSTUVWXYZ",i))

print (decodage("UT YK XKZXUABK IUSSK IUTBKTA PKAJO G YKVZ NKAXKY PK VUXZKXGO AT INGVKGA BKXZ KZ AT VGXGVRAOK HRKA RK ZGHRKGA KYZ KT YKIAXOZK OR KYZ OTAZORK JK INKXINKX G S'KTZUAXRUAVKX SKZZXK R'GXMKTZ JGTY AT YGI TUOX KZ BKTKF YKAR",6))

#########################
# Normalement le code fonctionne, je n'ai pas réussi à le faire avec la méthode .replace mais ça marche quand même.

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
