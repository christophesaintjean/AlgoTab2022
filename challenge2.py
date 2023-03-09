def max_local_dicho(T, l=0, r=None):
    if not T:
        return None
    if r is None:
        r = len(T) - 1
    if l == r:
        return l
    m = (l + r) // 2
    if T[m] >= T[m - 1] and T[m] >= T[m + 1]:
        return m
    elif T[m - 1] > T[m]:
        return max_local_dicho(T, l, m - 1)
    else:
        return max_local_dicho(T, m + 1, r)


def est_max_local(T, i):
    if not T:
        return i == None
    assert (0 <= i < len(T))
    if i == 0 and (len(T) == 1 or T[i] >= T[i + 1]):
        return True
    if i == len(T) - 1 and T[i] >= T[i - 1]:
        return True
    if T[i] >= T[i - 1] and T[i] >= T[i + 1]:
        return True
    return False


if __name__ == "__main__":
    T = [5, 10, 20, 15]
    i = max_local_dicho(T)
    print(f'{i=} {T[i]=} {est_max_local(T, i)=}')

    T = [10, 20, 15, 2, 23, 90, 67]
    i = max_local_dicho(T)
    print(f'{i=} {T[i]=} {est_max_local(T, i)=}')

    T = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    i = max_local_dicho(T)
    print(f'{i=} {T[i]=} {est_max_local(T, i)=}')

    T = [1, 2, 3, 4, 5, 6, 7, 8, 5]
    i = max_local_dicho(T)
    print(f'{i=} {T[i]=} {est_max_local(T, i)=}')

    T = [1, 2, 3, 4, 5, 6]
    i = max_local_dicho(T)
    print(f'{i=} {T[i]=} {est_max_local(T, i)=}')

    T = [1, 2, 3, 4, 5, 6][::-1]
    i = max_local_dicho(T)
    print(f'{i=} {T[i]=} {est_max_local(T, i)=}')
