import matplotlib.pyplot as plt
import numpy as np

def plotData(matrix):
  
  y = np.arange(0, 101)
  x = np.percentile(matrix, y)
  plt.plot(x, y) 
  plt.xlabel('Value')
  plt.ylabel('Percentile')
  plt.title('ECDF of matrix A')
  plt.show()