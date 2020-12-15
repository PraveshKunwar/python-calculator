def slopeCalc():
    print("""
    Please give me x1 y1 x2 y2!
    Example: 1 2 3 4
    1 would be x1
    2 would be y1
    3 would be x2
    4 would be y2!
    """)
    takeInputSplit = input().split()
    if len(takeInputSplit) > 4 or len(takeInputSplit) < 4:
        print("Please make sure to give me only four numbers!")
    slope = (int(takeInputSplit[3]) - int(takeInputSplit[1]))/(int(takeInputSplit[2]) - int(takeInputSplit[0]))
    bInt = (int(takeInputSplit[3]))-(slope * int(takeInputSplit[2]))
    equation = "y = " + str(slope) + "x+" + str(bInt)
    print("Equation: ", equation)
    print("Slope: ", slope)
    print("B int: ", bInt)
