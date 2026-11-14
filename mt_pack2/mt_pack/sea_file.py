"""
#import tkinter as tk
from tkinter import *
#from tkinter import ttk
#from tkinter.ttk import Combobox
#from tkinter import messagebox
"""

import easygui
name_file  = str("----------")
#P = Entry()

def search_file(PRE):
    print('start_search_file')
    #global P
    #pre2 = P

    global name_file
    #nf = name_file
    #pre2.delete(0, END)
    PRE.delete(0, "end")
    input_file = easygui.fileopenbox(filetypes=["*.docx"])
    #pre.insert(END,"hello")
    #name_file = input_file
    name_file = input_file
    PRE.insert("end",  input_file)
    #PRE.insert("end",  name_file)
    #pre2.insert(END,  name_file)
    #print(name_file)
    return name_file

    
def text_test(entry):
    entry.insert(0, "Введите имя")  # Вставляем текст в начало
    
#if __name__ == "main":
#    search_file()
#    text_test()
    