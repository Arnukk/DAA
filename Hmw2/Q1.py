__author__ = 'akarapetyan'
import random
from numpy import loadtxt
from numpy import inf
#Output Buffer
f = open('test.out', 'r+')


# A simple function for reading the file and checking whether the data is compatible with the input rules
def checkMe(function):
    #Loading the input file
    try:
        temp = loadtxt('test1.in', dtype='str').tolist()
    except:
         print "Something is wrong with the Input parameters, please check"
         exit()

    #Checking if the input parameters are right
    if isinstance(temp, list) and len(temp) > 0:
        for i in temp:
            if not isinstance(i, list) or len(i) != 2:
                print "Something is wrong with the Input parameters, please check"
                exit()
            else:
                for j in range(len(i)):
                    if not i[j].isdigit():
                        print "Something is wrong with the Input parameters, please check"
                        exit()
                    else:
                        i[j] = float(i[j])

    else:
        print "Something is wrong with the Input parameters, please check"
        exit()
    #This is in the case if you guys try to cheat
    for i in range(len(temp)):
        temp[i] = sorted(temp[i])
    #Everything is right with the data, let's manage it carefully
    def Caller(): pass
    Caller.__code__ = function.__code__
    Caller(temp)


class BST():
    left = None
    right = None
    key = None
    u = None
    sum = None
    max = None

    # The class "constructor" - It's actually an initializer
    def __init__(self, left, right, key, u, sum, max):
        self.left = left
        self.right = right
        self.key = key
        self.u = u
        self.sum = sum
        self.max = max

    def printme(self):
        output = 'my Key is %d ' % self.key + '\n'
        output += 'my Left is %d' % self.left.key + '\n' if self.left else 'My Left is empty\n'
        output += 'my Right is %d' % self.right.key + '\n' if self.right else 'My Right is empty\n'
        output += 'my U is %d' % self.u + '\n'
        output += 'my SUM is %d' % self.sum + '\n'
        output += 'my MAX is %d' % self.max + '\n'
        print output


mytree = None
def main(temp):
    Right = []
    Left = []
    #putting our endpoints into 2 one dimensional arrays
    random.shuffle(temp)
    for i in temp:
        Right.append(i[1])
        Left.append(i[0])
    #initializing the Binary tree
    mytree = BST(None, None, Left[0], 1, 1, 1)
    InsertintoBST(mytree, Right[0], -1)
    UpdateMax(mytree)
    ThePmo, counter = findthePMO(mytree, 0)
    f.write(str(ThePmo) + " " + str(counter))
    f.write("\n")
    for i in range(1, len(Left), 1):
        InsertintoBST(mytree, Left[i], 1)
        InsertintoBST(mytree, Right[i], -1)
        UpdateMax(mytree)
        ThePmo, counter = findthePMO(mytree, 0)
        f.write(str(ThePmo) + " " + str(counter))
        f.write("\n")
    f.close()
    PrintTheTree(mytree)
    ThePmo, counter = findthePMO(mytree, 0)
    print "The PMO is %d" % ThePmo


def PrintTheTree(object):
    object.printme()
    if object.left:
        PrintTheTree(object.left)
    if object.right:
        PrintTheTree(object.right)


def findthePMO(object, counter):
    counter += 1
    if not object:
        return
    else:
        MaxLeft, MaxRight, Sumleft = CatchtheExceptions(object)
        if object.max == Sumleft + object.u:
            PMO = object.key
            return PMO, counter
        elif object.max == MaxLeft:
            return findthePMO(object.left, counter)
        elif object.max == Sumleft + object.u + MaxRight:
            return findthePMO(object.right, counter)

def CatchtheExceptions(object):
    UpdateMax(object.left)
    UpdateMax(object.right)
    if not object.left:
        Sumleft = 0
        MaxLeft = -inf
    else:
        Sumleft = object.left.sum
        MaxLeft = object.left.max
    if not object.right:
        MaxRight = 0
    else:
        MaxRight = object.right.max
    return MaxLeft, MaxRight, Sumleft


def UpdateMax(object):
    if not object:
        return
    else:
        MaxLeft, MaxRight, Sumleft = CatchtheExceptions(object)
        object.max = max(MaxLeft, Sumleft + object.u, Sumleft + object.u + MaxRight)


def InsertintoBST(theobject, thevalue, u):
    if not theobject.key:
        return
    elif thevalue < theobject.key:
        #updating the path
        theobject.sum += u
        if theobject.left:
            InsertintoBST(theobject.left, thevalue, u)
        else:
            theobject.left = BST(None, None, thevalue, u, u, 0)
            return
    else:
        #updating the path
        theobject.sum += u
        if theobject.right:
            InsertintoBST(theobject.right, thevalue, u)
        else:
            theobject.right = BST(None, None, thevalue, u, u, 0)
            return



checkMe(main)