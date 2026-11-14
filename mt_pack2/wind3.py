from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from tkinter import messagebox

from .get_source_path import *
from .create_graf import *


def create_win3(win,zz,zzz,counter_plot,pre_x,post_x,root,var,xx,yy,sheet,nnc,point,a,nn,min,max,N,book,name_f):
    print("Проверка")
    #global Min
    #global Max
    global cp
    #global N
    global en2

    Min = int()
    Max = int()
    
    
    Min = min.get()
    try:
        Min = float(Min)
    except ValueError:
        messagebox.showwarning("Warning","Внимание некоректно выставленное значение!")
        win.after(100, lambda: win.destroy())
        
        
    
    Max = max.get()
    try:
        Max = float(Max)
    except ValueError:
        messagebox.showwarning("Warning","Внимание некоректно выставленное значение!")
        win.after(100, lambda: win.destroy())
                            
    
    cp = counter_plot.get()
    #cp = int(cp)
    try:
        cp = int(cp)
    except ValueError:
        messagebox.showwarning("Warning","Внимание некоректно выставленное значение!")
        win.after(100, lambda: win.destroy())
        
    
    
    en2 = 0 
    st2 = 0  
    
    
    st2 = pre_x.get()
    st2 = int(st2)
    en2 = post_x.get()
    en2 = int(en2)
    
    if en2 < st2:
        messagebox.showwarning("Warning","Внимание некоректно выставленное значение!")
        #N = N - 1
        return(0)
    
    
    print("st2 = ",st2)
    print("en2 = ",en2)
    
    if Max < Min:
        messagebox.showwarning("Warning","Значение Max не может быть меньше Min!")
        return(0)
        

    l = 0 

    for k in zz:

        if k < Min:
            k = Min
            zzz.append(k)
            print("<")
            continue
            
    
        if k > Max:
            k = Max
            zzz.append(k)
            print(">")
            continue
            

    
        if k >= Min and k <= Max:
            zzz.append(k)
            print("=")
            continue
            

        l += 1
        print("l = ",l)    
        print("k = ",k)




    N = N + 1
    print("Min = ",Min)
    print("Max = ",Max)
    print("cp = ",cp)
    s = cp
    print("N = ",N)
    
    
    
    if N == 1:
        win.after(100, lambda: win.destroy())
        print("zzz = ",zzz) 
        create_garf_0(xx, yy, zzz, s,point,sheet)
        if var.get() == 0:
            
            st = st2 - 1
            en = en2
        
            xx2 = list()
            yy2 = list()
            zz2 = list()
        
            T = 9
        
            for i in range(st,en):

                xx2.append(xx[i])
                yy2.append(yy[i])
                zz2.append(zzz[i])
        
                print("xx =",xx2)
                print("yy =",yy2)
                print("zz =",zz2)
            
            
            Ts = T + st 
            for i in zz2:
                #sheet["D"+str(T)].value = (zz2[0])
                sheet["D"+str(Ts)].value = (i)
                Ts += 1
                print("T = ",T)
                print("zz2 =",zz2)
                print("I = ", i)
                
            sheet['D1'] = 'P'+str(len(zz2))
            
            M = str()
            M = ("В_пределах_",st + 1,"-",en)
            create_garf_1(xx2, yy2, zz2, s,point,sheet,book,name_f,M)
        
    
            label_0 = Label(root, text = "Выполнено" , font='Arial 13' , bg = "#009919" )
            label_0.place(x=200 , y=350)
            root.after(3000, label_0.destroy)
            print("Выполнено")
            N = N - 1
            #return 0
            
        if var.get() == 1:
            print("Другой вариант")
                                        
            #root2 = Tk()
                
            root2 = Toplevel()
            root2.title("Выбор точек для графика")
            root2.geometry("800x340")
            #root2.resizable(width=False , height=False)
            root2.grab_set()
            root2.iconbitmap(dat_file_ico)
            
            
            img3 = PhotoImage(file=dat_file_gr_png3)
            l_logo3 = Label(root2, image=img3)
            l_logo3.image = img3
            #l_logo3.pack()
            l_logo3.place(x=-2,y=0)
                
                
            style = ttk.Style()

            style.theme_use("default")

            style.configure("Treeview",
                background="#D3D3D3",
                foreground="black",
                rowheight=25,
                fieldbackground="#D3D3D3")
                
                
            style.map("Treeview",
                background=[('selected',"#347083")])

            tree_farame = Frame(root2)
            tree_farame.pack(pady=10)
            #tree_farame.place(x=10 , y=50)

            tree_scroll = Scrollbar(tree_farame)
            tree_scroll.pack(side=RIGHT,fill=Y)

            my_tree = ttk.Treeview(tree_farame,yscrollcommand=tree_scroll.set,selectmode="extended")
            my_tree.pack()
            #my_tree.grid(row=0,column=0)
            #my_tree.place(x=100 , y=50)


            tree_scroll.config(command=my_tree.yview)
                
                
                
            my_tree['columns'] = ("N","Name", "ID", "Favorite Pizza")

            my_tree.column("#0", width=0, stretch=NO)
            my_tree.column("N", anchor=CENTER,width=140)
            my_tree.column("Name", anchor=CENTER,width=140)
            my_tree.column("ID", anchor=CENTER,width=100)
            my_tree.column("Favorite Pizza", anchor=CENTER, width=140)

            my_tree.heading("#0", text="", anchor=W)
            my_tree.heading("N", text="N", anchor=CENTER)
            my_tree.heading("Name", text="X", anchor=CENTER)
            my_tree.heading("ID",  text="Y", anchor=CENTER)
            my_tree.heading("Favorite Pizza", text="Z", anchor=CENTER)
                
                
                
            my_tree.tag_configure("evenrow", background="white")
            my_tree.tag_configure("oddrow", background="lightblue")
                
                
                
            global count
            count = 0

            for i in range(0,nn):
                if count % 2 == 0:
                    my_tree.insert(parent="", index="end", iid=count, text="", values=(nnc[i],xx[i],yy[i],zzz[i]), tags=('evenrow'))
                else:        
                    my_tree.insert(parent="", index="end", iid=count, text="", values=(nnc[i],xx[i],yy[i],zzz[i]), tags=('oddrow'))
                count += 1
            
                                
            x_x = list() 
            y_y = list()
            z_z = list()        
                        
            def get_selected():
                #global N
                T = 8
                selected_items = my_tree.selection()
                    #print(selected_items)
                for item in selected_items:
                    current_item = my_tree.item(item)
                    #print(current_item)
                    current_text = current_item.get("text")
                    current_value = current_item.get("values")
                    
                    Nub = int(current_item.get("values")[0])

                    X = float(current_item.get("values")[1])
                    Y = float(current_item.get("values")[2])
                    Z = float(current_item.get("values")[3])

                    print(type(current_value))
                    print(current_text,current_value)
                    print(X,Y,Z)
                    
                    #c_item = int(current_item)
                    c_i = T + Nub

                    sheet["D"+str(c_i)].value = (Z)
                    x_x.append(X)
                    y_y.append(Y)
                    z_z.append(Z)
                    
                root2.after(100, lambda: root2.destroy())




                W = ("По",len(x_x),"точкам")
                sheet['D1'] = 'P'+str(len(x_x))
                create_garf_2(x_x, y_y, z_z, s,point,W,sheet,book,name_f)
                
                
                label_0 = Label(root, text = "Выполнено" , font='Arial 13' , bg = "#009919" )
                label_0.place(x=200 , y=350)
                root.after(3000, label_0.destroy)
                print("Выполнено")
                N - 1


                print("x = ", len(xx))
                #root2.after(100, lambda: root2.destroy())
                    
            remove_many = Button(root2, text="Выбор через Ctrl", command=get_selected, bg = "#940099")
            remove_many.pack(pady=10)
                
        if var.get() == 2:
            
            root10 = Toplevel()
            root10.title("Список шаблонов")
            root10.geometry("530x350")
            #root10.resizable(width=False , height=False)
            root10.iconbitmap(dat_file_ico)
            
            img40 = PhotoImage(file=dat_file_gr_png4)
            l_logo40 = Label(root10, image=img40)
            l_logo40.image = img40
            l_logo40.place(x=-2,y=0)


            style = ttk.Style()

            style.theme_use("default")

            style.configure("Treeview",
                background="#D3D3D3",
                foreground="black",
                rowheight=25,
                fieldbackground="#D3D3D3")

            style.map("Treeview",
            background=[('selected',"#347083")])

            tree_farame = Frame(root10)
            tree_farame.pack(pady=10)

            tree_scroll = Scrollbar(tree_farame)
            tree_scroll.pack(side=RIGHT,fill=Y)

            my_tree30 = ttk.Treeview(tree_farame,yscrollcommand=tree_scroll.set,selectmode="extended")
            my_tree30.pack()

            tree_scroll.config(command=my_tree30.yview)


            my_tree30['columns'] = ("Name")

            my_tree30.column("#0", width=0, stretch=NO)
            my_tree30.column("Name", anchor=CENTER,width=140)

            my_tree30.heading("#0", text="", anchor=W)
            my_tree30.heading("Name", text="Шаблоны", anchor=CENTER)
            
            
            my_tree30.tag_configure("evenrow", background="white")
            my_tree30.tag_configure("oddrow", background="lightblue")


            global count30
            count30 = 0


            print(a.keys())

            b = list(a.keys())
            print(b)
            print(len(b))



            for i in range(0,(len(b))):
                if count30 % 2 == 0:
                    my_tree30.insert(parent="", index="end", iid=count30, text="", values=(b[i]), tags=('evenrow'))
                else:        
                    my_tree30.insert(parent="", index="end", iid=count30, text="", values=(b[i]), tags=('oddrow'))
                count30 += 1
            
            
            #win.after(100, lambda: win.destroy())
            
            
            def see_all():
                

                selected_items = my_tree30.selection()
                #print(selected_items)
                for item in selected_items:
                    current_item = my_tree30.item(item)
                    #print(current_item)
                    current_text = current_item.get("text")
                    current_value = current_item.get("values")

                    X = str(current_item.get("values")[0])
                    #Y = float(current_item.get("values")[1])
                    #Z = float(current_item.get("values")[2])

                    print(type(current_value))
                    print(current_text,current_value)
                    print("Ключь = ",X)
                    print(type(a[X]))
                    print("Вывод значений по ключу",a[X])

                root4 = Toplevel()
                root4.title("Предварительный просмотр")
                root4.geometry("600x380")
                root4.iconbitmap(dat_file_ico)
                root4.resizable(width=False , height=False)
                root4.config(bg = "gray")



                style = ttk.Style()

                style.theme_use("default")

                style.configure("Treeview",
                    background="#D3D3D3",
                    foreground="black",
                    rowheight=25,
                    fieldbackground="#D3D3D3")

                style.map("Treeview",
                    background=[('selected',"#347083")])

                tree_farame = Frame(root4)
                tree_farame.pack(pady=10)

                tree_scroll = Scrollbar(tree_farame)
                tree_scroll.pack(side=RIGHT,fill=Y)

                my_tree3 = ttk.Treeview(tree_farame,yscrollcommand=tree_scroll.set,selectmode="extended")
                my_tree3.pack()

                tree_scroll.config(command=my_tree3.yview)




                my_tree3['columns'] = ("n","X","Y","Z")

                my_tree3.column("#0", width=0, stretch=NO)
                my_tree3.column("n", anchor=CENTER,width=140)
                my_tree3.column("X", anchor=CENTER,width=140)
                my_tree3.column("X", anchor=CENTER,width=140)
                my_tree3.column("Y", anchor=CENTER,width=140)
                my_tree3.column("Z", anchor=CENTER,width=140)

                my_tree3.heading("#0", text="", anchor=W)
                my_tree3.heading("n", text="n", anchor=CENTER)
                my_tree3.heading("X", text="X", anchor=CENTER)
                my_tree3.heading("Y", text="Y", anchor=CENTER)
                my_tree3.heading("Z", text="Z", anchor=CENTER)


                my_tree3.tag_configure("evenrow", background="white")
                my_tree3.tag_configure("oddrow", background="lightblue")



                global ct3
                ct3 = 0


                    #for i in range(0,(len(x))):
                for i in a[X]:
                    if ct3 % 2 == 0:
                        my_tree3.insert(parent="", index="end", iid=ct3, text="", values=(nnc[i],xx[i],yy[i],zzz[i]), tags=('evenrow'))
                    else:        
                        my_tree3.insert(parent="", index="end", iid=ct3, text="", values=(nnc[i],xx[i],yy[i],zzz[i]), tags=('oddrow'))
                    ct3 += 1


            _button3 = Button(root10, text="Предварительный просмотр",command=see_all,fg="#CCFFFF", bg = "#940099" )
            _button3.place(x=10,y=100)
            
            
            
            def remove_many1():
                
                with open("data.json", "r") as json_file:
                    a = json.load(json_file)
                #global a 
                print(a)
                x = my_tree30.selection()
                print("x = ",x)
                
                print(a)
                
                y2= list()
                for record10 in x:
                    print("record10=",record10)
                    y = my_tree30.item(record10)
                    print("y=",y)
                    y2.append((y.get("values")[0]))
                    my_tree30.delete(record10)

                print("Y = ",y2)
                print(a)


                for i in y2:
                    print ("I=",i)

                    print(a)
                    del a[i]
                    print(a)

                with open("data.json", "w") as json_file:
                    a = json.dump(a,json_file)

                print(y)
                #del a["Task3"]

            _button30 = Button(root10, text="Удалить шаблон(Ы)",command=remove_many1,fg="#CCFFFF", bg = "#940099" )
            _button30.place(x=10,y=10)
            
            
            
            
            
            name_box2 = "P"+str(len(xx))+str("_")
            def add_one():
                #global a
                global count30
                #global N
                
                #x = "Task3"
                x1 = name_box.get()
                my_tree30.insert(parent="",index="end",iid=count30,text="",values=x1)
                count30 += 1

                print(a)


                root3 = Toplevel()
                root3.title("Обработчиик_данных")
                root3.geometry("600x400")
                root3.iconbitmap(dat_file_ico)
                root3.resizable(width=False , height=False)
                root3.config(bg = "gray")



                style = ttk.Style()

                style.theme_use("default")

                style.configure("Treeview",
                    background="#D3D3D3",
                    foreground="black",
                    rowheight=25,
                    fieldbackground="#D3D3D3")

                style.map("Treeview",
                    background=[('selected',"#347083")])

                tree_farame = Frame(root3)
                tree_farame.pack(pady=10)

                tree_scroll = Scrollbar(tree_farame)
                tree_scroll.pack(side=RIGHT,fill=Y)

                my_tree2 = ttk.Treeview(tree_farame,yscrollcommand=tree_scroll.set,selectmode="extended")
                my_tree2.pack()

                tree_scroll.config(command=my_tree2.yview)




                my_tree2['columns'] = ("n","X","Y","Z")

                my_tree2.column("#0", width=0, stretch=NO)
                my_tree2.column("n", anchor=CENTER,width=140)
                my_tree2.column("X", anchor=CENTER,width=140)
                my_tree2.column("Y", anchor=CENTER,width=140)
                my_tree2.column("Z", anchor=CENTER,width=140)

                my_tree2.heading("#0", text="", anchor=W)
                my_tree2.heading("n", text="n", anchor=CENTER)
                my_tree2.heading("X", text="X", anchor=CENTER)
                my_tree2.heading("Y", text="Y", anchor=CENTER)
                my_tree2.heading("Z", text="Z", anchor=CENTER)


                my_tree2.tag_configure("evenrow", background="white")
                my_tree2.tag_configure("oddrow", background="lightblue")



                global ct2
                ct2 = 0


                for i in range(0,(len(xx))):
                    if ct2 % 2 == 0:
                        my_tree2.insert(parent="", index="end", iid=ct2, text="", values=(nnc[i],xx[i],yy[i],zzz[i]), tags=('evenrow'))
                    else:        
                        my_tree2.insert(parent="", index="end", iid=ct2, text="", values=(nnc[i],xx[i],yy[i],zzz[i]), tags=('oddrow'))
                    ct2 += 1

                #stop = 0
                si2 = list()
                def get_selected20():
                    global stop
                    selected_items2 = my_tree2.selection()
                    print(type(selected_items2))
                    print("Выбранные точки",selected_items2)
                    #si2 = list()
                    for i in selected_items2:
                        i = int(i)
                        print("i=",i)
                        si2.append(i)
                    print("si2=",si2)
                    #stop += 1
                    root3.after(100, lambda: root3.destroy())

                    a[x1] = si2
                    print(a)
                    


                    with open("data.json", "w") as json_file:
                        json.dump(a, json_file,indent=4)
                        
                    



                remove_many = Button(root3, text="Выбор через контрол", command=get_selected20,fg="#CCFFFF", bg = "#940099" )
                remove_many.pack(pady=10)


            _butt32 = Button(root10, text="Добавить один шаблон",command=add_one,fg="#CCFFFF", bg = "#940099" )
            _butt32.place(x=10,y=50)

            name_box = Entry(root10)
            name_box.place(x=10,y=80)
            
            name_box.insert(END,  name_box2)
            
            
            
            
            xx20 = list() 
            yy20 = list()
            zz20 = list()   

            #print("Лист х",x)
            

            def get_selected21():
                #global N
                T_2 = 8
                selected_items = my_tree30.selection()
                #print(selected_items)
                for item in selected_items:
                    current_item = my_tree30.item(item)
                    #print(current_item)
                    current_text = current_item.get("text")
                    current_value = current_item.get("values")

                    X = str(current_item.get("values")[0])
                    #Y = float(current_item.get("values")[1])
                    #Z = float(current_item.get("values")[2])

                    print(type(current_value))
                    print(current_text,current_value)
                    print("Ключь = ",X)
                    print(type(a[X]))
                    print("Вывод значений по ключу",a[X])
                    #print(X,Y,Z)
                    p = list(a[X])

                
                for i in a[X]:
                    T_2 = 8
                    
                    c_i = T_2 + nnc[i]
                    sheet["D"+str(c_i)].value = (zzz[i])

                    xx20.append(xx[i])
                    yy20.append(yy[i])
                    zz20.append(zzz[i])

                    print("xx =",xx20)
                

                print("xx =",xx20)
                print("yy =",yy20)
                print("zz =",zz20)

                root10.after(100, lambda: root10.destroy())

                W = ("По",len(xx20),"точкам")
                sheet['D1'] = 'P'+str(len(xx20))
                
                create_garf_2(xx20, yy20, zz20, s,point,W,sheet,book,name_f)
                
                
                
                
                label_0 = Label(root, text = "Выполнено" , font='Arial 13' , bg = "#009919" )
                label_0.place(x=200 , y=350)
                root.after(3000, label_0.destroy)
                print("Выполнено")
                N - 1


                print("x = ", len(xx20))



            remove_many = Button(root10, text="Назначить шаблон", command=get_selected21,fg="#CCFFFF", bg = "#940099" )
            remove_many.pack(pady=10)  
        
    
    else:
        print("Пропуск")
        N = 0
        
        label_r = Label(root, text = "Ошибка" , font='Arial 13' , bg = "#E41313" )
        label_r.place(x=200 , y=350)
        root.after(3000, label_r.destroy)