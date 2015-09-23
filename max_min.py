''' Program to find the maximum of minimum of every window in an array.
    
    Basically an array is taken and staring from size 1, subarrays of 
    increasing size are formed. Minimum of these sub-arrays is taken 
    and maximum of these values is calculated for that size.
'''

print 'Enter the array'
arr = input()
n = len(arr)
forward = [n]*n
backward = [-1]*n
inter = []                       

for i in xrange (len(arr)):
  while (inter and arr[inter[-1]] >= arr[i]):                 
    inter.pop()

  if inter:
    backward[i] = inter[-1]                # inter[-1] is less than arr[i]

  inter.append(i)

inter = []
try:
  for i in xrange (len(arr)-1,0,-1):
    while (inter and arr[inter[-1]] >= arr[i]):
      inter.pop()

    if inter:
      forward[i] = inter[-1]

    inter.append(i)
except Exception as e:
 print 'Error occured'+str(e)

ans = [0]*(n)
for i in range(n):
  length = forward[i]-backward[i]-2
  ans[length] = max(arr[i] , ans[length])

for i in xrange (len(arr)-1,1,-1):
  if ans[i]>ans[i-1]:
    ans[i-1] = ans[i]

print forward
print backward
print ans
