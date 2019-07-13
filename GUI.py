from tkinter import *
import factorizacionLU as fac
from tkinter import messagebox
import gauss as g
import numpy as np
#'%.2E'%
def crearSistemaE(n,ventana):
    coordenadasX=10
    coordenadasY=10
    y.clear()
    for i in range(0,n):
        
        for j in range(0, n+1):
            if(j<n):
                entrada=StringVar()
                Entry(ventana, width=10, textvariable=entrada).place(x=coordenadasX, y=coordenadasY)
                y.append(entrada)
                y[len(y)-1].set(str(0.0))
                coordenadasX=coordenadasX+60
                Label(ventana, text='X'+str(j+1), font=("Futura Md BT", 12), bg='yellow').place(x=coordenadasX,y=coordenadasY)
                coordenadasX = coordenadasX+30
            else:
                entrada = StringVar()
                coordenadasX = coordenadasX+10
                Label(ventana, text='=', font=("Futura Md BT", 12),bg='yellow').place(x=coordenadasX, y=coordenadasY)
                coordenadasX = coordenadasX+20
                Entry(ventana, width=10, textvariable=entrada).place(x=coordenadasX, y=coordenadasY)
                y.append(entrada)
                y[len(y)-1].set(str(0.0))
        coordenadasY=coordenadasY+40
        coordenadasX = 10
    coordenadasY=coordenadasY+5
    Button(ventana, text="Factorizacion LU", command=VResultados,font=("Futura Md BT", 12), fg='white', bg="black", width=(20+(n-1)*10)).place(x=coordenadasX, y=coordenadasY)
    coordenadasY = coordenadasY+40
    Button(ventana, text="Metodo Jacobi", command=ventana3,font=("Futura Md BT", 12), fg='white', bg="black", width=(20+(n-1)*10)).place(x=coordenadasX, y=coordenadasY)
    coordenadasY = coordenadasY+40
    Button(ventana, text="Metodo Gauss-Seidel",command=ventana4,font=("Futura Md BT", 12), fg='white', bg="black", width=(20+(n-1)*10)).place(x=coordenadasX, y=coordenadasY)
                
def ventana2():
    try:
        n = int(entry.get())
        if(n>0):
            ventana2 = Toplevel(ventana, bg="yellow")
            ventana2.title("Ecuaciones")
            ventana2.geometry(str(210+(n-1)*90)+'x'+str(175+(n-1)*40)+'+600+100')
            crearSistemaE(n, ventana2)
        else:
            messagebox.showinfo("Error", "El valor ingresado no es permitido")
    except:
        messagebox.showinfo("Error", "El campo no esta lleno o el valor no es permitido")



def generarMatriz(n):
    A = np.zeros([n, n])
    b=[]
    k=0
    for i in range(0, n):
        for j in range(0,n+1):
            if(j<n):
                A[i,j]=float(y[k].get())
                k = k+1
            else:
                b.append(float(y[k].get()))
                k = k+1
    return A,b
    

def VResultados():
    
    n = int(entry.get())
    try:
        A, b = generarMatriz(n)
        if(fac.determinante(A)==0):
            messagebox.showinfo("Error", "El sistema no tiene o tiene infinitas soluciones")
        else:
            #L, U = fac.factorizacion(A)
            L, U =fac.factorizacion2(A)
            w = fac.solucionLU(L, b, U)
            ventanaR = Toplevel(ventana, bg="#00FF9E")
            ventanaR.title("Factorizacion LU")
            ventanaR.geometry(str(240+(n-1)*220)+'x'+str(180+(n-1)*60)+'+610+10')
            Label(ventanaR, text="Matriz L", font=("Futura Md BT", 12),bg="#00FF9E").place(x=round(n*45/2), y=0)
            Label(ventanaR, text="Matriz U", font=("Futura Md BT", 12),bg="#00FF9E").place(x=(round(n*140)), y=0)

            coordenadasX = 10
            coordenadasY = 30
            for i in range(0, n):
                for j in range(0, n):
                    Label(ventanaR, text=str(round(L[i, j], 3)), font=("Futura Md BT", 12), fg='black', bg="#00FF9E").place(x=coordenadasX, y=coordenadasY)
                    coordenadasX = coordenadasX+90
                    if(j == n-1):
                        coordenadasX = coordenadasX+60
                        for k in range(0, n):
                            Label(ventanaR, text=str(round(U[i, k], 3)), font=("Futura Md BT", 12), bg="#00FF9E", fg='black').place(x=coordenadasX, y=coordenadasY)
                            coordenadasX = coordenadasX+90
                coordenadasX = 10
                coordenadasY = coordenadasY+40

            coordenadasY = coordenadasY+30
            Label(ventanaR, text="Resultados:", font=("Futura Md BT", 12),fg='black', bg="#00FF9E").place(x=coordenadasX, y=coordenadasY)
            coordenadasY = coordenadasY+30
            for l in range(0, n):
                Label(ventanaR, text="X"+str(l+1)+"=", font=("Futura Md BT", 12),fg='black', bg="#00FF9E").place(x=coordenadasX, y=coordenadasY)
                coordenadasX = coordenadasX+30
                Label(ventanaR, text=str(round(w[l], 3)), font=("Futura Md BT", 12), fg='black', bg="#00FF9E").place(x=coordenadasX, y=coordenadasY)
                coordenadasX = coordenadasX+80
    except:
        messagebox.showinfo("Error", "valores no permitidos")


