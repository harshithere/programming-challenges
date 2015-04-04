''' Program to calculate minimum distance to be covered by gaurds to reach all rooms
    0 - Room is not accessible
    1 - Room has a door
    2 - Room has a gaurd present 

[1 2 1]          [1 0 1]
[1 0 1]   -->    [2 -1 2]
[1 2 1]          [1 0 1]

'''


values = {}
result = {}
visited = {}

# Checks if i,j do not cross limits
def check_limits(i , j ):
    if i>=N or j>=N or i<0 or j<0:
        return False
    else:
        return True
    

# Function to calculate distance of each door using BFS    
def bfs( i , j , steps):
  stack = []
    
  for (k,l) in [(i+1,j),(i,j+1),(i-1,j),(i,j-1)]:     # Get all immediate neighbours of a point
    if check_limits(k, l):
      if visited[k][l] == False:                      # Checks if a door is already visited
        visited[k][l] = True
      	if values[k][l] ==1:
          steps1 = steps+1
	  if steps1<result[k][l]:                     # Proceed only if distance is less than previous distance
            result[k][l] = steps1
            stack.append([k,l])			      # Add given room coordinates to stack
	  
        elif values[k][l] == 0:
          result[k][l] = -1
        elif values[k][l] == 2:
          result[k][l] = 0
    
  while stack:                                        # Iterate while stack is non empty
    points = stack.pop()
#    steps = steps+1
    bfs( points[0] , points[1] , steps+1)
        
# Visited initialised to false for each gaurd
def clear_visited():
  for i in range(N):
    for j in range(N):
      visited[i][j] = False
    
# Get input from user
N = int(raw_input())
for i in range(N):
    values[i] = input()
    visited[i] = []
    result[i] = []
    for j in range(N):
        result[i].append(N*N)          # Result initialised with maximum value (implies result not possible)
	visited[i].append(False)       # No room visited in start

# Call BFS if a gaurd is encountered
for i in range(N):
    for j in range(N):
        if values[i][j] == 2:
          clear_visited()
          result[i][j] = 0
          visited[i][j] = True
          bfs( i , j , 0)
          
# Print result
for i in range(N):
    print result[i]
