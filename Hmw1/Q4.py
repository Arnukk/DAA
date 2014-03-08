__author__ = 'akarapetyan'
from random import choice, randrange, shuffle
from numpy import loadtxt
import math
import numpy

#Output Buffer
f = open('test.out', 'r+')
FirstLine = []
OtherLines = []


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


def Table_Generation(temp):
        str_error = "Not executed yet."
        while str_error:
                    try:
                        #Finding the height of a table based on the input size
                        n = len(temp)
                        m = filter(lambda num: (num % numpy.arange(2, 1 + int(math.sqrt(num)))).all(), range(n, 2 * n+1))
                        m = m[len(m)-1]
                        #Generating the random sequence
                        a = []
                        table = [None] * m
                        for i in range(10):
                            a.append(randrange(0, m))
                        #First level hashing
                        for i in range(len(temp)):
                            sum = 0
                            for j in range(10):
                                    sum += a[j] * float(temp[i][j])
                            index = int(sum % m)
                            if table[index] is None:
                                table[index] = float(temp[i])
                            else:
                                v = table[index]
                                table[index] = []
                                table[index].append(v)
                                table[index].append(float(temp[i]))
                        str_error = None
                    except:
                        pass
        f.write(str(m) + " ")
        for i in range(len(a)):
            f.write(str(a[i]) + " ")
        f.write("\n")
        return table


def Perfect_Hash(temp):
        temp = temp[1:len(temp)].tolist()
        table = Table_Generation(temp)
        #First level hashing is done
        #Now looking for collisions in order to resolve them
        for i in range(len(table)):
            if table[i] is not None and type(table[i]) is not float:
                #There is a collision here
                trigger = True
                while trigger:
                    for j in range(len(table[i])):
                        table[i][j] = str(table[i][j])
                    second_table = Table_Generation(table[i])
                    flag = False
                    for z in range(len(second_table)):
                        if type(second_table[z]) is not float and second_table[z] is not None:
                            flag = True
                            break
                    if flag:
                        trigger = True
                    else:
                        trigger = False
                table[i] = second_table
            else:
                if table[i] is not None:
                    f.write(str(table[i]) + "\n")
                else:
                    f.write("0 0" + "\n")
        print table

checkMe(Perfect_Hash)