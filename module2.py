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
