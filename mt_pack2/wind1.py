"""
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from tkinter import messagebox
"""

import easygui

from .wind2 import *
from .pars_file import *

from .mt_pack import *

root = Tk()
root.title("Обработчиик_данных")
root.geometry("400x500")
#root.resizable(width=False , height=False)
root.iconbitmap(dat_file_ico)
root.protocol("WM_DELETE_WINDOW", root.destroy)
#root.config(bg="Black")
#root["bg"] = "#009999"
img = PhotoImage(file=dat_file_gr_png)
l_logo = Label(root, image=img)
l_logo.pack()

dat_file_gr_png5 = get_source_path("survey_clipboard_notes_icon_207103.png")

photo = PhotoImage(file = dat_file_gr_png5)
                   #"survey_clipboard_notes_icon_207103.png")
image_tul_bar = photo.subsample(21, 21)

#image0 = image_tul_bar

tab_control = ttk.Notebook(root,height=200,width=300)
tab_control.place(x=40,y=10)

lf = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
dop_win(tab2)
tab_control.add(lf,text="Обработка_данных")
tab_control.add(tab2,text="Создание_графика")

wind_param = 0

def window_two():
    window_2(image_tul_bar)


#lf = LabelFrame(root,text="Основные_параметры",bg = "gray",padx=30 ,pady=60)
#lf.place(x=10,y=10)
def on_tab_change(event):
    global wind_param
    selected_tab = event.widget.select()
    tab_text = event.widget.tab(selected_tab, "text")
    if (tab_text == "Обработка_данных"):
        wind_param = 0
        print(f"Вы переключились на: {tab_text},{selected_tab},{wind_param}" )
        btn.config(bg = "#940099" , activebackground = "#FF0099",command=click)
    elif (tab_text == "Создание_графика"):
        wind_param = 1
        btn.config(bg = "#E08105" , activebackground = "#FAB828",command=window_two)
        print(f"Вы переключились на: {tab_text},{selected_tab},{wind_param}" )
        
        
        
    
# Привязываем событие смены вкладки
tab_control.bind("<<NotebookTabChanged>>", on_tab_change)

input_file2  = str()
input_file3  = str() 
#input_file4  = str()
time = IntVar()
#time = int()
time = 10  


name_f = StringVar()
#name_f = str()
name_f = "text2.xlsx"

def read_name_f(entry):
    #global input_file2
    entry.delete(0, END)
    input_file = easygui.fileopenbox(filetypes=["*.docx"])
    #pre.insert(END,"hello")
    file = input_file
    entry.insert(END,  input_file)
    return file
   # print(file)

def click_1():
    global input_file2
    input_file2 = read_name_f(pre2)
    #print(input_file2)

    
label_0 = Label(lf, text = " Файл_PRE " , font='Arial 13' ,fg="#CCFFFF", bg = "#940099" )
#label_0.place(x=10 , y=50)
label_0.grid(row=0,column=0)

pre2 = Entry(lf)
#pre2.place(x=180 , y=50)
pre2.grid(row=0,column=1)

btn_1 = Button(lf, text = "Выбрать" , command = click_1 , font='Arial 10' , bg = "#940099" ,fg="#CCFFFF", activebackground = "#FF0099")
#btn_1.place(x=310 , y=50)
btn_1.grid(row=0,column=2)

def click_2():
    global input_file3
    input_file3 = read_name_f(post2)

    
label_1 = Label(lf, text = "Файл_POST" , font='Arial 13' ,fg="#CCFFFF", bg = "#940099" )
#label_1.place(x=10 , y=90)
label_1.grid(row=1,column=0)

post2 = Entry(lf)
#post2.place(x=180 , y=90)
post2.grid(row=1,column=1)

btn_2 = Button(lf, text = "Выбрать" , command = click_2 , font='Arial 10' ,fg="#CCFFFF", bg = "#940099" , activebackground = "#FF0099")
#btn_2.place(x=310 , y=90)
btn_2.grid(row=1,column=2)


    
def click_3():
    pass
    

label_2 = Label(lf, text = "Время_сек. " , font='Arial 13' ,fg="#CCFFFF", bg = "#940099" )
#label_2.place(x=10 , y=130)
label_2.grid(row=2,column=0)

file_r = Entry(lf)
#file_r.place(x=180 , y=130)
file_r.grid(row=2,column=1)

#btn_3 = Button(lf, text = "Назначить" , command = click_3 , font='Arial 10' , bg = "#940099" , activebackground = "#FF0099")
#btn_3.place(x=310 , y=130)
#btn_3.grid(row=2,column=2)


#label_14 = Label(root, font='Arial 13' , bg = "#940099")
#label_14.place(x=200 , y=300)
file_r.insert(END,  time)



    
def click_4():
    pass

label_4 = Label(lf, text = "Файл_Result" , font='Arial 13' ,fg="#CCFFFF", bg = "#940099" )
#label_4.place(x=10 , y=170)
label_4.grid(row=3,column=0)

name_r = Entry(lf)
#name_r.place(x=180 , y=170)
name_r.grid(row=3,column=1)

#btn_5 = Button(lf, text = "Назначить" , command = click_4 , font='Arial 10' , bg = "#940099" , activebackground = "#FF0099")
##btn_5.place(x=310 , y=170)
#btn_5.grid(row=3,column=2)


#label_15 = Label(root, font='Arial 13' , bg = "#940099")
#label_15.place(x=200 , y=320)
name_r.insert(END,  name_f)

point = IntVar(value=0)
#point = 0

rb1 = Radiobutton(lf,text="E, мкм\мин",variable=point,value=0)
rb1.grid(row=4,column=1)


rb2 = Radiobutton(lf,text="E,   A\мин   ",variable=point,value=1)
rb2.grid(row=5,column=1)



Min = 1000000.0
Max = 0.0
cp = 15
N = 0 


def click():
    global point
    print(input_file2)
    
    parametr = parsing_files (name_r,file_r,point,time,name_f,input_file2,input_file3,Min,Max)
    nnc = parametr[0]
    zzz = parametr[1]
    zz = parametr[2]
    nn = parametr[3]
    sheet = parametr[4]
    xx = parametr[5]
    yy = parametr[6]
    point = parametr[7]
    a = parametr[8]
    Min_win2  = parametr[9]
    Max_win2 = parametr[10]
    book = parametr[11]
    name_f_win2 = parametr[12]
    
    create_win2(Min_win2 ,Max_win2 ,cp,nnc,zzz,zz,root,xx,yy,sheet,point,a,nn,N,book,name_f_win2)
    writing_param_f(sheet,point,nn,time,input_file2,input_file3)



btn = Button(root, text = "Выполнить" , command = click , font='Arial 13' ,fg="#CCFFFF", bg = "#940099" , activebackground = "#FF0099")
btn.place(x=150 , y=450)


root.mainloop()