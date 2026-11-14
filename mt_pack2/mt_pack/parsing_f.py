from openpyxl import load_workbook
import csv


import numpy as np
import matplotlib.pyplot as plt
import statistics

def parf(nf):
    
    name_file = nf
    
    rnf = ('.'.join (name_file.split('.')[+1:]))
    rnf2 = 0 
    if rnf == "xlsx":
        rnf2 += 1

        
    if rnf2 == 1:
        workbook = load_workbook(name_file,data_only=True) 
        # Выбор листа для работы  
        sheet = workbook.active 
        cell_value = sheet.cell(row=1, column=1).value  
        print(cell_value)


        titl = list()
        til = 0
        qr = 1

        while til < 1:
            
            for i in range(1, sheet.max_column + 1):
                q = (sheet.cell(row=qr, column=i).value)
                print(q)
                titl.append(q)
                #if q in ["No","x(mm)","y(mm)",'Num','X','Y','Number','X(mm)','Y(mm)']:
                if q == "No" or q =="x(mm)" or q == "y(mm)" or q == 'Num' or q == 'X'  or q == 'Y' or q == 'Number' or q == 'X(mm)'  or q == 'Y(mm)' :
                    print("Нашел")
                    til += 1
                else:
                    print("----")      
            if til == 0:
                print("Зануление")
                titl = list()
            qr += 1
            print("til=",til)
            print("qr=",qr)
        print("title=",titl)



        counet_volt = 1
        valt = list()
        valt2 = list()
        counter_col=1

        if til > 1:
            #while counet_volt != None:
                #for i in range(1, sheet.max_column + 1):
                #    q = (sheet.cell(row=qr, column=i).value)
            while counter_col < ((len(titl))+1):
                for i in range(qr, sheet.max_row + 1):
                    q = (sheet.cell(row=i, column=counter_col).value)
                    
                    valt.append(q)
                
                    #print("q=",q)
                    #if q == None:
                    #    q = None
                    #    valt.append(q)
                    #else:
                    #    valt.append(q)
                        
                        #
                    #valt2.append(q)
                #print("valt=",valt[12])
                counet_volt = valt[12]
                #print("counet_volt =",counet_volt )
                valt2.append(valt)
                #titl_dict = {obj : state for obj, state in zip(titl, valt)}
                valt = list()
                #qr += 1
                counter_col += 1
        print("valt2=",valt2)
        print("title=",titl)
        
    else:
        titl= list()
        all_list=list()
        line_couner=0
        line_title = 0
        lt = 0

        with open(name_file, "r" , newline = '') as f:
            pre = (csv.reader(f,delimiter=","))
            
            for line in pre:
                print("line=",line_couner)
                print("line=",line)
                if lt > line_title:
                    all_list.append(line)
                #if line in str(["No","x(mm)","y(mm)",'Num','X','Y','Number','X(mm)','Y(mm)']):
                #if line in "No" or "x(mm)" or "y(mm)" or 'Num' or 'X' or 'Y' or 'Number' or 'X(mm)' or 'Y(mm)':
                if 'No' in line or 'x(mm)' in line or 'y(mm)' in line or 'Num' in line or 'X' in line or 'Y' in line:
                    titl = line
                    line_title = line_couner
                    lt = line_title + 1
                #if lt > line_title:
                #    all_list.append(line)
                if line == []:
                    break
                line_couner += 1
                #print("line=",line_couner)

        print("title=",titl)
        print("line_title=",line_title)
        print(len(all_list))
        #all_list = all_list.pop((len(all_list))-1)
        #del all_list(len(all_list))
        all_list.pop((len(all_list))-1)
        print("all_list=",all_list)
        #= lst.pop(2)
        result_list=list()
        j=0
        q= list()
        while j != (len(titl)):
            #q= list()
            for i in all_list:
                #print("i=",i[j])
                try:
                    q.append(float(i[j]))
                except ValueError:
                    q.append(str(i[j]))        
            result_list.append(q)
            #print("q=",q)
            q = list()
            j += 1
        print("res=",result_list)

        print("res=",len(result_list))
        print("titl=",len(titl))
        valt2 = result_list
        
        return rnf,rnf2,titl,valt2
        
