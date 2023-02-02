from random import randint, seed

def estTrie(T, deb=0, fin=None):
    if fin is None:
        fin = len(T)
    for i in range(deb, fin-1):
        if T[i] > T[i + 1]:
            return False
    return True

def triselect(T):
    for i in range(len(T)-1):
        jmin = i
        for j in range(i+1, len(T)):
            if T[j] < T[jmin]:
                jmin = j
        if jmin != i:
            T[i], T[jmin] = T[jmin], T[i]
    return T

def triselect_max(T):
    for i in range(len(T)-1, 0, -1):
        jmax = i
        for j in range(i-1, -1, -1):
            if T[j] > T[jmax]:
                jmax = j
        if jmax != i:
            T[i], T[jmax] = T[jmax], T[i]
    return T

def triselect_dec(T):
    for i in range(0, len(T)-1):
        jmax = i
        for j in range(i+1, len(T)):
            if T[j] > T[jmax]:
                jmax = j
        if jmax != i:
            T[i], T[jmax] = T[jmax], T[i]
    return T

if __name__ == "__main__":
    seed(13)
    T = [randint(1, 100) for _ in range(10)]
    print(triselect(T))
    print(triselect_dec(T))
    print(triselect_max(T))
    # ici utiliser perf_counter