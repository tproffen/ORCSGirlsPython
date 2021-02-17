#-------------------------------------------------------------------------------------------------------
# Turtle Graphics for Google Colab
# (c) Thomas Proffen, 2021
#-------------------------------------------------------------------------------------------------------
# Based on turtle graphics by Tolga Atam - https://github.com/tolgaatam/ColabTurtle
#
# Module for drawing classic Turtle figures on Google Colab notebooks.
# It uses html capabilites of IPython library to draw svg shapes inline.
# Looks of the figures are inspired from Blockly Games / Turtle (blockly-games.appspot.com/turtle)
#-------------------------------------------------------------------------------------------------------

import IPython
import time
import json
import math
import random
import colorsys

#-------------------------------------------------------------------------------------------------------
# JavaScript and HTML for the output canvas
#-------------------------------------------------------------------------------------------------------
createCanvas = '''
<style>
table {border-collapse: collapse;}
button {width: 80px; margin: 5px 5px 5px 0px; text-align: center; font-size: 1em;}
canvas {margin-top: 5px;}
#status {background-color: #cdcdff; font-size: 1em;}
#art {text-align: center; background-color: #efefff; padding: 0px 5px 0px 5px;}
.right {text-align: right;}
.left {text-align: left;}
.numbers {margin: 0px 10px 0px 10px; font-size: 1em; color: 'purple'; 
white-space: pre; font-family: 'Courier New', monospace;}
</style>
<table>
<tr><td colspan=4 id='art'><canvas id="turtleCanvas"></div></td></tr>
<tr id="status"><td class="left"><div id="info">-</div></td><td class="left"><div id="coord">
<div class='numbers'><b>Mouse</b> - x:   0 y:   0</div></div></td>
<td class="right">Show turtle <input type="checkbox" id="showturtle" onChange="setTurtle();">
<button onClick="replay();" id="replay">Replay</button>
<button onClick="saveImg();" id="save">Save</button></td></tr>
</table>
<script>
function saveImg() {
  var a = document.createElement("a");
  a.download = "turtle.png"; a.href = c.toDataURL("image/png"); a.click();
}
function replay() {
  var t=Math.round(3000/p.length);
  disableControls(true);
  setTimeout(function() { play(t); }, 50);
}
function disableControls(disable) {
  document.getElementById("replay").disabled = disable;
  document.getElementById("save").disabled = disable;
  document.getElementById("showturtle").disabled = disable;
}

function play(delay) {
  clearCanvas(bgcolor);
  cold = ctx.getImageData(0, 0, c.width, c.height);
  if(delay > 0) {
    (function myLoop(i) {
      setTimeout(function() {
        plot(i);
        if (++i < p.length) { myLoop(i); } else { disableControls(false); }
      }, delay)
    })(1);
  } else {
    for (var ip=1; ip<p.length; ip++) { plot(ip); }
    disableControls(false);
  }
}
function plot(ip) {
  clearCanvas(bgcolor);
  ctx.putImageData(cold, 0, 0);
  ctx.fillStyle='red';
  if(p[ip-1].fill!=p[ip].fill   || p[ip-1].width!=p[ip].width || 
     p[ip-1].color!=p[ip].color || p[ip-1].fillcolor!=p[ip].fillcolor ||
     ip==1) {
    if(p[ip-1].fill) {     
      ctx.fillStyle = p[ip-1].fillcolor;
      ctx.fill(); 
    }
    ctx.beginPath();
    ctx.moveTo(p[ip-1].x, p[ip-1].y);
    ctx.strokeStyle = p[ip].color;
    ctx.lineWidth = p[ip].width;
  }
  if(p[ip].pen) { ctx.lineTo(p[ip].x, p[ip].y); }
  else          { ctx.moveTo(p[ip].x, p[ip].y); }
  ctx.stroke();
  cold = ctx.getImageData(0, 0, c.width, c.height);
  showTurtle(p[ip].x, p[ip].y, p[ip].h);
  updateStatus(p[ip].x, p[ip].y, p[ip].h);
}
function updateStatus(x,y,h) {
  px=String(Math.round(x)).padStart(4,' ');
  py=String(Math.round(y)).padStart(4,' ');
  ph=String(Math.round(h)).padStart(4,' ');
  document.getElementById("info").innerHTML=
  "<div class='numbers'><b>Turtle</b> - x:"+px+" y:"+py+" Heading:"+ph+"</div>";
}
function getCoordinates(e) {
  var rect = c.getBoundingClientRect();
  mx=String(Math.round(e.clientX-rect.left)).padStart(4,' ');
  my=String(Math.round(e.clientY-rect.top)).padStart(4,' ');
  document.getElementById("coord").innerHTML=
  "<div class='numbers'><b>Mouse</b> - x:"+mx+" y:"+my+"</div>"; 
}
function showTurtle(x,y,h) {
  if(turtle) {
    ctx.translate(x, y);
    ctx.rotate(h*Math.PI/180.);
    ctx.drawImage(timg, -timg.width/2, -timg.height / 2, timg.width, timg.height);
    ctx.rotate(-h*Math.PI/180.);
    ctx.translate(-x, -y);
  }
}
function clearCanvas(color){
  bgcolor = color;
  ctx.fillStyle = color;
  ctx.fillRect(0, 0, c.width, c.height);
}
function initTurtle() {
  var turl = "https://raw.githubusercontent.com/tproffen/ORCSGirlsPython/master/Images/turtle.png";
  timg = new Image();
  timg.src = turl; timg.setAttribute('crossorigin', 'anonymous');
}
function setTurtle() {
  turtle=document.getElementById("showturtle").checked;
  ctx.putImageData(cold, 0, 0);
  showTurtle(p[p.length-1].x,p[p.length-1].y,p[p.length-1].h);
}
//----------- Functions called from Python ------------------------//
function updateDrawingCanvas(json) { 
  var art = JSON.parse(json);
  bgcolor = art.bgcolor;
  turtle = art.turtle;
  c.width = art.width; c.height = art.height;
  document.getElementById("showturtle").checked = art.turtle;
  document.getElementById("art").style.backgroundColor  = art.canvascolor;
  document.getElementById("status").style.backgroundColor  = art.statuscolor;

  p=art.lines;
  console.log(p.length);
  disableControls(true);
  setTimeout(function() { play(art.delay); }, 50);
}

var c = document.getElementById("turtleCanvas");
var ctx = c.getContext("2d");
var cold = ctx.getImageData(0, 0, c.width, c.height);
var p = [], timg, turtle = false; path = false;

initTurtle(); disableControls(true); c.addEventListener('mousemove',getCoordinates);
</script>
'''

