''' Find the longest increasing subsequence of a string of numbers '''

print 'Enter the array'
a = raw_input()
seq = map(int, a.split())

res = [0]*len(seq)
pos = [0]*len(seq)

l=1
res[0] = 0
for i in range(len(seq)):
  lower = 0
  upper = l

  if seq[res[upper-1]] < seq[i]:
    j = upper

  else:
    while upper - lower > 1:
      mid = (upper + lower) / 2
      if seq[res[mid-1]] < seq[i]:
        lower = mid
      else:
        upper = mid

    j = lower

  pos[i] = res[j-1]

  if j == l or seq[i] < seq[res[j]]:
    res[j] = i
    l = max(l, j+1)

result = []
loc = res[l-1]
for i in range(l):
  result.append(seq[loc])
  loc = pos[loc]

print result[::-1]
