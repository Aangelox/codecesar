# Créé par elevessi, le 10/10/2024 en Python 3.7
def codage(caractere, decalage):
    if decalage > 26:
        quotient = decalage//26
        decalage = decalage - quotient*26
    caractere= ord(caractere)
    if caractere>64 and caractere<91:
        caractere_code = chr(caractere+decalage)
        print(caractere_code)
    elif caractere>96 and caractere<123:
        caractere_code = chr(caractere+decalage-32)
        print(caractere_code)
    elif caractere == 39:
        caractere_code = chr(caractere)
        print(caractere_code)
    return caractere_code

def messagecodage(message,decalage):
    lettre=len(message)
    for lettre in message :
        codage(message[0],decalage)
    return codage

messagecodage("a",1)

