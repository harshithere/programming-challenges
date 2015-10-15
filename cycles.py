''' Program to find cycles in a directed graph using recursive DFS technique'''

graph = { 0 : [1, 2],
           1 : [3, 4],
           2 : [],
           3 : [],
           4 : [],
           5 : [6, 7],
           6 : [],
           7 : [] }

visited = []
path = []
score = 0

def checker(value):
  if value in visited:
    return True

  visited.append(value)
  path.append(value)
  if value in graph.keys():
    vals = graph[value]
    for val in vals:
      if val in path or checker(val)==False:           # Condition to see if current path is cyclic
        return False
  path.remove(value)

  return True

for v in graph:                   # Checks if there is any cyclic path
  if checker(v) == False:
    score = 1

if score:
  print 'Cyclic'
else:
  print 'Acyclic'
