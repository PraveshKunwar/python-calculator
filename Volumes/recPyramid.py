def recPyrmaidCalc():
    print("""Please give me length, width, and height!
    Ex: 3 4 5
    3 would be length
    4 would be width
    5 would be height!
    """)
    takeSplitInput = input().split()
    if len(takeSplitInput) > 3 or len(takeSplitInput) < 3:
        print("Please make sure to give me only three numbers!")
    value = (1/3) * (int(takeSplitInput[0])) * (int(takeSplitInput[1])) * (int(takeSplitInput[2]))
    print(value)