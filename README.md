# 1-D-topological-insulator
make 1-d topological insulator
</br></br>
### ssh(n,v,w)
The matrix for the Hamiltonian of the Su-Schrieffer–Heeger (SSH) model

The cell is consist of two sites(red and blue)

n:the number of sites (even number) v:intracell hopping w:intercell hopping 

![zczcvz](https://github.com/vadfq/1-D-topological-insulator/assets/138349650/3d49da0e-ae8a-4f76-8152-703bea3c39db)

</br></br>

### defect(n,d1,d2)

n: the number of sites (odd number) d1: first hopping in chain d2: second hopping in chain

![zxcfaf](https://github.com/vadfq/1-D-topological-insulator/assets/138349650/a6a48b5a-4174-4646-8146-34749d6ce17f)

</br></br>
### sorted_eigenvalue()

draw graph of sorted eigenvalues


![ㅁㄴㅇㄹㅋㅍㅊ](https://github.com/vadfq/1-D-topological-insulator/assets/138349650/cc900908-736c-47dd-9dcf-0a7391b450fc)


### state_all(w,h)     

draw all eigenstates (10 graphs per row) w: width of canvas h: height of canvas</br>
eigenstae number</br>
[&nbsp; 0  &nbsp;1 &nbsp; 2 &nbsp; 3 &nbsp; 4&nbsp;  5 &nbsp; 6&nbsp; 7 &nbsp;  8&nbsp;  9]</br>
[10 11 12 13 14 15 16 17 18 19]</br>
       &nbsp;&nbsp;      &nbsp; ...</br>
        &nbsp;&nbsp; &nbsp;     ...</br>
         &nbsp;&nbsp; &nbsp;    ...</br>

         </br></br>
x tick means site number
</br></br>

![zcmkovz](https://github.com/vadfq/1-D-topological-insulator/assets/138349650/12436a41-cdc8-4442-93cc-e0000ff68807)
</br></br>
### state(o)
draw o+1th eigenstate   (you can know eigenstate number by refering output of state_all(w,h))
</br></br>
x tick means site number
</br></br>
![ioqjoif](https://github.com/vadfq/1-D-topological-insulator/assets/138349650/d0b9c8bd-faec-45ce-b09b-151718779daf)
</br></br>

### pro(b,t)      
draw absolute value squared of amplitude change over time or space   </br>
b:initial state <(n*1) mp.matrix type>  t:range to draw graph (if t=500 : 0 to 50)
</br></br>y tick means site number</br></br>
In this picture, initial state is b=mp.matrix([0,0,0,0,0,0,1,0,0,0,0,0,0])
![awqerar](https://github.com/vadfq/1-D-topological-insulator/assets/138349650/4a9c67a6-ce1c-4ac4-9026-83481131a6c3)
