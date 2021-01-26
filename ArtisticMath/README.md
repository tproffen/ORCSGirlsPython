# Artistic Math

The activities use a modified version of [ColabTurtle](https://github.com/tolgaatam/ColabTurtle) developed by [Tolga Atam](https://github.com/tolgaatam). Here is a list of commands you can use to draw.

* **`initializeTurtle(initial_speed=DEFAULT_SPEED, initial_window_size=DEFAULT_WINDOW_SIZE)`** Initializes the drawing display. This command needs to be called *first*. The parameters are options. For example `initializeTurtle()` will create a drawing area with the default size and drawing speed. To create a area of e.g. 1000 x 800 pixles, you would use the command `initializeTurtle(initial_window_size=(1000,800))`
* **`forward(units)`** Moves the turtle (pen) forward by the amount `units`. 
* **`backward(units)`** Moves the turtle (pen) backward by the amount `units`. 
* **`right(degrees)`**  Turns the direction of the turtle (pen) to the right by `degrees`.
* **`face(degrees)`** Sets the direction or heading  of the turtle (pen) to `degrees`.
* **`left(degrees)`** Turns the direction of the turtle (pen) to the left by `degrees`.
* **`penup()`** Pen up. No lines will be drawn.
* **`pendown()`** Pen down. Lines between points will be drawn.
* **`speed(speed)`** Set drawing speed to `speed` (1:slowest, 13: fastest).
* **`setx(x)`** Move turtle x position to `x`.
* **`sety(y)`** Move turtle y position to `y`.
* **`getx()`** Get the current x position of the turtle.
* **`gety()`** Get the current y position of the turtle.
* **`goto(x, y)`** Move turtle position to `x,y`.
* **`jump(x, y)`** Set turtle position to `x,y` (no line drawn).
* **`showturtle()`** Show the turtle symbol on drawing.
* **`hideturtle()`** Hide the turtle symbol on drawing.
* **`liveon()`** Show drawing step by step.
* **`liveoff()`** Do not show drawing until `show()` command.
* **`show()`** Show current drawing.
* **`bgcolor(color)`** Set background color to `color` (CSS color names and #xxxxxx format allowed).
* **`color(color)`** Set line color to `color` (CSS color names and #xxxxxx format allowed).
* **`width(width)`** Set line width.

Contact: [thomas@orcsgirls.org](mailto:thomas@orcsgirls.org)
