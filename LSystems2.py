import turtle


# --------------------------------------------------------------------------
# These functions take a string-based L-System and create a string by applying
# the rewriting rules


def createLSystem(numIters, axiom, rules):
    """Takes in the number of iterations of the rewriting process, the starting
    axiom, and a list of rules. Each rule is a sublist with the symbol on the lefthand side
    first, followed by a string for the righthand side. Returns the final string."""
    currString = axiom
    nextString = ""
    for i in range(numIters):
        nextString = processString(currString, rules)
        currString = nextString
    return nextString


def processString(oldStr, rules):
    """Processes the current string by going through character by character and
    replacing each character by the application of a rule, if any. Returns the
    new string. This performs one step of the rewriting process."""
    newstr = ""
    for ch in oldStr:
        newstr = newstr + applyRules(ch, rules)
    return newstr


def applyRules(ch, rules):
    """Takes in a character and the list of rules, and finds the first rule that applies
    to the character and returns the righthand side. If no rules apply the character is
    returned unchanged."""
    newstr = ""
    for rule in rules:
        lhs = rule[0]
        rhs = rule[1]
        if ch == lhs:
            return rhs
    return ch


# --------------------------------------------------------------------------
# These functions take a string giving instructions for an L-system, and a list
# that decodes the characters in the string to tell what to do with them, and
# it has a turtle trace the shape given by the instructions

def drawLSystem(aTurtle, instructions, angle, distance):
    """Takes in a turtle, a string of instructions, plus the
    angle to turn when told to turn, and the distance forward to go.
    It loops over the instructions, and does the correct action for
    each. F means go forward distance while drawing, f means go forward
    distance without drawing, + means turn left by angle, - means turn right
    by angle, and | means turn 180 degrees."""
    savedInfoList = []
    for cmd in instructions:
        if cmd == 'F':
            aTurtle.forward(distance)
        elif cmd == 'f':
            aTurtle.up()
            aTurtle.forward(distance)
            aTurtle.down()
        elif cmd == '-':
            aTurtle.right(angle)
        elif cmd == '+':
            aTurtle.left(angle)
        elif cmd == '|':
            aTurtle.left(180)
        elif cmd == '[':
            currLoc = [aTurtle.heading(), aTurtle.xcor(), aTurtle.ycor()]
            savedInfoList.append(currLoc)
        elif cmd == ']':
            oldLoc = savedInfoList.pop()
            [head, x, y] = oldLoc
            aTurtle.up()
            aTurtle.setheading(head)
            aTurtle.setposition(x, y)
            aTurtle.down()
        else:
            # ignore any other characters in the instructions
            pass


def displayFractal(instructs, angle, dist, startPos=(-400, 0), startHead=0):
    """Takes in the string of instructions, the turn angle, the distance for
    moving forward, and then two optional arguments: a starting position for
    the turtle to start the fractal, and a starting heading. If no input is
    given for these, then they are assigned the value in the def line above.
    This function """
    # Make screen and turtle
    wn = turtle.Screen()
    t = turtle.Turtle()

    # Move turtle to starting position and heading and set it up otherwise
    t.hideturtle()
    t.up()
    t.goto(startPos)
    t.setheading(startHead)
    t.down()
    t.speed(0)

    # draw the picture
    drawLSystem(t, instructs, angle, dist)  # make sure to check angle here

    wn.exitonclick()


def main():
    # first defines a few L-systems for fractals
    kochAxiom = "F"
    kochRules = [['F', 'F+F--F+F']]
    kochAngle = 60

    hilbertAxiom = "L"
    hilbertRules = [['L', '+RF-LFL-FR+'], ['R', '-LF+RFR+FL-']]
    hilbertAngle = 90

    islandLakeAxiom = "F+F+F+F"
    islandLakeRules = [['F', 'F+f-FF+F+FF+Ff+FF-f+FF-F-FF-Ff-FFF'], ['f', 'ffffff']]
    islandLakeAngle = 90

    pythagAxiom = "X"
    pythagRules = [['X', 'F[-X]+X'], ['F', 'FF']]
    pythagAngle = 60

    # Build instructions with L-system
    instructs1 = createLSystem(5, pythagAxiom, pythagRules)

    displayFractal(instructs1, pythagAngle, 10, (0, -300), 90)

if __name__  == "__main__":
    main()