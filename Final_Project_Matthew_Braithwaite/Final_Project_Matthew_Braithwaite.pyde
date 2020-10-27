# Name: Matthew Braithwaite
# Course: Computer Science 20
# Date Created: 10/23/2020
# Description: You will be able to make your own drawings with the circle tool. You can also add shapes, edit the circle, and change the colour of circles and background alike.


x = 50
y = 50


# Function with text and starting colors
def setup():
    size(750, 750)
    frameRate(120)
    fill(255)
    background(0)
    print("In the text box below, you will be able to see all possible commands for this program.")
    print("+ will make the circle larger.")
    print("- will make the circle smaller.")
    print("r will make the circle red.")
    print("g will make the circle green.")
    print("b will make the circle blue.")
    print("p will make the circle purple.")
    print("u will make the circle yellow.")
    print("c will make the circle cyan.")
    print("k will make the circle pink.")
    print("0 (zero) will make the circle black.")
    print("1 (one) will make the circle white. Default circle colour.")
    print("R will make the background red.")
    print("G will make the background green.")
    print("B will make the background blue.")
    print("P will make the background purple.")
    print("U will make the background yellow.")
    print("C will make the background cyan.")
    print("K will make the background pink.")
    print("* will make the background black. Default background colour.")
    print("& will make the background white.")
    print("9 will place a square on your cursor's location.")
    print("8 will place a rectangle on your cursor's location.")
    print("7 will place a line on your cursor's location.")
    print("Q will reset everything to how it originally was.")
    print("X will let you increase the length of the circle.")
    print("Y will let you increase the height of the circle.")
    print("x will let you decrease the length of the circle.")
    print("y will let you decrease the height of the circle.")
    print("It is recommended that you use the program with Processing in full screen so you can see the commands better.")


def keyPressed():
    """This function contains all of the possible user inputs.
    """
    global x
    global y
# Increases size of the circle
    if key == "+":
        x = x + 10
        y = y + 10
# Reduces size of the circle
    elif key == "-":
        x = x - 10
        y = y - 10
# Makes the circle red
    elif key == "r":
        fill(255, 0, 0)
# Makes the circle green
    elif key == "g":
        fill(0, 255, 0)
# Makes the circle blue
    elif key == "b":
        fill(0, 0, 255)
# Makes the circle purple
    elif key == "p":
        fill(127, 0, 255)
# Makes the circle yellow
    elif key == "u":
        fill(255, 255, 0)
# Makes the circle cyan
    elif key == "c":
        fill(0, 255, 255)
# Makes the circle pink
    elif key == "k":
        fill(255, 0, 200)
# Makes the circle black
    elif key == "0":
        fill(0)
# Makes the circle white
    elif key == "1":
        fill(255)
# Makes the background red
    elif key == "R":
        background(255, 0, 0)
# Makes the background green
    elif key == "G":
        background(0, 255, 0)
# Makes the background blue
    elif key == "B":
        background(0, 0, 255)
# Makes the background purple
    elif key == "P":
        background(127, 0, 255)
# Makes the background yellow
    elif key == "U":
        background(255, 255, 0)
# Makes the background cyan
    elif key == "C":
        background(0, 255, 255)
# Makes the background pink
    elif key == "K":
        background(255, 0, 200)
# Makes the background black
    elif key == "*":
        background(0)
# Makes the background white
    elif key == "&":
        background(255)
# Places down a square at the cursor's location
    elif key == "9":
        square(mouseX, mouseY, 50)
# Places down a rectangle at the cursor's location
    elif key == "8":
        rect(mouseX, mouseY, 50, 70)
# Places down a line at the cursor's location.
    elif key == "7":
        triangle(mouseX, mouseY, 50, 50, 50, 50)
# Resets everything
    elif key == "Q":
        fill(255)
        background(0)
        x = 50
        y = 50
# Increases the length of the circle
    elif key == "X":
        x = x + 10
# Increases the height of the circle
    elif key == "Y":
        y = y + 10
# Decreases the length of the circle
    elif key == "x":
        x = x - 10
# Decreases the height of the circle
    elif key == "y":
        y = y - 10


# This is the function that draws the circle every frame
def draw():
    ellipse(mouseX, mouseY, x, y)
