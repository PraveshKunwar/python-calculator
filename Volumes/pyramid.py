def pyrmaidCalc():
    print("""
    Please give me base and height!
    Ex: 3 5
    3 would be base and 5 would be height!
    """)
    takeSplitInput = input().split()
    if len(takeSplitInput) > 2 or len(takeSplitInput) < 2:
        print("Please make sure you only give me two numbers!")
    value = (1/3) * (int(takeSplitInput[0])) * (int(takeSplitInput[1]))
    print(value)