def interest():
    print("""Please give me principal, rate, number of times compounded, and time!
    Ex: 2000 0.5 12 365
    2000 would be principal
    0.5 would be rate
    12 would be times compounded
    365 would be time!
    """)
    takeInput = input().split()
    value = (int(takeInput[0]))*(1 + ((int(takeInput[1]))/(int(takeInput[2])))**((int(takeInput[2])*(int(takeInput[3])))))
    print(value)