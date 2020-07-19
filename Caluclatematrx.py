# -*- coding: utf-8 -*-
"""
Created on Fri May 29 18:33:41 2020

@author: wwwds
"""

import numpy as np
import tkinter as tk
import tkinter.ttk as ttk
win=tk.TK()
win.title("2x3 Matrix Solver")
def multiply():
    a = entry1.get()
    a = list(map(int,a))
    b = entry2.get()
    b = list(map(int,b))
    c = entry3.get()
    c = list(map(int,c))
    d = entry4.get()
    d = list(map(int,d))
    e = entry5.get()
    e = list(map(int,e))
    X = np.array((a,b))
    Y = np.array((c,d,e))
    Z=np.dot(X,Y)
    print(Z)
label1 = tk.Label(win,text="Enter first row matrix")