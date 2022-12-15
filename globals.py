total = 100


def func3():
    listOfGlobals = globals()
    listOfGlobals['total'] = 15
    total = 22
    print('Local Total = ', total)


print('Total = ', total)
func3()
print('Total = ', total)
