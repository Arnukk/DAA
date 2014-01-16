__author__ = 'Areg'
import random


index = 0


def InsertionSort(InputArray):

    for j in range(1, len(InputArray), 1):
        key = InputArray[j]
        i = j-1
        while (InputArray[i] < key) and (i >= 0):
            InputArray[i+1] = InputArray[i]
            i = i - 1
        InputArray[i+1] = key
    for x in InputArray:
        print x


def Merge(InputArray, p, q, r):

    L = []
    R = []
    n1 = q - p + 1
    n2 = r - q

    for i in range(0, n1, 1):
        L.append(InputArray[p+i-1])

    for j in range(0, n2, 1):
        R.append(InputArray[q + j])


    i = 0
    j = 0

    for k in range(p, r, 1):

        if L[i] <= R[j]:
            InputArray[k] = L[i]
            i = i + 1
        else:
            InputArray[k] = R[j]
            j = j + 1




def MergeSort(InputArray, p, r):

    if p < r:
        q = int((p+r) / 2)
        MergeSort(InputArray, p, q)
        MergeSort(InputArray, q+1, r)
        Merge(InputArray, p, q, r)


def MyBubbleSort(InputArray):

    for i in range(len(InputArray)-2, 0, -1):
        if InputArray[i] >= InputArray[i+1]:
            a = InputArray[i+1]
            InputArray[i+1] = InputArray[i]
            InputArray[i] = a
        if InputArray[i] <= InputArray[i-1]:
            a = InputArray[i-1]
            InputArray[i-1] = InputArray[i]
            InputArray[i] = a

    for i in range(1, len(InputArray)-2, 1):
        if InputArray[i] >= InputArray[i+1]:
            a = InputArray[i+1]
            InputArray[i+1] = InputArray[i]
            InputArray[i] = a
        if InputArray[i] <= InputArray[i-1]:
            a = InputArray[i-1]
            InputArray[i-1] = InputArray[i]
            InputArray[i] = a

    for i in range(len(InputArray)-2, 0, -1):
        if InputArray[i] >= InputArray[i+1]:
            a = InputArray[i+1]
            InputArray[i+1] = InputArray[i]
            InputArray[i] = a
        if InputArray[i] <= InputArray[i-1]:
            a = InputArray[i-1]
            InputArray[i-1] = InputArray[i]
            InputArray[i] = a

    for i in range(1, len(InputArray)-2, 1):
        if InputArray[i] >= InputArray[i+1]:
            a = InputArray[i+1]
            InputArray[i+1] = InputArray[i]
            InputArray[i] = a
        if InputArray[i] <= InputArray[i-1]:
            a = InputArray[i-1]
            InputArray[i-1] = InputArray[i]
            InputArray[i] = a

    for i in range(len(InputArray)-2, 0, -1):
        if InputArray[i] >= InputArray[i+1]:
            a = InputArray[i+1]
            InputArray[i+1] = InputArray[i]
            InputArray[i] = a
        if InputArray[i] <= InputArray[i-1]:
            a = InputArray[i-1]
            InputArray[i-1] = InputArray[i]
            InputArray[i] = a

    for i in range(1, len(InputArray)-2, 1):
        if InputArray[i] >= InputArray[i+1]:
            a = InputArray[i+1]
            InputArray[i+1] = InputArray[i]
            InputArray[i] = a
        if InputArray[i] <= InputArray[i-1]:
            a = InputArray[i-1]
            InputArray[i-1] = InputArray[i]
            InputArray[i] = a

    for i in range(len(InputArray)-2, 0, -1):
        if InputArray[i] >= InputArray[i+1]:
            a = InputArray[i+1]
            InputArray[i+1] = InputArray[i]
            InputArray[i] = a
        if InputArray[i] <= InputArray[i-1]:
            a = InputArray[i-1]
            InputArray[i-1] = InputArray[i]
            InputArray[i] = a

    for i in range(1, len(InputArray)-2, 1):
        if InputArray[i] >= InputArray[i+1]:
            a = InputArray[i+1]
            InputArray[i+1] = InputArray[i]
            InputArray[i] = a
        if InputArray[i] <= InputArray[i-1]:
            a = InputArray[i-1]
            InputArray[i-1] = InputArray[i]
            InputArray[i] = a

    for i in range(len(InputArray)-2, 0, -1):
        if InputArray[i] >= InputArray[i+1]:
            a = InputArray[i+1]
            InputArray[i+1] = InputArray[i]
            InputArray[i] = a
        if InputArray[i] <= InputArray[i-1]:
            a = InputArray[i-1]
            InputArray[i-1] = InputArray[i]
            InputArray[i] = a

    for i in range(1, len(InputArray)-2, 1):
        if InputArray[i] >= InputArray[i+1]:
            a = InputArray[i+1]
            InputArray[i+1] = InputArray[i]
            InputArray[i] = a
        if InputArray[i] <= InputArray[i-1]:
            a = InputArray[i-1]
            InputArray[i-1] = InputArray[i]
            InputArray[i] = a

    for i in range(len(InputArray)-2, 0, -1):
        if InputArray[i] >= InputArray[i+1]:
            a = InputArray[i+1]
            InputArray[i+1] = InputArray[i]
            InputArray[i] = a
        if InputArray[i] <= InputArray[i-1]:
            a = InputArray[i-1]
            InputArray[i-1] = InputArray[i]
            InputArray[i] = a

    for i in range(1, len(InputArray)-2, 1):
        if InputArray[i] >= InputArray[i+1]:
            a = InputArray[i+1]
            InputArray[i+1] = InputArray[i]
            InputArray[i] = a
        if InputArray[i] <= InputArray[i-1]:
            a = InputArray[i-1]
            InputArray[i-1] = InputArray[i]
            InputArray[i] = a

    for i in range(len(InputArray)-2, 0, -1):
        if InputArray[i] >= InputArray[i+1]:
            a = InputArray[i+1]
            InputArray[i+1] = InputArray[i]
            InputArray[i] = a
        if InputArray[i] <= InputArray[i-1]:
            a = InputArray[i-1]
            InputArray[i-1] = InputArray[i]
            InputArray[i] = a

    for i in range(1, len(InputArray)-2, 1):
        if InputArray[i] >= InputArray[i+1]:
            a = InputArray[i+1]
            InputArray[i+1] = InputArray[i]
            InputArray[i] = a
        if InputArray[i] <= InputArray[i-1]:
            a = InputArray[i-1]
            InputArray[i-1] = InputArray[i]
            InputArray[i] = a





#MergeSort(InputArray, 0, len(InputArray)-1)
for i in range(0, 1000000, 1):
    InputArray = random.sample(range(1, 100), 20)
    MyBubbleSort(InputArray)
    for k in range(0, len(InputArray)-1, 1):
        if InputArray[k] > InputArray[k+1]:
            print "no !"