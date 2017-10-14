'''
GUI calculator

10. Oct 2017
by Are Granhaug (are@granhaug.no)

TODO:
X   Clean up the font system to remove repetitions
X   BASE-2,8,16
V   Add each number to a list or tuple
X   Enable handling of multi-operator problems
X   Use operator library
'''

#Imports GUI packages
import tkinter as tk
from tkinter import font
import operator

#Stores path in variable to later import icon file
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

#Main GUI window called root
root = tk.Tk()
root.title("Calculator")
root.iconbitmap(dir_path + '\icon.ico')

#print("Path: " + dir_path)

helv16 = font.Font(family='Helvetica', size=16, weight="bold")

#Make list global to allow it to be accessed by functions. ex numberList = [5, '+', '3', '-', '6']
global numberList
numberList=[]

operator_dict = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

#=================FUNCTIONS=================

#Stores the current value and the operator in a list
def storeValue(value, operator):
    numberList.append(value)
    numberList.append(operator)
    display.config(text='')

def addition():
    storeValue(int(display.cget('text')), "+")

def subtraction():
    storeValue(int(display.cget('text')), "-")

def multiplication():
    storeValue(int(display.cget('text')), "*")

def division():
    storeValue(int(display.cget('text')), "/")

#[5 + 4 + 2 - 7 / 8]
#[Value, operator, value, operator, value]
#Odd: Value
#Even: Operator

#Fancy algorithm that goes through valueList and packs it down and down
#according to PEMDAS until only final answer remains

def execute(i,o,j):
    if o = '+':
        newValue = operator.add(i,j)
    elif o = '-':
        newValue = operator.sub(i,j)
    elif o = '*':
        newValue = operator.mul(i,j)
    elif o = '/':
        newValue = operator.truediv(i,j)
    return newValue

def equals():
    numberList.append(display.cget('text'))
    print(numberList)
    for i in range(len(numberList)):
        newValue = execute(i,i+1,i+2)
        del numberList(i:i+2)
        numberList


def num1():
    display.config(text=display.cget('text') + '1')
    
def num2():
    display.config(text=display.cget('text') + '2')

def num3():
    display.config(text=display.cget('text') + '3')

def num4():
    display.config(text=display.cget('text') + '4')

def num5():
    display.config(text=display.cget('text') + '5')
    
def num6():
    display.config(text=display.cget('text') + '6')

def num7():
    display.config(text=display.cget('text') + '7')
    
def num8():
    display.config(text=display.cget('text') + '8')

def num9():
    display.config(text=display.cget('text') + '9')
    
def num0():
    display.config(text=display.cget('text') + '0')

#Resets list and display
def ce():
    del numberList[:]
    display.config(text='')

#=================GUI ELEMENT DESIGN=================

display = tk.Label(root, text='', width=40, background="lightgray", font=("25"), anchor='e')
butPlu = tk.Button(root, borderwidth="0", font=helv16, relief="groove",
                   text="+", height="3", width="5", padx="5", pady="5", border="5", command=addition)
butMin = tk.Button(root, borderwidth="0", font=helv16, relief="groove",
                   text="-", height="3", width="5", padx="5", pady="5", border="5", command=subtraction)
butMul = tk.Button(root, borderwidth="0", font=helv16, relief="groove",
                   text="*", height="3", width="5", padx="5", pady="5", border="5", command=multiplication)
butDiv = tk.Button(root, borderwidth="0", font=helv16, relief="groove",
                   text="/", height="3", width="5", padx="5", pady="5", border="5", command=division)
but1 = tk.Button(root, borderwidth="0", font=helv16, relief="groove",
                   text="1", height="3", width="5", padx="5", pady="5", border="5", command=num1)
but2 = tk.Button(root, borderwidth="0", font=helv16, relief="groove",
                   text="2", height="3", width="5", padx="5", pady="5", border="5", command=num2)
but3 = tk.Button(root, borderwidth="0", font=helv16, relief="groove",
                   text="3", height="3", width="5", padx="5", pady="5", border="5", command=num3)
but4 = tk.Button(root, borderwidth="0", font=helv16, relief="groove",
                   text="4", height="3", width="5", padx="5", pady="5", border="5", command=num4)
but5 = tk.Button(root, borderwidth="0", font=helv16, relief="groove",
                   text="5", height="3", width="5", padx="5", pady="5", border="5", command=num5)
but6 = tk.Button(root, borderwidth="0", font=helv16, relief="groove",
                   text="6", height="3", width="5", padx="5", pady="5", border="5", command=num6)
but7 = tk.Button(root, borderwidth="0", font=helv16, relief="groove",
                   text="7", height="3", width="5", padx="5", pady="5", border="5", command=num7)
but8 = tk.Button(root, borderwidth="0", font=helv16, relief="groove",
                   text="8", height="3", width="5", padx="5", pady="5", border="5", command=num8)
but9 = tk.Button(root, borderwidth="0", font=helv16, relief="groove",
                   text="9", height="3", width="5", padx="5", pady="5", border="5", command=num9)
but0 = tk.Button(root, borderwidth="0", font=helv16, relief="groove",
                   text="0", height="3", width="5", padx="5", pady="5", border="5", command=num0)
butEqu = tk.Button(root, borderwidth="0", font=helv16, relief="groove",
                   text="=", height="3", width="5", padx="5", pady="5", border="5", command=equals)
butCom = tk.Button(root, borderwidth="0", font=helv16, relief="groove",
                   text=",", height="3", width="5", padx="5", pady="5", border="5", command=division)
butCE = tk.Button(root, borderwidth="0", font=helv16, relief="groove",
                   text="CE", height="3", width="5", padx="5", pady="5", border="5", command=ce)

#=================GUI ELEMENT PLACEMENT=================
display.grid(row=0,column=1, columnspan=4,padx=5,pady=5)
butPlu.grid(row=5,column=4)
butMin.grid(row=4,column=4)
butMul.grid(row=3,column=4)
butDiv.grid(row=2,column=4)
butEqu.grid(row=6,column=4)
butCom.grid(row=6,column=3)
butCE.grid(row=6,column=1)

but1.grid(row=5,column=1)
but2.grid(row=5,column=2)
but3.grid(row=5,column=3)
but4.grid(row=4,column=1)
but5.grid(row=4,column=2)
but6.grid(row=4,column=3)
but7.grid(row=3,column=1)
but8.grid(row=3,column=2)
but9.grid(row=3,column=3)
but0.grid(row=6,column=2)

root.mainloop()