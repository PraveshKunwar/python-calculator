import math
def quadraticCalc():
    print("""
    Please give me the coefficients of Ax^2, Bx, and C!
    Ex: 3 4 5
    3 would be Ax^2
    4 would be Bx
    5 would be C!
    """)
    takeInputSplit = input().split()
    if len(takeInputSplit) > 3 or len(takeInputSplit) < 3:
        print("Please make sure to give me only three numbers!")
    # discriminant to show amount of solutions!
    Ax = int(takeInputSplit[0])
    Bx = int(takeInputSplit[1])
    C = int(takeInputSplit[2])
    d = (Bx ** 2) - 4 * (Ax * C)
    if d > 0:
        x1 = (-Bx+(math.sqrt(Bx**2-4*(Ax*C))))/(2 * Ax)
        x2 = (-Bx-(math.sqrt(Bx**2-4*(Ax*C))))/(2 * Ax)
        print("This equation has two solutions:", x1, x2)
    if d == 0:
        x = (-Bx+math.sqrt((Bx**2)-4*(Ax * C))) / (2 * Ax)
        print("This equation has one solution", x)
    if d < 0:
        print("This equation has no real solutions!")
