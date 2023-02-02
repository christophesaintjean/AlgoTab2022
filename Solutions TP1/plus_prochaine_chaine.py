from plus_proche import plus_proche
from supp_tp1 import levenshteinDistance
import random

if __name__ == "__main__":
    dico = []
    with open('dico_vrac.txt', 'r') as f:
        for ligne in f:
            dico.append(ligne.rstrip('\n'))
    req = "voitiure"
    i_req = plus_proche(dico, req, levenshteinDistance)
    print(dico[i_req])
    phrase = "li repa est servis e il lait choud"
    print(phrase)
    phrase_conv = " ".join([dico[plus_proche(dico, req, levenshteinDistance)] for req in phrase.split(' ')])
    print(phrase_conv)