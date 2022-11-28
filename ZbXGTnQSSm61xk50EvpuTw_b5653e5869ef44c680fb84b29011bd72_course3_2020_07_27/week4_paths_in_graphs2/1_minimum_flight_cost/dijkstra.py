#Uses python3
import sys
#root of the heap is always minimum
#support tuples, task priorities, inplace sorting
import heapq
def distance(adj, cost, totalCost,s, d):
    #write your code here
    dist = [totalCost+1]*len(adj)
    dist[s] = 0
    prev = [-1]*len(adj)
    h = list(zip(dist,range(len(dist))))
    #print(h)
    heapq.heapify(h)
    while len(h) > 0:
        w = heapq.heappop(h)
        print(w)
        for ind,i in enumerate(adj[w[1]]):
            print(ind, i)
            if dist[i] > w[0] + cost[w[1]][ind]:
                dist[i] = w[0] + cost[w[1]][ind]
                prev[i] = w[1]
                heapq.heappush(h,(dist[i],i))
                print((dist[i],i))
                print(h)
            #print(dist[i])
    if dist[d] == totalCost + 1:
        return -1
    else:
        return dist[d]
if __name__ == '__main__':
    #input = sys.stdin.read()
    data = list(map(int, input().split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    totalCost = 0
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
        totalCost += w
    #print(adj)
    #print(cost)
    s, d = data[0] - 1, data[1] - 1
    print(distance(adj, cost, totalCost, s, d))
