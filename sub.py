def sub():
    print("""
    Please enter the numbers you would like to subtract!
    Example: 2 3 4
    """)
    addInput = input()
    sign = "-"
    replaceComma = addInput.split()
    newStatement = sign.join(replaceComma)
    evalString = eval(newStatement)
    print(evalString)
    print("Make sure to run command again if you want to use other calculations!")