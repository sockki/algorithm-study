def solution(arrayA, arrayB):
    answer = 0
    arrayA.sort()
    arrayB.sort()
    Adivision = getdivision(arrayA[0])
    Bdivision = getdivision(arrayB[0])
    
    Amax = getMaxA(Adivision,arrayA,arrayB)
    Bmax = getMaxA(Bdivision,arrayB,arrayA)
    return max(Amax,Bmax)

def getdivision(n):
    result = []
    for i in range(1, int(n**(1/2))+1):
        if int(n % i) == 0:
            result.append(i)
            if (i**2) != n:
                result.append(n//i)
    result.sort()
    return result

def getMaxA(divisions,arr1,arr2):
    while divisions:
        right = True
        now = divisions.pop()
        for i in arr1:
            if int(i % now) != 0:
                right = False
                break
        if not right:
            continue
            
        for i in arr2:
            if int(i % now) == 0:
                right = False
                break
        if not right:
            continue
        else:
            return now
        
    return 0



#####
from functools import reduce
from math import gcd


def solution(nums1, nums2):
    gcd1, gcd2 = reduce(gcd, nums1), reduce(gcd, nums2)
    answer = []
    if all(each % gcd2 for each in nums1):
        answer.append(gcd2)
    if all(each % gcd1 for each in nums2):
        answer.append(gcd1)
    return max(answer) if answer else 0