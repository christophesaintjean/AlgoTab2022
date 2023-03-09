from random import randint, seed

from utils import estTrie


def tricomptage(T, m=None, M=None):
    if m is None:
        m = min(T)
    if M is None:
        M = max(T)
    cpt = [0] * (M - m + 1)
    for x in T:
        cpt[x - m] += 1
    print(cpt)
    j = 0
    x = m
    for rep in cpt:
        for _ in range(rep):
            T[j] = x
            j += 1
        else:
            x += 1
    return T


if __name__ == "__main__":
    seed(13)
    T = [randint(1, 100) for _ in range(10)]
    print(T)
    print(tricomptage(T))

    seed(13)
    T = [randint(1, 100) for _ in range(3000)]
    T2 = sorted(T.copy())
    print("Le tableau de 3000 éléments est trié:", estTrie(tricomptage(T)), T2 == T)
