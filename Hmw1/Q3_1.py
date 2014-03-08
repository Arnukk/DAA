__author__ = 'akarapetyan'
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


def Partition(A, p, r, y):
    if y is not None:
        m = A[A.index(y)]
        A[A.index(y)] = A[r]
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


def FindTheMedian(A, p, q, i, y):
    if p == q:
        return A[p]
    r = Partition(A, p, q, y)
    k = r - p + 1
    if i == k:
        return A[r]
    elif i < k:
        return FindTheMedian(A, p, r-1, i, None)
    else:
        return FindTheMedian(A, r+1, q, i-k, None)


def Select(median):
        medians = []
        if len(median) < 5:
            return median[(len(median)/2)-1]
        # Trying to find the median absolute price difference
        # Dividing the array into n/5 groups

        for i in range(0, len(median), 5):
            if i + 5 <= len(median):
                f = i + 4
                for j in range(i, f):
                    for k in range(j+1, f+1):
                        if median[j] > median[k]:
                            temp = median[j]
                            median[j] = median[k]
                            median[k] = temp
                medians.append(median[i+2])
            else:
                for j in range(i, len(median)-1):
                    for k in range(j+1, len(median)):
                        if median[j] > median[k]:
                            temp = median[j]
                            median[j] = median[k]
                            median[k] = temp
                if len(median)%5 == 1:
                    medians.append(median[len(median)-1])
                else:
                    medians.append(median[i-1 + (len(median)+1)%5/2])

        return Select(medians)


def All_in_nsquare(temp):
        temp = temp[1:len(temp)].tolist()
        # Initial smallest absolute price difference
        min = abs(float(temp[0]) - int(temp[1]))
        # Initial largest absolute price difference
        max = abs(float(temp[0]) - int(temp[1]))

        for i in range(len(temp)-1):
            for j in range(i+1, len(temp), 1):
                if abs(float(temp[i]) - float(temp[j])) < min:
                    min = abs(float(temp[i]) - float(temp[j]))
                elif abs(float(temp[i]) - float(temp[j])) > max:
                    max = abs(float(temp[i]) - float(temp[j]))
        # Initial value for average absolute price difference
        avg = 0
        # Array of median absolute price differences
        median = []
        for i in range(len(temp)-1):
            for j in range(len(temp)):
                avg += abs(float(temp[i]) - float(temp[j]))
                median.append(abs(float(temp[i]) - float(temp[j])))
        # The average absolute price difference
        avg = 1.0 * avg/(len(temp) * (len(temp)-1))
        y = Select(median)
        rc = FindTheMedian(median, 0, len(median)-1, (len(median)+1)/2, y)
        print "\nEventually I got all the answers that you have requested my Master !"
        print ("The smallest absolute price difference is %1.3f\n" % min)
        print ("The largest absolute price difference is %1.3f\n" % max)
        print ("The average absolute price difference is %1.3f\n" % avg)
        print ("The lower median absolute price difference is %1.3f\n" % rc)


checkMe(All_in_nsquare)