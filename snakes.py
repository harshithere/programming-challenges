''' A program to implement the snakes and ladders game using bfs
    Number of points in the game is taken as input from the user 
    Finds the shortest path to reach the end'''


print 'Enter number of elements'
n = int(raw_input())
moves = [-1]*n

# Ladders
moves[2] = 21
moves[4] = 7
moves[10] = 25
moves[19] = 28
 
#Snakes
moves[26] = 0
moves[20] = 8
moves[16] = 3
moves[18] = 6

steps = n

def snakes(steps):
  paths , visited = [] , [False]*n
  temp_res = []
  paths.append([1])              # Start from first point

  while paths:
#   print paths
    path = paths.pop(0)
    val = path[-1]
    if val not in visited:
      visited.append(val)
      if n-val<=6:
        path.append(n)
        if len(path)<steps:       # Check for shortest path
          temp_res = path
          steps = len(path)

      else:
        for i in range(1,7):      # Append values that can be reached from current point
          new_path = list(path)
          if moves[val+i] == -1:
            new_path.append(val+i)
          else:
            new_path.append(moves[val+i])
          paths.append(new_path)

  return temp_res
  

result = snakes(steps)
print result
