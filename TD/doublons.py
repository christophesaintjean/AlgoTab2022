from random import randint


def doublons(T):
    cpt = 0
    for i in range(len(T)):
        if T[abs(T[i])] >= 0:
            T[abs(T[i])] = -T[abs(T[i])]
        else:
            print(f"{abs(T[i])} en position {i} est un doublon")
            cpt += 1
        print(f"{i=} {T=}")
    print("Nombres de doublons: ", cpt)


if __name__ == "__main__":
    n = 10
    m = 8
    T = [randint(1, m) for _ in range(n)]
    T = [3, 4, 2, 1, 3, 2, 6, 3]
    print(T)
    doublons(T)
    print(T)
