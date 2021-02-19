from Helpers.turtleCanvas import *
from numpy import arange
import math

#------------------------------------------------------------------------
def koch(size, order):

    if order > 0:
        for t in [60, -120, 60, 0]:
            koch(size/3, order-1)
            left(t)
    else:
      pendown()
      forward(round(size))

#------------------------------------------------------------------------
def snowflake(x_start, y_start, size, order):

  # goto center
  penup()
  goto(x_start, y_start)
  backward(round(size/1.732))
  left(30)
  pendown()

  # Three Koch curves
  for i in range(3):
      koch(size, order)
      right(120)