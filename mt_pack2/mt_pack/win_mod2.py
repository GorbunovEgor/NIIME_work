import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from tkinter import messagebox

import sys
import os

import numpy as np

from .parsing_f import *
from .graf import *

def get_source_path(relative_path):
    if hasattr(sys,"_MEIPASS"):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path,relative_path)

dat_file_ico = get_source_path("1489187695-billingdatayencurrency_81853.ico")
#dat_file_gr_png5 = get_source_path("survey_clipboard_notes_icon_207103.png")

#photo = PhotoImage(file = dat_file_gr_png5)
                   #"survey_clipboard_notes_icon_207103.png")
#image = photo.subsample(21, 21)

#arrt = np.arange(0, 150,10)
"""
t = 0
z = 0 
p = 0 
c = 0
c2 = 0
point=0
point1 = 0
#test_p = 0
#test_p2 = 0
#test_s = 15

x_rb10 = 0
y_rb11 = 0

#test_X = 0
#test_Y =0
#test_en = 0
#test_en3 = 0
#test_t = 25

g1 = 0
g2 = 0
g3 = 0
g4 = 0
g5 = 0 
s = 15
Z1 = 0

cir1=0
cir2=0
cir3=0
cir4=0
cir5=0
cir6=0

var2 = 0
#en1 = 0
#en2 = 0
#en3 = 0
"""

