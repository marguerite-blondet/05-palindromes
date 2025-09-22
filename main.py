"""
Ce fichier contient une fonction principale et une fonction secondaire.
"""
#### Fonction secondaire


def ispalindrome(p):

    # votre code ici

    """
    Retourne True si la chaîne p est un palindrome, False sinon.
    Un palindrome est une chaîne qui se lit de la même façon de gauche à droite
    et de droite à gauche.
    """
    p = p.lower().replace("é", "e").replace("è", "e").replace("ê", "e").replace("ë", "e")\
                 .replace("à", "a").replace("ç", "c").replace("ô", "o").strip(",'!?")
    for a in p:
        if a.isalnum():
            continue
        p = p.replace(a, "")
    if p == p[::-1]:
        return True
    return False

#### Fonction principale


def main():
    """
    Fonction principale du programme.
    Appelle la fonction secondaire et vérifie son bon fonctionnement.
    """
    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
