##  BRAINROT TRANSLATOR
##  Version 1.0
##  August 31, 2024
##  A program by Logan Hanson
##  lwhanson04@gmail.com
##  If any of this is useful to you at all, feel free to go ahead and use it
##  I just ask that you give me a bit of credit if you do
##  Have fun!

import re
import random

random.seed()
regex = r"\b((G|g)\w+)\b|\b((F|f)\w+)\b|\b((S|s)\w+)\b|\b((E|e)\w+)\b|\b(?<!\')((R|r)\w+)\b|\b((M|m)\w+)\b|\b((O|o)\w+)\b"
base = "What if instead of "
middle = " it was "
final = ""
control = 1
fMatch = ["Freak", "Freaky"]
gMatch = ["Goon", "Gooner", "Gooning", "Gyatt"]
sMatch = ["Sigma", "Skibidi"]
eMatch = ["Edge", "Edging"]
locked = bool(False)

def changeMessage(string, lock):
    stringIn = str(string)
    tempStr = stringIn
    unlocked = lock

    if(re.search(regex, stringIn)):
        tempStr = re.sub(r'\b((G|g)\w+)\b', gMatch[random.randint(0,3)], tempStr)
        tempStr = re.sub(r'\b((F|f)\w+)\b', fMatch[random.randint(0,1)], tempStr)
        tempStr = re.sub(r'\b((S|s)\w+)\b', sMatch[random.randint(0,1)], tempStr)
        tempStr = re.sub(r'\b((E|e)\w+)\b', eMatch[random.randint(0,1)], tempStr)
        tempStr = re.sub(r'\b(?<!\')((R|r)\w+)\b', 'Rizz', tempStr)
        tempStr = re.sub(r'\b((M|m)\w+)\b', 'Mewing', tempStr)
        tempStr = re.sub(r'\b((O|o)\w+)\b', 'Ohio', tempStr)
        final = base + stringIn + middle + tempStr
        unlocked = True
    elif unlocked: final = "I cannot goon to this!"
    else: final = "I'm sorry, I cannot help you with this expression"

    return((final, unlocked))

def getInput():
    string = input("Enter Text -> ")
    string = str(string)

    return(string)

print("This is an automatic translator. Enter a phrase or sentence and see how it turns out. Something simple, like a fun fact or something you did today!")
while(1):
    words = getInput()
    output, locked = changeMessage(words, locked)
    print(output)