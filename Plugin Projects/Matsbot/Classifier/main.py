#IMPORTS
from threading import Thread

from ttkthemes import ThemedStyle

import Helper_Method
import tkinter as tk
import tkinter.ttk as ttk
import time

from AgglomerativeClusteringClassifier import ACC_Model_Trainer, ACC_Data_To_CSV, ACC_User_Input
from Constats import Status
from WordGramClassifier import WGC_Data_To_CSV, WGC_Model_Trainer, WGC_User_Input
from MergedClassifier import MC_Data_To_CSV, MC_Model_Trainer, MC_User_Input
from KmeanClusteringClassifier import CC_Data_To_CSV, CC_Model_Trainer, CC_User_Input
from StyleClassifier import SC_Data_To_CSV, SC_Model_Trainer, SC_User_Input
from pathlib import Path


def global_timer():
    while True:
        is_model_trained()
        time.sleep(1)

        if Status.is_app_waiting:
            message_status("Processing Please Wait!", 1)
            button2.configure(state='disabled')
            button3.configure(state='disabled')
            button4.configure(state='disabled')
        else:
            message_status("Waiting For Response", 1)
            is_model_trained()



def is_model_trained():
    if Status.is_app_waiting == False:
        if Status.classifier_type == 'stylometry':
            my_file = Path("stylometry_model")
            if my_file.is_file() == False:
                button3.configure(state='disabled')
                button4.configure(state='disabled')
            else:
                button3.configure(state='enabled')
                button4.configure(state='enabled')
        elif Status.classifier_type == 'content':
            my_file = Path("wordgram_model")
            if my_file.is_file() == False:
                button3.configure(state='disabled')
                button4.configure(state='disabled')
            else:
                button3.configure(state='enabled')
                button4.configure(state='enabled')
        elif Status.classifier_type == 'agglomerative':
            my_file = Path("agglomerative_model")
            if my_file.is_file() == False:
                button3.configure(state='disabled')
                button4.configure(state='disabled')
            else:
                button3.configure(state='enabled')
                button4.configure(state='enabled')
        else:
            my_file = Path("clustering_model")
            if my_file.is_file() == False:
                button3.configure(state='disabled')
                button4.configure(state='disabled')
            else:
                button3.configure(state='enabled')
                button4.configure(state='enabled')
        button2.configure(state='enabled')

def message_status(message,type):

    if type == 0:
        status.configure(foreground="red")
        status_text.set(message)
    else:
        status.configure(foreground="green")
        status_text.set(message)

#EVENT HANDLER

def model_trainer_start():
    update_status()
    if Status.classifier_type == 'stylometry':
        SC_Data_To_CSV.runProgram()
        SC_Model_Trainer.runProgram()
    elif Status.classifier_type == 'content':
        WGC_Data_To_CSV.runProgram()
        WGC_Model_Trainer.runProgram()
    elif Status.classifier_type == 'merged':
        MC_Data_To_CSV.runProgram()
        MC_Model_Trainer.runProgram()
    elif Status.classifier_type == 'agglomerative':
        ACC_Data_To_CSV.runProgram()
        ACC_Model_Trainer.runProgram()
    else :
        CC_Data_To_CSV.runProgram()
        CC_Model_Trainer.runProgram()
    is_model_trained()
    Status.is_app_waiting = False
    button2.configure(state='enabled')
    button3.configure(state='enabled')
    button4.configure(state='enabled')

def model_trainer():
    button2.configure(state='disabled')
    button3.configure(state='disabled')
    button4.configure(state='disabled')
    Status.is_app_waiting = True
    t = Thread(target=model_trainer_start)
    t.start()

def form_sheet_start():
    update_status()
    if Status.classifier_type == 'stylometry':
        view = Helper_Method.popupmsg(SC_User_Input.runProgram(textarea.get("1.0", tk.END)))
    elif Status.classifier_type == 'content':
        view = Helper_Method.popupmsg(WGC_User_Input.runProgram(textarea.get("1.0", tk.END)))
    elif Status.classifier_type == 'merged':
        view = Helper_Method.popupmsg(MC_User_Input.runProgram(textarea.get("1.0", tk.END)))
    elif Status.classifier_type == 'agglomerative':
        view = Helper_Method.popupmsg(ACC_User_Input.runProgram(textarea.get("1.0", tk.END)))
    else :
        view = Helper_Method.popupmsg(CC_User_Input.runProgram(textarea.get("1.0", tk.END)))
    Status.is_app_waiting = False

def form_sheet_all():
    Status.is_report_prediction = True
    Status.is_app_waiting = True
    t1 = Thread(target=form_sheet_start)
    t1.start()

def form_sheet():
    Status.is_app_waiting = True
    t1 = Thread(target=form_sheet_start)
    t1.start()

def update_status_combo(index, value, op):
    classifier_Type.selection_clear()
    if classifier_Type.current() == 1:
        ngram_type.configure(state='disabled')
    else:
        ngram_type.configure(state='readonly')
    update_status()
    is_model_trained()


