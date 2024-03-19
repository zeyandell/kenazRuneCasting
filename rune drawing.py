import tkinter as tk
from turtle import RawTurtle, TurtleScreen
import random
"""Practice to figure out how drawing runes should work. Ignore the last two functions."""

class BasicGUI:

    def __init__(self):
        self.rootWin = tk.Tk()
        newCanvas = tk.Canvas(self.rootWin)
        newCanvas.config(width=200, height=300, relief=tk.SUNKEN, bd=5)
        newCanvas.grid(row=0, column=1)
        self.screen = TurtleScreen(newCanvas)
        self.turtle = RawTurtle(newCanvas)
        self.runeFuncDict = [{"name":"Fehu", "instructions": "||F+s|||s+s|s|||f", "meaning": "abundance, prosperity, luck",
                              "Murkstave meaning": "impoverishment, material loss, greed, excessive materialism"},
                             {"name":"Kenaz", "instructions": "-f.|||fs+||fs", "meaning":
            "warmth, illumination, learning, gathering, togetherness", "Murkstave meaning": "blockage of vital light, fever, ulcer, inflammation"},
                             {"name":"Othila", "instructions": "|ff||f||f||ff", "meaning": "a sense of home, property, contentment",
                              "Murkstave meaning": "displacement, alienation, homelessness"}]
        self.drawFourRunes()




    def run(self):
        self.rootWin.mainloop()

    def drawRune(self, instructions):
        """"Given a set of instructions, draws a rune. (Works similar to L-Systems)"""
        for cmd in instructions:
            if cmd == 'F':
                self.turtle.forward(200)
            elif cmd == 'f':
                self.turtle.forward(80)
            elif cmd == 's':
                self.turtle.forward(40)
            elif cmd == '+':
                self.turtle.left(180)
            elif cmd == '|':
                self.turtle.left(45)
            elif cmd == '-':
                self.turtle.up()
            elif cmd == '.':
                self.turtle.down()
            else:
                # ignore any other characters in the instructions
                pass

    def chooseRune(self):
        """Randomly picks a rune from the list and then decides if the rune will be reversed or not. Then draws
        the rune with turtle in the canvas. Returns the rune entry and whether it was reversed, in a tuple."""
        runeNumber = random.randint(0, len(self.runeFuncDict)-1)
        rune = self.runeFuncDict[runeNumber]
        print(rune["name"])  # remove in final program
        reverse = random.randint(0, 1)
        print(reverse)  # remove in final program

        self.turtle.pensize(5)
        self.turtle.speed(3)
        self.turtle.hideturtle()
        self.turtle.up()
        if reverse == 0:
            self.turtle.goto(-50, -100)
        else:
            self.turtle.goto(50, 100)
            self.turtle.left(180)
        self.turtle.down()
        self.drawRune(self.runeFuncDict[runeNumber]["instructions"])

        return rune, reverse

    def drawFourRunes(self):
        """Randomly picks draws the four runes (by calling chooseRune), then prints their meanings."""
        (rune1, reverse1) = self.chooseRune()
        if reverse1 == 0:
            print(rune1["meaning"])
        elif reverse1 ==1:
            print(rune1["Murkstave meaning"])


# these functions are obsolete
    def drawOthila(self):
        self.turtle.left(45)
        self.turtle.down()
        self.turtle.forward(150)
        self.turtle.left(90)
        self.turtle.forward(75)
        self.turtle.left(90)
        self.turtle.forward(75)
        self.turtle.left(90)
        self.turtle.forward(150)

    def drawKenaz(self):
        self.turtle.forward(100)
        self.turtle.left(135)
        self.turtle.down()
        self.turtle.forward(150)
        self.turtle.right(90)
        self.turtle.forward(150)

myGUI = BasicGUI()
myGUI.run()