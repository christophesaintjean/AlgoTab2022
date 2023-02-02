import requests

def sous_chaine_egales(T1, T2):
    for i in range(len(T1)):
        if T1[i] != T2[i]:
            return False
    return True

def sous_chaine(T, req):
    n, n_req = len(T), len(req)
    for i in range(n - n_req):
       if sous_chaine_egales(T[i:i+n_req], req):
           return i
    return None

def count_sous_chaine(T, req):
    n, n_req = len(T), len(req)
    cpt = 0
    for i in range(n - n_req):
       if sous_chaine_egales(T[i:i+n_req], req):
           cpt +=  1
    return cpt

def idx_sous_chaine(T, req):
    n, n_req = len(T), len(req)
    idx = []
    for i in range(n - n_req):
       if sous_chaine_egales(T[i:i+n_req], req):
           idx.append(i)
    return idx

def my_replace(T, req, rep):
    idx = idx_sous_chaine(T, req)  
    n_req = len(req)
    texte2 = ""
    for i in range(len(idx)):
        if i == 0:
            texte2 += T[:idx[0]] + rep
        else:
            texte2 += T[idx[i-1]+n_req:idx[i]] + rep
    else:
        texte2 += T[idx[-1]+n_req:]                    
    return texte2

def my_replace_2(T, req, rep):
    return rep.join(T.split(req))

if __name__ == "__main__":
    """url = 'https://www.gutenberg.org/files/55456/55456-0.txt'
    myfile = requests.get(url)
    with open('Alice.txt', 'wb') as f:
        f.write(myfile.content)"""

    with open('Alice.txt', 'r') as f:
        texte = f.read()

    idx1 = sous_chaine(texte, "[Illustration]\n\nCHAPITRE PREMIER.\n\nAU FOND DU TERRIER.")
    idx2 = texte.find("[Illustration]\n\nCHAPITRE PREMIER.\n\nAU FOND DU TERRIER.")
    assert(idx1 == idx2)
    texte = texte[idx1:]
    
    cpt1 = count_sous_chaine(texte, "Alice")
    cpt2 = texte.count("Alice")
    assert(cpt1 == cpt2)
    
    idx_alice = idx_sous_chaine(texte, "Alice")
    
    rep1 = my_replace(texte, "Alice", "Pam Pam")
    rep2 = my_replace_2(texte, "Alice", "Pam Pam")
    texte2 = texte.replace("Alice", "Pam Pam")
    assert(rep1 == texte2)
    assert(rep2 == texte2)
    
    
    