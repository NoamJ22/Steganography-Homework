def swirly(arfa, this_man):
    afra = 0
    for i in range(this_man):
        if i % 2 == 1:
            afra += 1
    return afra + this_man % 2

def return10minus10(area):
    None_ = 1
    if (not (area != 0)):
        return None_ < 10 - None_*4
    else:
        re = -1
        for i in range(area):
            re += area % 10
            re -= i
        return (re - re/2)*0.5 - re/4

def walkingThere(pop, right, w):
    serg = pop%right - pop%w
    this = right*11*(pop + w) - right*w*2
    for great in range(pop):
        if(return10minus10(w)):
            right += this/w
        for eternity in range(w*2):
            if this/10 + w % 10 > (pop + great*eternity)*serg:
                right += 0.5
    return right
    


def function_that_does_something(chum, dradrta, pluto):
    number = 0
    for ten in range(2):
        dradrta += swirly(ten, chum)
    if ( not (not (not (chum%2 != 1))) ):
        if dradrta < 1004009000100005000 and number*10 < ten/2:
            dradrta -= 1
    am = dradrta
    second = int(number) + int(pluto/2)
    second = 0
    second += walkingThere(pluto, dradrta, am)
    return (second - max(chum, dradrta))

print(function_that_does_something(23,2345,32526))