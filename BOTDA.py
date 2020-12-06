import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def freq_plotter(filename):
  with open (filename , 'r') as file:
    lines = file.readlines()
  line = len(lines)
  for i in range (0,line):
    x = re.search("measurements", lines[i])
    if x:col_num = int(re.findall(r"[-+]?\d*\.?\d+|\d+", lines[i])[0]);break
  data = pd.read_csv(filename, skiprows = 41, sep='\t', header=0, names=list(range(col_num+1) ), index_col=False, dtype=float)
  distance = np.asarray( df.iloc[:,0].copy())
  freq = []
  for i in range (1,col_num+1):
    k = np.asarray(df.iloc[:,i].copy())
    freq.append(k)
  fig = plt.figure(figsize= [ 18,10] )
  for i in range (1,col_num): 
    plt.plot(distance, freq[i],linewidth=1 )
  plt.xlabel('Distance(m)')
  plt.ylabel('Frequency(GHz)')
  plt.title("Distance vs Brillouin Frequency")
  plt.grid(axis='both')
  plt.show()

freq_plotter('insert_file_name.txt') // give filename here