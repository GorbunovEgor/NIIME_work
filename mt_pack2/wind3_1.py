    
def create_wind3_1():  
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
        global N
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


        print("x = ", len(xx))
        #root2.after(100, lambda: root2.destroy())
            
    remove_many = Button(root2, text="Выбор через Ctrl", command=get_selected, bg = "#940099")
    remove_many.pack(pady=10)