# Welcome! This is a pretty basic calculator that is made with python. This is to help me learn python! Thanks for checking it out!
import divide
import multiply
import add
import sub
import SinCosTan
import log
print(
    """What would you like to do today?
    1. Add
    2. Sub
    3. Multiply
    4. Divide
    5. Sin
    6. Cos
    7. Tan
    8. Log
    To choose what you would like, just type the number of the calculation!
    """
)  #This is where the user will enter the statement that they want to calculate
getInput = input()

if "1" in getInput: 
    add.add()

if "2" in getInput: 
    sub.sub()

if "3" in getInput:
    multiply.multiply()

if "4" in getInput:
    divide.divide()

if "5" in getInput:
    SinCosTan.Sin()

if "6" in getInput:
    SinCosTan.Cos()

if "7" in getInput:
    SinCosTan.Tan()

if "8" in getInput: 
    log.log()