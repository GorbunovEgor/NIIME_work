
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from .pars_file import *

def create_garf_0(xx, yy, zzz, s,point,sheet):
    fig, ax = plt.subplots(facecolor = "#eee")
    fig.suptitle("Скорость травления")
    ax.set_xlabel("X,мм")
    ax.set_ylabel("Y,мм")
    
    c2 = ax.tricontourf(xx, yy, zzz, s , cmap = "bwr")
    plt.colorbar(c2)
    if point.get() == 0:
        plt.title("                                                                                        ER, мкм/мин")
    else:
        plt.title("                                                                                        ER, A/мин")

    angle = np.linspace( 0 , 2 * np.pi , 150 ) 
    radius = 150
    x = radius * np.cos( angle ) 
    y = radius * np.sin( angle ) 
    ax.plot( x, y ,"black") 
    ax.set_aspect( 1 )
    
    plt.savefig("myplot.png", dpi = 70)
    
    safe_graf(sheet)
    
    #img = openpyxl.drawing.image.Image('myplot.png')
    #sheet.add_image(img, "E8")
    
    
    plt.show(block=False)
    plt.close("all")
    
    
    
def create_garf_1(xx2, yy2, zz2, s,point,sheet,book,name_f,M):
    fig, ax = plt.subplots(facecolor = "#eee")
                        
    #ax = fig.add_subplot()
    #M = str()
    #M = ("В_пределах_",st + 1,"-",en)

    fig.suptitle(M)

    ax.set_xlabel("X,мм")
    ax.set_ylabel("Y,мм")
        
    try:
        c2 = ax.tricontourf(xx2, yy2, zz2, s , cmap = "bwr")
    except ValueError:
        messagebox.showwarning("Warning","При выставлении меньше двух точек в диапозоне,создаст пустой график!")
        return(0)

    angle = np.linspace( 0 , 2 * np.pi , 150 ) 
    radius = 150
    x = radius * np.cos( angle ) 
    y = radius * np.sin( angle ) 
    ax.plot( x, y ,"black") 
    ax.set_aspect( 1 )
    
    plt.colorbar(c2)
    
    if point.get() == 0:
        plt.title("                                                                                        ER, мкм/мин")
    else:
        plt.title("                                                                                        ER, A/мин")

    
    plt.savefig("myplot2.png", dpi = 70)
    
    safe_graf_two(sheet)
    
    
    plt.show(block=False)
    plt.close("all")

    close_file(book,name_f)


def create_garf_2(x_x, y_y, z_z, s,point,W,sheet,book,name_f):
    fig, ax = plt.subplots( facecolor = "#eee")
    #ax = fig.add_subplot()
    fig.suptitle(W)



    plt.xlabel("X,мм")
    plt.ylabel("Y,мм")

    c2 = ax.tricontourf(x_x, y_y, z_z, s , cmap = "bwr")
    
    
    angle = np.linspace( 0 , 2 * np.pi , 150 ) 
    radius = 150
    x = radius * np.cos( angle ) 
    y = radius * np.sin( angle ) 
    ax.plot( x, y ,"black") 
    ax.set_aspect( 1 )
    
    plt.colorbar(c2)
    
    if point.get() == 0:
        plt.title("                                                                                        ER, мкм/мин")
    else:
        plt.title("                                                                                        ER, A/мин")

    
    plt.savefig("myplot2.png", dpi = 70)
    
    safe_graf_two(sheet)
    
    plt.show(block=False)
    plt.close("all")
    
    close_file(book,name_f)