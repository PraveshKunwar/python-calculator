import math
def log(): 
    print("Please give me base of Log")
    base = input()
    print("Please give me the number you would like to Log")
    logNumber = input()
    baseInt = int(base)
    logInt = int(logNumber)
    logValue = math.log(logInt, baseInt)
    print(logValue)