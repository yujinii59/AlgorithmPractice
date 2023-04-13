from math import gcd
from functools import reduce

def solution(arrayA:list, arrayB:list):
    answer = 0
    gcdA = reduce(lambda x, y: gcd(x, y), arrayA)
    gcdB = reduce(lambda x, y: gcd(x, y), arrayB)
    boolA = True
    for elem in arrayB:
        if elem % gcdA == 0:
            boolA = False
            break
    boolB = True
    for elem in arrayA:
        if elem % gcdB == 0:
            boolB = False
            break
    if boolA and boolB:
        return max(gcdA, gcdB)
    elif boolA:
        return gcdA
    elif boolB:
        return gcdB
    else:
        return 0