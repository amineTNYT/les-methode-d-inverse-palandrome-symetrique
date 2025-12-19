#test si une chaine est palandrome
def palindrome(ch):
    i = 0
    n = len(ch)
    p = True
    while i < n // 2 and p:
        if ch[i] != ch[n - 1 - i]:
            p= False
        i= i+ 1
    return p

# Example usage
print(palindrome("radar"))  # True
print(palindrome("hello"))  # False
#--------------------------------------------------------------------------

def is_palindrome(ch):
    left = 0
    right = len(ch) - 1
    p=True
    while left < right:
        if word[left] != word[right]:
            p=False
        left += 1
        right = right-1

    return p

w = input()
print(is_palindrome(w))

#----------------------------------------------------------------------------------------------------
#inverser une chaine(boucle pour pas="-1")
def inverser_chaine(ch):
    resultat = ""
    for i in range(len(ch)-1, -1, -1):
        resultat += ch[i]
    return resultat

print(inverser_chaine("hello"))  # "olleh"


#----------------------------------------------------------------------------------------------------
#inverser une chaine(boucle pour)
def inverse(ch):
    ch0 = ""
    for i in range(len(ch)):
        ch0 = ch[i] + ch0
    return ch0
#---------------------------------------------------------------------------
#seullment pour les entiers
def palindrome_nombre(x):
    original = x
    m = 0
    while x > 0:
        s = x % 10      # reste de la division par 10
        m = m * 10 + s  # construire le nombre inversé
        x = x // 10     # diviser par 10 pour enlever le dernier chiffre
    return m == original  # vérifier si le nombre inversé est égal à l'original

# Exemple d'utilisation
print(palindrome_nombre(121))  # True
print(palindrome_nombre(123))  # False
#-----------------------------------------------------------------------------
#seullement pour les entiers
def inverser_nombre(x):
    nombre_inverse = 0
    while x > 0:
        chiffre = x % 10           # obtenir le dernier chiffre
        nombre_inverse = nombre_inverse * 10 + chiffre  # ajouter le chiffre à l'inverse
        x = x // 10                # supprimer le dernier chiffre
    return nombre_inverse          # retourner le nombre inversé

# Exemples d'utilisation
print(inverser_nombre(17415))   # 54321
 
#----------------------------------------------------------------------------
#inverse une chaine de caractére

def inverser_nombre_texte(x):
    ch = str(x)                    # Convch(x) - Convertir en chaîne
    chx = ""                       # chx ← "" - Chaîne inversée vide
    while ch != "":                # Tant que ch ≠ ""
        chx = ch[0] + chx          # chx ← ch[0] + chx (ajouter premier caractère au début)
        ch = ch[1:]                # Effacer(ch, 0, 1) - Supprimer premier caractère
    return (chx)                   # Retourner chx 




