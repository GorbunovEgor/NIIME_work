import csv
import openpyxl
from openpyxl.styles import Font, Fill, PatternFill, NamedStyle, Side, Border
import json

from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from tkinter import messagebox

#input_file2  = str()
#input_file3  = str() 
#input_file4  = str()
#time = IntVar()
#time = int()
#time = 10  


#name_f = StringVar()
#name_f = str()
#name_f = "text2.xlsx"   



def parsing_files (name_r,file_r,point,time,name_f,input_file2,input_file3 ,Min,Max):

    try:
        name_f = str(name_r.get())
    except ValueError:
        messagebox.showwarning("Warning","Внимание некоректно выставленное значение!")
        return (0)
        
    try:    
        time = int(file_r.get())
    except ValueError:
        messagebox.showwarning("Warning","Внимание некоректно выставленное значение!")
        return (0)
        
        
    with open(input_file2, "r" , newline = '') as f:
        pre = (csv.reader(f,delimiter=","))
    
        with open(input_file3, "r" , newline = '') as f:
            post = (csv.reader(f,delimiter=","))
            
            
            with open("data.json", "r") as json_file:
                a = json.load(json_file)
            print(a)
            
            #nn = ct#49 # количество_выводимых_ТОЧЕК
            nn = 0 
            #n = nn + 4
            n2 = nn + 3
        
            #s = cp #20 # количество_выводимых_СЛОЁВ
        
            i = 0
            x = 0
        
            i2=0
            x2=0 
        
            line=list()
            newl = list()
            
            i3 = 9
            i4 = 9
        
            i5 = 9
            j = 0
            j2 = 0
            float(j2)
        
            j3 = 0
        
            r = 0
        
            xx = list()
            yy = list()
            zz = list()
            zzz = list()
            nnc = list()
        
            book=openpyxl.Workbook()
            #book = openpyxl.open("text2.xlsx")
            sheet=book.active
            #sheet = book[name] 
            
            fill1 = PatternFill("solid" , fgColor="FF9999")#red
            fill2 = PatternFill("solid" , fgColor="66FFCC")#grin
            fill3 = PatternFill("solid" , fgColor="FFFF99")#yellow
            fill4 = PatternFill("solid" , fgColor="FF9966")#orange
            
            try:
                
                for line , newl in zip(pre,post):
                
                    if i in range(0,4):       
            
                        if 'Company:' in line  and i == 0:    
                            x += 1
                            print("x = ",x)
            
                    line_bt = 0.1 
                    (float(line_bt))
                    
                        
                    if x == 1 and i == 3:
                        print(line[7],line[8])
                        sheet["P8"].value = line[7]
                        sheet["Q8"].value = line[8]
            
                    if x == 1 and i > 3:
                        print(line[0],line[1],line[2],line[7],line[8])
                
                
                
                        line2 = [int(line[0])]
                        line3 = [float(line[1])]
                        line4 = [float(line[2])]
                
                        line5 = [float(line[8])]
                        line6 = [float(line[7])]
                
                            #xx.append(line3)
                        for p in line3:
                                xx.append(p)
                        for p2 in line4:
                            yy.append(p2)
                    
                        line_bt = line5[0]
                
                        sheet["M"+str(i3)].value = (line2[0])
                        sheet["N"+str(i3)].value = (line3[0])
                        sheet["O"+str(i3)].value = (line4[0])
                
                        sheet["Q"+str(i3)].value = (line5[0])
                        sheet["P"+str(i3)].value = (line6[0])
                    
                        if line6[0] > 0.95 or line6[0] > 0.96:
                            sheet["P"+str(i3)].fill = fill3
                        #else:
                            #sheet["P"+str(i3)].fill = fill1
                            
                        
                        if line6[0] < 0.95: #or line6[0] > 0.99:
                            sheet["P"+str(i3)].fill = fill1
                            
                        
                        if line6[0] > 0.98:
                            sheet["P"+str(i3)].fill = fill2
                        
                    
                        nn += 1
                        i3 += 1
                        print("i = ",i)
                        print("nn = ",nn)
                        nnc.append(nn)
                
                        print("line_bt = ",line_bt)
                
                
                    if x == 0:
                        print(line[0],line[2],line[9])
                
                        sheet["G"+str(i3)].value = ''.join(line[2])
                        sheet["H"+str(i3)].value = ''.join(line[9])
                    
                        i3 += 1    
                        print("i = ",i)  
                    
                    i += 1
            
                    
            #===========================================
            
                    newl_bt = 0.1 
                    (float(newl_bt))
            
                
                    if i2 in range(0,4):       
            
                        if 'Company:' in (newl)  and i2 == 0:
                            x2 += 1
                            print("x2 = ",x2)
                            
                    
                    
                    if x2 == 1 and i2 == 3:
                        print(newl[7],newl[8])
                        sheet["T8"].value = newl[7]
                        sheet["U8"].value = newl[8]
            
                    if x2 == 1 and i2 > 3:
                        print(newl[0],"|",newl[1],"|",newl[2],"|",newl[7],"|",newl[8])
                
                        newl2 = [int(newl[0])]
                        newl3 = [float(newl[1])]
                        newl4 = [float(newl[2])]
                
                        newl5 = [float(newl[8])]
                        newl6 = [float(newl[7])]
                
                        newl_bt = newl5[0]


                        sheet["M"+str(i4)].value = (newl2[0])
                        sheet["N"+str(i4)].value = (newl3[0])
                        sheet["O"+str(i4)].value = (newl4[0])
                
                        sheet["U"+str(i4)].value = (newl5[0])
                        sheet["T"+str(i4)].value = (newl6[0])
                    
                        
                        if newl6[0] > 0.95 or newl6[0] > 0.96:
                            sheet["T"+str(i4)].fill = fill3
                        
                            
                        if newl6[0] < 0.95: 
                            sheet["T"+str(i4)].fill = fill1
                            
                        
                        if newl6[0] > 0.98:
                            sheet["T"+str(i4)].fill = fill2
                        
                
                        i4 += 1
                
                
                        print("newl_bt = ",newl_bt)
                
            
                    if x2 == 0 and i2 <= (n2 + 4):
                        print(newl[0],newl[2],newl[9])
                
                        sheet["J"+str(i4)].value = ''.join(newl[2])
                        sheet["K"+str(i4)].value = ''.join(newl[9])
                
                        i4 += 1    
                        print("i2 = ",i2)
                
                    i2 += 1


            
            #==============================================
                    if i > 4 and i2 > 4 :
                        sheet['B8'] = "DELTA"
                
                        bt = [((line_bt) - (newl_bt))]
                        print ("bt = ",bt)
                        for bt2 in bt:
                            sheet["B"+str(i5)].value = bt2
                    
                    
                        #er = list()
                        if point.get() == 0:
                        #er = ([((line_bt) + (newl_bt) + (bt2)) * 3])
                            er = [(bt2 / time * 60 / 1000)]
                            print ("er = ",er)
                        else:
                            er = [(bt2 / time * 60 * 10)]
                            print ("er = ",er)
                
                
                        for er2 in er:        
                            if Max < er2:
                                Max = er2
                            if Min > er2:
                                Min = er2
                            sheet["C"+str(i5)].value = er2
                            zz.append(er2)    
                    
                        j3 += 1
                        i5 += 1
                
                    
            except IndexError:   
                
                print("Ошибка")       
            print("nnc = ",nnc)
        
            print("max = ",Max)
            print("min = ",Min)
        
                
            print("x = ",xx) 
            print("y = ",yy)
            print("z = ",zz)
            
    return nnc,zzz,zz,nn,sheet,xx,yy,point,a,Min,Max,book,name_f


