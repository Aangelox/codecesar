# Créé par elevessi, le 10/10/2024 en Python 3.7
# Décoder un message 
alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lettre=5
mess=input("Quel messsage souhaitez vous décoder ?")    
try: 
    for i in mess:
        if i in alphabet:
            pass
        else:
            mess=input("Vous devez entrer des lettres en majuscule !  Message à décoder :")
except:
    pass
        
mess
mess_decode=[]

for i in mess:
    i=1
    ord(mess[0-i])
    nouv=ord(mess[0-i])-lettre
    remplacer=chr(nouv)
    mess_decode.append(remplacer)
    i+=1
print("".join(mess_decode))
mess_decode=[]
