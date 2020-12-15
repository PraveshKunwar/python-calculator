def prismCalc():
    print("""Please give me the base and height respectively!
    Ex: 2 3
    2 would be base and 3 would be height!
    """)
    takeInput = input()
    splitInput = takeInput.split()
    if len(splitInput) > 2 or len(splitInput) < 2:
        print("Please make sure that you only give me two numbers!")
    value = (int(splitInput[0])) * (int(splitInput[1]))
    print(value)