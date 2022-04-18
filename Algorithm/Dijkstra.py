graph = {} # 整个图的散列表(字典)

graph['start'] = {} # 起点的散列表
graph['start']['B'] = 6
graph['start']['A'] = 2

graph['A'] = {} # A节点的散列表
graph['A']['end'] = 1

graph['B'] = {} # B节点的散列表
graph['B']['A'] = 3
graph['B']['end'] = 5

graph['end'] = {} # 终点的散列表

costs = {} # 节点的开销指的是从起点出发前往该节点的权重和
costs['A'] = 6
costs['B'] = 2
costs['end'] = float('inf')

parents = {} # 存储各节点父节点的散列表
parents['A'] = 'start'
parents['B'] = 'start'
parents['end'] = None

processed = []

def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

def Dijkstra(graph, costs, parents):
    node = find_lowest_cost_node(costs)
    while node:
        cost = costs[node]
        neighbors = graph[node]
        for n in  neighbors.keys():
            new_cost = cost + neighbors[n]
            if new_cost < costs[n]:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs)
    return parents,costs['end']

print(Dijkstra(graph, costs, parents))