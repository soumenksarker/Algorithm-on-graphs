#Uses python3
#Uses python3

import sys

def negative_cycle(adj, cost):
    #write your code here
    dist = [-1] * len(adj)
    prev = [-1] * len(adj)
    #just start from first vertex
    dist[0] = 0
    #first run Bellamford V - 1 cycles.
    #if no negative cycles then this should be the last iteration of changes
    for l in range(len(adj)):   #do this V times total
        for m in range(len(adj)):
            for ind,k in enumerate(adj[m]):
                mkCost = cost[m][ind]
                if dist[k] > dist[m] + mkCost:
                    dist[k] = dist[m] + mkCost
                    prev[k] = m
        #check at V - 1 and then V to see if they change
        if l == len(adj)-2:
            com_path_weight_at_Vminus1iteration = list(dist)
        if l == len(adj)-1:
            com_path_weightV_at_iteration = list(dist)
    #if there are changes on the Vth cycle,  then there was a negative cycle
    if com_path_weight_at_Vminus1iteration == com_path_weightV_at_iteration:
        return 0
    else:
        #print(com_path_weight_at_Vminus1iteration, com_path_weightV_at_iteration)
        return 1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost))
