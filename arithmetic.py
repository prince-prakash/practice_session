def ath(choice):
    switcher = {
    1: print("add"),
    2: print("Subtract"),
    3: print("Multitply"),
    }
    return switcher.get(choice,"nothing")

ath(1)