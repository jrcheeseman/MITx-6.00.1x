def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    result = 1
    exp -= 1
    while exp >= 0:
        result *= base
        exp -= 1
    return result

iterPower(2, 3)


def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    if exp == 1:
        return base
    elif exp == 0:
        return 1
    elif exp >= 0:
        return base * recurPower(base, exp-1)

recurPower(2, 3)


def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    test = a
    while test > 0:
        if ((a % test) == 0) and ((b % test) == 0):
            return test
            break
        else:
            test -= 1

gcdIter(17, 12)


def gcdRecur(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)

gcdRecur(17, 12)


def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    if aStr == '':
        return False
    elif char == aStr[len(aStr)//2]:
        return True
    elif char < aStr[len(aStr)//2] and len(aStr) > 1:
        return isIn(char, aStr[:len(aStr)//2])
    elif char > aStr[len(aStr)//2] and len(aStr) > 1:
        return isIn(char, aStr[len(aStr)//2:])
    else:
        return False

isIn('f', 'bfhknopxxyyz')
isIn('a', 'abcdefg')
isIn('j', 'gjnpsuxy')
isIn('o', 'a')
isIn('a', 'ab')



















