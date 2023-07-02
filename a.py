import numpy as np

def ssh(n,v,w):     # The matrix for the Hamiltonian of the Su-Schrieffer–Heeger (SSH) model n:the number of unit cells (even number) v:intracell hopping w:intercell hopping

    lm=[[0]*n for _ in range(n)]
    
    lm[0][1]=v

    for i in range(1,n-1):
        if i%2==1:
            lm[i][i-1]=v
            lm[i][i+1]=w
                
        else:
            lm[i][i-1]=w
            lm[i][i+1]=v
        
    lm[n-1][n-2]=v

    return(lm)
