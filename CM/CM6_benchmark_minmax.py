from random import randint, seed
from statistics import mean
from time import perf_counter as time

import matplotlib.pyplot as plt
from tqdm import tqdm

from CM3_triinsert import triinsert
from CM4_triselect import triselect
from CM5_trifusion import trifusion
from CM5_trirapide import trirapide
from CM6_tricomptage import tricomptage
from CM6_tritimsort import timSort as tritimsort

algos = {
    "Tri par insertion": triinsert,
    "Tri par selection": triselect,
    "Tri par Fusion": trifusion,
    "Tri rapide": trirapide,
    "Tri Tim": tritimsort,
}

algos = {
    "Tri par Fusion": trifusion,
    "Tri rapide": trirapide,
    "Tri Tim": tritimsort,
}

algos = {
    "Tri par Fusion": trifusion,
    "Tri rapide": trirapide,
    "Tri Tim": tritimsort,
    "Tri par comptage": tricomptage,
}

rep = 3
pmax = 20
N = [2 ** p for p in range(pmax)]

for name, algo in tqdm(algos.items()):
    seed(13)  # memes tableaux à trier
    tps_min, tps_mean, tps_max = [], [], []
    for n in N:
        tps_n = []
        for _ in range(rep):
            T = [randint(1, 10000) for _ in range(n)]
            debut = time()
            _ = algo(T)
            fin = time()
            tps_n.append(fin - debut)
        else:
            T = [randint(1, 10000) for _ in range(n)]
            T.sort()
            debut = time()
            _ = algo(T)
            fin = time()
            tps_n.append(fin - debut)
            T.sort(reverse=True)
            debut = time()
            _ = algo(T)
            fin = time()
            tps_n.append(fin - debut)
        tps_min.append(min(tps_n))
        tps_mean.append(mean(tps_n))
        tps_max.append(max(tps_n))

    plt.fill_between(N, tps_min, tps_max, label=algo.__name__, alpha=0.5)
    plt.plot(N, tps_mean, marker='+')
plt.legend()
plt.xscale("log")
plt.yscale("log")
plt.show()
