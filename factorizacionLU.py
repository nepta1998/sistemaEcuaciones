import numpy as np


def factorizacion(matriz):
    n=len(matriz)
    L = np.zeros([n, n])
    U = matriz
    for k in range(0,n):
        for r in range(0,n):
            if(k==r):
                L[k,r]=1
            if(k<r):
                factor=(matriz[r,k]/matriz[k,k])
                L[r,k]=factor
                for c in range(0,n):
                    U[r,c] = U[r,c]-(factor*U[k, c])   
    return L,U


def factorizacion2(matriz):
    n = len(matriz)
    L = np.zeros([n, n])
    U = np.zeros([n, n])
    for k in range(0, n):
        L[k,k]=1
        
        for j in range(k, n):
            U[k, j] = matriz[k, j]-np.dot(L[k, 0:k], U[0:k, j])
        for i in range(k+1, n):
            L[i, k] = (matriz[i, k]-np.dot(L[i,0:k], U[0:k,k]))/U[k,k]
    return L, U

def solucionLU(L,b,U):
    n = len(L)
    for k in range(1,n):
        b[k]=b[k]-np.dot(L[k,0:k],b[0:k])
    
    b[n-1]=b[n-1]/U[n-1,n-1]
    for k in range(n-2, -1, -1):
        b[k] = (b[k]-np.dot(U[k,k+1:n], b[k+1:n]))/U[k, k]
    return b

def determinante(matriz):
    sign, det = np.linalg.slogdet(matriz)
    det = sign*np.exp(det)
    return det




