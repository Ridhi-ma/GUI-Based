
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
from tkinter.ttk import Progressbar
root =Tk()
root.title("PYTHON GUI")
# 
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
root.geometry('350x200')
TAB_CONTROL=ttk.Notebook(root)
TAB1=ttk.Frame(TAB_CONTROL)
TAB_CONTROL.add(TAB1,text="Tab1")
TAB2=ttk.Frame(TAB_CONTROL)
TAB_CONTROL.add(TAB2,text="Tab2")
TAB_CONTROL.pack(expand=1,fill="both")
ttk.Label(TAB1,text="The Snake").grid(column=0,row=0,padx=10,pady=10)
ttk.Label(TAB2,text="The Snake").grid(column=0,row=0,padx=10,pady=10)
v1 =IntVar()
v2=IntVar()
v3=IntVar()
cb1=Checkbutton(TAB2,text='Disabled',variable=v1,onvalue=1,offvalue=0)
cb1.grid(row=1,column=1)
cb2=Checkbutton(TAB2,text='Unchecked',variable=v2,onvalue=1,offvalue=0)
cb2.grid(row=1,column=2)
cb3=Checkbutton(TAB2,text='Enabled',variable=v3,onvalue=1,offvalue=0)
cb3.grid(row=1,column=3)
radio=IntVar()
rb1=Radiobutton(TAB2,text='Blue',variable=radio,value=1)
rb1.grid(row=2,column=1)
rb2=Radiobutton(TAB2,text='Gold',variable=radio,value=2)
rb2.grid(row=2,column=2)
rb3=Radiobutton(TAB2,text='Red',variable=radio,value=3)
rb3.grid(row=2,column=3)
ttk.Label(TAB2,text="Progress bar").grid(column=0,row=3,padx=10,pady=10)
button1 = ttk.Button(TAB2,text='Run Progress bar',width=25)
button1.grid(row=4,column=0)
button2 = ttk.Button(TAB2,text='Start Progress bar',width=25)
button2.grid(row=5,column=0)
button3 = ttk.Button(TAB2,text='Stop Progress bar',width=25)
button3.grid(row=6,column=0)
button4 = ttk.Button(TAB2,text='Stop after second',width=25)
button4.grid(row=7,column=0)
style = ttk.Style()
style.theme_use('default')
style.configure("black.Horizontal.TProgressbar", background='green')
bar = Progressbar(TAB2, length=250, style='black.Horizontal.TProgressbar')
bar['value'] = 10
bar.grid(column=0, row=10,padx=10,pady=10)

# cb1.pack()
# cb2.pack()
# cb3.pack()
root.mainloop()