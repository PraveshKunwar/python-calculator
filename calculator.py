# Welcome! This is a pretty basic calculator that is made with python. This is to help me learn python! Thanks for checking it out!
import divide
import multiply
import add
import sub
print(
    """What would you like to do today?
    1. Add
    2. Sub
    3. Multiply
    4. Divide
    To choose what you would like, just type the number of the calculation!
    """
)  #This is where the user will enter the statement that they want to calculate
getInput = input()

if "1" in getInput: 
    add.add()