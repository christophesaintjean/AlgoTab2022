from random import randint


def degre(P):
    return len(P) - 1


def rndi_poly(n, min=-5, max=5):
    R = [0] * (n + 1)
    for i in range(n + 1):
        R[i] = randint(min, max)
    while R[-1] == 0:
        R[-1] = randint(min, max)
    return R


def eval_poly(P, x):
    return sum(ai * x ** i for i, ai in enumerate(P))


def eval_rec(P, x):
    if len(P) == 1:
        return P[0]
    if len(P) > 1:
        return P[0] + x * eval_rec(P[1:], x)


def eval_iter(P, x):
    R = 0
    for a_i in reversed(P):
        R = x * R + a_i
    return R


def add_poly(P, Q):
    d = max(len(P), len(Q))
    R = [0] * d
    for i in range(d):
        Pi = P[i] if i < len(P) else 0
        Qi = Q[i] if i < len(Q) else 0
        R[i] = Pi + Qi
    while len(R) > 1 and R[-1] == 0:
        R.pop()
    return R


def sub_poly(P, Q):
    d = max(len(P), len(Q))
    R = [0] * d
    for i in range(d):
        Pi = P[i] if i < len(P) else 0
        Qi = Q[i] if i < len(Q) else 0
        R[i] = Pi - Qi
    while len(R) > 1 and R[-1] == 0:
        R.pop()
    return R


def mult_poly(P, Q):
    R = [0] * (degre(P) + degre(Q) + 1)
    for i, ai in enumerate(P):
        for j, bj in enumerate(Q):
            R[i + j] += ai * bj
    return R


def mult_rec(P, Q):
    """Multiplication de deux polynômes par la méthode récursive"""
    if len(P) == 1:
        return [P[0] * Q[i] for i in range(len(Q))]
    elif len(Q) == 1:
        return [Q[0] * P[i] for i in range(len(P))]
    else:
        n2 = len(P) // 2
        Pl, Ph = div_poly(P, n2)
        Ql, Qh = div_poly(Q, n2)
        R1 = T1 = mult_rec(Pl, Ql)
        R3 = mult_rec(Ph, Qh)
        T3 = xn_poly(R3, 2 * n2)
        R2 = mult_rec(add_poly(Pl, Ph), add_poly(Ql, Qh))
        T2 = xn_poly(sub_poly(sub_poly(R2, R1), R3), n2)
        return add_poly(add_poly(T1, T2), T3)


def div_poly(P, n):
    """Division euclidienne de P par x**n"""
    deg = degre(P)
    if deg < n:
        return P, [0]
    else:
        return P[:n], P[n:]


def xn_poly(P, n):
    R = [0] * n + P
    while len(R) > 1 and R[-1] == 0:
        R.pop()
    return R


def rndi_poly_dict(n, min=-5, max=5):
    D = {0: 0}
    for i in range(n + 1):
        Ri = randint(min, max)
        if Ri != 0:
            D[i] = Ri
    while n not in D:
        Rn = randint(min, max)
        if Rn != 0:
            D[n] = Rn
    return D


def eval_poly_dict(P, x):
    return sum(ai * x ** i for i, ai in P.items())


def eval_rec_dict(P, x):
    """Evaluation d'un polynôme par la méthode récursive"""
    pass  # n'a pas de sens


def add_poly_dict(P, Q):
    """Addition de deux polynômes représentés par des dictionnaires"""
    ## | designe l'union des clés de P et Q  (.keys() n'est pas obligatoire)
    ##  P.get(k, 0) renvoie la valeur de la clé k dans P ou 0 si k n'est pas dans P
    R = {k: P.get(k, 0) + Q.get(k, 0) for k in set(P.keys()) | set(Q.keys())}
    R = {k: v for k, v in R.items() if v != 0}
    return R


def sub_poly_dict(P, Q):
    """Soustraction de deux polynômes représentés par des dictionnaires"""
    R = {k: P.get(k, 0) - Q.get(k, 0) for k in set(P.keys()) | set(Q.keys())}
    R = {k: v for k, v in R.items() if v != 0}
    return R


def mult_poly_dict(P, Q):
    """Multiplication de deux polynômes représentés par des dictionnaires"""
    R = {0: 0}
    for i, ai in P.items():
        for j, bj in Q.items():
            if i + j in R:
                R[i + j] += ai * bj
            else:
                R[i + j] = ai * bj
    return R


if __name__ == "__main__":
    P = rndi_poly(2)
    Q = rndi_poly(2)
    print(P, Q)
    print(eval_poly(P, 2))
    print(eval_rec(P, 2))
    print(eval_iter(P, 2))
    print(add_poly(P, Q))
    print(sub_poly(P, Q))
    print(mult_poly(P, Q))
    P = rndi_poly(500)
    Q = rndi_poly(500)
    PQ_rec = mult_rec(P, Q)
    PQ_iter = mult_poly(P, Q)
    assert (PQ_rec == PQ_iter)
    print("-" * 20)
    P_dict = rndi_poly_dict(5)
    Q_dict = rndi_poly_dict(3)
    print(P_dict, Q_dict)
    print(eval_poly_dict(P_dict, 2))
    print(add_poly_dict(P_dict, Q_dict))
    print(sub_poly_dict(P_dict, Q_dict))
    print(mult_poly_dict(P_dict, Q_dict))
