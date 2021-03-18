from Helpers.turtleCanvas import *
from Helpers.quickdraw.data import *
from matplotlib import pyplot as plt
from datetime import datetime
from numpy import arange

import random
import math

#------------------------------------------------------------------------
# Some plotting helpers
#------------------------------------------------------------------------

def plot_image(img):
  plt.figure()
  plt.imshow(image)
  plt.axis("off")
  plt.show()

def plot(numbers, labels):
  plt.figure(figsize=(12, 8))
    
  pos = list(range(len(numbers)))
  plt.bar(pos, numbers)
  plt.xticks(pos, list(labels), rotation=90)    
  plt.show()