def parf_two(nf,rnf2,titl):
    name_file = nf
    
    if rnf2 == 1:
        #from openpyxl import load_workbook
        wb = load_workbook(filename=name_file, read_only=True,data_only=True)
        ws = wb.active
        #['D5 (2)']
        #row = 4
        r_set = [row for row in ws.iter_rows(values_only=True)]
        # l1=r_set.pop(0) # Collect the first row as column headers 
        #wb.close()# Close the workbook after reading
        #print("r_set=",r_set)
        #print("l1=",l1)

        #sheet = workbook.active 
        cell_value = ws.cell(row=1, column=1).value
        #titl = list()
        #til = 0
        #qr = 1

        #while til < 1:
        #    
        #    for i in range(1, ws.max_column + 1):
        #        q = (ws.cell(row=qr, column=i).value)
        #        print(q)
        #        titl.append(q)
        #        if q == "No" or q =="x(mm)" or q == "y(mm)":
        #            print("Нашел")
        #            til += 1
        #        else:
        #            print("----")      
        #    if til == 0:
        #        print("Зануление")
        #        titl = list()
        #    qr += 1
        #    print("til=",til)
        #    print("qr=",qr)
        #print("title=",titl)

        l1 = titl
        print("l1=",l1)
        # Using CSV file 
    else:
        #import csv
        file = open(name_file) # Path of CSV data file
        csvreader = csv.reader(file)
        l1 = []
        l1 = next(csvreader) # column headers as first row 
        r_set = [row for row in csvreader]
        l1 = titl
        print("l1=",l1)
        return l1,r_set
#event = None    


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




def update_test(event):
    print("UPDATE_TEST")
    
