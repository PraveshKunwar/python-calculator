def exponent():
    print("""
    Please give me base of number and exponent you want to raise it to!
    Ex: 3 4
    3 would be base 4 would be exponent!
    """)
    takeSplitInput = input().split()
    if len(takeSplitInput) > 2 or len(takeSplitInput) < 2:
     print("Please give me two numbers only to work with!")
    value = (int(takeSplitInput[0]) ** int(takeSplitInput[1]))
    print(value)