#-------------------------------------------------------------------------------------------------------
# Turtle state and default values
#-------------------------------------------------------------------------------------------------------

defaultCanvas={'bgcolor':'white', 'statuscolor': '#ededff', 'turtle':False,
                 'canvascolor': '#fafafa', 'width':1000, 'height':600, 'delay':0}
defaultTurtle={'pen':False, 'x':0, 'y':0, 'h':0, 'color':'blue', 'width':2, 
                 'fill':False, 'fillcolor':'yellow'}
currentCanvas = defaultCanvas.copy()
currentTurtle = defaultTurtle.copy()
life = False

#-------------------------------------------------------------------------------------------------------
# initializeTurtle(width=width, height=height)
#-------------------------------------------------------------------------------------------------------
def initializeTurtle(initial_window_size=(defaultCanvas['width'],defaultCanvas['height'])):
  global defaultCanvas, defaultTurtle, currentCanvas, currentTurtle, life
  global drawing_window

  drawing_window = display(IPython.display.HTML(createCanvas), display_id=True)
  currentCanvas = defaultCanvas.copy()
  (currentCanvas['width'],currentCanvas['height'])=initial_window_size
  currentCanvas['lines']=[]
  currentTurtle=defaultTurtle.copy()

  _updateTurtleXY(currentCanvas['width']/2, currentCanvas['height']/2, 0.0)
  _updateDrawing()

