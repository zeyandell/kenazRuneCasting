import tkinter as tk
from turtle import RawTurtle, TurtleScreen


class DrawingGUI:

    def __init__(self):
        self.rootWin = tk.Tk()
        newCanvas = tk.Canvas(self.rootWin)
        newCanvas.config(width=200, height=300, relief=tk.SUNKEN, bd=5)
        newCanvas.grid(row=0, column=1)
        self.screen = TurtleScreen(newCanvas)
        self.turtle = RawTurtle(newCanvas)
        # self.runeFuncDict = {"Kenaz": self.drawKenaz, "Othila": self.drawOthila}
        self.drawRune("||Frrrf")

    def run(self):
        self.rootWin.mainloop()

    def drawRune(self, instructions):
        self.turtle.pensize(5)
        self.turtle.speed(3)
        self.turtle.hideturtle()
        self.turtle.up()
        self.turtle.goto(-50, -100)
        self.turtle.down()
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
            elif cmd == 'r':
                self.turtle.right(45)
            elif cmd == 'l':
                self.turtle.left(10)
            elif cmd == 'a':
                self.turtle.right(10)
            elif cmd == 'E':
                self.turtle.left(15)
            elif cmd == 'D':
                self.turtle.forward(100)
            elif cmd == 'd':
                self.turtle.forward(50)
            elif cmd == 'C':
                self.turtle.forward(30)
            elif cmd == 'c':
                self.turtle.forward(40)
            elif cmd == 'B':
                self.turtle.forward(5)
            elif cmd == 'b':
                self.turtle.left(5)

            else:
                # ignore any other characters in the instructions
                pass


myGUI = DrawingGUI()
myGUI.run()
