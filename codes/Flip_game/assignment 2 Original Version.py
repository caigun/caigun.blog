import turtle
import random


#constants
SIZE = 5
RESPONSE_TIME = 30  # the refresh rate of the live select box, the less the faster

#global variables
g_numberSet = []  #store the data of the sheet

g_colorList = ["yellow1", "lawn green", "RoyalBlue1", 
            "orange", "dark orchid", "purple", 
            "firebrick1", "sky blue", "peach puff", 
            "honeydew2", "gray73", "red4", 
            "cyan", "midnight blue"]  #stores the color names that can be used

g_digitRange = 5  #the total number of colors that will appear each game

g_x, g_y = 0, 0  #the coordinates of the selected button

g_targetNumber = None  #the coordinates of the selected color n
g_targetEntry = None  #the coordinates of the selected entry (x, y)

g_draw = turtle.Turtle(shape = "square")  # the turtle used for graphics

g_box = turtle.Turtle(shape = "square")  # the turtle used for the UI (selecting the color bar)

g_title = turtle.Turtle()  # the turtle used for the texts

g_select = turtle.Turtle()  # the turtle used for indicating which block the user is selecting

g_steps = 0  # the steps that the player use



def mouse(x, y):  # to draw the select bar when user clicks one of the blocks, and return the coordinates of the chosen block

    global g_x, g_y, g_targetNumber, g_targetEntry, g_box

    # set the coordinates with respect to the first block
    x += 185
    y += 120

    # calculate the coordinates using block coordinates (a, b)
    # where 1 <= a <= 5, 1 <= b <= 5
    # and when the block is the color choosing bar, b = "bar"

    x_coordinate = int(x//70)

    if y <= -50 and y >= -110:
        y_coordinate = "bar"
    else:
        y_coordinate = int(SIZE - y//70 -1)

    # to draw the select indication (a thin black edge)

    if (x_coordinate <= 4 and x_coordinate >= 0) and\
        y_coordinate == "bar":

        g_targetNumber = x_coordinate

        g_box.setposition(-150 + x_coordinate * 70, -200)

        g_box.clearstamps()
        g_box.stamp()

        g_draw.setposition(-150 + x_coordinate * 70, -200)
        g_draw.color(g_colorList[x_coordinate])
        g_draw.stamp()
    
    elif  x_coordinate <= 4 and x_coordinate >= 0 and\
        y_coordinate <= 4 and y_coordinate >= 0:

        g_box.setposition(-150 + x_coordinate * 70, 200 - y_coordinate * 70)

        g_box.clearstamps()
        g_box.stamp()

        g_draw.setposition(-150 + x_coordinate * 70, 200 - y_coordinate * 70)
        g_draw.color(g_colorList[g_numberSet[x_coordinate + y_coordinate * 5]])
        g_draw.stamp()

        g_targetEntry = (x_coordinate, y_coordinate)


def liveSelectBar():  # is used to draw the live select state, showing the users which blocks they are selecting

    global g_select, g_targetEntry, g_colorList, g_targetNumber
    
    # stores the information about the mouse and the window's location and size
    canvas = turtle.getcanvas()
    x1, y1 = canvas.winfo_pointerxy()   
    rx, ry = canvas.winfo_rootx(), canvas.winfo_rooty()
    wx, wy = canvas.winfo_width(), canvas.winfo_height()
    dwx = wx - 500
    dwy = wy - 600

    x1 =  x1 - rx - 70 - dwx/2
    y1 =  y1 - ry - 70 - dwy/2

    xb = int(x1//70)

    if y1 <= 470 and y1 >= 400:
        yb = "bar"
    else:
        yb = int(y1//70)

    # if the bar is already been selected, then no live selecting state is shown
    if (xb, yb) == g_targetEntry or (xb, yb) == (g_targetNumber, "bar"):
        pass
    
    # otherwise draw the live selecting state (the block will be enlarged a little bit)
    elif (xb <= 4 and xb >= 0) and yb == "bar":

        g_select.setposition(-150 + xb * 70, -200)

        g_select.clearstamps()

        g_select.color(g_colorList[xb])
        g_select.stamp()
    
    elif  xb <= 4 and xb >= 0 and\
        yb <= 4 and yb >= 0:

        g_select.setposition(-150 + xb * 70, 200 - yb * 70)
        g_select.clearstamps()
        g_select.color(g_colorList[g_numberSet[xb + yb * 5]])
        g_select.stamp()


def getCoordinate():  # main function when the game is running

    global g_targetEntry, g_targetNumber, g_title, g_draw, g_steps, g_box

    liveSelectBar()

    # below are for the user input
    if g_targetEntry != None and g_targetNumber != None:
        connectNumber(g_targetNumber, g_targetEntry[1] * SIZE + g_targetEntry[0])

        g_box.clearstamps()

        g_targetNumber = None
        g_targetEntry = None

        printSheet()

        g_steps += 1

    if len(set(g_numberSet)) != 1:
        turtle.ontimer(getCoordinate, t = RESPONSE_TIME)
    
    # detects the game ends and ask for a new game
    else:
        g_title.clear()
        g_title.setposition(-60, 240)
        g_title.write("Solved!", font = ("Verdana", 20, "normal"))

        g_title.setposition(-80, -150)
        g_title.write("Steps used: "+str(g_steps), font = ("Verdana", 18, "normal"))

        g_title.setposition(-230, -270)
        g_title.write("Select both sheet and color bar to start a new game!", font = ("Verdana", 13, "normal"))

        g_steps = -1

        g_box.clear()

        turtle.ontimer(restart, t = 200)  # wait for the start signal

def restart():

    if g_targetEntry != None and g_targetNumber != None:

        g_title.clear()

        createGame()
    
        turtle.ontimer(getCoordinate, t = 100)

    else:

        liveSelectBar()

        turtle.ontimer(restart, t = RESPONSE_TIME)




def printSheet():  # print the board

    g_draw.setposition(-150, 200)

    i = 0

    while i < SIZE**2:

        if i == SIZE**2 - 1:
            g_draw.color(g_colorList[g_numberSet[i]])
            g_draw.stamp()

        if (i + 1) % SIZE == 0:

            g_draw.color(g_colorList[g_numberSet[i]])  # reset to left align
            g_draw.stamp()
            g_draw.setheading(-90)
            g_draw.forward(70)
            g_draw.setheading(180)
            g_draw.forward(280)
            g_draw.setheading(0)

        else:

            g_draw.color(g_colorList[g_numberSet[i]])
            g_draw.stamp()
            g_draw.forward(70)

        i += 1



def connectNumber(number, index):  # use recursion to filp the numbers(colors) one by one
    
    target = g_numberSet[index]
    g_numberSet[index] = number

    if number == target:
        return None

    if (index + 1) % SIZE != 0 and g_numberSet[index + 1] == target:
            connectNumber(number, index + 1)

    if g_numberSet[index - 1] == target and index % SIZE != 0:
        connectNumber(number, index -1)

    if (index + SIZE) <= len(g_numberSet) - 1:
        if g_numberSet[index + SIZE] == target:
            connectNumber(number, index + SIZE)

    if (index - SIZE) >= 0:
        if g_numberSet[index - SIZE] == target:
            connectNumber(number, index - SIZE)



def createGame():  # initialize the gameboard
    
    global g_numberSet, g_colorList, g_targetNumber, g_targetEntry, g_draw, g_title

    g_numberSet = []

    random.shuffle(g_colorList)

    g_draw.clear()

    for i in range(SIZE**2):
        g_numberSet.append(random.randint(0, g_digitRange-1))

    g_title.setposition(-200, 250)
    g_title.color("black")
    g_title.write("Filp all the colors with the fewest steps!", font = ("Verdana", 15, "normal"))

    printSheet()

    # draw the color choosing bar
    g_draw.setposition(-150,-200)
    g_draw.setheading(0)

    for i in range(g_digitRange):
        g_draw.color(g_colorList[i])
        g_draw.stamp()
        g_draw.forward(70)


if __name__ == "__main__":

    #initialize the window
    sc = turtle.Screen()
    sc.setup(500, 600)
    turtle.title("Filp Game")

    #initialize the turtles
    turtle.tracer(False)

    g_draw.hideturtle()
    g_box.hideturtle()
    g_title.hideturtle()
    g_select.hideturtle()

    g_draw.up()
    g_box.up()
    g_title.up()
    g_select.up()

    g_box.shape("square")
    g_box.shapesize(3.4)

    g_draw.shape("square")
    g_draw.shapesize(3)
    g_draw.color("white")

    g_select.shape("square")
    g_select.shapesize(1)

    g_select.stamp()
    g_select.shapesize(3.4)

    sc.onclick(mouse)

    createGame()

    turtle.ontimer(getCoordinate, t = 100)

    turtle.listen()
    turtle.mainloop()