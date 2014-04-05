__author__ = 'akarapetyan'
#Global Variables
Vertexes = {}
RootVertexes = []
ordNodes = []
VertexesAlive = []
DeadVertexes = []
Memory = 0
n = 0
#Output Buffer
f = open('test.out', 'r+')


class Node:
    def __init__(self, ID, Memory, Priority):
        self.ID = ID
        self.Priority = Priority
        self.Memory = Memory
        self.Sub = 0
        self.children = []


# A simple function for reading the file and checking whether the data is compatible with the input rules
def checkMe(function):
    #Loading the input file
    global n
    global Memory
    f = open("test.in", "r")
    temp = f.readline().split()
    n = int(temp[0])
    Memory = int(temp[1])
    childs = []
    for i in range(n):
        temp = f.readline().split()
        node = Node(int(temp[0]), int(temp[1]), int(temp[2]))
        for j in range(3, len(temp)):
            childs.append(int(temp[j]))
            node.children.append(int(temp[j]))
        Vertexes[int(temp[0])] = node
    RootVertexes.extend(list(set(Vertexes.keys())-set(childs)))
    #Everything is right with the data, let's manage it carefully
    def Caller(): pass
    Caller.__code__ = function.__code__
    Caller()


def MagicOrdering(root):
    sum = 0
    if len(root.children) != 0:
        for n in root.children:
            sum += MagicOrdering(Vertexes[n])
    root.indSub = sum + len(root.children)
    ordNodes.append(root)
    return root.indSub


def CoolNapsack():
    L = []
    for i in range(n+1):
        L.append([])
        for j in range(Memory+1):
            L[i].append(0)
    track = []
    for i in range(n+1):
        track.append([])
        for j in range(Memory+1):
            track[i].append(0)
    for i in range(1, n+1):
        for j in range(1, Memory+1):
            if ordNodes[i-1].Memory > j:
                L[i][j] = L[i-1-ordNodes[i-1].indSub][j]
                track[i][j] = 1
            elif L[i-1-ordNodes[i-1].indSub][j] > ordNodes[i-1].Priority + L[i-1][j-ordNodes[i-1].Memory]:
                L[i][j] = L[i-1-ordNodes[i-1].indSub][j]
                track[i][j] = 1
            else:
                L[i][j] = ordNodes[i-1].Priority + L[i-1][j-ordNodes[i-1].Memory]
                track[i][j] = 2
    col = Memory
    row = n
    while row >= 1 and col >= 1:
        if track[row][col] == 1:
            row = row-1-ordNodes[row-1].indSub
        else:
            VertexesAlive.append(ordNodes[row-1].ID)
            col -= ordNodes[row-1].Memory
            row -= 1


def main():
    for v in RootVertexes:
        MagicOrdering(Vertexes[v])
    CoolNapsack()
    nodesToTerm = list(set(Vertexes.keys())-set(VertexesAlive))
    TerminatedMem = 0
    for id in nodesToTerm:
        TerminatedMem += Vertexes[id].Memory
    f.write(str(TerminatedMem) + " ")
    for i in nodesToTerm:
        f.write(str(i) + " ")
    f.close()


checkMe(main)