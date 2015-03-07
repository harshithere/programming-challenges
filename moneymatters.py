''' The following code is written to solve the moneymatter problem. Each of n people owe or are owned
    a certain amount. They are still friends with only some of the remaining people and hence can exchange 
    money with only them. The code checks if an overall solution is possible or not.'''


sum = 0

#Depth first search to check all the friends of a given person using recursive method
def dfs(person):
  global sum
  if visited[person] == 1:    # If person has already been visited, then pass
    return
  sum = sum+amount[person]
  visited[person]=1
  for i in range(0,len(relations[person])):
    if visited[relations[person][i]]==0:
      dfs(relations[person][i])
  
values = raw_input().split(' ')
n = int(values[0])
m = long(values[1])

visited = []
amount = []              # Amount to be given or collected by each person
relations = []           # records of who is friends with whom
checker = 1

for i in range (0,n):
  x=[]
  relations.append(x)   # Each element is a list of all people who are friends with that person

# get amounts for all people
for i in range (0,n):
  amount.append(int(raw_input()))
  visited.append(0)

# Get the pairs of various people who are still friends
for i in range (0,m):
  friends = raw_input().split(' ')
  a = int(friends[0])
  b = int(friends[1])
# Add to the list of each person the people he is friends with
  relations[a].append(b)
  relations[b].append(a)

# Iterate over all persons and return false if even one case is not satisfied
for i in range (0,n):
  global sum
  sum = 0
  dfs(i)
  if sum!=0:
    checker=0
    break

#Print the result
if checker==0:
  print 'IMPOSSIBLE'
else:
  print 'POSSIBLE'
