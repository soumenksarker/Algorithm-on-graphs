# Uses python3
#import sys
import math
def distance(v1, v2, x, y):
    return math.sqrt((x[v1] - x[v2]) ** 2 + (y[v1] - y[v2]) ** 2)
def minimum_distance(x, y):
    # create edge list with possible distance in pairs of nodes
    edges = []
    for i in range(n):
        for j in range(i, n):
            if i != j:
                edges.append([i, j, distance(i, j, x, y)])
    #print(edges)
    # sort edges by distances
    sorted_Edges = sorted(edges, key=lambda tup: tup[2])
    # for ind,i in enumerate(sorted_Edges):
    #    print(i)
    # print()

    # initialize disjoint data structure, we'll do union if there's edge between two nodes before
    membership = range(n)
    # for i in membership:
    #    print(i)
    # print()
    # run Kruskal algorithm
    MST = []  # initialize minimum spanning tree
    minDist = 0
    for i in sorted_Edges:
        # make sure vertices are not already joined, or in same masks
        if membership[i[0]] != membership[i[1]]:
            # add edge
            MST.append(i)
            minDist += i[2]
            # join/union groups
            membership = list(map(lambda x: membership[i[0]] if x == membership[i[1]] else x, membership))
            #print(membership)
    # print()
    # for i in MST:
    #    print(i)
    # print()
    # write your code here
    return minDist
if __name__ == '__main__':
    #input = sys.stdin.read()
    data = list(map(int, input().split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
