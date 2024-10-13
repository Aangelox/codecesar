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
