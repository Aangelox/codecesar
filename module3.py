# Créé par elevessi, le 10/10/2024 en Python 3.7
# Décoder un message 
lettre=int(input("lettre codeuse"))
messagecode=input("Quel messsage souhaitez vous décoder ?")
for i in mess:
    nouv_mess=int(ord(mess[i]))
    mess.replace([i-1],chr(nouv_mess-lettre))
print(mess)
