__author__ = 'akarapetyan'


# A simple function for reading the file and checking whether the data is compatible with the input rules
def checkMe(function):
    #Loading the input file
    try:
        f = open("test.in", 'r')
        firstLine = f.readline().split()
        n = int(firstLine[0])
        newweights = {}
        for i in range(n+1):
            newweights[i] = {}
        for i in range(1,n+1):
            newweights[0][i] = 0

        for i in range(n):
            line = f.readline().split(" ")
            if "," in line[0]:
                for j in line:
                    newweights[int(j.split(",")[0])][i+1] = -int(j.split(",")[1])
                    print j.split(",")[0], j.split(",")[1]
        f.close()
    except:
         print "Something is wrong with the Input parameters, please check"
         exit()
    #Everything is right with the data, let's manage it carefully
    def Caller(): pass
    Caller.__code__ = function.__code__
    Caller(newweights)



# Step 1: For each node prepare the destination and predecessor
def initialize(graph, source):
    d = {} # Stands for destination
    p = {} # Stands for predecessor
    for node in graph:
        d[node] = float('Inf') # We start admiting that the rest of nodes are very very far
        p[node] = None
    d[source] = 0 # For the source we know how to reach
    return d, p

def relax(node, neighbour, graph, d, p):
    # If the distance between the node and the neighbour is lower than the one I have now
    if d[neighbour] > d[node] + graph[node][neighbour]:
        # Record this lower distance
        d[neighbour] = d[node] + graph[node][neighbour]
        p[neighbour] = node

def bellman_ford(graph, source):
    d, p = initialize(graph, source)

    for i in range(len(graph)-1): #Run this until is converges
        for u in graph:
            for v in graph[u]: #For each neighbour of u
                relax(u, v, graph, d, p) #Lets relax it
    # Step 3: check for negative-weight cycles
    for u in graph:
        for v in graph[u]:
            if d[v] > d[u] + graph[u][v]:
                return False, False
    return d, p


def main(newweights):
    f = open('test.out', 'w+')
    print newweights
    d, r = bellman_ford(newweights, 0)
    print d
    if d:
        result = d.values()[1:]
        for i in range(len(result)):
            result[i] = abs(result[i])
            f.write(str(result[i]) + " ")
    else:
        f.write("INFEASIBLE")
    f.close()

checkMe(main)
