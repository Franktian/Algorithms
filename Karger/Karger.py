import random, copy

def chooseRandomEdge(G): #return an edge represented by 2 ints
    v1= G.keys() [random.randint(0,len(G)-1)]
    v2= G[v1] [random.randint(0,len(G[v1])-1)]
    return v1, v2

def kargerStep(G):
    v1,v2= chooseRandomEdge(G)
    #1. attach v2's list to v1
    G[v1].extend(G[v2])
    #2. replace all appearance of v2 as v1
    for x in G[v2]:
        lst=G[x]
        for i in range(0,len(lst)):
            if lst[i]==v2: lst[i]=v1        
    #3.remove self-loop
    while v1 in G[v1]:
        G[v1].remove(v1)
    #4. remove v2's list
    del G[v2]
    
def karger(G): 
    while len(G)>2: kargerStep(G)
    return len(G[G.keys()[0]])

if __name__ == "__main__":
    f = open('kargerMinCut.txt')
    
    line = f.readline()
    graph = {}
    while line:

        ints = [int(x) for x in line.split()]
        graph[ints[0]] = ints[1:]
        line = f.readline()
    
    f.close()
    
    min=karger(copy.deepcopy(graph))
    for i in range(0,100): # run many tests
        instance=karger(copy.deepcopy(graph))
        if instance<min: min=instance    
    
    print 'Finally:',min