def safe_graf(sheet):
    img = openpyxl.drawing.image.Image('myplot.png')
    sheet.add_image(img, "E8")
    
def safe_graf_two(sheet):
    img = openpyxl.drawing.image.Image('myplot2.png')
    sheet.add_image(img, "E26")
        
def close_file(book,name_f):
    print("закрытие_файла")
    #"text2.xlsx"
    book.save(name_f)
    book.close        

def writing_param_f(sheet,point,nn,time,input_file2,input_file3):
    sheet['N8'] = 'X (mm)'
    sheet['O8'] = 'Y (mm)'
    sheet['M8'] = 'Number'
    
    if point.get() == 0:
        sheet['C8'] = 'ER, мкм/мин'        
    else:
        sheet['C8'] = 'ER, A/мин'
        
    sheet["P7"] = "PRE"
    sheet["T7"] = "POST"
    
    PRE = ('\\'.join (input_file2.split('\\')[-1:]))
    POST = ('\\'.join (input_file3.split('\\')[-1:]))
    
    sheet["P1"].value = PRE
    sheet["T1"].value = POST


    sheet['C1'] = 'P'+str(nn)
    #sheet['D1'] = 'По_заданым'
    #sheet['E1'] = 'ER А/мин'

    sheet['B4'] = 'СРЗНАЧ'
    sheet['B5'] = '3сигма, %'
    sheet['B2'] = 'Мин'
    sheet['B3'] = 'Макс'
    sheet['B6'] = 'Время в сек.'
    #sheet['B7'] = 'Сигма%'STDEV.S

    sheet['C4'].value = '=AVERAGE(C9:C109)'#+str(i4)
    sheet['C5'].value = '=(STDEV(C9:C109)/C4*100)*3'
    sheet['C2'].value = '=MIN(C9:C109)'
    sheet['C3'].value = '=MAX(C9:C109)'
    sheet['C6'].value = time
    #sheet['C7'].value = '=C9/C81*100' 
    

    sheet['D4'].value = '=AVERAGE(D9:D109)'
    sheet['D5'].value = '=(STDEV(D9:D109)/D4*100)*3'
    sheet['D2'].value = '=MIN(D9:D109)'
    sheet['D3'].value = '=MAX(D9:D109)'