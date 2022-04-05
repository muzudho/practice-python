for dice1 in range(1, 7):
    for dice2 in range(1, 7):
        one = ""
        both = ""
        summ = dice1 + dice2
        if summ == 2:
            both = "xx"

        if dice1 == 1 or dice2 == 1:
            one = "x"
        print("{} {} {: >1} {: >2}".format(dice1, dice2, one, both))
