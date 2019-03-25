
#Turtle Recursion (25pts)

#1)  Using the turtle library, create the H fractal pattern according to the file shown in the data folder. (10pts)  

#2)  Using the turtle library, create any of the other recursive patterns in the data folder. 
#  Challenge yourself to match your pattern as closely as you can to the image.  (10pts)
#  Note:  The Koch snowflake shows step by step building of the fractal.  
#  The rectangle fractal example shows 4 possible drawings of the same fractal (choose any one)


#3)  Create your own work of recursive art with a repeating pattern of your making (or choose another one from the files).  
#  It must be a repeated pattern using recursion (not just loops). Snowflakes, trees, and spirals are a common choice.  
#  Play around and have fun with it.  (5pt) 

#  General expectations for all problems
#  Give all your fractals a depth of at least 4.  (Don't make programs that take forever though)  
#  Ensure the recursive drawing is contained on the screen (at whatever size you set it).
#  All three recursive drawings can be on the same program.  Just use screen.clear() between problems.  Alternately, you could draw to three different screen objects.
#  Run your turtles at max speed.
#  Have fun!
 
#  Resource to help you out >>> https://docs.python.org/3.3/library/turtle

import turtle
import math

my_turtle = turtle.Turtle()  # create a turtle object
my_screen = turtle.Screen()  # create a screen object

my_turtle.width(4)
my_turtle.speed(0)
turtle.delay(0)
turtle.ht()

#IT'S TILTED
def htree(depth, center, size):

    if depth < 0:
        return

    if center is not None:
        turtle.up()
        turtle.goto(center)
        turtle.down()

    turtle.forward(size / 2)
    turtle.right(90)
    turtle.forward(size / 2)
    turtle.left(90)

    htree(depth - 1, None, size / 2)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(270)

    htree(depth - 1, None, size / 2)
    turtle.right(90)
    turtle.forward(size / 2)
    turtle.right(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size / 2)
    turtle.right(90)

    htree(depth - 1, None, size / 2)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)

    htree(depth - 1, None, size / 2)
    turtle.right(90)
    turtle.forward(size / 2)
    turtle.left(90)
    turtle.forward(size / 2)


htree(3, (0,0), 100)

my_screen.clear()

def escher(depth, size):

    if depth > 0:
        turtle.up()
        turtle.goto(size / 2, size / 2)
        turtle.down()

        turtle.right(90)
        turtle.forward(size)
        turtle.right(90)
        turtle.forward(size)
        turtle.right(90)
        turtle.forward(size)
        turtle.right(90)
        turtle.forward(size)

        turtle.goto(0, size / 2)
        turtle.right(45)
        pythag = math.sqrt(size**2 + size**2) / 2
        turtle.forward(pythag)
        turtle.right(90)
        turtle.forward(pythag)
        turtle.right(90)
        turtle.forward(pythag)
        turtle.right(90)
        turtle.forward(pythag)
        turtle.right(45)

        escher(depth - 1, size / 2)


escher(9, 500)

my_screen.clear()
'''
def triangle (depth, size):

    if depth > 0:
        turtle.up()
        turtle.goto(0, size / 3)
        turtle.down()

        pos1 = turtle.position()
        turtle.right(60)
        turtle.forward(size)
        pos2 = turtle.position()
        turtle.right(120)
        turtle.forward(size)
        pos3 = turtle.position()
        turtle.right(60)
        turtle.forward(size)

        turtle.goto(pos1)
        turtle.right(60)
        turtle.forward(size)
        turtle.right(60)
        turtle.forward(size)
        turtle.right(60)
        turtle.forward(size)




triangle(1, 100)
'''

def that_thing (depth, size):

    if depth > 0:
        turtle.up()
        turtle.goto(size / 4, size / 4)
        turtle.down()

        turtle.right(90)
        turtle.forward(size * (4/6))
        pos = turtle.position()
        turtle.forward(size * (2/6))
        turtle.goto(pos)

        turtle.right(90)
        turtle.forward(size * (4 / 6))
        pos = turtle.position()
        turtle.forward(size * (2 / 6))
        turtle.goto(pos)

        turtle.right(90)
        turtle.forward(size * (4 / 6))
        pos = turtle.position()
        turtle.forward(size * (2 / 6))
        turtle.goto(pos)

        turtle.right(90)
        turtle.forward(size * (4 / 6))
        pos = turtle.position()
        turtle.forward(size * (2 / 6))
        turtle.goto(pos)

        that_thing(depth - 1, size / 2)

that_thing(9, 400)


my_screen.exitonclick()
