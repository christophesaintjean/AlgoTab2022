def fusion_inp(T, left, mid, right):
    """Fusion en place de deux sous-tableaux triés de T"""
    i = left
    j = mid
    if (right - left + 1) == 2:  # deux éléments
        if T[left] > T[right]:
            T[left], T[right] = T[right], T[left]
        return
    while i <= right:
        if T[i] <= T[j]:
            i += 1
        else:
            tmp = T[j]
            for k in range(j, i - 1, -1):
                T[k] = T[k - 1]
            T[i] = tmp
            i += 1
            j += 1
        if j > right or i == j:
            break


def tri_fusion(T, left=0, right=None):
    """Tri fusion de T[left:right]"""
    if right is None:
        right = len(T) - 1
    print(f"Tri de {T[left:right + 1]} {left=} {right=}")

    # if left == right - 1:
    #     print(f'fusion {T[left:right+1]=}')
    #     fusion_inp(T, left, right, right)
    #     print(f'Resultat Fusion {T[left:right+1]=}')
    if left < right:
        mid = (left + right) // 2 + 1
        print(f'{mid=}')
        print("Tri de gauche")
        tri_fusion(T, left, mid - 1)
        print("Tri de droite")
        tri_fusion(T, mid, right)
        print(f'Fusion {T[left:mid]=} et {T[mid:right+1]=}')
        fusion_inp(T, left, mid, right)
        print(f'Resultat Fusion {T[left:right+1]=}')
    print(f"Fin de tri de {T[left:right + 1]}")
    return T


def estTrie(L, deb=0, fin=None):
    if fin is None:
        fin = len(L)
    for i in range(1, fin):
        if L[i - 1] > L[i]:
            return False
    return True


if __name__ == "__main__":
    T = [95, 10, 4, 15, -1, 5, 12, 48, 2, 0 - 1, 3, 2, 6]
    print(f'{T=} {tri_fusion(T)=}')
