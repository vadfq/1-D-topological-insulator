from mpmath import mp
import matplotlib.pyplot as plt
import matplotlib.cm as ccm
import copy

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


class wa:                                #integrated class for SSH and defect
  def __init__(self,n,d1,d2):            # n: the number of sites   d1: first hopping in chain   d2: second hopping in chain
    self.n=n
    self.d1=d1
    self.d2=d2

    if n%2==0:                           # SSH
      self.l=ssh(n,d1,d2)
      print("{0} SSH array, intracell hopping : {1}, intercell hopping : {2}".format(n,d1,d2))
      
    else:                                # defect
      self.l=defect(n,d1,d2)
      print("{0} defect array, first hopping : {1}, second hopping : {2}".format(n,d1,d2))
      
    self.m=mp.matrix(self.l)
    self.v,self.s=mp.eig(self.m)
  
  def sorted_eigenvalue(self):           # draw graph of sorted eigenvalues
    nn=range(1,self.n+1)
    plt.xlabel('Sorted state index',fontdict={'size':16})
    plt.ylabel('Eigenvalue',fontdict={'size':16})
    plt.tick_params(axis='both',labelsize='16')
    plt.plot(nn,sorted(self.v),'b.')
    plt.show()

  def state_all(self,w,h):           #draw all eigenstates (10 graphs per row) w: width of canvas h: height of canvas
    if self.n%10==0:
      x=self.n//10
    else:
      x=self.n//10+1
    fig,axes=plt.subplots(nrows=x,ncols=10,figsize=(w,h))    #size of canvas w*h, number of rows:x, number of columns:10
    
    if x==1:                      #number of rows : 1
      for col in range(self.n):
        ax=axes[col]
        nn=range(1,self.n+1)
        #ax.set_xlabel('E = '+str(self.v[col]),fontsize=5)
        ax.bar(nn,self.s[:,col])                
        ax.tick_params(axis='x',which='both',bottom=False,top=False, labelbottom=False)
        plt.setp(ax.get_yticklabels(),fontsize=5)
      plt.tight_layout()
      plt.show()

    else:                        #number of rows : more than 1
     for row in range(x):
        for col in range(10):
            idx = row*10+col

            if idx < self.n:
                ax=axes[row][col]
                nn=range(1,self.n+1)
                #ax.set_xlabel('E = '+str(self.v[idx]),fontsize=5)
                ax.bar(nn,self.s[:,idx])                
                ax.tick_params(axis='x',which='both',bottom=False,top=False, labelbottom=False)
                plt.setp(ax.get_yticklabels(),fontsize=5)
     plt.tight_layout()
     plt.show()

  def state(self,o):          #draw o+1th state
    nn=range(1,self.n+1)
    #nn=list(range(1,n+1))
    plt.title('E = '+str(self.v[o]))
    plt.ylim([-0.65,0.65])                 #range of y axis   change for purpose   max [-1,1]
    plt.bar(nn,self.s[:,o])                #o+1th state
    plt.xlabel('Site number',fontdict={'size':16})
    plt.ylabel('Normalized amplitude',fontdict={'size':16})
    plt.tick_params(axis='both',labelsize='16')
    plt.show()

  def cc(self,b,x): #s:고유벡터 행렬(n*n)     b:initial state (n*1) mp.matrix    x: time or propagation length
    c=(self.s**-1)*b      #sc=b
    g=c.copy()
    for i in range(len(c)):
     g[i]=g[i]*mp.e**(mp.j*self.v[i]*x)  #e^(ikx)         time : change e^(-ikx)
  
    d=self.s*g          #d=sg

    for i in range(len(c)):
     d[i]=mp.fabs(d[i])**2  #absolute value squared
  
    return d      #파의 진행 후 진폭 분포

  def pro(self,b,t):                #draw absolute value squared of amplitude change over time or space   b:initial state (n*1) mp.matrix   t:range to draw graph (t=500 :  0 to 50)
    plt.figure(figsize=(30,10))
    for i in range(t):
       ll=self.cc(b,i/10)
       plt.scatter([i/10]*len(b),range(1,len(b)+1),c=ll,cmap='YlOrRd')
    cbar=plt.colorbar()
    cbar.set_label('Intensity',size=25)
    cbar.ax.tick_params(labelsize=25)
    plt.clim(0,1)
    plt.xlabel('x',fontdict={'size':25})
    plt.ylabel('site number',fontdict={'size':25})
    plt.tick_params(axis='both',labelsize='25')
    plt.show()
