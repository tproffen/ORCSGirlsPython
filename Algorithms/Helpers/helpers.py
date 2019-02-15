import matplotlib.pyplot as plt
import matplotlib
import time
from IPython import display

# Plotting 

def updateGraph(i, data):
  plt.style.use('bmh');
  matplotlib.rcParams.update({'font.size': 14});
  matplotlib.rcParams.update({'figure.figsize': [12.0, 6.0]});

  colors = ["blue" for x in range(len(data))];
  colors[i] = "red";
  colors[i+1] = "red";
  
  positions = range(len(data));
  plt.clf();
  plt.bar(positions, data, color=colors);
  display.display(plt.gcf()); 
  display.clear_output(wait=True);
  time.sleep(0.2);

