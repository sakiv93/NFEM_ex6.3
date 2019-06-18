import numpy as np
import matplotlib.pyplot as plt
import math

def G_Subroutine(y):   #y should be np array of ([[],[]])
    y1=y[0,0]
    y2=y[1,0] 
    return np.array([[4*y1*y1+y2*y2+2*y1*y2-y2-2],[2*y1*y1+y2*y2+3*y1*y2-3]])

def Kt_Subroutine(y):
    y1=y[0,0]
    y2=y[1,0]
    return np.array([[8*y1+2*y2,2*y2+2*y1-1],[4*y1+3*y2,2*y2+3*y1]])


def newton_raphson(y):
    k=1
    while 1:
        Kt_sub=Kt_Subroutine(y)
        g_sub=G_Subroutine(y)
        delta_y=-np.matmul(np.linalg.inv(Kt_sub),g_sub)
        y=y+delta_y
        k=k+1
        print(y)
        if (np.linalg.norm(g_sub)<=1e-6 or np.linalg.norm(delta_y)<=1e-6) and k>=5:
            break
    return y

y=np.array([[0.4],[0.9]])
y_converged=newton_raphson(y)
print(y_converged)

