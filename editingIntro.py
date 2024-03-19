explanationText = "Runes are an ancient set of symbols or letters of an alphabet that were used for writing, magic, and "\
                  "divination in northern Europe in the first century A.D. Runic divination is not a tool for fortune" \
                  "telling but rather a tool to self-knowledge - guiding you to the answer that is already within you.\n \n"\
                  \
                  "The format in this divination is the three norm spread, which will give you insight into your current " \
                  "problem, root of the problem, present situation and the likely outcome. The program will present a " \
                  "rune for each part of the spread with a small description of the rune to guide your interpretation " \
                  "of your divination. Remember to focus on a general question before you cast the runes and use that " \
                  "question to guide your interpretation. \n \n" \
                  "Remember not to be fatalistic about the Runes’ advice for the future. It should be regarded as flexible" \
                  "and not concrete. Runes aid in having deep counsel with the question you pose but their interpretation" \
                  " should be complemented by your own intuition and healthily developed sense of free will.\n \n" \
                  "Once you are ready, click start ..."
#
# explanationText = "This is a practice explanation text. \n Hopefully it will work."

labelWidth = 100
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
print(explanationIndented)