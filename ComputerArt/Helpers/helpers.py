from Helpers.turtleCanvas import *
from numpy import arange
import math

#------------------------------------------------------------------------
# Some useful helper functions
#------------------------------------------------------------------------
def grid(delta):
  xmax=1000
  ymax=1000

  penup()
  width(1)
  for x in range(0,1000,delta):
    goto(x,0)
    pendown()
    goto(x,ymax)
    penup()
  for y in range(0,1000,delta):
    goto(0,y)
    pendown()
    goto(xmax,y)
    penup()
    