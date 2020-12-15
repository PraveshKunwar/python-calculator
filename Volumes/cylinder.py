import math
def cylinderCalc():
    print("""Please give me the radius and height respectively:
    Ex: 3 4 
    3 would be radius and 4 would be height!
    """)
    takeInput = input()
    splitInput = takeInput.split()
    if len(splitInput) > 1 or len(splitInput) < 1 :
        print("Please make sure to enter only two values!")
    cylinderValue = (math.pi)*(int(splitInput[0]) ** 2)*(int(splitInput[1]))
    print(cylinderValue)