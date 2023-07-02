import numpy as np

def ssh(n,v,w):     # The matrix for the Hamiltonian of the Su-Schrieffer–Heeger (SSH) model n:the number of sites (even number) v:intracell hopping w:intercell hopping
                                                                                            # Each unit cell hosting two sites, so total number of sites is even number
    lm=[[0]*n for _ in range(n)]
    
    lm[0][1]=v      # 1st row

    for i in range(1,n-1):   # 2nd~(n-1)th row
        if i%2==1:
            lm[i][i-1]=v
            lm[i][i+1]=w
                
        else:
            lm[i][i-1]=w
            lm[i][i+1]=v
        
    lm[n-1][n-2]=v  # nth row

    return(lm)

def defect(n,d1,d2):     # n: the number of sites (odd number) d1: first hopping in chain d2: second hopping in chain
    
    lm=[[0]*n for _ in range(n)]

    lm[0][1]=d1                # 1st row

    for i in range(1,(n-1)//2): # 2nd~(middle-1)th row
        if i%2==1:
            lm[i][i-1]=d1
            lm[i][i+1]=d2
                
        else:
            lm[i][i-1]=d2
            lm[i][i+1]=d1

    
    if n%4==1:                                                      # middle row
        lm[(n-1)//2][(n-1)//2-1]=lm[(n-1)//2][(n-1)//2+1]=d2
    elif n%4==3:
        lm[(n-1)//2][(n-1)//2-1]=lm[(n-1)//2][(n-1)//2+1]=d1
        
    for i in range((n-1)//2+1,n-1):     # (middle+1)~(n-1)th row
        if i%2==1:
            lm[i][i-1]=d2
            lm[i][i+1]=d1
                
        else:
            lm[i][i-1]=d1
            lm[i][i+1]=d2

    lm[n-1][n-2]=d1                 # nth row

    return lm
