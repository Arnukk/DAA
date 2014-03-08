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


def merge_sort(m):
    if len(m) <= 1:
        return m

    middle = len(m) / 2
    left = m[:middle]
    right = m[middle:]

    left = merge_sort(left)
    right = merge_sort(right)
    return list(merge(left, right))


def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
    if left:
        result.extend(left[left_idx:])
    if right:
        result.extend(right[right_idx:])
    return result


def In_nlogn(temp):
        temp = temp[1:len(temp)].tolist()
        for i in range(len(temp)):
            temp[i] = float(temp[i])
        # I will sort the array using Merge Sort
        temp = merge_sort(temp)
        # Now i will store in the other array absolute price differences of consequent elem.
        newtemp = []
        for i in range(len(temp)-1):
            newtemp.append(abs(temp[i+1]-temp[i]))
        #I am looking for the smallest element in this new array
        min = newtemp[0]
        for i in range(len(newtemp)):
            if newtemp[i] < min:
                min = newtemp[i]
        print "\nDearest Master I got what you have requested !"
        print ("The smallest absolute price difference is %1.3f\n" % min)

checkMe(In_nlogn)