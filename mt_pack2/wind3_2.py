
def create_wind3_2():
    
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
        global N
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
        fig, ax = plt.subplots( facecolor = "#eee")
        #ax = fig.add_subplot()
        fig.suptitle(W)



        plt.xlabel("X,мм")
        plt.ylabel("Y,мм")

        c20 = ax.tricontourf(xx20, yy20, zz20, s , cmap = "bwr")
        plt.colorbar(c20)
        
                
        angle = np.linspace( 0 , 2 * np.pi , 150 ) 
        radius = 150
        x = radius * np.cos( angle ) 
        y = radius * np.sin( angle ) 
        ax.plot( x, y ,"black") 
        ax.set_aspect( 1 )
        
        
        if point.get() == 0:
            plt.title("                                                                                        ER, мкм/мин")
        else:
            plt.title("                                                                                        ER, A/мин")

        
        plt.savefig("myplot2.png", dpi = 70)
        img = openpyxl.drawing.image.Image('myplot2.png')
        sheet.add_image(img, "E26")
        
        
        plt.show(block=False)
        plt.close("all")
        
        
        print("закрытие_файла")
        #"text2.xlsx"
        book.save(name_f)
        book.close
        
        
        label_0 = Label(root, text = "Выполнено" , font='Arial 13' , bg = "#009919" )
        label_0.place(x=200 , y=350)
        root.after(3000, label_0.destroy)
        print("Выполнено")
        N = N - 1


        print("x = ", len(xx20))



    remove_many = Button(root10, text="Назначить шаблон", command=get_selected21,fg="#CCFFFF", bg = "#940099" )
    remove_many.pack(pady=10)

