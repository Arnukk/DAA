__author__ = 'akarapetyan'
from random import choice
from numpy import loadtxt


# A simple function for reading the file and checking whether it is compatible with the input rules
def checkMe(function):
    #Loading the input file
    temp = loadtxt('test.in', dtype='str')
    #Checking if the input parameters are right
    if temp[0].isdigit() and int(temp[0]) > 0 and len(temp) == int(temp[0])+1:
        def Caller():pass
        Caller.__code__ = function.__code__
        Caller(temp)
    else:
        print "Something is wrong with the Input parameters, please check"


def Partition(A, p, r):
    # Choosing a random element from the array and substituting it with the last one
    m = choice(A[p:r+1])
    A[A.index(m)] = A[r]
    A[r] = m

    x = A[r]
    i = p - 1
    for j in range(p, r, 1):
        if A[j] <= x:
            i += 1
            temp = A[i]
            A[i] = A[j]
            A[j] = temp
    temp = A[i+1]
    A[i+1] = A[r]
    A[r] = temp
    return i+1


def FindTheMedian(A, p, q, i):
    if p == q:
        return A[p]
    r = Partition(A, p, q)
    k = r - p + 1
    if i == k:
        return A[r]
    elif i < k:
        return FindTheMedian(A, p, r-1, i)
    else:
        return FindTheMedian(A, r+1, q, i-k)


def Randomized_in_nsquare(temp):
        temp = temp[1:len(temp)].tolist()
        median = []
        for i in range(len(temp)-1):
            for j in range(len(temp)):
                median.append(abs(float(temp[i]) - float(temp[j])))
        rc = FindTheMedian(median, 0, len(median)-1, (len(median)+1)/2)
        print "\nDearest Master I got what you have requested !"
        print ("The lower median absolute price difference is %1.3f\n" % rc)


checkMe(Randomized_in_nsquare)