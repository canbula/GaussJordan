import numpy as np

def GaussJordan(x,y):
    m,n=x.shape
    augmat=np.zeros(shape=(m,n+1))
    augmat[:m,:n]=x
    augmat[:,m]=y
    np.set_printoptions(precision=2,suppress=True)
    print('# Original augmented matrix')
    print(augmat)
    for i in range(0,m-1):
        for j in range(i+1,m):
            k=(-1)*augmat[j,i]/augmat[i,i]
            temprow=augmat[i,:]*k
            print('# Use line %2i for line %2i'%(i+1,j+1))
            print('k=%.2f'%k,'*',augmat[i,:],'=',temprow)
            augmat[j,:]=augmat[j,:]+temprow
            print(augmat)
    for i in range(m-1,0,-1):
        for j in range(i-1,-1,-1):
            k=(-1)*augmat[j,i]/augmat[i,i]
            temprow=augmat[i,:]*k
            print('# Use line %2i for line %2i'%(i+1,j+1))
            print('k=%.2f'%k,'*',augmat[i,:],'=',temprow)
            augmat[j,:]=augmat[j,:]+temprow
            print(augmat)
    for i in range(0,m):
        augmat[i,:]=augmat[i,:]/augmat[i,i]
    print('# Normalize the rows')
    print(augmat)
    return augmat[:,n]

x=np.array([[5,15,25],[15,25,55],[25,55,225]])
y=np.array([15,25,225])
b=GaussJordan(x,y)
print(b)