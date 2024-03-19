"""
Team Kenaz: Aaliyah Dick, Amman Hussein, and Zoey Yandell
Core Concepts in Comp Sci
Lauren Milne
This program allows users to automatically cast runes for divination by pressing the start button in the opening window.
It will randomly choose runes and draw them in real time, displaying their names and meanings. Settings can also be adjusted
to make the runes draw faster or hide the meanings."""

import tkinter as tk
from turtle import RawTurtle, TurtleScreen
import random


class RuneGUI:

    def __init__(self):
        self.rootWin = tk.Tk()
        self.rootWin.title("Opening Screen")
        self.rootWin.config(bg="black")
        blankspace = tk.Label(self.rootWin, height=5, width=15, bg="black")
        blankspace.grid(row=0, column=0)
        startButton = tk.Button(self.rootWin)
        startButton.config(text="START", relief=tk.RIDGE, command=self.startFunction, font="BradleyHand 12",
                           bg="black")
        startButton.grid(row=1, column=0)

        intro = tk.Label(self.rootWin)
        labelWidth = 100
        explanationIndented = self.indentExplanation(labelWidth)
        intro.config(text=explanationIndented, bg="black", height=25, fg="white", font="BradleyHand 14",
                     width=labelWidth,
                     justify=tk.LEFT, padx=20)
        intro.grid(row=2, column=0)

        #  These lines initialize the variables referenced in the settings functions to change explanations and
        #  turtle speed. Rune background is no longer referenced but I left it in to allow for later use.
        self.explanations = True
        self.runeBG = "white"
        self.turtSpeed = 3
        settingsButton = tk.Button(self.rootWin, text="Settings", relief=tk.RIDGE, command=self.settingsFunction,
                                   bg="black")
        settingsButton.grid(row=3, column=0)
        blankLabel = tk.Label(self.rootWin, height=1, bg="black")
        blankLabel.grid(row=4, column=0)

        endButton = tk.Button(self.rootWin, text="End Program", command=self.endFunction)
        endButton.grid(row=0, column=1)

        self.runeFuncDict = [
            {"name": "Fehu", "instructions": "||F+s|||s+s|s|||f", "meaning": "abundance, prosperity, luck",
             "Murkstave meaning": "impoverishment, material loss, greed, excessive materialism"},
            {"name": "Urox", "instructions":
                "||F+|f|||+ff", "meaning": "a challenge, facing/meeting adversity", "Murkstave meaning":
                 "failing to meet life’s trails, being gored in the game of life"},
            {"name": "Thurisaz", "instructions":
                "||F+s|f+||f", "meaning": "threat/disruption, pain through unfortunate and unpredictable events",
                "Murkstave meaning":"intensification of: threat/disruption, \npain through unfortunate and unpredictable events"},
            {"name": "Ansuz",
             "instructions": "||F+|f+f|||f|f", "meaning": "speech and writing, the spoken word, communication",
             "Murkstave meaning":
                 "misinformation, lies, deceit"},
            {"name": "Raido", "instructions": "||Frrrfrrf||fs", "meaning": "travel, "
                                                                           "going places, movement",
             "Murkstave meaning": "a failed or fruitless voyage, going astray"},
            {"name": "Kenaz", "instructions": "-f.|||fs+||fs", "meaning": "warmth, illumination, learning, gathering, "
                                                                          "togetherness",
             "Murkstave meaning": "blockage of vital light, fever, ulcer, inflammation"},
            {"name": "Gebo", "instructions": "|EFEE||-D.||EEF","meaning": "giving/receiving a gift, exchange, sacrificing",
            "Murkstave meaning": "giving/receiving a gift, exchange, sacrificing"},
            {"name": "Wunjo", "instructions": "||F||||EEd||||||EC",
             "meaning": "happiness, fulfillment, a joyful time with people or community", "Murkstave meaning":
                 "unhappiness, misery, loneliness"},
            {"name": "Hagalaz", "instructions": "||F||||-d.|D|||fc||||F", "meaning":
                "disruption, change, delay, cancellation of plan",
             "Murkstave meaning": "disruption, change, delay, cancellation of plan"},
            {"name": "Naudiz", "instructions": "-d.||F||||D|d||||D", "meaning": "hardship, constraint, healing, "
                                                                                "acceptance",
             "Murkstave meaning": "hardship, constraint, healing, acceptance"}, {"name": "Jera", "instructions":
                "-c||D|.c||||||c|||||-C.|c||||||c",
                                                                                 "meaning": "growing time, festivity, harvest seasons, richness and ripeness",
                                                                                 "Murkstave meaning": "growing time, festivity, harvest seasons, richness and ripeness"},
            {"name": "Eihwaz",
             "instructions": "-s|||f+.f|||Frrrf", "meaning": "transition, death (literal or symbolic), regeneration",
             "Murkstave meaning": "transition, death (literal or symbolic), regeneration"},
            {"name": "Pertho", "instructions":
                "||F+|CC||CC|||-dCB.||F|||CC+||CC", "meaning": "play, fun, laughter, self gratification, celebration, "
                                                               "quest for self knowledge",
             "Murkstave meaning": "sadness, melancholy, the need to lighten up and enjoy yourself"},
            {"name": "Algiz", "instructions": "-C.||F+CC||EEEECC+CC+|ECC",
             "meaning": "protection, defense, safety from harm",
             "Murkstave meaning": "lack of protection, defenselessness, vulnerability, danger"},
            {"name": "Tiwaz", "instructions":
                "-s||.F+rs+srrs", "meaning": "justice, honor, bravery, dedication",
             "Murkstave meaning": "futile conflict,"
                                  " lost cause"},
            {"name": "Berkana", "instructions": "||F+EEf+EEE|ECC||CC+||CC", "meaning": "new beginnings,"
                                                                                       " purification, driving out the old, reproduction, fertility",
             "Murkstave meaning": "difficult beginnings,"
                                  " aborted plans, reproductive concerns"},
            {"name": "Mannaz", "instructions": "||F+|CCCC|||fB+F+F|||CCCC",
             "meaning": "inspiration, creativity, compassion, love",
             "Murkstave meaning": "dormant talents, misanthropy,"
                                  " hatred, farewells"},
            {"name": "Inguz", "instructions": "-|f.f||f||f||f", "meaning": "sexuality, family lines, "
                                                                           "ancestry",
             "Murkstave meaning": "sexuality, family lines, ancestry"},
            {"name": "Othila", "instructions": "|ff||f||f||ff", "meaning": "a sense of home, property, contentment",
             "Murkstave meaning": "displacement, alienation, homelessness"},
            {"name": "Sowulo", "instructions": "|f||frrf",
             "meaning": "spiritual power, enlightenment, guidance, growth and prosperity",
             "Murkstave meaning": "spiritual power, enlightenment, guidance, growth and prosperity"},
            {"name": "Isa", "instructions": "||F", "meaning": "stasis, danger, entrapment, seductive beauty, renewal",
             "Murkstave meaning": "stasis, danger, entrapment, seductive beauty, renewal"},
            {"name": "Laguz", "instructions": "||Frrrf",
             "meaning": "journey by water, depths of self, metaphysical insight",
             "Murkstave meaning": "blockage, perils, the danger of the unconscious"}]
        #  missing: Ehwaz, Dagaz


    def run(self):
        """Runs the code to create the first window."""
        self.rootWin.mainloop()

    def indentExplanation(self, labelWidth):
        """Adds indents to the explanation based on the label width. I just thought it made life easier."""
        explanationIndented = ""
        n = -1
        needIndent = False
        for i in range(0, len(explanationText) - 1):
            explanationIndented = explanationIndented + explanationText[i]
            n = n + 1
            if n % labelWidth == 0 and n != 0:
                if explanationText[i] == " ":
                    explanationIndented = explanationIndented + "\n"
                else:
                    needIndent = True
            if needIndent and explanationText[i] == " ":
                explanationIndented = explanationIndented + "\n"
                needIndent = False
            if explanationText[i] == "\n":
                n = 0
        return explanationIndented

    def settingsFunction(self):
        """Creates the settings window and the buttons to manipulate explanations and rune speed and to quit
        the settings window."""
        self.settWin = tk.Tk()
        self.settWin.title("Settings")
        settLabel = tk.Label(self.settWin, text="Settings", width=30, height=3)
        settLabel.grid(row=0, column=0)
        self.expButton = tk.Button(self.settWin, text="Turn explanations off", command=self.expToggle)
        self.expButton.grid(row=1, column=0)
        var= tk.IntVar()
        speedLabel = tk.Label(self.settWin, text="\nChange how fast runes are drawn here. \n0 is slowest, 10 is fastest.",
                              width=30, height=3)
        speedLabel.grid(row=2, column=0)
        speedSlider = tk.Scale(self.settWin, orient=tk.HORIZONTAL, variable=var, from_=0, to=10,
                               command=self.setSpeed)
        speedSlider.grid(row=3, column=0)
        blankLabel = tk.Label(self.settWin, height=1)
        blankLabel.grid(row=4, column=0)
        quitSettings = tk.Button(self.settWin, text="Quit to Main Screen", command=self.quitSettings)
        quitSettings.grid(row=5, column=0)
        blankLabel2 = tk.Label(self.settWin, height=1)
        blankLabel2.grid(row=6, column=0)

    def expToggle(self):
        """Turns explanations on or off."""
        if self.explanations:
            self.explanations = False
            # self.expLabel["text"]="Explanations are off"
            self.expButton["text"] = "Turn explanations on"
        else:
            self.explanations = True
            # self.expLabel["text"] = "Explanations are on"
            self.expButton["text"] = "Turn explanations off"

    #
    # def choosePink(self):
    #     self.runeBG = "pink"
    #     self.colorLabel["text"] = "The current background color is "+ self.runeBG + "."
    #
    # def chooseBlue(self):
    #     self.runeBG = "cornflower blue"
    #     self.colorLabel["text"] = "The current background color is "+ self.runeBG + "."
    #
    # def chooseBlack(self):
    #     self.runeBG = "black"
    #     self.colorLabel["text"] = "The current background color is "+ self.runeBG + "."
    #
    # def chooseGreen(self):
    #     self.runeBG = "forest green"
    #     self.colorLabel["text"] = "The current background color is "+ self.runeBG + "."
    #
    # def chooseGoldenrod(self):
    #     self.runeBG = "dark goldenrod"
    #     self.colorLabel["text"] = "The current background color is "+ self.runeBG + "."
    def setSpeed(self, number):
        """Given the input of the number selected by the sliding scale, sets the global variable turtle speed."""
        if int(number) == 0:
            self.turtSpeed = 1
        elif int(number) == 10:
            self.turtSpeed = 10
        else:
            self.turtSpeed = int(number)

    def quitSettings(self):
        """Closes the settings window."""
        self.settWin.destroy()

    def startFunction(self):
        """Creates a new window which contains canvases for four runes, as well as labels for all the canvases. Calls
        chooseRune() four times to randomly select and draw a rune in each canvas, randomly decide whether or not
         to draw runes upside down, and check to make sure runes are not repeated. After each rune is drawn, displays
         its name and meaning underneath the canvas. The new window also contains an 'End Program' button, which can
         quit the program."""
        self.newWin = tk.Tk()
        self.newWin.title("Rune Screen")
        self.newWin.config(bg=self.runeBG)
        self.problemCanvas = tk.Canvas(self.newWin)
        self.problemCanvas.config(width=200, height=300, relief=tk.SUNKEN, bd=3)
        self.problemCanvas.grid(row=1, column=1)
        problemLabel = tk.Label(self.newWin, text="Current Problem", bg=self.runeBG)
        problemLabel.grid(row=0, column=1)
        problemDescr = tk.Label(self.newWin, text="", width=50, height=3, bg=self.runeBG)
        problemDescr.grid(row=2, column=1)

        # add newlines to some meanings

        self.rootCanvas = tk.Canvas(self.newWin, width=200, height=300, relief=tk.SUNKEN, bd=5)
        self.rootCanvas.grid(row=4, column=0)
        rootLabel = tk.Label(self.newWin, text="Root Problem", bg=self.runeBG)
        rootLabel.grid(row=3, column=0)
        rootDescr = tk.Label(self.newWin, text="", width=50, height=3, bg=self.runeBG)
        rootDescr.grid(row=5, column=0)

        self.presentCanvas = tk.Canvas(self.newWin, width=200, height=300, relief=tk.SUNKEN, bd=5)
        self.presentCanvas.grid(row=4, column=1)
        presentLabel = tk.Label(self.newWin, text="Present Situation", bg=self.runeBG)
        presentLabel.grid(row=3, column=1)
        presentDescr = tk.Label(self.newWin, text="", width=50, height=3, bg=self.runeBG)
        presentDescr.grid(row=5, column=1)

        self.futureCanvas = tk.Canvas(self.newWin, width=200, height=300, relief=tk.SUNKEN, bd=5)
        self.futureCanvas.grid(row=4, column=2)
        futureLabel = tk.Label(self.newWin, text="Future Direction", bg=self.runeBG)
        futureLabel.grid(row=3, column=2)
        futureDescr = tk.Label(self.newWin, text="", width=50, height=3, bg=self.runeBG)
        futureDescr.grid(row=5, column=2)

        exitButton = tk.Button(self.newWin, text="End Program", command=self.endFunction)
        exitButton.grid(row=0, column=2)

        recastButton = tk.Button(self.newWin, text="Recast Runes", command=self.recastRunes)
        recastButton.grid(row=1, column=2)
        # This section generates the runes and updates the labels. Add a wait time between drawings.

        (self.rune1, reverse1) = self.chooseRune(self.problemCanvas)
        if reverse1 == 0:
            meaning = self.rune1["meaning"]
        else:
            meaning = self.rune1["Murkstave meaning"]
        if self.explanations:
            problemDescr["text"] = self.rune1["name"] + "\n" + meaning


        (self.rune2, reverse2) = self.chooseRune(self.rootCanvas)
        if reverse2 == 0:
            meaning = self.rune2["meaning"]
        else:
            meaning = self.rune2["Murkstave meaning"]
        if self.explanations:
            rootDescr["text"] = self.rune2["name"] + "\n" + meaning


        (self.rune3, reverse3) = self.chooseRune(self.presentCanvas)
        if reverse3 == 0:
            meaning = self.rune3["meaning"]
        else:
            meaning = self.rune3["Murkstave meaning"]
        if self.explanations:
            presentDescr["text"] = self.rune3["name"] + "\n" + meaning
        (self.rune4, reverse4) = self.chooseRune(self.futureCanvas)
        if reverse4 == 0:
            meaning = self.rune4["meaning"]
        else:
            meaning = self.rune4["Murkstave meaning"]
        if self.explanations:
            futureDescr["text"] = self.rune4["name"] + "\n" + meaning

    def drawRune(self, instructions):
        """"Given a string of instructions, draws a rune with our global turtle. This function is called in
        chooseRune."""
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
                pass
            #  In a separate file, every set of instructions was tested with this part of the code to make sure it
            #  drew the right thing.

    def chooseRune(self, canvas):
        """Randomly picks a rune from the list and then decides if the rune will be reversed or not. Then draws
        the rune with turtle in the given canvas. Returns the rune entry and whether it was reversed, in a tuple. Checks
        to make sure runes are not repeated. NOTE: The checking code must be modified for other rune configurations."""
        self.screen = TurtleScreen(canvas)
        self.turtle = RawTurtle(canvas)
        self.turtle.hideturtle()
        runeNumber = random.randint(0, len(self.runeFuncDict) - 1)
        rune = self.runeFuncDict[runeNumber]
        reverse = random.randint(0, 1)
        # The random generation was tested separately before being added to the code.

        if canvas == self.rootCanvas:
            while rune == self.rune1:
                runeNumber = random.randint(0, len(self.runeFuncDict) - 1)
                rune = self.runeFuncDict[runeNumber]

        elif canvas == self.presentCanvas:
            while rune == self.rune1 or rune == self.rune2:
                runeNumber = random.randint(0, len(self.runeFuncDict) - 1)
                rune = self.runeFuncDict[runeNumber]

        elif canvas == self.futureCanvas:
            while rune == self.rune1 or rune == self.rune2 or rune == self.rune3:
                runeNumber = random.randint(0, len(self.runeFuncDict) - 1)
                rune = self.runeFuncDict[runeNumber]

        self.turtle.pensize(5)
        self.turtle.speed(self.turtSpeed)
        self.turtle.up()
        if reverse == 0:
            self.turtle.goto(-50, -100)
        else:
            self.turtle.goto(50, 100)
            self.turtle.left(180)
        self.turtle.down()
        self.drawRune(self.runeFuncDict[runeNumber]["instructions"])

        return rune, reverse

    def endFunction(self):
        """When 'End Program' button is clicked, will quit the program."""
        self.rootWin.quit()

    def recastRunes(self):
        """Destroys the previous rune-drawing screen and recreates the screen, repeating the random rune selection
        and drawing."""
        self.newWin.destroy()
        self.startFunction()


explanationText = "Runes are an ancient set of symbols or letters of an alphabet that were used for writing, magic, and " \
                  "divination in northern Europe in the first century A.D. Runic divination is not a tool for fortune" \
                  "telling but rather a tool to self-knowledge - guiding you to the answer that is already within you.\n \n" \
 \
                  "The format in this divination is the three norm spread, which will give you insight into your current " \
                  "problem, root of the problem, present situation and the likely outcome. The program will present a " \
                  "rune for each part of the spread with a small description of the rune to guide your interpretation " \
                  "of your divination. Remember to focus on a general question before you cast the runes and use that " \
                  "question to guide your interpretation. \n \n" \
                  "Remember not to be fatalistic about the Runes’ advice for the future. It should be regarded as flexible " \
                  "and not concrete. Runes aid in having deep counsel with the question you pose but their interpretation" \
                  " should be complemented by your own intuition and healthily developed sense of free will.\n \n" \
                  "Once you are ready, click start ..."
if __name__ == "__main__":
    myGUI = RuneGUI()
    myGUI.run()
