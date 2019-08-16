from tkinter import *
from sklearn import preprocessing
import pandas as pd
import tkinter as tk
import tkinter.ttk as ttk

from ttkthemes import ThemedStyle


def stylometryFilter(str):
    filtered_string = ""

    for c in str:
        if c == ',' or c == '.' or c == '@' or c == ')' or c == '(' or c == '!' or c == '_' or c == '?' or c == '%' or c == '&' or c == '#' or c == '-' or c == '=' or c == ':' or c == ';' or c == ' ' or c == '/':
            filtered_string += c
        elif c.isdigit():
            filtered_string += '1'
        elif c.isalpha() and c.islower():
            filtered_string += '2'
        elif c.isalpha() and c.isupper():
            filtered_string += '3'

    return filtered_string


def encode_data(key=str,frame=pd.core.frame.DataFrame):

    labelEncode = preprocessing.LabelEncoder()

    return labelEncode.fit_transform(frame[key])

def center_window(w=100, h=300,root=tk):
    # get screen width and height
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    # calculate position x, y
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))

def popupmsg(msg):

    root = tk.Tk()
    root.title("Accuracy")
    style = ThemedStyle(root)
    style.set_theme("arc")
    center_window(280, 110, root)

    popup = tk.Frame(root, width=350, bg='white', height=200, relief='sunken', borderwidth=2)

    label = Label(popup, text=msg,background="white")
    label.pack(side="top", fill="x", pady=5)
    ttk.Separator(popup, orient="vertical").pack(padx=5, pady=10)
    B1 = ttk.Button(popup, text="Okay", command = root.destroy)
    B1.pack()

    popup.pack(expand=True, fill='both', side='right')

    root.mainloop()
