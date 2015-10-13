''' Program to check if a graph is bipartite or not 

    A Bipartite Graph is a graph whose vertices can be divided into two independent sets, 
    U and V such that every edge (u, v) either connects a vertex from U to V or a vertex 
    from V to U

    There are 2 possible values (represented by red and blue colors)
    If these are different for adjacent nodes, graph is bipartite'''

graph = [[0, 1, 0, 1],
        [1, 0, 1, 0],
        [0, 1, 0, 1],
        [1, 0, 1, 0]]


def bipartite(start):
  visited = []
  values = [-1]*len(graph)
  paths = [start]
  values[start] = 1
  visited.append(start)
  while paths:
    point = paths.pop(0)
    visited.append(point)
    for i in range(len(graph)):
      if graph[point][i]!=0:
        if i not in visited:
          paths.append(i)
        if values[i] == values[point]:
          return False
        else:
          values[i] = 1 - values[point]


  return True


print bipartite(0)
        
