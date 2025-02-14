

l1=[1]
l2=[1]
def itemInCommon(l1=list, l2=list):
    checkDict = {}
    for n in l1:
        checkDict[n] = checkDict.get(n, 0) + 1
    print(checkDict)

    for n in l2:
        if n in checkDict:
            return True
    return False

# itemInCommon(l1, l2)
print(itemInCommon(l1, l2))


def propriation(JESUS = bool):
    if JESUS:
        print('You are saved!')
    else:
        print('You need JESUS')

propriation(False)