def ventana3():
    def resultado():
        try:
            w=g.jacobi(A,b,float(entrada2.get()),int(entrada1.get()))
            coordenadasX = 10
            for i in range(0,n):
                Label(ventana3, text="X"+str(i+1)+"=", font=("Futura Md BT", 12),fg='black', bg="#00FF9E").place(x=coordenadasX, y=140)
                coordenadasX = coordenadasX+30
                Label(ventana3, text=str(round(w[i], 3)), font=("Futura Md BT", 12), fg='black', bg="#00FF9E").place(x=coordenadasX, y=140)
                coordenadasX = coordenadasX+80
        except:
            messagebox.showinfo("Error", "El campo no esta lleno o el valor no es permitido")
    n = int(entry.get())
    try:
        A, b = generarMatriz(n)
        if(fac.determinante(A) == 0):
            messagebox.showinfo("Error", "El sistema no tiene o tiene infinitas soluciones")
        else:
            A, b, k = g.diagonalDominante(A, b)
            if(k != -1):
                ventana3 = Toplevel(ventana, bg="#00FF9E")
                ventana3.title("Metodo Jacobi")
                ventana3.geometry(str(210+(n-1)*100)+'x' +str(190)+'+600+100')
                entrada1 = StringVar()
                entrada2 = StringVar()
                Label(ventana3, text='Iteraciones:', font=("Futura Md BT", 13),bg="#00FF9E").place(x=10, y=10)
                Entry(ventana3, width=10, textvariable=entrada1).place(x=110, y=10)
                Label(ventana3, text='Tolerancia:', font=("Futura Md BT", 13),bg="#00FF9E").place(x=10, y=50)
                Entry(ventana3, width=10, textvariable=entrada2).place(x=110, y=50)
                Button(ventana3, text="Calcular", command=resultado,font=("Futura Md BT", 14),bg="#05BA75").place(x=10, y=90)
            else:
                messagebox.showinfo("Error", "La matriz no es diagonal dominate")
    except:
        messagebox.showinfo("Error", "El campo no esta lleno o el valor no es permitido")


def ventana4():
    def resultado():
        try:
            w = g.seidel(A, b, float(entrada2.get()), int(entrada1.get()))
            coordenadasX = 10
            for i in range(0, n):
                Label(ventana4, text="X"+str(i+1)+"=", font=("Futura Md BT", 12),fg='black', bg="#00FF9E").place(x=coordenadasX, y=140)
                coordenadasX = coordenadasX+30
                Label(ventana4, text=str(round(w[i], 3)), font=("Futura Md BT", 12), fg='black', bg="#00FF9E").place(x=coordenadasX, y=140)
                coordenadasX = coordenadasX+80
        except:
            messagebox.showinfo("Error", "El campo no esta lleno o el valor no es permitido")
    n = int(entry.get())
    try:
        A, b = generarMatriz(n)
        if(fac.determinante(A) == 0):
            messagebox.showinfo("Error", "El sistema no tiene o tiene infinitas soluciones")
        else:
            A, b, k = g.diagonalDominante(A, b)
            if(k!=-1):
                ventana4 = Toplevel(ventana, bg="#00FF9E")
                ventana4.title("Metodo Gauss-Seidel")
                ventana4.geometry(str(210+(n-1)*100)+'x' +str(190)+'+600+100')
                entrada1 = StringVar()
                entrada2 = StringVar()
                Label(ventana4, text='Iteraciones:', font=("Futura Md BT", 13), bg="#00FF9E").place(x=10, y=10)
                Entry(ventana4, width=10, textvariable=entrada1).place(x=110, y=10)
                Label(ventana4, text='Tolerancia:', font=("Futura Md BT", 13), bg="#00FF9E").place(x=10, y=50)
                Entry(ventana4, width=10, textvariable=entrada2).place(x=110, y=50)
                Button(ventana4, text="Calcular", command=resultado, font=("Futura Md BT", 14), bg="#05BA75").place(x=10, y=90)
            else:
               messagebox.showinfo("Error", "La matriz no es diagonal dominate")
    except:
        messagebox.showinfo("Error", "El campo no esta lleno o el valor no es permitido")



ventana = Tk()

y = []
ventana.geometry('400x330+100+100')
ventana.configure(background='yellow')
ventana.title("Calculo De Sistemas De Ecuaciones")
titulo=Label(ventana,text='SISTEMA DE ECUACIONES',font=("Forte",20,"bold"),bg='yellow')
titulo.pack()
imagen = PhotoImage(file="sistema.png")

Label(ventana, image=imagen, bg="black").pack(pady=5)

Label(ventana, text='Filas,Columnas:', font=("Futura Md BT", 14), bg='yellow').pack(fill=X)
entry = Entry(ventana)
entry.bind("<Return>", (lambda event: ventana2()))
entry.pack(fill=X, padx=5, pady=5, ipadx=2, ipady=5)


Button(ventana, text="Generar Sistema", command=ventana2, font=("Futura Md BT", 14), bg="black", width=34,fg="white").pack(fill=X, padx=5, pady=5, ipadx=2, ipady=5)
ventana.mainloop()
