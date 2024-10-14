# Décoder un message
alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lettre=6
mess_decode=[]
mess=input("Quel messsage souhaitez vous décoder ?")
c=0
try:
    while c==0:
        for i in mess:
            if i in alphabet:
                c=1
            else:
                mess=input("Vous devez entrer des lettres en majuscule !  Message à décoder :")
except:
    pass

taille=len(mess)
for i in range (0,taille,1):
    ord(mess[0+i])
    nouv=ord(mess[0+i])-lettre
    remplacer=chr(nouv)
    mess_decode.append(remplacer)
print("".join(mess_decode))

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
