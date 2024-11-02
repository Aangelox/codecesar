# Créé par elevessi, le 10/10/2024 en Python 3.7
mot=str(input("lettre codeuse"))
chaine="abcdefghijklmnopqrstuvwxyz"
nombre=[]
def freq():
    if freq(2):
        for chaine in freq:
            if mot in chaine:
                nombre=[1+chaine.index(chaine)]
return nombre

print(nombre)

#code invalid pour l'instant
#############
#Voilà ce que j'ai fait, dites moi ce que vous en pensez.
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
