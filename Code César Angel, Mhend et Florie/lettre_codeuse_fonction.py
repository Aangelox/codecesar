def lettre_codeuse () :
    """
    Permet de demander la phrase qui contient la lettre codeuse, et de définir qu'elle est cette dernière.
    Elle retourne le nombre qui sert de décalage.
    """
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
    return code
