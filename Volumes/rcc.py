import math
def rccCalc():
    print("""
    Please give me radius and height!
    Example: 9 10
    9 would be radius and 10 would be height!
    """)
    takeSplitInput = input().split()
    if len(takeSplitInput) > 2 or len(takeSplitInput) < 2:
        print("Please give me two numbers only to work with!")
    value = (1/3)*(int(takeSplitInput[0]) ** 2)*(math.pi)*(int(takeSplitInput[1]))
    print(value)