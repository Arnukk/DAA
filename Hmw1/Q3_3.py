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


def Largest_in_n(temp):
        temp = temp[1:len(temp)].tolist()
        # Initial smallest element of the array
        min = float(temp[0])
        # Initial largest element of the array
        max = float(temp[0])

        for i in range(len(temp)):
            if float(temp[i]) < min:
                min = float(temp[i])
            if float(temp[i]) > max:
                max = float(temp[i])
        largest = max - min
        print "\nIt was critically difficult but i found what you have requested  !"
        print ("The largest absolute price difference is %1.3f\n" % largest)


checkMe(Largest_in_n)