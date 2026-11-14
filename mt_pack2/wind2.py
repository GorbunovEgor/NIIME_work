"""
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from tkinter import messagebox
"""

from .get_source_path import *
from .wind3 import *


def create_win2(Min,Max,cp,nnc,zzz,zz,root,xx,yy,sheet,point,a,nn,N,book,name_f):
    
    win = Toplevel()
    win.title("Параметры_графика")
    win.geometry('630x200')
    win.grab_set()
    win.iconbitmap(dat_file_ico)
    win.resizable(width=False , height=False)
    
    img2 = PhotoImage(file=dat_file_gr_png2)
    l_logo2 = Label(win, image=img2)
    l_logo2.image = img2
    l_logo2.pack()
    
    
    
    lfw = LabelFrame(win,text="Общие_параметры_графика",bg = "gray",padx=20 ,pady=20)
    lfw.place(x=10,y=10)
    
    lfw2 = LabelFrame(win,text="Параметры_2_графика",bg = "gray",padx=20 ,pady=20)
    lfw2.place(x=300,y=10)
    
    
    l = Label(lfw, text = ("               min =") , font='Arial 13' ,fg="#CCFFFF", bg = "#940099" ).grid(row=0,column=0)
    
    l_1 = Label(lfw, text = ("               max =") , font='Arial 13' ,fg="#CCFFFF", bg = "#940099" ).grid(row=1,column=0)
    #place(x=10 , y=40)
    l_2 = Label(lfw, text = ("counter_slize = ") , font='Arial 13' ,fg="#CCFFFF", bg = "#940099" ).grid(row=2,column=0)
    #place(x=10 , y=70)


    min = Entry(lfw)
    min.grid(row=0,column=1)
    #place(x=130 , y=10)
    min.insert(END,Min)

    max = Entry(lfw)
    max.grid(row=1,column=1)
    #place(x=130 , y=40)
    max.insert(END,Max)

    counter_plot = Entry(lfw)
    counter_plot.grid(row=2,column=1)
    #place(x=130 , y=70)
    counter_plot.insert(END,cp)
    
    
    l1 = Label(lfw2, text = ("С этой точки ") , font='Arial 13' ,fg="#CCFFFF", bg = "#940099" ).grid(row=0,column=0)
    l1 = Label(lfw2, text = ("До этой точки") , font='Arial 13' ,fg="#CCFFFF", bg = "#940099" ).grid(row=1,column=0)
    
    pre_x = Combobox(lfw2,values=(nnc),justify=CENTER,state="readonly")
    pre_x.current(0)
    #pre_x.place(x=300 , y=10)
    pre_x.grid(row=0,column=1)
    post_x = Combobox(lfw2,values=(nnc),justify=CENTER,state="readonly")
    post_x.current(2)
    #post_x.place(x=300 , y=40)
    post_x.grid(row=1,column=1)
    
    var = IntVar(value=0)
    
    
    rb10 = Radiobutton(lfw2,text="По пределу точек      ",variable=var,value=0)
    rb10.grid(row=2,column=1)

    rb11 = Radiobutton(lfw2,text="По выбранным точ.  ",variable=var,value=1)
    rb11.grid(row=3,column=1)
    
    rb12 = Radiobutton(lfw2,text="По шаблонам точек  ",variable=var,value=2)
    rb12.grid(row=4,column=1)
    
    def click_2():
        create_win3(win,zz,zzz,counter_plot,pre_x,post_x,root,var,xx,yy,sheet,nnc,point,a,nn,min,max,N,book,name_f)
    
    btn_0 = Button(win, text = "Назначить" , command = click_2 , font='Arial 13' ,fg="#CCFFFF", bg = "#940099" , activebackground = "#FF0099")
    btn_0.place(x=200 , y=150)