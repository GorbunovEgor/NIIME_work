import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#import matplotlib
#matplotlib.rcParams["toolbar"] = "toolmanager"
from matplotlib.backend_tools import ToolBase
from matplotlib.figure import Figure  
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

from tkinter import *

from scren_shot import take_screenshot

#def take_screenshot1():
#    pass

def graf_test(X1,Y1,Z1,titl,s,p,root,frame,imag,Label,tab1):
    Rad = list()
    for xr, yr in zip(X1,Y1):
        Rad.append(np.sqrt((xr**2)+(yr**2)))
    
    def take_screenshot1():
        take_screenshot(root,Label,tab1)
    
    
    
    fig = Figure( dpi=93)
    
    #x_2d=[-200,200]
    #y_2d=[-200,200]
# zs=0
    #ax.plot(x_2d, y_2d,label='Sine Wave')
    #fig, ax = fig.subplots(111,facecolor = "#eee")coolvarm
    #fig, 
    g1 = 0 #ax.grid(True)
    g2 = ax = fig.subplots()                    
    g3 = fig.suptitle(f"                                                                          {(titl[p])}")
    g4 = ax.set_xlabel("X,мм")
    g5 = ax.set_ylabel("Y,мм")
    #ax.grid(True)
    #plt.title("hi")
    #ax.title()
    #fig.suptitle("Скорость травления")
                        
    c2 = ax.tricontourf(X1, Y1, Z1, s , cmap = "coolwarm")
    c= fig.colorbar(c2,ax=ax,label=(titl[p]))
    #X2 = min(X)**2
    #Y2 = min(Y)**2
    cir1=angle = np.linspace( 0 , 2 * np.pi , 150 ) 
    cir2=radius = max(Rad)
    #max(X1)
    #np.sqrt(Y2+X2)
    #150
    cir3=x = radius * np.cos( angle ) 
    cir4=y = radius * np.sin( angle ) 
    cir5=ax.plot( x, y ,"black") 
    cir6=ax.set_aspect( 1 )
    
        
        
        
    #tm = fig.canvas.manager.toolmanager
    #tm.add_tool("newtool", NewTool)
    #fig.canvas.manager.toolbar.add_tool(tm.get_tool("newtool"), "toolgroup")
    #x_2d=[-200,200]
    #y_2d=[-200,200]
# zs=0
    #ax.plot(x_2d, y_2d,label='Sine Wave')
    #plt.show

    point1 = 0

    canvas = FigureCanvasTkAgg(fig, root)  
    canvas.draw()  
    toolbar = NavigationToolbar2Tk(canvas, frame,pack_toolbar=False)
                                   #root)  
    #toolbar.update()  
    toolbar.place(x=0, y=0, width=950, height=45)
    canvas.get_tk_widget().place(x=0,y=0)
    
    
    #b = tix.Balloon(frame)  
    #for sub in b.subwidgets_all():
    #    print(sub)
        #if sub == ("."and".!frame.!balloon.f1" and ".!frame.!balloon.f1.lab"and ".!frame.!balloon.f2"and".!frame.!balloon.f2.message"):  
    #    sub.config(bg='white',width = 12,height=1,padx=-1)
    
    
    
    
    sev = Button(frame,image=imag, command = take_screenshot1 , relief=FLAT,borderwidth=1)
    sev.place(x=225,y=7)
    #b.bind_widget(sev, balloonmsg="Save graf in BUF")
    #myTip = Hovertip(sev,'Save graf in BUF')
    #sev2=Hovertip(sev,'Save graf in BUF')
    
    def focus_in(e = None):
        sev.configure(relief=GROOVE)

    def focus_out(e = None):
        sev.configure(relief=FLAT)
        
    sev.bind('<Enter>', focus_in) # При входе курсора в область кнопки выполняем focus_in
    sev.bind('<Leave>', focus_out)
    
    return fig
    

    

    