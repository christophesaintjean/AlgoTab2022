def l2c(l):
    N2L = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
           "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

    L2N = {L: N for N, Ls in N2L.items() for L in Ls}
    return L2N[l]


def chiffrage(ch):
    num = ""
    for c in ch:
        num += l2c(c)
    return num


def c2ls(c):
    N2L = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
           "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
    return list(N2L[c])

dico = []
with open('dico_vrac.txt', 'r') as f:
   for ligne in f:
       dico.append(ligne.rstrip('\n'))


def dechiffrage(D, nombre):
    # filtre sur la taille
    D = [mot for mot in D if len(mot) == len(nombre)]
    for i, c in enumerate(nombre):
        D = [mot for mot in D if mot[i] in c2ls(c)]
    return D


if __name__ == "__main__":
    print(dechiffrage(dico, "666"))
