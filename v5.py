import tkinter
from tkinter import * 
import pandas as pd
import re
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  NavigationToolbar2Tk) 
from tkinter.filedialog import askopenfilename

filename = 'data.txt'
#def freq_plotter(filename):
with open (filename , 'r') as file:
  lines = file.readlines()
line = len(lines)
for i in range (0,line):
  x = re.search("measurements", lines[i])
  if x:col_num = int(re.findall(r"[-+]?\d*\.?\d+|\d+", lines[i])[0]);break
data = pd.read_csv(filename, skiprows = 41, sep='\t', header=0, names=list(range(col_num+1) ), index_col=False, dtype=float)
#col_numb = col_num
distance = np.asarray( data.iloc[:,0].copy())
#global freq
freq = []
for i in range (1,col_num+1):
  k = np.asarray(data.iloc[:,i].copy())
  freq.append(k)
print(type(freq))
f = np.array(freq)
print(f.shape)
fig = plt.figure(figsize= [ 5,5] )
for i in range (1,col_num): 
    plt.plot(distance, freq[i],linewidth=1 )
plt.xlabel('Distance(m)')
plt.ylabel('Frequency(GHz)')
plt.title("Distance vs Brillouin Frequency")
plt.grid(axis='both')
#plt.show()

#fig2 = freq_plotter('data.txt') 
#fig2.show()
col_numb = 0

def open_file():
    """Open a file for editing."""
    filename = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filename:
        return
    #txt_edit.delete("1.0", tk.END)
    #with open(filepath, "r") as input_file:
    #    text = input_file.read()
    #    txt_edit.insert(tk.END, text)
    #window.title(f"Simple Text Editor - {filepath}")

    with open (filename , 'r') as file:
        lines = file.readlines()
    line = len(lines)
    for i in range (0,line):
        x = re.search("measurements", lines[i])
        if x:
            global col_num
            col_num = int(re.findall(r"[-+]?\d*\.?\d+|\d+", lines[i])[0]);break
    print('okkkkk')
    global data
    data = pd.read_csv(filename, skiprows = 41, sep='\t', header=0, names=list(range(col_num+1) ), index_col=False, dtype=float)
#    global data
    col_numb = col_num
    global distance
    distance = np.asarray( data.iloc[:,0].copy())
    
    global freq
    freq = []
    for i in range (1,col_num+1):
        k = np.asarray(data.iloc[:,i].copy())
        freq.append(k)
    
def printers():
    print(freq[0][2])
    print(distance[0])
    print(col_num)

def plott():
    fig = plt.figure(figsize= [ 5,5] )
    for i in range (1,col_num): 
        plt.plot(distance, freq[i],linewidth=1 )
    plt.xlabel('Distance(m)')
    plt.ylabel('Frequency(GHz)')
    plt.title("Distance vs Brillouin Frequency")
    plt.grid(axis='both')
    
    y = FigureCanvasTkAgg(fig, x)
    y.get_tk_widget().pack(side=tkinter.LEFT, fill=tkinter.BOTH,expand = 1)
    toolbar = NavigationToolbar2Tk(y,x) 
    toolbar.update()
    y.get_tk_widget().pack(side=tkinter.LEFT, fill=tkinter.BOTH,expand = 1)


x = Tk()
x.title('BOTDA Interface')
x.geometry("500x500") 
load_button = Button(master = x,  
                     command = open_file, 
                     height = 2,  
                     width = 10, 
                     text = "Load file")
load_button.pack()
plot_button = Button(master = x,  
                     command = plott, 
                     height = 2,  
                     width = 10, 
                     text = "Plot the data")

plot_button.pack()
x.mainloop() 