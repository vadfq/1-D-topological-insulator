import numpy as np

def ssh(n,v,w):     # Hamiltonian matrix of The Su-Schrieffer–Heeger (SSH) model n:전체 격자 수(짝수) v:intracell hopping w:intercell hopping

    lm=[]

    l1=[]
    l1.append(0)
    l1.append(v)
    for i in range(n-2):
        l1.append(0)

    lm.append(l1)

    l1=[]

    for i in range(n-2):
        for j in range(n):
            if i%2==0:
                if j==i:
                    l1.append(v)
                elif j==i+2:
                    l1.append(w)
                else:
                    l1.append(0)
            else:
                if j==i:
                    l1.append(w)
                elif j==i+2:
                    l1.append(v)
                else:
                    l1.append(0)
        lm.append(l1)
        l1=[]

    for i in range(n-2):
        l1.append(0)
    l1.append(v)
    l1.append(0)

    lm.append(l1)

    return(lm)