def update_status():
    classifier_Type.selection_clear()
    if classifier_Type.current() == 0:
        Status.classifier_type = 'clustering'
    elif classifier_Type.current() == 1:
        Status.classifier_type = 'stylometry'
    elif classifier_Type.current() == 2:
        Status.classifier_type = 'content'
    elif classifier_Type.current() == 3:
        Status.classifier_type = 'agglomerative'
    elif classifier_Type.current() == 4:
        Status.classifier_type = 'merged'

    if ngram_type.current() == 0:
        Status.vector_analyser_type = "word"
    else :
        Status.vector_analyser_type = "char"

    if ngram_val.current() == 0:
        Status.vector_analyser_range = 2
    elif ngram_val.current() == 1:
        Status.vector_analyser_range = 1
    elif ngram_val.current() == 2:
        Status.vector_analyser_range = 3
    elif ngram_val.current() == 4:
        Status.vector_analyser_range = 4
    elif ngram_val.current() == 5:
        Status.vector_analyser_range = 5
    elif ngram_val.current() == 6:
        Status.vector_analyser_range = 6
    elif ngram_val.current() == 7:
        Status.vector_analyser_range = 7
    elif ngram_val.current() == 8:
        Status.vector_analyser_range = 8
    elif ngram_val.current() == 9:
        Status.vector_analyser_range = 9
    else :
        Status.vector_analyser_range = 10

    if select_kbest_range.current() == 0:
        kbest_threshhold = 1000
    elif select_kbest_range.current() == 1:
        kbest_threshhold = 500
    else:
        kbest_threshhold = 5000


# root
root = tk.Tk()
root.title("Gender Identifier")
style = ThemedStyle(root)
style.set_theme("arc")
Helper_Method.center_window(1010, 580,root)

# sidebar
sidebar = tk.Frame(root, width=350, bg='white', height=800, relief='sunken', borderwidth=2)

# TYPES
ttk.Separator(sidebar,orient="vertical").pack(padx=5, pady=2)
ttk.Label(sidebar,text="Classifier Type", style="BW.TLabel",width=22,background="white",foreground="black").pack(side=tk.TOP)
ttk.Separator(sidebar,orient="vertical").pack(padx=5, pady=2)
classifier_Type_Text = tk.StringVar()
classifier_Type = ttk.Combobox(sidebar,textvariable=classifier_Type_Text,width=22,height=45,state="readonly", values=("KMean Cluster (Recommended)", "Stylometry Method", "Content Method","Agglomerative Cluster","Merged Classifier"))
classifier_Type.pack(side=tk.TOP)
classifier_Type.current(0)
ttk.Separator(sidebar,orient="vertical").pack(padx=5, pady=3)

ttk.Label(sidebar,text="N-Gram Type", style="BW.TLabel",width=22,background="white",foreground="black").pack(side=tk.TOP)
ttk.Separator(sidebar,orient="vertical").pack(padx=5, pady=2)
ngram_type_text = tk.StringVar()
ngram_type = ttk.Combobox(sidebar,textvariable=ngram_type_text,width=22,height=15,state="readonly", values=("Word (Recomended)", "Char"))
ngram_type.pack(side=tk.TOP)
ngram_type.current(0)
ttk.Separator(sidebar,orient="vertical").pack(padx=5, pady=3)

ttk.Label(sidebar,text="N-Gram Range", style="BW.TLabel",width=22,background="white",foreground="black").pack(side=tk.TOP)
ttk.Separator(sidebar,orient="vertical").pack(padx=5, pady=2)
ngram_val_text = tk.StringVar()
ngram_val = ttk.Combobox(sidebar,textvariable=ngram_val_text,width=22,height=15,state="readonly", values=("1-2 (Recomended)", "1-1", "1-3", "1-4", "1-5", "1-6", "1-7", "1-8", "1-9", "1-10"))
ngram_val.pack(side=tk.TOP)
ngram_val.current(0)
ttk.Separator(sidebar,orient="vertical").pack(padx=5, pady=3)

ttk.Label(sidebar,text="KBest Threshhold", style="BW.TLabel",width=20,background="white",foreground="black").pack(side=tk.TOP)
ttk.Separator(sidebar,orient="vertical").pack(padx=5, pady=2)
select_kbest_range_text = tk.StringVar()
select_kbest_range = ttk.Combobox(sidebar,textvariable=select_kbest_range_text,width=22,height=15,state="readonly", values=("1000 (Recomended)", "500", "5000"))
select_kbest_range.pack(side=tk.TOP)
select_kbest_range.current(0)

# ACTIONS
ttk.Separator(sidebar,orient="vertical").pack(padx=5, pady=33)
ttk.Separator(sidebar,orient="vertical").pack(padx=5, pady=33)
ttk.Separator(sidebar,orient="vertical").pack(padx=5, pady=20)
status_text = tk.StringVar()
status_text.set('Waiting For Response')
status = ttk.Label(sidebar,textvariable=status_text, style="BW.TLabel",width=22,background="white",foreground="green")
status.pack(side=tk.TOP)
ttk.Separator(sidebar,orient="vertical").pack(padx=5, pady=15)
button4 = ttk.Button(sidebar,width=22,text="Report Prediction",command=form_sheet)
button2 = ttk.Button(sidebar,width=22,text="Re-Train Model",command=model_trainer)
button3 = ttk.Button(sidebar,width=22,text="Make Prediction",command=form_sheet_all)
button2.pack(side=tk.TOP, pady=4, padx=10)
button3.pack(side=tk.TOP, pady=4, padx=10)
button4.pack(side=tk.TOP, pady=4, padx=10)
sidebar.pack(expand=False, fill='both', side='left', anchor='nw')

# combo changing events
classifier_Type_Text.trace('w',update_status_combo)
ngram_type_text.trace('w',update_status_combo)
ngram_val_text.trace('w',update_status_combo)
select_kbest_range_text.trace('w',update_status_combo)

# main content area
mainarea = tk.Frame(root, bg='#CCC', width=700, height=800)
textarea = tk.Text(mainarea,height=72,width=120)
textarea.pack(side=tk.RIGHT)
textarea.insert(tk.END, "Write your Code")
mainarea.pack(expand=True, fill='both', side='right')
is_model_trained()

t = Thread(target=global_timer)
t.start()

root.mainloop()
