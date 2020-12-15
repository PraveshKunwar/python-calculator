import math
def sphereCalc():
    print("""
    Please give me radius of sphere!
    Ex: 3
    """)
    intInput = int(input())
    value = (4 / 3) * (math.pi) * (intInput ** 3)
    print(value)