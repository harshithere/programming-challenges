''' Get the minimum cost of operations for converting one string to another
    I have used the levenshtein algorithm 
    Assuming cost of deletion, addition and subsitution is same'''

print 'Enter string one'
a_str = str(raw_input())
a = list(a_str)
print a

print 'Enter string two'
b_str = str(raw_input())
b = list(b_str)

''' I have used dynamic programming. Basically starting from smallest sub-strings, we add one 
    digit in each iteration and check what is minimum number of changes for matching that. This 
    process is repeated till the entire string is traversed '''

#[cost[:] for cost in [[0]*10]*15]
cost = [[i if j==0 else 0 for i in range(len(b)+1)] for j in range(len(a)+1)]     # Initialize 2-D matrix to store iterations
for i in range(len(a)+1):
  cost[i][0]=i

for i in range(1,len(a)+1):
  for j in range(1,len(b)+1):
    if a[i-1] == b[j-1]:                  # if elements are same
      cost[i][j] = cost[i-1][j-1]
    else:
      cost[i][j] = min(cost[i-1][j-1],cost[i][j-1],cost[i-1][j])+1

print 'Min number of iterations: '+ str(cost[len(a)][len(b)])
