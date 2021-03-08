# Artistic Math

These activities use a modified version of [ColabTurtle](https://github.com/tolgaatam/ColabTurtle) developed by [Tolga Atam](https://github.com/tolgaatam). Here is a list of commands you can use to draw.

* **`initializeTurtle(initial_window_size=WINDOW_SIZE, mode=DAWRINGMODE)`** Initializes the drawing display. This command needs to be called *first*. The parameters are options. For example `initializeTurtle()` will create a drawing area with the default size and drawing speed. To create a area of e.g. 1000 x 800 pixles, you would use the command `initializeTurtle(initial_window_size=(1000,800))`. The optional parameter `mode` can take three values: `auto` which will pick between an interactive plot and statig plot depending on the number of points. `svg` will select a static plot and `canvas` will select the interactive (you can replay the plot) version.
* **`forward(units)`** Moves the turtle (pen) forward by the amount `units`. 
* **`backward(units)`** Moves the turtle (pen) backward by the amount `units`. 
* **`right(degrees)`**  Turns the direction of the turtle (pen) to the right by `degrees`.
* **`face(degrees)`** Sets the direction or heading  of the turtle (pen) to `degrees`.
* **`left(degrees)`** Turns the direction of the turtle (pen) to the left by `degrees`.
* **`penup()`** Pen up. No lines will be drawn.
* **`pendown()`** Pen down. Lines between points will be drawn.
* **`speed(speed)`** Set drawing speed to `speed` (in lines/second).
* **`begin_fill()`** Start an area to be filled.
* **`end_fill()`** Ends the area to be filled.
* **`setx(x)`** Set turtle x position to `x`.
* **`sety(y)`** Set turtle y position to `y`.
* **`getx()`** Get the current x position of the turtle.
* **`gety()`** Get the current y position of the turtle.
* **`heading()`** Get the current heading of the turtle.
* **`goto(x, y)`** Set turtle position to `x,y`.
* **`showturtle()`** Show the turtle symbol on drawing.
* **`hideturtle()`** Hide the turtle symbol on drawing.
* **`show()`** Show current drawing.
* **`fillcolor(color)`** Sets the fill color (CSS names and #xxxxxx allowed)
* **`bgcolor(color)`** Set background color to `color` (CSS color names and #xxxxxx format allowed).
* **`color(color)`** Set line color to `color` (CSS color names and #xxxxxx format allowed).
* **`width(width)`** Set line width.

And there are some color helper functions. The returned value can be used as argument for the `color` and `bgcolor` commands.

* **`color_rgb(r,g,b)`** Returns HEX color string given by values `r` (red), `g` (green), and `b` (blue). Note these range from 0.0 to 1.0
* **`color_hsv(h,s,v)`** Returns HEX color string given by values `h` (hue), `s` (saturation), and `v` (vibrance). Note these range from 0.0 to 1.0
* **`color_random()`** Return a HEX string of a random color.

Contact: [thomas@orcsgirls.org](mailto:thomas@orcsgirls.org)
