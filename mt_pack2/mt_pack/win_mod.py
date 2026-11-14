"""
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from tkinter import messagebox

import sys
import os

def get_source_path(relative_path):
    if hasattr(sys,"_MEIPASS"):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path,relative_path)

"""
from .win_mod2 import *
from .sea_file import *
#import sea_file

#dat_file_ico = get_source_path("1489187695-billingdatayencurrency_81853.ico")
#dat_file_gr_png = get_source_path("gradient_400_500.png")
#dat_file_gr_png2 = get_source_path("gradient_630_200.png")
#dat_file_gr_png3 = get_source_path("gradient_800_340.png")
#dat_file_gr_png4 = get_source_path("gradient_530_350.png")
#dat_file_gr_png5 = get_source_path("survey_clipboard_notes_icon_207103.png")

"""
root0 = tk.Tk()
#tix.Tk()
root0.title("Обработчиик_данных")
root0.geometry("400x500")
root0.resizable(width=False , height=False)
root0.iconbitmap(dat_file_ico)
root0.protocol("WM_DELETE_WINDOW", root0.destroy)
#root.config(bg="Black")
#root["bg"] = "#009999"
img = PhotoImage(file=dat_file_gr_png)
l_logo = Label(root0, image=img)
l_logo.pack()
"""
#photo = PhotoImage(file = dat_file_gr_png5)
                   #"survey_clipboard_notes_icon_207103.png")
#image = photo.subsample(21, 21)

#lf = LabelFrame(root0,text="Основные_параметры",bg = "gray",padx=30 ,pady=60)
#lf.place(x=10,y=10)


#def click_1():
#    pass
#def search_file():
#    pass

# Файл_PRE 
def dop_win(lf):         
    label_0 = Label(lf, text = " Файл_xlsx/csv " , font='Arial 13' ,fg="#CCFFFF", bg = "#940099" )
    label_0.grid(row=0,column=0)

    def sear_f():
        global name_file
        name_file = search_file(pre2)
        #print(name_file)
        
    pre2 = Entry(lf)
    pre2.grid(row=0,column=1)

    btn_1 = Button(lf, text = "Выбрать" , command = sear_f , font='Arial 10' , bg = "#940099" ,fg="#CCFFFF", activebackground = "#FF0099")
    btn_1.grid(row=0,column=2)

#def print_name():
#    global name_file
#    print(name_file)
#new_window
#image0 = 0 

def window_2(image0):
    new_window(name_file,image0)
    print(name_file)

"""
btn = Button(root0, text = "Выполнить" , command = window_two , font='Arial 13' ,fg="#CCFFFF", bg = "#940099" , activebackground = "#FF0099")
btn.place(x=150 , y=450)

root0.mainloop()

def main():
    pass

if __name__ == "main":
    main()
"""