#-------------------------------------------------------------------------------------------------------
# forward(units)
#-------------------------------------------------------------------------------------------------------
def forward(units):
  global currentCanvas, currentTurtle

  alpha = math.radians(currentTurtle['h'])
  cind = len(currentCanvas['lines'])-1
  endx = currentCanvas['lines'][cind]['x'] + units * math.sin(alpha)
  endy = currentCanvas['lines'][cind]['y'] - units * math.cos(alpha)
  _updateTurtleXY(endx,endy,currentTurtle['h'])

#-------------------------------------------------------------------------------------------------------
# backward(units)
#-------------------------------------------------------------------------------------------------------
def backward(units):
  forward(-units)

#-------------------------------------------------------------------------------------------------------
# setx(x)
#-------------------------------------------------------------------------------------------------------
def setx(x):
  global currentTurtle
  newh = _newHeading(x,currentTurtle['y'])
  _updateTurtleXY(x,currentTurtle['y'],newh)

#-------------------------------------------------------------------------------------------------------
# sety(y)
#-------------------------------------------------------------------------------------------------------
def sety(y):
  global currentTurtle
  newh = _newHeading(currentTurtle['x'],y)
  _updateTurtleXY(currentTurtle['x'],y,newh)

#-------------------------------------------------------------------------------------------------------
# goto(x,y)
#-------------------------------------------------------------------------------------------------------
def goto(x,y):
  global currentTurtle
  newh = _newHeading(x,y)
  _updateTurtleXY(x,y,newh)

#-------------------------------------------------------------------------------------------------------
# jump(x,y)
#-------------------------------------------------------------------------------------------------------
def jump(x,y):
  penup()
  goto(x,y)
  pendown()

#-------------------------------------------------------------------------------------------------------
# getx()
#-------------------------------------------------------------------------------------------------------
def getx():
  global currentTurtle
  return currentTurtle['x']

#-------------------------------------------------------------------------------------------------------
# gety()
#-------------------------------------------------------------------------------------------------------
def gety():
  global currentTurtle
  return currentTurtle['y']

#-------------------------------------------------------------------------------------------------------
# heading()
#-------------------------------------------------------------------------------------------------------
def heading():
  global currentTurtle
  return currentTurtle['h']

#-------------------------------------------------------------------------------------------------------
# face(degrees)
#-------------------------------------------------------------------------------------------------------
def face(degrees):
  global currentCanvas, currentTurtle
  newheading = degrees % 360
  _updateTurtleXY(currentTurtle['x'],currentTurtle['y'],newheading)

#-------------------------------------------------------------------------------------------------------
# left(degrees)
#-------------------------------------------------------------------------------------------------------
def left(degrees):
  global currentCanvas, currentTurtle
  newheading = (currentTurtle['h'] - degrees) % 360
  _updateTurtleXY(currentTurtle['x'],currentTurtle['y'],newheading)

#-------------------------------------------------------------------------------------------------------
# right(degrees)
#-------------------------------------------------------------------------------------------------------
def right(degrees):
  left(-degrees)

#-------------------------------------------------------------------------------------------------------
# penup
#-------------------------------------------------------------------------------------------------------
def penup():
  global currentTurtle
  currentTurtle['pen']=False

#-------------------------------------------------------------------------------------------------------
# pendown
#-------------------------------------------------------------------------------------------------------
def pendown():
  global currentTurtle
  currentTurtle['pen']=True

#-------------------------------------------------------------------------------------------------------
# show
#-------------------------------------------------------------------------------------------------------
def show():
  _updateDrawing()

#-------------------------------------------------------------------------------------------------------
# liveon
#-------------------------------------------------------------------------------------------------------
def liveon():
  global life
  life=True

#-------------------------------------------------------------------------------------------------------
# liveon
#-------------------------------------------------------------------------------------------------------
def liveoff():
  global life
  life=False

