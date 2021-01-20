from Helpers.turtle import *
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
    
#------------------------------------------------------------------------
# Different curve functions
#------------------------------------------------------------------------
def roseCurve(x_start, y_start, sizefactor, petalsCount):

  penup()

  for t in arange(0,10,0.05):
    x = sizefactor * (math.cos(t) * math.cos(t*petalsCount))
    y = sizefactor * (math.sin(t) * math.cos(t*petalsCount))
    goto(x+x_start, y+y_start)
    pendown()

#------------------------------------------------------------------------
def parabola(x_start, y_start, sizefactor):

  penup()
  
  for t in arange(-1,1,0.05):
    x = sizefactor * t
    y = sizefactor * t*t
    goto(x+x_start, y+y_start)
    pendown()
    
#------------------------------------------------------------------------
def spiral(x_start, y_start, sizefactor, spiralLength):

  penup()

  for t in arange(1,spiralLength,0.05):
    x = sizefactor * t * math.cos(t)
    y = sizefactor * t * math.sin(t)
    goto(x+x_start, y+y_start)
    pendown()

#------------------------------------------------------------------------
def circle(x_start, y_start, sizefactor):

  penup()

  for t in arange(0.0,6.5,0.05):
    x = sizefactor * math.cos(t)
    y = sizefactor * math.sin(t)
    goto(x+x_start, y+y_start)
    pendown()

#------------------------------------------------------------------------
def polygon(x_start, y_start, sizefactor, numSides):

  penup()
  goto(x_start, y_start)
  pendown()
  
  fulldegrees = (((numSides-2)*180))
  angle = 180-(fulldegrees/numSides)
  print('Angle: '+angle)
 
  for t in range(1,numSides+1):
    left(angle)
    forward(sizefactor)

#------------------------------------------------------------------------
def bowtie(x_start, y_start, sizefactor):
 
  penup()

  for u in arange(1,14):
    for v in arange(0.0,1.0,0.01):
      t = u + v
      x = sizefactor * (2*t + 2*math.cos(14*t) + 1/t)
      y = sizefactor * (2*t + 2*math.sin(15*t) + 1/t)
      goto(x+x_start, y+y_start)
      pendown()
