import random


def tri_lent(L):
    def estTrie(L, deb=0, fin=None):
        if fin is None:
            fin = len(L)
        for i in range(1, fin):
            if L[i - 1] > L[i]:
                return False
        return True

    while not estTrie(L):
        random.shuffle(L)
    return L
