__author__ = 'akarapetyan'
import random
from numpy import loadtxt
import math
mycounter = 0
#Output Buffer
f = open('test.out', 'r+')

# A simple function for reading the file and checking whether the data is compatible with the input rules
def checkMe(function):
    #Loading the input file
    try:
        temp = loadtxt('test2.in', dtype='str').tolist()
    except:
         print "Something is wrong with the Input parameters, please check"
         exit()

    #Checking if the input parameters are right
    try:
        if isinstance(temp, list) and len(temp) > 0:
            for i in range(len(temp)):
                if not temp[i].isdigit():
                    print "Something is wrong with the Input parameters, please check"
                    exit()
                else:
                    temp[i] = int(temp[i])
        else:
            print "Something is wrong with the Input parameters, please check"
            exit()
    except:
        print "Something is wrong with the Input parameters, please check"
        exit()
    #Everything is right with the data, let's manage it carefully
    def Caller(): pass
    Caller.__code__ = function.__code__
    Caller(temp)




def main(temp):
    #Counters
    SuccessfulSearches = 0
    SuceessfullComparisons = 0
    UnsucessfullComparisons = 0
    UnsucessfullSearches = 0
    InsertionComparisons = 0
    Insertions = 0
    global mycounter
    #Lets create the Data Structure
    TheMagicData = []
    Temporary = random.sample(range(100), 18)
    n = "{0:b}".format(len(Temporary))
    k = int(math.ceil(math.log(len(temp)+1, 2)))
    flag = 0
    for i in range(k):
        A = []
        #if int(n[-i-1]) == 1:
            #for j in range(int(math.pow(2, i))):
                   # A.append(Temporary[flag])
                   # flag += 1
        TheMagicData.append(A)
    #Ok we have the data already, let's start playing with it
    #Let's Search for what you are looking for
    print temp
    print TheMagicData
    for i in temp:
        OUTER, INNER, Comparisons = SEARCH(TheMagicData, i)
        if INNER is not None:
            print "You were looking for %d ? it is in ! %d, %d" % (i, OUTER, INNER)
            SuccessfulSearches += 1
            SuceessfullComparisons += Comparisons
        else:
            UnsucessfullSearches += 1
            UnsucessfullComparisons += Comparisons
            #Let's insert it
            INSERT(TheMagicData, i)
            InsertionComparisons += mycounter
            Insertions += 1
            mycounter = 0

    print "Successfull Searches %d" % SuccessfulSearches
    f.write(str(SuccessfulSearches) + " ")
    bin = SuceessfullComparisons/SuccessfulSearches if SuccessfulSearches != 0 else 0
    print "Amortized number of comparisons per Successfull Search is %d" % bin
    f.write(str(bin) + " ")
    bin  = UnsucessfullComparisons/UnsucessfullSearches if UnsucessfullSearches !=0  else 0
    print "Amortized number of comparisons per Unsuccessfull Search is %d" % bin
    f.write(str(bin) + " ")
    bin  = InsertionComparisons/Insertions if Insertions !=0 else 0
    print "Amortized number of comparisons per Insertion is %d" % bin
    f.write(str(bin) + " ")
    print TheMagicData
    f.close


def SEARCH(theArray, theElement):
    ANCSS = 0
    Index = None
    for i in range(len(theArray)):
        Index, bin = binary_search(theArray[i], theElement)
        ANCSS += bin
        if Index is not None:
            return i, Index, ANCSS
    return None, Index, ANCSS


def INSERT(theArray, theElement):
    Z = []
    Z.append(theElement)
    for i in range(len(theArray)):
        if i == len(theArray)-1:
            theArray.append(Z)
            return
        if not len(theArray[i]):
            theArray[i] = Z
            return
        else:
            Z.extend(theArray[i])
            del theArray[i][:]
            Z = merge_sort(Z)


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
    global mycounter
    result = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):
        mycounter += 1
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

def binary_search(l, value):
    counter = 0
    low = 0
    high = len(l)-1
    while low <= high:
        counter += 1
        mid = (low+high)//2
        if l[mid] > value: high = mid-1
        elif l[mid] < value: low = mid+1
        else: return mid, counter
    return None, counter

checkMe(main)