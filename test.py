
x = (1, 2, (3, 'John', 4), 'Hi')

aTup = ('I', 'am', 'a', 'test', 'Tup')

def oddTups (aTup):
    aNewTup = aTup[0::2]
    return aNewTup
oddTups(aTup)

x = [1, 2, [3, 'John', 4], 'Hi']

listA = [1, 4, 3, 0]
listB = ['x', 'z', 't', 'q']

[100, 0, 1, 4, 7, 4, 1, 6, 3, 4]


alist = [100, 0, 1, 4, 4, 1, 6, 3, 4]
blist = alist



testList = [1, -4, 8, -9]

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

def absSqr(a):
    return abs(a) ** 2

applyToEach(testList, absSqr)

print(testList)


animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    count = 0
    for i in aDict:
        count += len(aDict[i])
    return count

how_many(animals)


nothing = {}

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    for i in aDict:
        if aDict[i] == max(aDict.values()):
            return i
        elif aDict == {}:
            return None

biggest(nothing)



