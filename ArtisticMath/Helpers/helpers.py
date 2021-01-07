from ColabTurtle.Turtle import *
import math

#------------------------------------------------------------------------
# Different curve functions
#------------------------------------------------------------------------
def roseCurve(x_start, y_start, sizefactor, petalsCount):

  speed(10)
  penup()
  x = x_start
  y = y_start
  goto(x, y)
  pendown()
  penup()
 
  for t in range(1000):
    tdiv = t/100
    k = petalsCount
    ktx = k*tdiv
    kty = k*tdiv
    x = math.cos(tdiv)
    x*=math.cos(ktx)
    x *= sizefactor
    y=(math.sin(tdiv))
    y *= math.cos(kty)
    y *= sizefactor
    x = round(x)
    y = round(y)
    goto(x+x_start, y+y_start)
    pendown()


#------------------------------------------------------------------------
def parabola(x_start, y_start, sizefactor):

  speed(10)
  penup()
  x = x_start
  y = y_start
  goto(x, y)
  pendown()
  penup()
 
  for t in range(-100,100):
    tdiv = t/100
    x = tdiv
    x *= sizefactor*3
    y = tdiv*tdiv
    y *= sizefactor*3
    x = round(x)
    y = round(y)
    goto(x+x_start, y+y_start)
    pendown()
    
#------------------------------------------------------------------------
def spiral(x_start, y_start, sizefactor, spiralLength):

  speed(10)
  penup()
  x = x_start
  y = y_start
  goto(x, y)
  pendown()
  
 
  for t in range(1,spiralLength):
    tdiv = t/10
    x = tdiv*math.cos(tdiv)
    x *= sizefactor
    y = tdiv*math.sin(tdiv)
    y *= sizefactor
    y = round(y)
    x = round(x)
    goto(x+x_start, y+y_start)


#------------------------------------------------------------------------
def circle(x_start, y_start, sizefactor):

  speed(10)
  penup()
  tdivv = 0
  x = x_start
  y = y_start
  goto(x, y)
  penup()
 
  for t in range(1,65):
    tdiv = t/10
    x = math.cos(tdiv)
    x *= sizefactor
    y = math.sin(tdiv)
    y *= sizefactor
    goto(x+x_start, y+y_start)
    pendown()

#------------------------------------------------------------------------
def polygon(x_start, y_start, sizefactor, numSides):

  speed(10)
  penup()
  x = x_start
  y = y_start
  pendown()
  
  fulldegrees = (((numSides-2)*180))
  print(fulldegrees)
  angle = 180-(fulldegrees/numSides)
  print(angle)
 
  for t in range(1,numSides+1):
    left(angle)
    forward(sizefactor)

#------------------------------------------------------------------------
def bowtie(x_start, y_start, sizefactor):
 
  speed(10)
  penup()
  tdivv = 0
  x = x_start
  y = y_start
  goto(x, y)
  pendown()
 
  for t in range(1,14):
    for tdiv in range(1,100):
      tdivv = (tdiv/100)+t
      x = 2 * tdivv
      x += (2 * math.cos( 14* tdivv))
      x += (1/tdivv)
      y = 2 * tdivv
      y += (2 * math.sin( 15 * tdivv))
      y += (1/tdivv)
      x *= sizefactor
      y *= sizefactor
      x = round(x)
      y = round(y)
      goto(x+x_start, y+y_start)
