import numpy as np


def jacobi(matriz,b,tolerancia,iteraciones):
    n=len(matriz)
    x=np.zeros(n)
    error=[]
    k=0
    while(k<iteraciones):
        k=k+1
        error.clear()
        xanterior = x.copy()
        for i in range(0,n):
            sumatoria = 0
            for j in range(0,n):
                if(i!=j):
                    sumatoria=sumatoria+matriz[i,j]*xanterior[j]
            x[i]=(b[i]-sumatoria)/matriz[i,i]
            dif = abs(x[i]-xanterior[i])
            error.append(dif)
        if all(i<=tolerancia for i in error)==True:
            break
    return x
        

def seidel(matriz, b, tolerancia, iteraciones):
    n = len(matriz)
    x = np.zeros(n)
    error = []
    k = 0
    while(k < iteraciones):
        k=k+1
        error.clear()
        xanterior = x.copy()
        for i in range(0,n):
            sumatoria = 0
            for j in range(0, n):
                if(j<i):
                    sumatoria = sumatoria+matriz[i, j]*x[j]
                if(j>i):
                    sumatoria = sumatoria+matriz[i, j]*xanterior[j]
            x[i] = (b[i]-sumatoria)/matriz[i, i]
            dif = abs(x[i]-xanterior[i])
            error.append(dif)
        if all(i <= tolerancia for i in error) == True:
            break
    return x
                

def diagonalDominante(matriz,b):
    n=len(matriz)
    temp=np.zeros(n)
    temp1=0
    k=0
    for i in range(0,n-1):
        for j in range(i+1,n):
            sumatoria = 0
            for k in range(0,n):
                if(i != k):
                    sumatoria = abs(sumatoria)+abs(matriz[i, k])
            if(abs(matriz[i, i]) < abs(sumatoria)):
                temp=matriz[j,:].copy()
                matriz[j,:]=matriz[i,:].copy()
                matriz[i,:]=temp.copy()
                temp1=b[j]
                b[j]=b[i]
                b[i]=temp1
            else: 
                break

    for i in range(0,n):
        sumatoria1=0
        for j in range(0,n):
            if(i != j):
                sumatoria1 = sumatoria1+abs(matriz[i,j])
        if(abs(matriz[i, i]) < abs(sumatoria1)):
            k=-1
            break
    return matriz,b,k



