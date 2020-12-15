def calc():
    print("""
    Please give me length, width, and height respectively!
    Ex: 2 3 4
    2 Would be length, 3 width, and 4 height!
    """)    
    takeInput = input()
    splitInput = takeInput.split()
    sign = "*"
    if len(splitInput) != 2 or len(splitInput) > 2 or len(splitInput) < 2:
        print("Please make sure that you have all three measurements, and not have more or less!")
    joinInput = sign.join(splitInput)
    value = eval(joinInput)
    print(value)
    