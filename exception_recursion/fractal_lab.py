
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

my_turtle = turtle.Turtle()  # create a turtle object
my_screen = turtle.Screen()  # create a screen object

my_turtle.width(4)
my_turtle.speed(0) # 0 means as fast as it will
my_turtle.shape("turtle") # makes the pen that draws it look like a turtle

def h_tree(x, y, size, depth):
    # top of the C bracket

    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.pendown()
    my_turtle.setheading(90)
    my_turtle.forward(size)
    my_turtle.right(270)
    my_turtle.forward(size)
    my_turtle.right(180)
    my_turtle.forward(size * 2)
    my_turtle.goto(x, y)
    my_turtle.setheading(270)
    my_turtle.forward(size)
    my_turtle.left(270)
    my_turtle.forward(size)
    my_turtle.left(180)
    my_turtle.forward(size * 2)

h_tree(0, 0, 80, 1)

my_screen.exitonclick()