#-------------------------------------------------------------------------------------------------------
# speed(delay)
#-------------------------------------------------------------------------------------------------------
def speed(delay):
  global currentCanvas;
  currentCanvas['delay']=delay     # delay is in ms between points

#-------------------------------------------------------------------------------------------------------
# bgcolor(color)
#-------------------------------------------------------------------------------------------------------
def bgcolor(color):
  global currentCanvas, life;
  currentCanvas['bgcolor']=color
  if (life): _updateDrawing()

#-------------------------------------------------------------------------------------------------------
# color(color)
#-------------------------------------------------------------------------------------------------------
def color(color):
  global currentTurtle
  currentTurtle['color']=color

#-------------------------------------------------------------------------------------------------------
# fillcolor(color)
#-------------------------------------------------------------------------------------------------------
def fillcolor(color):
  global currentTurtle
  currentTurtle['fillcolor']=color

#-------------------------------------------------------------------------------------------------------
# begin_fill()
#-------------------------------------------------------------------------------------------------------
def begin_fill():
  global currentTurtle
  currentTurtle['fill']=True

#-------------------------------------------------------------------------------------------------------
# end_fill()
#-------------------------------------------------------------------------------------------------------
def end_fill():
  global currentTurtle
  currentTurtle['fill']=False
  _updateTurtleXY(currentTurtle['x'],currentTurtle['y'],currentTurtle['h'])

#-------------------------------------------------------------------------------------------------------
# width(width)
#-------------------------------------------------------------------------------------------------------
def width(width):
  global currentTurtle
  currentTurtle['width']=width

#-------------------------------------------------------------------------------------------------------
# showturtle()
#-------------------------------------------------------------------------------------------------------
def showturtle():
  global currentCanvas, life;
  currentCanvas['turtle']=True
  if (life): _updateDrawing()

#-------------------------------------------------------------------------------------------------------
# hideturtle()
#-------------------------------------------------------------------------------------------------------
def hideturtle():
  global currentCanvas, life;
  currentCanvas['turtle']=False
  if (life): _updateDrawing()

#-------------------------------------------------------------------------------------------------------
# Color functions - inputs are from 0.0 to 1.0
#-------------------------------------------------------------------------------------------------------

def color_rgb(r, g, b):
    rgb = list(round(i * 255) for i in [r, g, b])
    return  '#'+''.join(f'{i:02x}' for i in rgb)

def color_hsv(h, s, v):
    rgb = list(round(i * 255) for i in colorsys.hsv_to_rgb(h,s,v))
    return '#'+''.join(f'{i:02x}' for i in rgb)

def color_random():
  return "#%06x" % random.randint(0, 0xFFFFFF)

#-------------------------------------------------------------------------------------------------------
# Internal functions
#-------------------------------------------------------------------------------------------------------
def _updateDrawing():
  global currentCanvas, drawing_window
  if(drawing_window == None):
    raise AttributeError("Display has not been initialized yet. Call initializeTurtle() before using.")

  jsondrawing = json.dumps(currentCanvas)
  #print(jsondrawing)
  cmd='updateDrawingCanvas(\''+jsondrawing+'\')'
  display(IPython.display.Javascript(cmd))

#-------------------------------------------------------------------------------------------------------
def _updateTurtleXY(nx,ny,nh):
  global currentTurtle, currentCanvas, life
  currentTurtle['x'] = nx
  currentTurtle['y'] = ny
  currentTurtle['h'] = nh
  currentCanvas['lines'].append(currentTurtle.copy())
  if (life): _updateDrawing()
#-------------------------------------------------------------------------------------------------------
def _newHeading(x,y):
  global currentCanvas
  cind = len(currentCanvas['lines'])-1
  h = math.degrees(math.atan2(x-currentCanvas['lines'][cind]['x'],currentCanvas['lines'][cind]['y']-y))
  h = (h + 360) % 360
  return h
