import math

def Sin():
    print("""Please type the number you would like to take the Sine of
    Example: -1
    """)
    sinInput = input()
    convertInput = int(sinInput)
    sinValue = math.sin(convertInput)
    print(sinValue)
    
def Cos():
    print("""Please type the number you would like to take the Cosine of
    Example: -1
    """)
    cosInput = input()
    convertInput = int(cosInput)
    cosValue = math.cos(convertInput)
    print(cosValue)

def Tan():
    print("""Please type the number you would like to take the Tangent of
    Example: -1
    """)
    tangentInput = input()
    convertInput = int(tangentInput)
    tangentValue = math.tan(convertInput)
    print(tangentValue)