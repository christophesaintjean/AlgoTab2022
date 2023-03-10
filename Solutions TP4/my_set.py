from bisect import *


def set_len(E):
    return len(E)


def set_in(E, x):
    return E and x <= E[-1] and E[bisect_left(E, x)] == x


def set_not_in(E, x):
    return not E or x > E[-1] or E[bisect_left(E, x)] != x
    # return not set_in(E, x)


def set_add(E, x):
    index_x = bisect_left(E, x)
    if index_x == len(E) or E[index_x] != x:
        E.insert(index_x, x)
    return E


def set_rm(E, x):
    index_x = bisect_left(E, x)
    if index_x < len(E) and E[index_x] == x:
        del E[index_x]  # x est dans E
    return E


def set_create(L):
    S = sorted(L)  # N'importe quel algo de tri du cours
    E = []
    for s in S:
        # s in E -> O(|E|) // set_in(E, s) -> O(log(|E|))
        if not E or s != E[-1]:  # -> O(1)
            E.append(s)
    return E


def set_union(E1, E2):  # O(|E1| + |E2|)
    U = []
    i_1, i_2 = 0, 0
    while i_1 < len(E1) and i_2 < len(E2):
        if E1[i_1] == E2[i_2]:
            U.append(E1[i_1])
            i_1 += 1
            i_2 += 1
        elif E1[i_1] < E2[i_2]:
            U.append(E1[i_1])
            i_1 += 1
        else:  # E2[i_2] < E1[i_1]
            U.append(E2[i_2])
            i_2 += 1
    while i_1 < len(E1):  # ou U.extend(E1[i_1:]) pour terminer E1
        U.append(E1[i_1])
        i_1 += 1
    while i_2 < len(E2):  # ou U.extend(E2[i_2:]) pour terminer E2
        U.append(E2[i_2])
        i_2 += 1
    return U


def set_union_2(E1, E2):
    U = []
    for e1 in E1:
        set_add(U, e1)
    for e2 in E2:
        set_add(U, e2)
    return U


def set_inter(E1, E2):  # O(|E1| + |E2|)
    I = []
    i_1, i_2 = 0, 0
    while i_1 < len(E1) and i_2 < len(E2):
        if E1[i_1] == E2[i_2]:
            I.append(E1[i_1])
            i_1 += 1
            i_2 += 1
        elif E1[i_1] < E2[i_2]:
            i_1 += 1
        else:  # E2[i_2] < E1[i_1]
            i_2 += 1
    return I


def set_diff(E1, E2):  # # O(|E1| + |E2|)
    D = []
    i_1, i_2 = 0, 0
    while i_1 < len(E1) and i_2 < len(E2):
        if E1[i_1] == E2[i_2]:
            i_1 += 1
            i_2 += 1
        elif E1[i_1] < E2[i_2]:
            D.append(E1[i_1])
            i_1 += 1
        else:  # E2[i_2] < E1[i_1]
            i_2 += 1
    while i_1 < len(E1):  # ou D.extend(E1[i_1:]) pour terminer E1
        D.append(E1[i_1])
        i_1 += 1
    return D


def set_diff_2(E1, E2):  # O(|E1| * log (|E2|)) car |E1| dichotomies sur E2
    D = []
    for e1 in E1:
        if set_not_in(E2, e1):
            D.append(e1)
    return D


def set_isdisjoint(E1, E2):
    i_1, i_2 = 0, 0
    while i_1 < len(E1) and i_2 < len(E2):
        if E1[i_1] == E2[i_2]:
            return False
        elif E1[i_1] < E2[i_2]:
            i_1 += 1
        else:  # E2[i_2] < E1[i_1]
            i_2 += 1
    return True


def set_isdisjoint2(E1, E2):
    return len(set_inter(E1, E2)) == 0


def set_issub(E1, E2):  # tous les elements de E1 sont dans E2
    i_1, i_2 = 0, 0
    while i_1 < len(E1) and i_2 < len(E2):
        if E2[i_2] < E1[i_1]:
            i_2 += 1
        elif E1[i_1] == E2[i_2]:
            i_1 += 1
            i_2 += 1
        else:
            return False
    if i_1 == len(E1):
        return True
    else:
        return False


def set_issub2(E1, E2):
    return set_len(set_inter(E1, E2)) == set_len(E1)


def set_issup(E1, E2):
    return set_issub(E2, E1)


def set_xor(E1, E2):
    X = []
    i_1, i_2 = 0, 0
    while i_1 < len(E1) and i_2 < len(E2):
        if E1[i_1] < E2[i_2]:
            X.append(E1[i_1])
            i_1 += 1
        elif E1[i_1] > E2[i_2]:
            X.append(E2[i_2])
            i_2 += 1
        else:
            i_1 += 1
            i_2 += 1
    while i_1 < len(E1):
        X.append(E1[i_1])
        i_1 += 1
    while i_2 < len(E2):
        X.append(E2[i_2])
        i_2 += 1
    return X


def set_xor2(E1, E2):
    return set_union(set_diff(E1, E2), set_diff(E2, E1))


if __name__ == "__main__":
    E = set_create([3, 6, 3, 5, 9, -1, 6])
    print(E)

    E = [3, 6, 9]
    print(set_in(E, 6), set_in(E, 3), set_in(E, 9))
    print(set_in(E, 5), set_in(E, 2), set_in(E, 12))
    assert (set_add([3, 6, 9], 3) == [3, 6, 9])
    assert (set_add([3, 6, 9], 5) == [3, 5, 6, 9])
    assert (set_add([3, 6, 9], 10) == [3, 6, 9, 10])

    assert (set_rm([3, 6, 9], 3) == [6, 9])
    assert (set_rm([3, 6, 9], 5) == [3, 6, 9])
    assert (set_rm([3, 6, 9], 9) == [3, 6])

    assert (set_union([3, 6, 9], [4, 7, 8]) == [3, 4, 6, 7, 8, 9])
    assert (set_union([3, 6, 9], [3, 6]) == [3, 6, 9])
    assert (set_union_2([3, 6, 9], [4, 7, 8]) == [3, 4, 6, 7, 8, 9])
    assert (set_union_2([3, 6, 9], [3, 6]) == [3, 6, 9])

    assert (set_inter([3, 6, 9], [4, 6, 9]) == [6, 9])

    assert (set_diff([3, 6, 9, 10, 12], [6, 9, 15]) == [3, 10, 12])
    assert (set_diff_2([3, 6, 9, 10, 12], [6, 9, 15]) == [3, 10, 12])

    assert (set_isdisjoint([3, 6, 9, 10], [2, 15]))

    assert (set_issub([3, 6], [2, 3, 4, 6, 9, 10]))
    assert (set_issub([3, 6], [3, 6]))
    assert (not set_issub([3, 5], [3, 6, 7, 10]))

    assert (set_xor([3, 6, 9, 10], [2, 6, 9, 15]) == [2, 3, 10, 15])
    assert (set_xor2([3, 6, 9, 10], [2, 6, 9, 15]) == [2, 3, 10, 15])
