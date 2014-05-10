__author__ = 'akarapetyan'
vertices = []


class Vertex:
    def __init__(self, Id, p, childNodes):
        self.Id = Id
        self.p = p
        self.alreadyDone = 0
        self.childNodes = childNodes


# A simple function for reading the file and checking whether the data is compatible with the input rules
def checkMe(function):
    #Loading the input file
    try:
        f = open("test.in", 'r')
        firstLine = f.readline().split()
        n = int(firstLine[0])
        for i in range(n):
            line = f.readline().split()
            vertices.append(Vertex(i, int(line[0]), list(map(int, line[1:]))))
        f.close()
    except:
         print "Something is wrong with the Input parameters, please check"
         exit()
    #Everything is right with the data, let's manage it carefully
    def Caller(): pass
    Caller.__code__ = function.__code__
    Caller()


def CycleFinder(vertices):
    flag = False
    for i in range(len(vertices)):
        temp = vertices[i]
        if temp.alreadyDone == 0:
            temp.alreadyDone = 1
            flag = DFS_2(vertices, temp)
            if flag:
                break
    return flag
   

def DFS_2(vertices, vertex):
    flag = False
    for i in range(len(vertex.childNodes)):
        temp = vertices[vertex.childNodes[i]]
        if temp.alreadyDone == 0:
            temp.alreadyDone = 1
            flag = DFS_2(vertices, temp)
            if flag:
                break
        elif temp.alreadyDone == 1:
            flag = True
            break
    vertex.alreadyDone = 2
    return flag


def Sheduling_DP(vertex, Schedule):
    if Schedule[vertex.Id] is not None:
        return Schedule[vertex.Id]
    if len(vertex.childNodes) == 0:
        Schedule[vertex.Id] = 0
        return Schedule[vertex.Id]
    earliestStartTime = 0
    for i in range(len(vertex.childNodes)):
        temp = vertices[vertex.childNodes[i]]
        if earliestStartTime < Sheduling_DP(temp, Schedule) + temp.p:
            earliestStartTime = Sheduling_DP(temp, Schedule) + temp.p
    Schedule[vertex.Id] = earliestStartTime
    return Schedule[vertex.Id]


def main():
    f = open('test.out', 'w+')
    if CycleFinder(vertices):
        f.write("INFEASIBLE")
    else:
        Schedule = {}
        for vertex in vertices:
            Schedule[vertex.Id] = None
        for temp in vertices:
            Sheduling_DP(temp, Schedule)
        for temp in Schedule.keys():
            f.write(str(Schedule[temp]) + str(" "))
    f.close()

checkMe(main)