def update_1(event,pre_x,pre_t,rb10_x,rb11_y,var,enabled,enabled2,enabled3,rnf,rnf2,pre_s,fig,valt2,titl
             ,min_m,max_m,avg_m,std_m,unif_m):
    global z
    global c
    global c2
    global point
    global point1
    global x_rb10
    global y_rb11
    global t
    
    global g1
    global g2
    global g3
    global g4
    global g5
    global s
    global Z1
    
    
    global cir1
    global cir2
    global cir3
    global cir4
    global cir5
    global cir6    
    
    global var2 
    global en1
    global en2
    global en3
    
    #global test_p
    #global test_p2
    #global test_s
    #global test_X 
    #global test_Y
    #global test_en
    #global test_en3
    #global test_t
    
    
    #global rnf
    #global rnf2
    #l.config(text=str(random.random()))
    #min_m.config(text=z)
    #min_m.delete(0, END)
    #min_m.insert(END,z)
    # root.after(3000, update)
    print("проверка")
    #root.update()
    #root.update_idletasks()
    z += 1
    print("z=",z)
    p=pre_x.current()
    #t=pre_t.current()
    t=pre_t.get()
    x_rb10=rb10_x.current()
    y_rb11=rb11_y.current()
    #s=pre_s.get()
    var2 = var.get()
    en1 = enabled.get()
    en2 = enabled2.get()
    en3 = enabled3.get()
    print("p=",p)
    print("var=",var2)
    print("en1=",en1)
    print("en2=",en2)
    print("en3=",en3)
    #print("en1=",enabled.get())
    #print("en2=",enabled2.get())
    #print("en3=",enabled3.get())
    print("X=",x_rb10)
    print("Y=",y_rb11)
    
    print("rnf=",rnf)
    print("rnf2=",rnf2)
    
    #print("maxX=",max(valt2[x_rb10]))
    
    s=pre_s.get()
    s = int(s)
    print("s=",s)
    print("t=",t)
    
    
    
    if rnf2 == 0 :#and (test_p != p or test_s != s or point != en2 or test_X != x_rb10 or test_Y != y_rb11 or test_en != en1 or test_en3 != en3 or test_t != t) :
                
        fig.clf()
        Z1=(valt2[p])
        
        X1=(valt2[x_rb10])
        Y1=(valt2[y_rb11])
        #s=pre_s.get()
        #s = int(s)
        Rad = list()
        for xr, yr in zip(X1,Y1):
            Rad.append(np.sqrt((xr**2)+(yr**2)))
        
        #t = 25
        
        if en3 == 1:
            X2 = list(X1)
            Y2 = list(Y1)
            Z2 = list(Z1)
            #ARR = np.array(Z1)
            ARR = np.mean(Z1)
            angle = np.linspace( 0 , 2 * np.pi , int(t) ) 
            radius = (max(Rad)+1)
            x = radius * np.cos( angle ) 
            y = radius * np.sin( angle )
            #X2.append(radius * np.cos( angle )) 
            #Y2.append(radius * np.sin( angle ))
            arr_l= [ARR]*int(t)
            for i,xj,yj in zip(arr_l,x,y):
                #print("z=",i)
                #print("x=",xj)
                #print("y=",yj)
                X2.append(xj) 
                Y2.append(yj)
                Z2.append(float(i))
            #print(ARR)
            print("X=",X2)
            print("Y=",Y2)  
            print("Z=",Z2)        
            
        g2 = ax = fig.subplots()
        if en1 ==0:
            g1 = 0 #ax.grid(True)
        elif en1 == 1:
            g1 = ax.grid(True)           
        g3 = fig.suptitle(f"                                                                          {(titl[p])}")
        #fig.suptitle("Скорость травления")
        g4 = ax.set_xlabel("X,мм")
        g5 = ax.set_ylabel("Y,мм")
        if en3 == 0:                  
            c2 = ax.tricontourf(X1, Y1, Z1, s , cmap = "coolwarm")
        elif en3 == 1:
            c2 = ax.tricontourf(X2, Y2, Z2, s , cmap = "coolwarm")
                
        c= fig.colorbar(c2,ax=ax,label=(titl[p]))
        
        cir1=angle = np.linspace( 0 , 2 * np.pi , 150 ) 
        cir2=radius = (max(Rad)+1)
        #max(X1)
        #150
        cir3=x = radius * np.cos( angle ) 
        cir4=y = radius * np.sin( angle )
        #z = z <  (min(valt2[p])) 
        cir5=ax.plot( x, y ,"black") 
        cir6=ax.set_aspect( 1 )
        
        if en2 == 0:
            point1 = 0
        elif en2 == 1:
            point1 = ax.plot(X1,Y1,"ok",ms=3)
            
        ax.set_xlim(((max(Rad)+10)*-1),(max(Rad)+10))
        ax.set_ylim(((max(Rad)+10)*-1),(max(Rad)+10))
        

        fig.canvas.draw()
        #fig.canvas.flush_events()
        #print("valt2=",(max(valt2[p])))statistics.mean(numbers)
        
        #test_p = p
        #test_s = s
        #point = en2
        #test_X = x_rb10
        #test_Y = y_rb11
        #test_en = en1
        #test_en3 = en3
        #test_t = t
    
    #else:
    if rnf2 == 1 :#and (test_p != p or test_s != s or point != en2 or test_X != x_rb10 or test_Y != y_rb11 or test_en != en1 or test_en3 != en3 or test_t != t):
        valtrx = list(valt2[x_rb10])
        valtry = list(valt2[y_rb11])
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
                
        if len(valtrz) < 3:
            valtrx = np.random.rand(100) * 4*np.pi - 2*np.pi
            valtry = np.random.rand(100) * 4*np.pi - 2*np.pi#  
            valtrz = np.sin(valtrx) * np.sin(valtry) / (1+np.abs(valtrx * valtry))
        
            X1=valtrx
            Y1=valtry
            Z1=valtrz
            
            
        
        fig.clf()
        
        X1=valtrx
        Y1=valtry
        Z1=valtrz
        
        Rad = list()
        for xr, yr in zip(X1,Y1):
            Rad.append(np.sqrt((xr**2)+(yr**2)))
        
        #t = 25
        
        if en3 == 1:
            X2 = list(X1)
            Y2 = list(Y1)
            Z2 = list(Z1)
            #ARR = np.array(Z1)
            ARR = np.mean(Z1)
            angle = np.linspace( 0 , 2 * np.pi , int(t) ) 
            radius = (max(Rad)+1)
            x = radius * np.cos( angle ) 
            y = radius * np.sin( angle )
            #X2.append(radius * np.cos( angle )) 
            #Y2.append(radius * np.sin( angle ))
            arr_l= [ARR]*int(t)
            for i,xj,yj in zip(arr_l,x,y):
                #print("z=",i)
                #print("x=",xj)
                #print("y=",yj)
                X2.append(xj) 
                Y2.append(yj)
                Z2.append(float(i))
            #print(ARR)
            print("X=",X2)
            print("Y=",Y2)  
            print("Z=",Z2)
        
        #X1=(valt2[x_rb10])
        #Y1=(valt2[y_rb11])
        #Z1=(valt2[p])
        #s=pre_s.get()
        #s = int(s)
        
        g2 = ax = fig.subplots()
        if en1 ==0:
            g1 = 0 #ax.grid(True)
        elif en1 == 1:
            g1 = ax.grid(True)           
        g3 = fig.suptitle(f"                                                                          {(titl[p])}")
        #fig.suptitle("Скорость травления")
        g4 = ax.set_xlabel("X,мм")
        g5 = ax.set_ylabel("Y,мм") 
        if en3 == 0:                  
            c2 = ax.tricontourf(X1, Y1, Z1, s , cmap = "coolwarm")
        elif en3 == 1:
            c2 = ax.tricontourf(X2, Y2, Z2, s , cmap = "coolwarm")                  
        #c2 = ax.tricontourf(X1, Y1, Z1, s , cmap = "coolwarm")
        c= fig.colorbar(c2,ax=ax,label=(titl[p]))
        
        #Rad = list()
        #for xr, yr in zip(X1,Y1):
        #    Rad.append(np.sqrt((xr**2)+(yr**2)))
        
        cir1=angle = np.linspace( 0 , 2 * np.pi , 150 ) 
        cir2=radius = (max(Rad)+1)
        #max(X1)
        #150
        cir3=x = radius * np.cos( angle ) 
        cir4=y = radius * np.sin( angle )
        #z = z <  (min(valt2[p])) 
        cir5=ax.plot( x, y ,"black") 
        cir6=ax.set_aspect( 1 )
        
        if en2 == 0:
            point1 = 0
        elif en2 == 1:
            point1 = ax.plot(X1,Y1,"ok",ms=3)
            
            
        ax.set_xlim(((max(Rad)+10)*-1),(max(Rad)+10))
        ax.set_ylim(((max(Rad)+10)*-1),(max(Rad)+10))
        

        fig.canvas.draw()
        #fig.canvas.flush_events()
        #print("valt2=",(max(valt2[p])))statistics.mean(numbers)
        #test_p = p
        #test_s = s
        #point = en2
        #test_X = x_rb10
        #test_Y = y_rb11
        #test_en = en1
        #test_en3 = en3
        #test_t = t
            
    
    
    
    
    if rnf2 == 0:
    #test_p2 != p and rnf2 == 0:
        min_m.delete(0, "end")
        min_m.insert("end",round( (min(valt2[p])),4))
        max_m.delete(0, "end")
        max_m.insert("end",round( (max(valt2[p])),4))
        avg_m.delete(0, "end")
        avg_m.insert("end",round( (( (sum(valt2[p])) / (len(valt2[p])) )) ,4))
        std_m.delete(0, "end")
        try:
            std_m.insert("end",round( (statistics.stdev(valt2[p])) / ( (sum(valt2[p])) / (len(valt2[p])) ) *100  ,4))
        except ZeroDivisionError:
            std_m.insert("end","!_Деление на наль_!")
        unif_m.delete(0, "end")
        try:
            unif_m.insert("end",round( ( ( (max(valt2[p]))-(min(valt2[p])) ) / ( (max(valt2[p]))+(min(valt2[p])) ) )*100 ,4))
        except ZeroDivisionError:
            unif_m.insert("end","!_Деление на наль_!")
            
        #test_p2 = p
        
    if rnf2 == 1:
    #test_p2 != p and rnf2 == 1:
        min_m.delete(0, "end")
        min_m.insert("end",round( (min(valtrz)) ,4))
        max_m.delete(0, "end")
        max_m.insert("end",round( (max(valtrz)) ,4))
        avg_m.delete(0, "end")
        avg_m.insert("end",round( (( (sum(valtrz)) / (len(valtrz)) )) ,4))
        std_m.delete(0, "end")
        try:
            std_m.insert("end",round( (statistics.stdev(valtrz)) / ( (sum(valtrz)) / (len(valtrz)) ) *100  ,4))
        except ZeroDivisionError:
            std_m.insert("end","!_Деление на наль_!")
        unif_m.delete(0, "end")
        try:
            unif_m.insert("end",round( ( ( (max(valtrz))-(min(valtrz)) ) / ( (max(valtrz))+(min(valtrz)) ) )*100 ,4))
        except ZeroDivisionError:
            unif_m.insert("end","!_Деление на наль_!")
            
        #test_p2 = p
    
    
    
    
    print("UPDATE")
    

def update_2(pre_x,pre_t,rb10_x,rb11_y,var,enabled,enabled2,enabled3,rnf,rnf2,pre_s,fig,valt2,titl
             ,min_m,max_m,avg_m,std_m,unif_m):#(enabled,enabled2,enabled3):
    print("en1=",enabled.get())
    print("en2=",enabled2.get())
    print("en3=",enabled3.get())
    event = None
    #update(event,pre_x,pre_t,rb10_x,rb11_y,var,enabled,enabled2,enabled3,rnf,rnf2,pre_s)
    update_1(event ,pre_x,pre_t,rb10_x,rb11_y,var,enabled,enabled2,enabled3,rnf,rnf2,pre_s,fig,valt2,titl
             ,min_m,max_m,avg_m,std_m,unif_m)
    print("UPDATE_TWO")