#找最短距离，带权重。
import heapq
import math
graph={
    "A":{"B":5,"C":1},
    "B":{"A":5,"C":2,"D":1},
    "C":{"A":1,"B":2,"D":4,"E":8},
    "D":{"B":1,"C":4,"E":3,"F":6},
    "E":{"C":8,"D":3},
    "F":{"D":6}
}
def dijkstra(graph,s):
    pqueue=[]
    heapq.heappush(pqueue,(0,s))#优先级队列
    seen=set()#已经走过的节点
    parent = {s:None}#走到当前节点的前一个点
    distance = {s:0}#起始点到各个节点的最短距离

    for node in graph:
        if node != s:
            distance[node]=math.inf
    print(distance)
    while (len(pqueue)>0):
        dist,vertex=heapq.heappop(pqueue)
        seen.add(vertex)#真的被拿出来之后才加
        nodes=graph[vertex].keys()
        for w in nodes:
            if w not in seen:
                if dist + graph[vertex][w] < distance[w]:
                    #seen.add(w)
                    heapq.heappush(pqueue,(dist + graph[vertex][w],w))
                    parent[w] = vertex
                    distance[w] = dist + graph[vertex][w]

    return parent,distance
parent,distance=dijkstra(graph,"A")
print(parent,distance)
