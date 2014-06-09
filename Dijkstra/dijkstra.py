import sys
def Dijkstra(V):
    X = {} # vertices processed so far
    A = {} # computed shortest path so far
    X[1] = True
    A[1] = 0
    
    while len(X) != len(V):
        min_dst = 0
        min_src = 0
        min_wgt = sys.maxint
        for u in X:
            for v, l_uv in V[u]:
                if v in X:
                    continue
                if A[u] + l_uv < min_wgt:
                    min_src, min_dst = u, v
                    min_wgt = A[u] + l_uv
        if min_src == 0:
            print 'Found nothing to match the greedy criterion! X = %s' % X
        X[min_dst] = True
        A[min_dst] = min_wgt
        
    targets = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
    #print A
    for t in targets:
        print A[t]

if __name__ =='__main__':
    # read in to generate graph representation
    graph = {}
    f = open('dijkstraData.txt')
    line = f.readline()
    while line:
        fields = line.split()
        edges = []
        vertex = int(fields.pop(0))
        for edge in fields:
            edges.append((int(edge.split(",")[0]), int(edge.split(",")[1])))
        graph[vertex] = edges
        line = f.readline()
    
    f.close()
    
    Dijkstra(graph)
    