def new_window(nf,imag):
    rnf_title = parf(nf)
    #rnf_title[0]
    rnf = rnf_title[0]
    rnf2 = rnf_title[1]
    titl = rnf_title[2]
    valt2 = rnf_title[3]
    
    def update(event):
        #event = None
        update_1(event,pre_x,pre_t,rb10_x,rb11_y,var,enabled,enabled2,enabled3,rnf,rnf2,pre_s,fig,valt2,titl
                 ,min_m,max_m,avg_m,std_m,unif_m)
        update_test(event)
            
    def update_two():
        #update_2(enabled,enabled2,enabled3)
        update_2(pre_x,pre_t,rb10_x,rb11_y,var,enabled,enabled2,enabled3,rnf,rnf2,pre_s,fig,valt2,titl
             ,min_m,max_m,avg_m,std_m,unif_m)
    
    root = Toplevel() 
    root.geometry('940x490')#x/y 
    root.configure(background="darkgray")
    #root.resizable(width=False , height=False)
    root.iconbitmap(dat_file_ico)
    #fig = Figure(figsize=(5, 4), dpi=100)  
    #ax = fig.add_subplot(111)  
    #ax.plot([1, 2, 3], [1, 2, 3])
          
    frame = Frame(root,background='lightgreen', width=939, height=150)
    #tk.Frame(root,background='lightgreen', width=939, height=150)
    frame.place(x=0,y=446)
    #label = tk.Label(frame,text = "Matplotlib + Tkinter")
    #label.config(font=("Courier,32"))
    #label.place(x=0,y=30)
    
    


    tab_control = ttk.Notebook(root,height=420,width=340)

    tab1 = ttk.Frame(tab_control)
    tab2 = ttk.Frame(tab_control)
    tab_control.add(tab1,text="Первая_вкладка")
    tab_control.add(tab2,text="Вторая_вкладка")
    
    
    l1_r = parf_two(nf,rnf2,titl)
    l1 = l1_r[0]
    r_set = l1_r[1]
    
    # Data Sources to create header list and row of data is over. 
    style = ttk.Style()

    style.theme_use("default")

    style.configure("Treeview",
        background="#D3D3D3",
        foreground="black",
        rowheight=25,
        fieldbackground="#D3D3D3")
        
        
    style.map("Treeview",
        background=[('selected',"#347083")])




    

    tree_farame = Frame(tab2)
    tree_farame.pack(pady=10)
    

    tree_scroll = Scrollbar(tree_farame,orient="vertical")
    tree_scroll.pack(side=RIGHT,fill=Y)


    tree_scroll2 = Scrollbar(tree_farame,orient="horizontal")
    tree_scroll2.pack(side=BOTTOM,fill=X)

    trv = ttk.Treeview(tree_farame,yscrollcommand=(tree_scroll2.set,tree_scroll.set),selectmode="extended")
    trv.pack() 
    tree_scroll2.config(command=trv.xview)
    trv.pack()
    tree_scroll.config(command=trv.yview)


    
    trv['height']=10 # Number of rows to display, default is 10
    trv['show'] = 'headings' 
    # Adding headers and columns using lists 
    trv["columns"] = l1
    # Defining headings, other option in tree
    # width of columns and alignment 
    for i in l1:
        print("i=",i)
        if i == None:
            i = 1
            trv.column(i, width = 100, anchor ='c')
            print(trv.column(i, width = 100, anchor ='c'))
            print("i=",i)
            # Headings of respective columns
            trv.heading(i, text =i)
            print(trv.heading(i, text =i))
            print("i=",i)
        else:
            trv.column(i, width = 100, anchor ='c')
            print(trv.column(i, width = 100, anchor ='c'))
            print("i=",i)
            # Headings of respective columns
            trv.heading(i, text =i)
            print(trv.heading(i, text =i))
            print("i=",i)


    trv.tag_configure("evenrow", background="white")
    trv.tag_configure("oddrow", background="lightgray")
            
    global count
    count = 0

    ## Adding data to treeview 
    for dt in r_set:  
        v=[r for r in dt] # creating a list from each row 
        print("v=",v)
        if v == []:
            break
        ## trv.insert("",'end',iid=v[0],values=v) # adding row
    #data=[1,'Alex','Four',45,'Male'] # sample data to insert 
    #trv.insert("",'end',iid=1,values=data)
        if count % 2 == 0:
            trv.insert("",'end',iid=v[0],values=v,tags=('evenrow'))
        else:
            trv.insert("",'end',iid=v[0],values=v, tags=('oddrow'))
        count += 1





    lb2 = Label(tab1,text="Вторая_вкладка")
    lb2.grid(column=0,row=0,padx=150,pady=197)
    
    
    

    indx=0
    indx2=0
    #for i in titl:
    #    i2 = i
    #    if (i2 != "x(mm)") or (i2 != "X"):
    #        print("i2=",i2)
    #        indx += 1
    #    else:
    #        break

    # indx = titl.index(('x(mm)') or ("X"))
    try:
        indx = titl.index('x(mm)')
    except ValueError:
        indx = 0
    try:
        indx2 = titl.index("X")
    except ValueError:
        indx2 = 0  
        
    if indx2 > indx:
        indx = indx2  

    indy=0
    indy2 =0 
    #for i in titl:
    #    i2 = i
    #    if (i2 != "y(mm)") or (i2 != "Y"):
    #        print("i2=",i2)
    #        indy += 1
    #    else:
    #        break
    try:
        indy = titl.index('y(mm)')
    except ValueError:
        indy = 1
    try:
        indy2 = titl.index("Y")
    except ValueError:
        indy2 = 1

    if indy2 > indy:
        indy = indy2     
    
    print("indx=",indx)
    print("indy=",indy)
    
    X1=list()
    Y1=list()
    Z1=list()
    
    
    if rnf2 == 1:
        valtrx = list(valt2[indx])
        valtry = list(valt2[indy])
        valtrz = list(valt2[p])
        
        iindex2 =0 
        for index, nof in enumerate(valt2[p]):
            if nof == None :#and iindex2 == 0:
                print(f"Index: {index}, Number: {nof}")
                #valtrx = 
                index2 = index - iindex2
                print(valtrx[index2],valtry[index2],valtrz[index2])
                del valtrx[index2]
                del valtry[index2]
                del valtrz[index2]
                #valtrx.pop(index)
                #valtry = valtry.pop(index)
                #valtrz = valtrz.pop(index)
                iindex2 += 1
            #else:
            #    print(f"Index2: {index}, Number2: {nof}")
            #    #valtrx = 
            #    index2 = index - 1
            #    print(valtrx[index2],valtry[index2],valtrz[index2])
            #    del valtrx[index2]
            #    del valtry[index2]
            #    del valtrz[index2]
            
        X1=valtrx
        Y1=valtry
        Z1=valtrz
                
        if len(valtrz) < 3:
            valtrx = np.random.rand(100) * 4*np.pi - 2*np.pi
            valtry = np.random.rand(100) * 4*np.pi - 2*np.pi#  
            valtrz = np.sin(valtrx) * np.sin(valtry) / (1+np.abs(valtrx * valtry))
        
            X1=valtrx
            Y1=valtry
            Z1=valtrz
    else:
        
        X1=(valt2[indx])
        Y1=(valt2[indy])
        Z1=(valt2[p])
    print(X1,Y1,Z1)
    print("-----------")
    
    #X1=(valtrx)
    #Y1=(valtry)
    #Z1=(valtrz)
    
    
    
    
    lfw1 = LabelFrame(tab1,text="",bg = "gray",padx=20 ,pady=20)
    lfw1.place(x=0,y=0)

    var = IntVar(value=0)

            
    rb10_x =  Combobox(lfw1,values=(titl),justify=CENTER,state="readonly")
    rb10_x.current(indx)
    rb10_x.grid(row=0,column=1)
    #Radiobutton(lfw1,text="2D    ",variable=var,value=0)
    #rb10.grid(row=1,column=1)
    rb11_y = Combobox(lfw1,values=(titl),justify=CENTER,state="readonly")
    rb11_y.current(indy)
    #Radiobutton(lfw1,text="3D",variable=var,value=1)
    rb11_y.grid(row=1,column=1)
    #var2 = var.
    rb10_x.bind("<<ComboboxSelected>>", update)
    rb11_y.bind("<<ComboboxSelected>>", update)

    l1 = Label(lfw1, text = ("X") , font='Arial 13' ,fg="#CCFFFF", bg = "#940099" ).grid(row=0,column=0)
    l2 = Label(lfw1, text = ("Y") , font='Arial 13' ,fg="#CCFFFF", bg = "#940099" ).grid(row=1,column=0)



    lfw2 = LabelFrame(tab1,text="Параметры_графика",bg = "gray",padx=20 ,pady=20)
    lfw2.place(x=0,y=90)

    enabled = IntVar()
    enabled_checkbutton = ttk.Checkbutton(lfw2,text="Grid", variable=enabled,command=update_two)
    enabled_checkbutton.place(x=0,y=20)
    #enabled_checkbutton.bind("<ButtonPress-1>", update)
    #grid(row=1,column=0)
    enabled2 = IntVar()
    enabled_checkbutton2 = ttk.Checkbutton(lfw2,text="Point", variable=enabled2,command=update_two)
    enabled_checkbutton2.place(x=60,y=20)
    #enabled_checkbutton2.bind("<ButtonPress-1>", update)
    #grid(row=1,column=1) place(x=60,y=20)
    enabled3 = IntVar()
    enabled_checkbutton3 = ttk.Checkbutton(lfw2,text="Circle", variable=enabled3,command=update_two)
    enabled_checkbutton3.place(x=138,y=20)
    #enabled_checkbutton3.bind("<ButtonPress-1>", update)
    #grid(row=1,column=1)
    #place(x=120,y=20)

    pre_x = Combobox(lfw2,values=(titl),justify=CENTER,state="readonly")
    pre_x.current(0)
    pre_x.grid(row=0,column=0)
    pre_x.bind("<<ComboboxSelected>>", update)


    j = list()
    for i in range(15,100):
        j.append(i)
        
    pre_s = Combobox(lfw2,values=(j),justify=CENTER,state="readonly")
    pre_s.current(0)
    pre_s.grid(row=0,column=1)
    pre_s.bind("<<ComboboxSelected>>", update)
    
    #t = list()
    #for i in range(3,150):
    #    t.append(i)
        
    arrt = np.arange(0, 150,step=10)
    t = list()
    for i in arrt:
        t.append(int(i))    
    pre_t = Combobox(lfw2,values=(t),justify=CENTER,state="readonly",width=5)
    #pre_t.current(22)
    pre_t.current(3)
    pre_t.place(x=188,y=20)
    pre_t.bind("<<ComboboxSelected>>", update)
    #grid(row=1,column=1)

    #p=pre_x.current()
    #print("p=",p)
    #print("valt2=",valt2[p])


    lfw3 = LabelFrame(tab1,text="",bg = "gray",padx=20 ,pady=10)
    lfw3.place(x=0,y=168)

    l1 = Label(lfw3, text = ("          Min:") , font='Arial 13' ,fg="#CCFFFF", bg = "#940099" ).grid(row=0,column=0)
    l2 = Label(lfw3, text = ("         Max:") , font='Arial 13' ,fg="#CCFFFF", bg = "#940099" ).grid(row=1,column=0)
    l3 = Label(lfw3, text = ("         Avg:") , font='Arial 13' ,fg="#CCFFFF", bg = "#940099" ).grid(row=2,column=0)
    l4 = Label(lfw3, text = ("   Std Dev:") , font='Arial 13' ,fg="#CCFFFF", bg = "#940099" ).grid(row=3,column=0)
    l5 = Label(lfw3, text = ("Uniformity:") , font='Arial 13' ,fg="#CCFFFF", bg = "#940099" ).grid(row=4,column=0)

    min_m = Entry(lfw3)
    min_m.grid(row=0,column=1)
    min_m.insert(END,z)
    max_m = Entry(lfw3)
    max_m.grid(row=1,column=1)
    max_m.insert(END,z)
    #max_m.insert(END,(max(valtrz)))
    #max_m.insert(END,(max(valt2[p])))
    avg_m = Entry(lfw3)
    avg_m.grid(row=2,column=1)
    avg_m.insert(END,z)
    std_m = Entry(lfw3)
    std_m.grid(row=3,column=1)
    std_m.insert(END,z)
    unif_m = Entry(lfw3)
    unif_m.grid(row=4,column=1)
    unif_m.insert(END,z)
    
    
    fig = graf_test(X1,Y1,Z1,titl,s,p,root,frame,imag,Label,tab1)
    
    
    
    
    
    
    
    
    tab_control.place(x=595,y=0)